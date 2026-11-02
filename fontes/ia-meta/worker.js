// ia-meta — Instagram (app próprio na Meta) → Claude
// Auditor Discursivas (@auditor_discursivas). Versão 1 (02/11/2026).
//
// Bindings / variáveis (Cloudflare → Worker ia-meta → Settings):
//   CONVERSAS     KV ia-direct-conversas (o mesmo do ia-direct: chave "prompt", contextos, pausas)
//   META_VERIFY   texto combinado com a Meta na verificação do webhook (variável comum)
//   IG_APP_SECRET segredo do app na Meta (SECRET — só o Samuel cola)
//   (token: obtido pelo próprio servidor no login /conectar e guardado no KV "meta:auth")
//   ANTHROPIC_API_KEY  chave da Anthropic (SECRET — só o Samuel cola; só precisa no modo "responder")
//   MODO          "ouvir" (padrão: só registra e pausa) | "responder" (o Claude responde no direct)
//   MODELO        opcional (padrão claude-opus-5-5)
//   NTFY_TOPICO   tópico do aviso no celular
//
// Rotas: GET / (status) · GET /meta (verificação) · POST /meta (eventos) ·
//        GET /privacidade · GET /exclusao-dados · GET /log?k=<META_VERIFY> (últimos eventos, sem conteúdo)
//        GET /conectar (Samuel faz login na Meta) → GET /retorno (troca o código pelo token, acha Página e Instagram, assina webhooks)

const VERSAO = "ia-meta v4 (02/11/2026)";
const GRAPH = "https://graph.facebook.com/v24.0";
const APP_ID = "2312368952948712";      // app "Auditor Discursivas IA" na Meta
const CONFIG_ID = "1433066778420394";   // configuração "Pagina + Instagram (usuario)" (token de usuário → token da Página)
// (a 1313923144139531, "API do Instagram (login unificado)", deu token de sistema sem a conta — não usar)
const NEGOCIO = "1530179278566154";     // portfólio "Samuel Wolf | Recursos Profissionais"
const IG_CONHECIDO = "17841472070663168"; // @auditor_discursivas (Configurações do negócio → Contas do Instagram)
const PAUSA_SEG = 24 * 60 * 60;
const LOG_MAX = 80;

export default {
  async fetch(req, env, ctx) {
    const url = new URL(req.url);
    const p = url.pathname.replace(/\/+$/, "") || "/";

    if (req.method === "GET" && p === "/") {
      const auth = await env.CONVERSAS.get("meta:auth", "json");
      return json({ versao: VERSAO, modo: env.MODO || "ouvir", segredo_app: !!env.IG_APP_SECRET, conectado: !!(auth && auth.page_token), instagram: auth?.ig_username || null, pagina: auth?.page_name || null, assinatura: auth?.assinatura || null, conectado_em: auth?.em || null, chave_anthropic: !!env.ANTHROPIC_API_KEY });
    }
    if (req.method === "GET" && p === "/conectar") {
      if (!env.IG_APP_SECRET) return html(pagina("Falta um passo", "Antes de conectar, cole o <b>IG_APP_SECRET</b> no Cloudflare (Workers → ia-meta → Settings → Variables and Secrets, tipo Secret)."));
      const state = crypto.randomUUID();
      await env.CONVERSAS.put("meta:state:" + state, "1", { expirationTtl: 900 });
      const u = new URL("https://www.facebook.com/v24.0/dialog/oauth");
      u.searchParams.set("client_id", APP_ID); u.searchParams.set("config_id", CONFIG_ID);
      u.searchParams.set("redirect_uri", url.origin + "/retorno"); u.searchParams.set("response_type", "code");
      u.searchParams.set("override_default_response_type", "true"); u.searchParams.set("state", state);
      return Response.redirect(u.toString(), 302);
    }
    if (req.method === "GET" && p === "/diagnostico") {
      if (!env.META_VERIFY || url.searchParams.get("k") !== env.META_VERIFY) return new Response("forbidden", { status: 403 });
      const auth = await env.CONVERSAS.get("meta:auth", "json");
      if (!auth?.user_token) return json({ erro: "sem token: abra /conectar" });
      return json(await configurarInstagram(auth.user_token, env, auth));
    }
    if (req.method === "GET" && p === "/consulta") {
      // Consulta de leitura na Graph API com o token guardado (diagnóstico; o token nunca é devolvido).
      if (!env.META_VERIFY || url.searchParams.get("k") !== env.META_VERIFY) return new Response("forbidden", { status: 403 });
      const auth = await env.CONVERSAS.get("meta:auth", "json");
      const q = url.searchParams.get("q") || "me";
      const r = await fetch(`${GRAPH}/${q}`, { headers: { authorization: "Bearer " + auth.user_token } });
      return new Response(await r.text(), { status: r.status, headers: { "content-type": "application/json" } });
    }
    if (req.method === "GET" && p === "/retorno") {
      return html(await conectar(url, env));
    }
    if (req.method === "GET" && p === "/meta") {
      const mode = url.searchParams.get("hub.mode");
      const tok = url.searchParams.get("hub.verify_token");
      const ch = url.searchParams.get("hub.challenge");
      if (mode === "subscribe" && env.META_VERIFY && tok === env.META_VERIFY) return new Response(ch || "", { status: 200 });
      return new Response("forbidden", { status: 403 });
    }
    if (req.method === "POST" && p === "/meta") {
      const raw = await req.text();
      if (env.IG_APP_SECRET) {
        const ok = await assinaturaOk(raw, req.headers.get("x-hub-signature-256"), env.IG_APP_SECRET);
        if (!ok) { ctx.waitUntil(registrar(env, { t: agora(), tipo: "assinatura_invalida" })); return new Response("bad signature", { status: 401 }); }
      }
      let body; try { body = JSON.parse(raw); } catch { return new Response("bad json", { status: 400 }); }
      ctx.waitUntil(processar(body, env, !env.IG_APP_SECRET).catch(e => registrar(env, { t: agora(), tipo: "erro", erro: String(e).slice(0, 200) })));
      return new Response("EVENT_RECEIVED", { status: 200 });
    }
    if (req.method === "GET" && p === "/privacidade") return html(PAG_PRIVACIDADE);
    if (req.method === "GET" && p === "/exclusao-dados") return html(PAG_EXCLUSAO);
    if (req.method === "POST" && p === "/exclusao-dados") {
      // Callback de exclusão de dados da Meta: confirma e devolve código de acompanhamento.
      const cod = crypto.randomUUID();
      return json({ url: `${url.origin}/exclusao-dados?codigo=${cod}`, confirmation_code: cod });
    }
    if (req.method === "GET" && p === "/log") {
      if (!env.META_VERIFY || url.searchParams.get("k") !== env.META_VERIFY) return new Response("forbidden", { status: 403 });
      const log = (await env.CONVERSAS.get("meta:log", "json")) || [];
      return json(log);
    }
    return new Response("not found", { status: 404 });
  },
};

// ---------- eventos ----------
async function processar(body, env, semSegredo) {
  if (body.object !== "instagram") { await registrar(env, { t: agora(), tipo: "objeto_" + body.object }); return; }
  for (const entry of body.entry || []) {
    const contaId = String(entry.id || "");
    for (const ev of entry.messaging || []) await eventoMensagem(ev, contaId, env, semSegredo);
    for (const ev of entry.standby || []) await eventoMensagem({ ...ev, _standby: true }, contaId, env, semSegredo);
    for (const ch of entry.changes || []) {
      await registrar(env, { t: agora(), tipo: "change_" + ch.field, de: ch.value?.from?.id || null, media: ch.value?.media?.id || null, len: (ch.value?.text || "").length, sem_segredo: semSegredo || undefined });
    }
  }
}

async function eventoMensagem(ev, contaId, env, semSegredo) {
  const m = ev.message || {};
  const sender = String(ev.sender?.id || ""), recipient = String(ev.recipient?.id || "");
  const base = { t: agora(), conta: contaId, de: sender, para: recipient, standby: ev._standby || undefined, sem_segredo: semSegredo || undefined };

  if (ev.read || ev.reaction || ev.postback || ev.referral) {
    await registrar(env, { ...base, tipo: ev.read ? "lida" : ev.reaction ? "reacao" : ev.postback ? "postback" : "referral" });
    return;
  }

  if (m.is_echo) {
    // Mensagem que SAIU do @auditor_discursivas. Pode ser: o Samuel (app do Instagram), o próprio ia-meta ou outro app (InfluenciMax).
    const aluno = recipient;
    const nossa = m.mid ? await env.CONVERSAS.get("enviado:" + m.mid) : null;
    const info = { ...base, tipo: "eco", mid: m.mid ? m.mid.slice(-12) : null, nossa: !!nossa, app_id: m.app_id ?? ev.app_id ?? null, chaves: Object.keys(m).join(","), len: (m.text || "").length, self: m.is_self || undefined };
    if (nossa || m.is_self) { await registrar(env, info); return; }
    // Espera curta: o eco pode chegar antes de o envio ser gravado.
    await dormir(4000);
    if (m.mid && await env.CONVERSAS.get("enviado:" + m.mid)) { info.nossa = true; await registrar(env, info); return; }
    const humano = await ehHumano(m, env);
    info.humano = humano;
    if (humano) {
      await env.CONVERSAS.put("pausa:" + aluno, JSON.stringify({ desde: agora(), motivo: "samuel" }), { expirationTtl: PAUSA_SEG });
      const user = await usernameDe(aluno, env);
      if (user) await env.CONVERSAS.put("pausa-user:" + user.toLowerCase(), JSON.stringify({ desde: agora(), motivo: "samuel" }), { expirationTtl: PAUSA_SEG });
      info.pausou = true;
    }
    await registrar(env, info);
    return;
  }

  if (sender && sender !== contaId) {
    const pausa = await env.CONVERSAS.get("pausa:" + sender);
    const info = { ...base, tipo: "msg_aluno", len: (m.text || "").length, anexo: m.attachments ? m.attachments.map(a => a.type).join(",") : undefined, story: m.reply_to?.story ? true : undefined, pausada: !!pausa };
    await registrar(env, info);
    if ((env.MODO || "ouvir") === "responder" && !pausa && m.text && !ev._standby) await responder(sender, m.text, env);
  }
}

// Eco de quem? Regra configurável na chave KV "meta:apps_automacao" (lista de app_id que NÃO são o Samuel, ex.: InfluenciMax).
// Sem app_id no eco = mensagem digitada no app do Instagram = Samuel.
async function ehHumano(m, env) {
  const appId = m.app_id ?? null;
  if (appId == null) return true;
  const lista = (await env.CONVERSAS.get("meta:apps_automacao", "json")) || [];
  return !lista.map(String).includes(String(appId));
}

// ---------- resposta do Claude (modo "responder") ----------
async function responder(alunoId, texto, env) {
  const t = texto.toLowerCase();
  if (/falar com (o )?samuel|falar com (um )?humano|atendente humano/.test(t)) return passarParaSamuel(alunoId, env);
  const prompt = await env.CONVERSAS.get("prompt");
  if (!prompt || !env.ANTHROPIC_API_KEY) return passarParaSamuel(alunoId, env);
  const histKey = "histig:" + alunoId;
  const hist = (await env.CONVERSAS.get(histKey, "json")) || [];
  const ctxIg = (await env.CONVERSAS.get("contexto:instagram")) || "";
  const msgs = [...hist, { role: "user", content: texto }].slice(-20);
  while (msgs.length && msgs[0].role !== "user") msgs.shift();
  const r = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "x-api-key": env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json" },
    body: JSON.stringify({ model: env.MODELO || "claude-opus-5-5", max_tokens: 800, system: prompt + (ctxIg ? "\n\nCONTEXTO DESTA CONVERSA:\n" + ctxIg : ""), messages: msgs }),
  });
  if (!r.ok) return passarParaSamuel(alunoId, env);
  const d = await r.json();
  let resp = (d.content || []).filter(c => c.type === "text").map(c => c.text).join("").trim();
  if (!resp || resp.includes("[HUMANO]")) return passarParaSamuel(alunoId, env);
  // Pausa pode ter entrado enquanto o Claude pensava.
  if (await env.CONVERSAS.get("pausa:" + alunoId)) return;
  for (const parte of partes(resp, 990)) await enviar(alunoId, parte, env);
  await env.CONVERSAS.put(histKey, JSON.stringify([...msgs, { role: "assistant", content: resp }].slice(-20)), { expirationTtl: 14 * 86400 });
}

async function passarParaSamuel(alunoId, env) {
  await enviar(alunoId, "Combinado! Já avisei o Samuel e ele vai te responder pessoalmente aqui no direct assim que puder. 🙏", env);
  await env.CONVERSAS.put("pausa:" + alunoId, JSON.stringify({ desde: agora(), motivo: "pediu_samuel" }), { expirationTtl: PAUSA_SEG });
  if (env.NTFY_TOPICO) await fetch("https://ntfy.sh/", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ topic: env.NTFY_TOPICO, title: "Aluno quer falar com voce", message: "Abra o direct do @auditor_discursivas.", priority: 5 }) });
}

async function enviar(alunoId, texto, env) {
  const auth = await env.CONVERSAS.get("meta:auth", "json");
  if (!auth?.page_token) return null;
  const r = await fetch(auth.envio === "ig" ? `${GRAPH}/${auth.ig_id}/messages` : `${GRAPH}/me/messages`, {
    method: "POST",
    headers: { authorization: "Bearer " + auth.page_token, "content-type": "application/json" },
    body: JSON.stringify({ recipient: { id: alunoId }, message: { text: texto } }),
  });
  const d = await r.json().catch(() => ({}));
  if (d.message_id) await env.CONVERSAS.put("enviado:" + d.message_id, "1", { expirationTtl: 3 * 86400 });
  else await registrar(env, { t: agora(), tipo: "erro_envio", status: r.status, erro: JSON.stringify(d.error || {}).slice(0, 200) });
  return d.message_id || null;
}

async function usernameDe(id, env) {
  const auth = await env.CONVERSAS.get("meta:auth", "json");
  if (!auth?.page_token) return null;
  const k = "user:" + id;
  const c = await env.CONVERSAS.get(k);
  if (c) return c;
  const r = await fetch(`${GRAPH}/${id}?fields=username`, { headers: { authorization: "Bearer " + auth.page_token } });
  const d = await r.json().catch(() => ({}));
  if (d.username) { await env.CONVERSAS.put(k, d.username, { expirationTtl: 30 * 86400 }); return d.username; }
  return null;
}

// ---------- conexão com a Meta (login do Samuel) ----------
async function conectar(url, env) {
  const code = url.searchParams.get("code"), state = url.searchParams.get("state");
  if (url.searchParams.get("error")) return pagina("Conexão cancelada", "A Meta devolveu: " + esc(url.searchParams.get("error_description") || url.searchParams.get("error")));
  if (!code || !state || !(await env.CONVERSAS.get("meta:state:" + state))) return pagina("Link expirado", "Abra de novo <a href='/conectar'>/conectar</a>.");
  await env.CONVERSAS.delete("meta:state:" + state);
  const tk = new URL(GRAPH + "/oauth/access_token");
  tk.searchParams.set("client_id", APP_ID); tk.searchParams.set("client_secret", env.IG_APP_SECRET);
  tk.searchParams.set("redirect_uri", url.origin + "/retorno"); tk.searchParams.set("code", code);
  const t = await (await fetch(tk)).json();
  if (!t.access_token) { await registrar(env, { t: agora(), tipo: "erro_conectar", etapa: "token", erro: JSON.stringify(t.error || t).slice(0, 300) }); return pagina("Erro ao obter o token", esc(JSON.stringify(t.error || t))); }
  let userToken = t.access_token;
  // Token de longa duração (60 dias); os tokens de Página tirados dele não expiram.
  const ll = new URL(GRAPH + "/oauth/access_token");
  ll.searchParams.set("grant_type", "fb_exchange_token"); ll.searchParams.set("client_id", APP_ID);
  ll.searchParams.set("client_secret", env.IG_APP_SECRET); ll.searchParams.set("fb_exchange_token", userToken);
  const lj = await (await fetch(ll)).json();
  if (lj.access_token) userToken = lj.access_token;
  const contas = await (await fetch(`${GRAPH}/me/accounts?fields=id,name,access_token,instagram_business_account{id,username}&limit=50`, { headers: { authorization: "Bearer " + userToken } })).json();
  const lista = (contas.data || []);
  const pag = lista.find(x => x.instagram_business_account?.username?.toLowerCase() === "auditor_discursivas") || lista.find(x => x.instagram_business_account);
  const resumo = lista.map(x => `${esc(x.name)} → ${esc(x.instagram_business_account?.username || "sem Instagram")}`).join("<br>");
  if (!pag) {
    const r = await configurarInstagram(userToken, env, { em: agora(), user_token: userToken });
    if (r.ig_id) return pagina("Conectado ✅", `Instagram: <b>@${esc(r.ig_username)}</b> (acesso direto, sem Página)<br>Assinatura dos webhooks: <b>${esc(r.assinatura)}</b><br><br>Pode fechar esta aba e voltar para a Central de Marketing.`);
    return pagina("Token obtido, mas sem conta do Instagram", "Detalhe: " + esc(JSON.stringify(r).slice(0, 600)));
  }
  const sub = await (await fetch(`${GRAPH}/${pag.id}/subscribed_apps?subscribed_fields=messages,messaging_postbacks,messaging_referral,message_echoes,messaging_handovers,standby`, { method: "POST", headers: { authorization: "Bearer " + pag.access_token } })).json();
  const auth = { em: agora(), user_token: userToken, page_id: pag.id, page_name: pag.name, page_token: pag.access_token, ig_id: pag.instagram_business_account.id, ig_username: pag.instagram_business_account.username, assinatura: sub.success ? "ok" : JSON.stringify(sub.error || sub).slice(0, 200) };
  await env.CONVERSAS.put("meta:auth", JSON.stringify(auth));
  await registrar(env, { t: agora(), tipo: "conectado", ig: auth.ig_username, pagina: auth.page_name, assinatura: auth.assinatura });
  return pagina("Conectado ✅", `Instagram: <b>@${esc(auth.ig_username)}</b><br>Página: <b>${esc(auth.page_name)}</b><br>Assinatura dos webhooks: <b>${esc(auth.assinatura)}</b><br><br>Pode fechar esta aba e voltar para a Central de Marketing.`);
}
// Login unificado (app novo): o token dá acesso direto à conta do Instagram, sem Página.
async function configurarInstagram(userToken, env, base) {
  const out = { ...base };
  const dbg = await (await fetch(`${GRAPH}/debug_token?input_token=${encodeURIComponent(userToken)}`, { headers: { authorization: `Bearer ${APP_ID}|${env.IG_APP_SECRET}` } })).json();
  const escopos = dbg.data?.granular_scopes || [];
  out.escopos = escopos.map(g => g.scope + ":" + (g.target_ids || []).length);
  out.tipo_token = dbg.data?.type || null;
  const ids = [...new Set(escopos.filter(g => /instagram/.test(g.scope)).flatMap(g => g.target_ids || []))];
  // Sem target_ids: procurar contas do Instagram por outros caminhos.
  if (!ids.length) {
    const tentativas = { me: "me?fields=id,name", me_ig: "me/instagram_accounts?fields=id,username", neg_ig: `${NEGOCIO}/instagram_accounts?fields=id,username`, neg_owned: `${NEGOCIO}/owned_instagram_accounts?fields=id,username`, neg_client: `${NEGOCIO}/client_instagram_accounts?fields=id,username`, me_contas: "me/accounts?fields=id,name,instagram_business_account{id,username}" };
    out.busca = {};
    for (const [k, path] of Object.entries(tentativas)) {
      const j = await (await fetch(`${GRAPH}/${path}`, { headers: { authorization: "Bearer " + userToken } })).json();
      out.busca[k] = j.error ? "erro: " + (j.error.message || "").slice(0, 120) : (j.data ? j.data.map(x => (x.username || x.name || "") + "#" + x.id).join(", ") || "vazio" : (j.name || "") + "#" + (j.id || ""));
      for (const x of (j.data || [])) if (x.username) ids.push(x.id);
    }
  }
  if (!ids.includes(IG_CONHECIDO)) ids.push(IG_CONHECIDO);
  for (const id of ids) {
    const u = await (await fetch(`${GRAPH}/${id}?fields=id,username`, { headers: { authorization: "Bearer " + userToken } })).json();
    if (u.username) { out.ig_id = u.id; out.ig_username = u.username; if (u.username.toLowerCase() === "auditor_discursivas") break; }
    else out["erro_" + id] = JSON.stringify(u.error || u).slice(0, 200);
  }
  if (out.ig_id) {
    const sub = await (await fetch(`${GRAPH}/${out.ig_id}/subscribed_apps?subscribed_fields=messages,messaging_postbacks,messaging_referral,comments`, { method: "POST", headers: { authorization: "Bearer " + userToken } })).json();
    out.assinatura = sub.success ? "ok" : JSON.stringify(sub.error || sub).slice(0, 300);
    out.page_token = userToken;   // token usado para enviar
    out.envio = "ig";             // envio por /{ig_id}/messages
    delete out.sem_pagina;
  }
  out.em = agora();
  await env.CONVERSAS.put("meta:auth", JSON.stringify(out));
  await registrar(env, { t: agora(), tipo: out.ig_id ? "conectado" : "erro_conectar", ig: out.ig_username || null, assinatura: out.assinatura || null, tipo_token: out.tipo_token, escopos: out.escopos });
  const { user_token, page_token, ...resumo } = out;
  return resumo;
}
function pagina(titulo, corpo) { return `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${titulo}</title>${ESTILO}</head><body><h1>${titulo}</h1><p>${corpo}</p></body></html>`; }
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

// ---------- utilitários ----------
async function assinaturaOk(raw, header, segredo) {
  if (!header || !header.startsWith("sha256=")) return false;
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(segredo), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sig = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(raw));
  const hex = [...new Uint8Array(sig)].map(b => b.toString(16).padStart(2, "0")).join("");
  const rec = header.slice(7);
  if (hex.length !== rec.length) return false;
  let diff = 0; for (let i = 0; i < hex.length; i++) diff |= hex.charCodeAt(i) ^ rec.charCodeAt(i);
  return diff === 0;
}
async function registrar(env, item) {
  const log = (await env.CONVERSAS.get("meta:log", "json")) || [];
  log.unshift(item);
  await env.CONVERSAS.put("meta:log", JSON.stringify(log.slice(0, LOG_MAX)));
}
function partes(s, n) { const out = []; let x = s; while (new TextEncoder().encode(x).length > n) { let i = Math.min(x.length, n); while (new TextEncoder().encode(x.slice(0, i)).length > n) i--; const corte = x.lastIndexOf("\n", i) > i * 0.5 ? x.lastIndexOf("\n", i) : (x.lastIndexOf(" ", i) > i * 0.5 ? x.lastIndexOf(" ", i) : i); out.push(x.slice(0, corte).trim()); x = x.slice(corte).trim(); } if (x) out.push(x); return out; }
const agora = () => new Date().toISOString();
const dormir = ms => new Promise(r => setTimeout(r, ms));
const json = o => new Response(JSON.stringify(o, null, 2), { headers: { "content-type": "application/json; charset=utf-8" } });
const html = s => new Response(s, { headers: { "content-type": "text/html; charset=utf-8" } });

const ESTILO = `<style>body{font-family:system-ui,sans-serif;max-width:720px;margin:40px auto;padding:0 20px;color:#2A3544;line-height:1.6}h1{color:#2A3544}h2{color:#F04E23;font-size:1.1em}</style>`;
const PAG_PRIVACIDADE = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Política de privacidade — Auditor Discursivas</title>${ESTILO}</head><body>
<h1>Política de privacidade — Auditor Discursivas</h1><p>Atualizada em 02/11/2026. Responsável: Samuel Wolf (@auditor_discursivas, Instagram). Contato: pelo direct do @auditor_discursivas ou wolfsamuel16@gmail.com.</p>
<h2>O que coletamos</h2><p>Quando você manda mensagem ou comenta no @auditor_discursivas, recebemos pelo Instagram o seu identificador na plataforma, o nome de usuário e o conteúdo das mensagens que você enviar ao perfil.</p>
<h2>Para que usamos</h2><p>Só para responder você no direct sobre o serviço de recursos contra notas de provas discursivas, entregar materiais gratuitos que você pedir e encaminhar a conversa ao Samuel quando necessário. As respostas automáticas são geradas por inteligência artificial (Claude, da Anthropic), que processa o texto da conversa para isso.</p>
<h2>Por quanto tempo</h2><p>O histórico da conversa usado pelo assistente é apagado automaticamente em até 14 dias. Não vendemos nem compartilhamos seus dados com terceiros para publicidade.</p>
<h2>Seus direitos (LGPD)</h2><p>Você pode pedir acesso, correção ou exclusão dos seus dados a qualquer momento pelo direct do @auditor_discursivas ou por e-mail. Veja também <a href="/exclusao-dados">como excluir seus dados</a>.</p></body></html>`;
const PAG_EXCLUSAO = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Exclusão de dados — Auditor Discursivas</title>${ESTILO}</head><body>
<h1>Como excluir seus dados</h1><p>Para apagar os dados das suas conversas com o @auditor_discursivas, mande no direct do perfil a mensagem <b>"excluir meus dados"</b> ou escreva para wolfsamuel16@gmail.com informando o seu @ do Instagram. A exclusão é feita em até 7 dias e confirmada para você. De qualquer forma, o histórico usado pelo assistente é apagado automaticamente em até 14 dias.</p></body></html>`;
