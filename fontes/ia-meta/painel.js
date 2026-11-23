// painel.js — módulo do ia-meta (v5.6). Importado por worker.js. Publicar junto (2 partes no multipart).
const GRAPH = "https://graph.facebook.com/v24.0";
const APP_ID = "2312368952948712";
const CONFIG_ID = "1433066778420394";
const PAUSA_SEG = 24 * 60 * 60;
const agora = () => new Date().toISOString();
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const json = o => new Response(JSON.stringify(o, null, 2), { headers: { "content-type": "application/json; charset=utf-8" } });
const html = s => new Response(s, { headers: { "content-type": "text/html; charset=utf-8" } });
// registrar e assinarPagina vêm do worker.js (injetados por setDeps para evitar import circular)
let registrar = async () => {}, assinarPagina = async () => "indisponível";
export function setDeps(d) { registrar = d.registrar; assinarPagina = d.assinarPagina; }

// =====================================================================
// PAINEL /app (v5.6) — interface em inglês exigida pelo App Review da Meta.
// Login com a Meta (mesma configuração 1433066778420394) → sessão própria (KV app:sess:<id>, 12 h).
// O painel NUNCA altera meta:auth (o token do robô). Mensagem enviada pelo painel = atendimento humano
// → pausa a IA daquela conversa por 24 h (mesma regra do eco do app do Instagram).
// =====================================================================
const SESS_TTL = 12 * 3600;
const EVENTOS_MAX = 40;

export async function guardarEvento(env, ev) {
  try {
    const l = (await env.CONVERSAS.get("app:eventos", "json")) || [];
    l.unshift({ t: agora(), ...ev, texto: String(ev.texto || "").slice(0, 280) });
    await env.CONVERSAS.put("app:eventos", JSON.stringify(l.slice(0, EVENTOS_MAX)), { expirationTtl: 3 * 86400 });
  } catch (e) { console.log("guardarEvento", String(e).slice(0, 120)); }
}

function lerCookie(req, nome) {
  const c = req.headers.get("cookie") || "";
  for (const parte of c.split(";")) { const [k, ...v] = parte.trim().split("="); if (k === nome) return v.join("="); }
  return null;
}
async function sessao(req, env) {
  const sid = lerCookie(req, "ad_sess");
  if (!sid || !/^[0-9a-f-]{36}$/.test(sid)) return null;
  const s = await env.CONVERSAS.get("app:sess:" + sid, "json");
  return s ? { ...s, sid } : null;
}
async function gget(path, token) {
  const r = await fetch(`${GRAPH}/${path}`, { headers: { authorization: "Bearer " + token } });
  return r.json().catch(() => ({ error: { message: "HTTP " + r.status } }));
}
async function gsend(method, path, token, body) {
  const r = await fetch(`${GRAPH}/${path}`, { method, headers: { authorization: "Bearer " + token, "content-type": "application/json" }, body: body ? JSON.stringify(body) : undefined });
  return r.json().catch(() => ({ error: { message: "HTTP " + r.status } }));
}

// Chamado por conectar() quando o state veio de /app/login.
export async function painelLogin(userToken, url, env) {
  const me = await gget("me?fields=id,name", userToken);
  if (!me.id) return html(painelPagina("Login error", "<p>Meta did not return the user: " + esc(me.error?.message || "") + "</p><p><a class='btn' href='/app'>Back</a></p>"));
  const contas = await gget("me/accounts?fields=id,name,category,access_token,instagram_business_account{id,username}&limit=50", userToken);
  const pages = (contas.data || []).map(x => ({ id: x.id, name: x.name, category: x.category || "", token: x.access_token, ig_id: x.instagram_business_account?.id || null, ig_username: x.instagram_business_account?.username || null }));
  let scopes = [];
  if (env.IG_APP_SECRET) {
    const dbg = await gget(`debug_token?input_token=${encodeURIComponent(userToken)}`, `${APP_ID}|${env.IG_APP_SECRET}`);
    scopes = dbg.data?.scopes || [];
  }
  const sel = pages.find(x => (x.ig_username || "").toLowerCase() === "auditor_discursivas") || pages.find(x => x.ig_id) || pages[0] || null;
  const sid = crypto.randomUUID();
  await env.CONVERSAS.put("app:sess:" + sid, JSON.stringify({ user_id: me.id, user_name: me.name, user_token: userToken, pages, sel: sel?.id || null, scopes, em: agora() }), { expirationTtl: SESS_TTL });
  await registrar(env, { t: agora(), tipo: "painel_login", paginas: pages.length, escopos: scopes.length });
  return new Response(null, { status: 302, headers: { location: url.origin + "/app", "set-cookie": `ad_sess=${sid}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=${SESS_TTL}` } });
}

export async function painel(req, url, p, env) {
  if (req.method === "GET" && p === "/app/login") {
    if (!env.IG_APP_SECRET) return html(painelPagina("Not configured", "<p>The app secret is missing on the server.</p>"));
    const state = crypto.randomUUID();
    await env.CONVERSAS.put("meta:state:" + state, "app", { expirationTtl: 900 });
    const u = new URL("https://www.facebook.com/v24.0/dialog/oauth");
    u.searchParams.set("client_id", APP_ID); u.searchParams.set("config_id", CONFIG_ID);
    u.searchParams.set("redirect_uri", url.origin + "/retorno"); u.searchParams.set("response_type", "code");
    u.searchParams.set("override_default_response_type", "true"); u.searchParams.set("state", state);
    return Response.redirect(u.toString(), 302);
  }
  const s = await sessao(req, env);
  if (req.method === "GET" && p === "/app/logout") {
    if (s) await env.CONVERSAS.delete("app:sess:" + s.sid);
    return new Response(null, { status: 302, headers: { location: url.origin + "/app", "set-cookie": "ad_sess=; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=0" } });
  }
  if (req.method === "GET" && p === "/app") return html(s ? PAINEL_HTML : painelPagina("Auditor Discursivas IA", PAINEL_ENTRADA));
  if (!p.startsWith("/app/api/")) return new Response("not found", { status: 404 });
  if (!s) return json({ error: "Not signed in" });
  const rota = p.slice("/app/api/".length);
  const page = s.pages.find(x => x.id === s.sel) || null;
  const corpo = req.method === "POST" ? await req.json().catch(() => ({})) : {};
  const q = k => url.searchParams.get(k) || corpo[k] || "";
  const idOk = v => /^[0-9_]{3,64}$/.test(String(v || ""));
  const conv = v => /^[A-Za-z0-9_\-:=]{3,200}$/.test(String(v || ""));
  try {
    if (rota === "me") return json({ user_name: s.user_name, user_id: s.user_id, scopes: s.scopes, sel: s.sel, signed_in_at: s.em, pages: s.pages.map(x => ({ id: x.id, name: x.name, category: x.category, ig_id: x.ig_id, ig_username: x.ig_username })) });
    if (rota === "select" && req.method === "POST") {
      if (!s.pages.some(x => x.id === corpo.page_id)) return json({ error: "Page not available for this user" });
      const { sid, ...guardar } = s; guardar.sel = corpo.page_id;
      await env.CONVERSAS.put("app:sess:" + sid, JSON.stringify(guardar), { expirationTtl: SESS_TTL });
      return json({ ok: true });
    }
    if (!page) return json({ error: "No Facebook Page was shared with the app. Sign in again and select your Page." });
    const tk = page.token;
    const igIds = [page.id, page.ig_id].filter(Boolean);
    if (rota === "events") {
      const l = (await env.CONVERSAS.get("app:eventos", "json")) || [];
      return json({ events: l.filter(e => !e.conta || igIds.includes(e.conta) || e.campo === "comments").slice(0, 25) });
    }
    if (rota === "webhooks") {
      const sub = await gget(`${page.id}/subscribed_apps`, tk);
      return json({ callback: url.origin + "/meta", page: { id: page.id, name: page.name }, subscribed: (sub.data || []).map(a => ({ app: a.name, id: a.id, fields: a.subscribed_fields || [] })), error: sub.error?.message });
    }
    if (rota === "webhooks/subscribe" && req.method === "POST") {
      const r = await assinarPagina(page.id, tk);
      await registrar(env, { t: agora(), tipo: "painel_assinar", resultado: r });
      const sub = await gget(`${page.id}/subscribed_apps`, tk);
      return json({ result: r, subscribed: (sub.data || []).map(a => ({ app: a.name, id: a.id, fields: a.subscribed_fields || [] })) });
    }
    if (rota === "webhooks/unsubscribe" && req.method === "POST") {
      const r = await gsend("DELETE", `${page.id}/subscribed_apps`, tk);
      return json({ result: r.success ? "unsubscribed" : (r.error?.message || "error") });
    }
    if (rota === "page") {
      const info = await gget(`${page.id}?fields=id,name,category,fan_count,followers_count,link,picture{url}`, tk);
      const posts = await gget(`${page.id}/posts?fields=id,message,created_time,permalink_url,comments.summary(true).limit(0),reactions.summary(true).limit(0)&limit=5`, tk);
      const ig = page.ig_id ? await gget(`${page.ig_id}?fields=id,username,name,profile_picture_url,followers_count,media_count`, tk) : null;
      return json({ page: info, posts: posts.data || [], posts_error: posts.error?.message, instagram: ig });
    }
    if (!page.ig_id) return json({ error: "This Page has no Instagram professional account linked." });
    if (rota === "media") {
      const m = await gget(`${page.ig_id}/media?fields=id,caption,media_type,media_product_type,thumbnail_url,media_url,permalink,timestamp,comments_count,like_count&limit=12`, tk);
      return json({ media: m.data || [], error: m.error?.message });
    }
    if (rota === "comments") {
      const media = q("media"); if (!idOk(media)) return json({ error: "invalid media id" });
      const info = await gget(`${media}?fields=id,caption,permalink,comments_count,like_count,timestamp`, tk);
      const c = await gget(`${media}/comments?fields=id,text,username,timestamp,hidden,like_count,replies{id,text,username,timestamp,hidden}&limit=50`, tk);
      return json({ media: info, comments: c.data || [], error: c.error?.message || info.error?.message });
    }
    if (rota === "comments/create" && req.method === "POST") {
      if (!idOk(corpo.media) || !String(corpo.message || "").trim()) return json({ error: "media and message are required" });
      const r = await gsend("POST", `${corpo.media}/comments`, tk, { message: String(corpo.message).slice(0, 2000) });
      await registrar(env, { t: agora(), tipo: "painel_comentar", ok: !!r.id });
      return json(r.id ? { ok: true, id: r.id } : { error: r.error?.message || "error" });
    }
    if (rota === "comments/reply" && req.method === "POST") {
      if (!idOk(corpo.comment) || !String(corpo.message || "").trim()) return json({ error: "comment and message are required" });
      const r = await gsend("POST", `${corpo.comment}/replies`, tk, { message: String(corpo.message).slice(0, 2000) });
      return json(r.id ? { ok: true, id: r.id } : { error: r.error?.message || "error" });
    }
    if (rota === "comments/hide" && req.method === "POST") {
      if (!idOk(corpo.comment)) return json({ error: "invalid comment id" });
      const r = await gsend("POST", `${corpo.comment}`, tk, { hide: !!corpo.hide });
      return json(r.success ? { ok: true } : { error: r.error?.message || "error" });
    }
    if (rota === "comments/delete" && req.method === "POST") {
      if (!idOk(corpo.comment)) return json({ error: "invalid comment id" });
      const r = await gsend("DELETE", `${corpo.comment}`, tk);
      await registrar(env, { t: agora(), tipo: "painel_apagar_comentario", ok: !!r.success });
      return json(r.success ? { ok: true } : { error: r.error?.message || "error" });
    }
    if (rota === "media/comments-toggle" && req.method === "POST") {
      if (!idOk(corpo.media)) return json({ error: "invalid media id" });
      const r = await gsend("POST", `${corpo.media}`, tk, { comment_enabled: !!corpo.enabled });
      return json(r.success ? { ok: true } : { error: r.error?.message || "error" });
    }
    if (rota === "conversations") {
      // Caixa grande: a Meta recusa a lista completa ("reduce the amount of data"). Tenta a lista curta;
      // se falhar, monta pelas pessoas que mandaram DM recentemente (eventos do webhook) usando user_id.
      // A lista geral demora ~25 s e falha nesta caixa: depois de uma falha, pula por 30 min.
      const pular = await env.CONVERSAS.get("app:conv_lista_falha");
      const c = pular ? { data: [] } : await gget(`${page.id}/conversations?platform=instagram&fields=id,updated_time&limit=5`, tk);
      if (c.error) await env.CONVERSAS.put("app:conv_lista_falha", "1", { expirationTtl: 1800 });
      let lista = c.data || [];
      if (lista.length) {
        await Promise.all(lista.map(async x => { const d = await gget(`${x.id}?fields=participants`, tk); x.participants = d.participants; }));
      }
      const evs = (await env.CONVERSAS.get("app:eventos", "json")) || [];
      const ids = [...new Set(evs.filter(e => e.campo === "messages" && e.de).map(e => e.de))].slice(0, 8);
      const jaTem = new Set(lista.map(x => x.id));
      for (const id of ids) {
        const d = await gget(`${page.id}/conversations?platform=instagram&user_id=${encodeURIComponent(id)}&fields=id,updated_time,participants`, tk);
        const x = d.data && d.data[0];
        if (x && !jaTem.has(x.id)) { lista.push(x); jaTem.add(x.id); }
      }
      lista.sort((a, b) => String(b.updated_time).localeCompare(String(a.updated_time)));
      return json({ ig_id: page.ig_id, ig_username: page.ig_username, conversations: lista });
    }
    if (rota === "thread") {
      const id = q("id"); if (!conv(id)) return json({ error: "invalid conversation id" });
      const c = await gget(`${id}?fields=participants,messages.limit(15){id,message,from,to,created_time}`, tk);
      return json({ ig_id: page.ig_id, participants: c.participants?.data || [], messages: c.messages?.data || [], error: c.error?.message });
    }
    if (rota === "send" && req.method === "POST") {
      const to = String(corpo.to || ""), text = String(corpo.text || "").trim();
      if (!idOk(to) || !text) return json({ error: "recipient and text are required" });
      const r = await gsend("POST", `${page.id}/messages`, tk, { recipient: { id: to }, message: { text: text.slice(0, 1000) } });
      if (r.message_id) {
        await env.CONVERSAS.put("enviado:" + r.message_id, "1", { expirationTtl: 3 * 86400 });
        // Mensagem de pessoa (painel) → a IA fica pausada nessa conversa por 24 h.
        await env.CONVERSAS.put("pausa:" + to, JSON.stringify({ desde: agora(), motivo: "painel" }), { expirationTtl: PAUSA_SEG });
        await registrar(env, { t: agora(), tipo: "painel_dm", para: to });
        return json({ ok: true, message_id: r.message_id, ai_paused: true });
      }
      return json({ error: r.error?.message || "error" });
    }
    return json({ error: "unknown route" });
  } catch (e) {
    return json({ error: String(e).slice(0, 200) });
  }
}

export function painelPagina(titulo, corpo) {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(titulo)}</title>${PAINEL_CSS}</head><body><header class="top"><div class="brand"><span class="logo">AD/IA</span> Auditor Discursivas IA</div></header><main class="narrow"><h1>${esc(titulo)}</h1>${corpo}</main></body></html>`;
}

const PAINEL_CSS = String.raw`<style>
:root{--navy:#2A3544;--orange:#F04E23;--bg:#F5F6F8;--line:#DDE1E7;--muted:#66717F;--ok:#1B8A4A;--bad:#C0392B}
*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--navy);font-size:15px}
.top{background:var(--navy);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:12px 22px;gap:12px;flex-wrap:wrap}
.brand{font-weight:700;font-size:17px;display:flex;align-items:center;gap:10px}.logo{background:var(--orange);border-radius:6px;padding:3px 7px;font-size:13px}
.who{font-size:13px;opacity:.9}.who a{color:#fff}
main{max-width:1100px;margin:0 auto;padding:22px}.narrow{max-width:720px}
h1{font-size:24px}h2{font-size:18px;margin:0 0 6px}
nav.tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:16px}
nav.tabs button{border:1px solid var(--line);background:#fff;color:var(--navy);padding:9px 14px;border-radius:8px;cursor:pointer;font-weight:600}
nav.tabs button.on{background:var(--navy);color:#fff;border-color:var(--navy)}
.card{background:#fff;border:1px solid var(--line);border-radius:10px;padding:16px;margin-bottom:14px}
.help{background:#FFF4EF;border-left:4px solid var(--orange);padding:10px 12px;border-radius:6px;font-size:13.5px;margin-bottom:14px}
.help b{color:var(--orange)}
.perm{display:inline-block;background:#EEF1F5;border-radius:4px;padding:1px 6px;font-family:ui-monospace,monospace;font-size:12.5px;margin:2px}
.btn{display:inline-block;background:var(--orange);color:#fff;border:0;border-radius:8px;padding:9px 14px;font-weight:700;cursor:pointer;text-decoration:none;font-size:14px}
.btn.sec{background:#fff;color:var(--navy);border:1px solid var(--line)}.btn.danger{background:var(--bad)}.btn.small{padding:5px 9px;font-size:12.5px}
.fb{background:#1877F2;font-size:16px;padding:12px 18px}
input,textarea,select{font:inherit;border:1px solid var(--line);border-radius:8px;padding:8px 10px;width:100%}
.row{display:flex;gap:8px;align-items:center}.row>input{flex:1}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px}
.media{border:2px solid var(--line);border-radius:8px;overflow:hidden;cursor:pointer;background:#fff}.media.sel{border-color:var(--orange)}
.media img{width:100%;height:150px;object-fit:cover;display:block;background:#ddd}.media div{padding:6px 8px;font-size:12.5px}
.cm{border-bottom:1px solid var(--line);padding:9px 0}.cm .meta{font-size:12.5px;color:var(--muted)}.cm.reply{margin-left:26px}
.hidden-tag{background:#FDECEA;color:var(--bad);border-radius:4px;padding:0 5px;font-size:11.5px;font-weight:700}
.cols{display:grid;grid-template-columns:300px 1fr;gap:14px}@media(max-width:760px){.cols{grid-template-columns:1fr}}
.conv{padding:9px;border-bottom:1px solid var(--line);cursor:pointer}.conv.sel,.conv:hover{background:#FFF4EF}
.thread{height:380px;overflow:auto;background:var(--bg);border-radius:8px;padding:10px;margin-bottom:10px}
.msg{max-width:75%;padding:8px 11px;border-radius:12px;margin:6px 0;font-size:14px;white-space:pre-wrap}
.msg.in{background:#fff;border:1px solid var(--line)}.msg.out{background:var(--navy);color:#fff;margin-left:auto}
.msg small{display:block;font-size:11px;opacity:.7;margin-top:3px}
table{width:100%;border-collapse:collapse;font-size:13.5px}td,th{border-bottom:1px solid var(--line);padding:7px;text-align:left;vertical-align:top}
.ev-new{animation:pulse 2s}@keyframes pulse{from{background:#FFE3D8}to{background:transparent}}
.ok{color:var(--ok);font-weight:700}.bad{color:var(--bad);font-weight:700}.muted{color:var(--muted)}
#toast{position:fixed;bottom:18px;right:18px;background:var(--navy);color:#fff;padding:10px 14px;border-radius:8px;display:none;max-width:420px}
</style>`;

const PAINEL_ENTRADA = String.raw`<p><b>Auditor Discursivas IA</b> is the internal console of the Instagram professional account <b>@auditor_discursivas</b>. It is used only by the account owner and staff to answer Direct messages, moderate comments and monitor the webhooks that power the AI assistant.</p>
<div class="help"><b>What happens when you continue:</b> Meta asks you to log in, choose the Facebook Page and Instagram account, and approve the permissions below. You can change or revoke this access at any time in your Facebook settings (Business integrations).</div>
<p><span class="perm">pages_show_list</span> list the Pages you manage · <span class="perm">pages_manage_metadata</span> subscribe the Page to webhooks · <span class="perm">pages_read_engagement</span> read Page content and engagement · <span class="perm">instagram_basic</span> read the Instagram profile and posts · <span class="perm">instagram_manage_comments</span> create, hide and delete comments · <span class="perm">instagram_manage_messages</span> send and receive Direct messages</p>
<p><a class="btn fb" href="/app/login" title="Opens the Meta login dialog to grant this app access to your Page and Instagram account">Continue with Facebook</a></p>
<p class="muted"><a href="/privacidade">Privacy policy</a> · <a href="/exclusao-dados">Data deletion</a></p>`;

const PAINEL_HTML = String.raw`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Auditor Discursivas IA — Console</title>` + PAINEL_CSS + String.raw`</head><body>
<header class="top"><div class="brand"><span class="logo">AD/IA</span> Auditor Discursivas IA — Console</div><div class="who" id="who">Loading…</div></header>
<main>
<nav class="tabs" id="tabs">
<button data-t="overview" title="Signed-in user, connected Page and Instagram account, and the permissions you granted">1 · Account</button>
<button data-t="webhooks" title="Subscribe the Page to webhooks and watch events arriving in real time">2 · Webhooks</button>
<button data-t="comments" title="Read posts, add, hide/unhide and delete comments">3 · Comments</button>
<button data-t="messages" title="Send and receive Instagram Direct messages">4 · Messages</button>
<button data-t="engagement" title="Page and Instagram engagement: followers, posts, reactions and comment counts">5 · Engagement</button>
</nav>

<section id="t-overview">
<div class="help"><b>Account.</b> Shows who is signed in with Meta, the Facebook Pages you shared with the app (<span class="perm">pages_show_list</span>), the linked Instagram professional account (<span class="perm">instagram_basic</span>) and the permissions you granted in the login dialog.</div>
<div class="card"><h2>Signed in</h2><div id="ov-user"></div></div>
<div class="card"><h2>Your Facebook Pages <span class="perm">pages_show_list</span></h2><p class="muted">Choose the Page this console manages. Its linked Instagram account is used in the other tabs.</p><div id="ov-pages"></div></div>
<div class="card"><h2>Permissions granted to this app</h2><div id="ov-scopes"></div></div>
</section>

<section id="t-webhooks" hidden>
<div class="help"><b>Webhooks.</b> <span class="perm">pages_manage_metadata</span> lets the app subscribe your Page to webhook events. Click <b>Subscribe Page</b>, then comment on a post or send a Direct message to the account: the event appears below within seconds (auto-refresh every 4 s).</div>
<div class="card"><h2>Page subscription</h2><div id="wh-sub"></div>
<p><button class="btn" id="wh-subscribe" title="Subscribes this Page to the app's webhook fields (messages, message echoes, postbacks, referrals)">Subscribe Page to app events</button>
<button class="btn sec" id="wh-unsub" title="Removes the app subscription from this Page">Unsubscribe</button>
<button class="btn sec" id="wh-refresh" title="Reads the current subscription again">Refresh</button></p>
<p class="muted">Callback URL: <code id="wh-cb"></code></p></div>
<div class="card"><h2>Webhook events received</h2><table><thead><tr><th>Time</th><th>Field</th><th>From</th><th>Content</th></tr></thead><tbody id="wh-events"></tbody></table></div>
</section>

<section id="t-comments" hidden>
<div class="help"><b>Comments.</b> Pick a post (<span class="perm">instagram_basic</span>). Then use <span class="perm">instagram_manage_comments</span>: <b>Add comment</b> publishes a comment as @account; <b>Hide / Unhide</b> updates a comment (the Instagram API supports updating a comment's visibility, not its text); <b>Delete</b> removes it. Open the post in the Instagram app to confirm the final state.</div>
<div class="card"><h2>Recent posts</h2><div class="grid" id="cm-media"></div></div>
<div class="card" id="cm-box" hidden><h2 id="cm-title">Comments</h2><p><a id="cm-link" target="_blank" title="Opens this post on Instagram to confirm the change">Open post on Instagram ↗</a> · <span id="cm-counts" class="muted"></span></p>
<div class="row"><input id="cm-new" placeholder="Write a comment as the account…"><button class="btn" id="cm-add" title="Publishes this text as a new comment on the selected post">Add comment</button><button class="btn sec" id="cm-reload" title="Reloads comments and counts">Refresh</button></div>
<div id="cm-list" style="margin-top:10px"></div></div>
</section>

<section id="t-messages" hidden>
<div class="help"><b>Messages.</b> <span class="perm">instagram_manage_messages</span>: select a conversation, type a reply and click <b>Send</b>. The message is delivered to the recipient's Instagram Direct. Replies from the other person appear here automatically (refresh every 4 s). Sending from this console pauses the AI assistant in that conversation for 24 h, so a person stays in charge.</div>
<div class="cols"><div class="card" style="padding:0"><div style="padding:12px 12px 0"><h2>Conversations</h2></div><div id="ms-list"></div></div>
<div class="card"><h2 id="ms-title">Select a conversation</h2><div class="thread" id="ms-thread"></div>
<div class="row"><input id="ms-text" placeholder="Type a message…" disabled><button class="btn" id="ms-send" title="Sends this message to the selected Instagram user via the Messenger API for Instagram" disabled>Send</button></div></div></div>
</section>

<section id="t-engagement" hidden>
<div class="help"><b>Engagement.</b> <span class="perm">pages_read_engagement</span> reads the Page's followers, posts, reactions and comment counts; <span class="perm">instagram_basic</span> reads the Instagram profile and media counts. Add a comment in the Comments tab and click <b>Refresh</b> here to see the count change on the same post.</div>
<p><button class="btn sec" id="en-refresh" title="Reads engagement data again">Refresh</button></p>
<div class="card"><h2>Facebook Page</h2><div id="en-page"></div></div>
<div class="card"><h2>Instagram account</h2><div id="en-ig"></div></div>
<div class="card"><h2>Instagram posts — likes and comments</h2><table><thead><tr><th>Post</th><th>Date</th><th>Likes</th><th>Comments</th></tr></thead><tbody id="en-media"></tbody></table></div>
<div class="card"><h2>Page posts — reactions and comments</h2><table><thead><tr><th>Post</th><th>Date</th><th>Reactions</th><th>Comments</th></tr></thead><tbody id="en-posts"></tbody></table></div>
</section>
</main>
<div id="toast"></div>
<script>
var ME=null, SEL_MEDIA=null, SEL_CONV=null, SEL_PEER=null, TIMER=null, SEEN={};
function e(s){return String(s==null?"":s).replace(/[&<>"']/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
function $(id){return document.getElementById(id)}
function toast(t,bad){var x=$("toast");x.textContent=t;x.style.background=bad?"#C0392B":"#2A3544";x.style.display="block";clearTimeout(x._t);x._t=setTimeout(function(){x.style.display="none"},4000)}
function dt(s){if(!s)return"";var d=new Date(s);return d.toLocaleString("en-GB",{day:"2-digit",month:"short",hour:"2-digit",minute:"2-digit",second:"2-digit"})}
function api(path,body){return fetch("/app/api/"+path,body?{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(body)}:{}).then(function(r){return r.json()}).then(function(d){if(d.error)toast("Meta API: "+d.error,true);return d})}
function tab(t){Array.prototype.forEach.call(document.querySelectorAll("nav.tabs button"),function(b){b.classList.toggle("on",b.dataset.t===t)});
 ["overview","webhooks","comments","messages","engagement"].forEach(function(n){$("t-"+n).hidden=n!==t});
 clearInterval(TIMER);
 if(t==="overview")loadMe();if(t==="webhooks"){loadSub();loadEvents();TIMER=setInterval(loadEvents,4000)}
 if(t==="comments")loadMedia();if(t==="messages"){loadConvs();TIMER=setInterval(function(){loadConvs(true);if(SEL_CONV)loadThread(true)},4000)}
 if(t==="engagement")loadEng()}
Array.prototype.forEach.call(document.querySelectorAll("nav.tabs button"),function(b){b.onclick=function(){tab(b.dataset.t)}});
function loadMe(){return api("me").then(function(d){ME=d;var p=(d.pages||[]).filter(function(x){return x.id===d.sel})[0];
 $("who").innerHTML="Signed in as <b>"+e(d.user_name)+"</b>"+(p?" · Page: <b>"+e(p.name)+"</b>"+(p.ig_username?" · Instagram: <b>@"+e(p.ig_username)+"</b>":""):"")+" · <a href='/app/logout' title='Ends this console session'>Log out</a>";
 $("ov-user").innerHTML="<p><b>"+e(d.user_name)+"</b> <span class='muted'>(Meta user id "+e(d.user_id)+", signed in "+dt(d.signed_in_at)+")</span></p>";
 $("ov-pages").innerHTML=(d.pages||[]).length?"<table><thead><tr><th></th><th>Page</th><th>Category</th><th>Linked Instagram account</th></tr></thead><tbody>"+d.pages.map(function(x){return"<tr><td><input type='radio' name='pg' style='width:auto' title='Manage this Page' value='"+e(x.id)+"'"+(x.id===d.sel?" checked":"")+"></td><td><b>"+e(x.name)+"</b><br><span class='muted'>"+e(x.id)+"</span></td><td>"+e(x.category)+"</td><td>"+(x.ig_username?"@"+e(x.ig_username):"<span class='muted'>none</span>")+"</td></tr>"}).join("")+"</tbody></table>":"<p class='bad'>No Page was shared. Log out and sign in again, selecting your Page in the Meta dialog.</p>";
 Array.prototype.forEach.call(document.querySelectorAll("input[name=pg]"),function(r){r.onchange=function(){api("select",{page_id:r.value}).then(function(){toast("Page selected");loadMe()})}});
 $("ov-scopes").innerHTML=(d.scopes||[]).length?(d.scopes||[]).map(function(s){return"<span class='perm'>✓ "+e(s)+"</span>"}).join(" "):"<span class='muted'>Not available</span>"})}
function loadSub(){api("webhooks").then(function(d){$("wh-cb").textContent=d.callback||"";var subs=d.subscribed||[];
 $("wh-sub").innerHTML="<p>Page: <b>"+e(d.page&&d.page.name)+"</b></p>"+(subs.length?subs.map(function(a){return"<p><span class='ok'>Subscribed</span> — app <b>"+e(a.app)+"</b> ("+e(a.id)+")<br>Fields: "+a.fields.map(function(f){return"<span class='perm'>"+e(f)+"</span>"}).join(" ")+"</p>"}).join(""):"<p class='bad'>This Page is not subscribed to any app.</p>")})}
$("wh-subscribe").onclick=function(){api("webhooks/subscribe",{}).then(function(d){toast("Result: "+(d.result||""));loadSub()})};
$("wh-unsub").onclick=function(){api("webhooks/unsubscribe",{}).then(function(d){toast("Result: "+(d.result||""));loadSub()})};
$("wh-refresh").onclick=loadSub;
function loadEvents(){api("events").then(function(d){var ev=d.events||[];$("wh-events").innerHTML=ev.length?ev.map(function(x){var k=x.t+x.campo+(x.mid||x.comentario||"");var nw=!SEEN[k];SEEN[k]=1;return"<tr"+(nw?" class='ev-new'":"")+"><td>"+dt(x.t)+"</td><td><span class='perm'>"+e(x.campo)+"</span></td><td>"+(x.user?"@"+e(x.user):e(x.de||""))+"</td><td>"+e(x.texto)+(x.media?"<br><span class='muted'>media "+e(x.media)+"</span>":"")+"</td></tr>"}).join(""):"<tr><td colspan=4 class='muted'>No events yet. Comment on a post or send a Direct message to the account.</td></tr>"})}
function loadMedia(){api("media").then(function(d){$("cm-media").innerHTML=(d.media||[]).map(function(m){var img=m.thumbnail_url||m.media_url||"";return"<div class='media"+(m.id===SEL_MEDIA?" sel":"")+"' data-id='"+e(m.id)+"' title='Select this post to manage its comments'>"+(img?"<img src='"+e(img)+"' alt=''>":"")+"<div>"+e((m.caption||"(no caption)").slice(0,60))+"<br><span class='muted'>♥ "+e(m.like_count)+" · 💬 "+e(m.comments_count)+"</span></div></div>"}).join("")||"<p class='muted'>No posts.</p>";
 Array.prototype.forEach.call(document.querySelectorAll(".media"),function(x){x.onclick=function(){SEL_MEDIA=x.dataset.id;Array.prototype.forEach.call(document.querySelectorAll(".media"),function(y){y.classList.toggle("sel",y===x)});loadComments()}})})}
function cmHtml(c,reply){return"<div class='cm"+(reply?" reply":"")+"'><div><b>@"+e(c.username)+"</b> "+(c.hidden?"<span class='hidden-tag'>HIDDEN</span> ":"")+e(c.text)+"</div><div class='meta'>"+dt(c.timestamp)+" · id "+e(c.id)+"</div><div style='margin-top:5px'>"+
 (reply?"":"<button class='btn sec small' data-a='reply' data-id='"+e(c.id)+"' title='Publishes a public reply to this comment'>Reply</button> ")+
 "<button class='btn sec small' data-a='"+(c.hidden?"unhide":"hide")+"' data-id='"+e(c.id)+"' title='"+(c.hidden?"Makes this comment visible again":"Hides this comment from the public (update)")+"'>"+(c.hidden?"Unhide":"Hide")+"</button> <button class='btn danger small' data-a='delete' data-id='"+e(c.id)+"' title='Permanently deletes this comment from the post'>Delete</button></div></div>"}
function loadComments(){if(!SEL_MEDIA)return;api("comments?media="+encodeURIComponent(SEL_MEDIA)).then(function(d){$("cm-box").hidden=false;var m=d.media||{};
 $("cm-title").textContent="Comments — "+(m.caption||"post").slice(0,70);$("cm-link").href=m.permalink||"#";$("cm-counts").textContent="♥ "+(m.like_count||0)+" likes · 💬 "+(m.comments_count||0)+" comments";
 var h="";(d.comments||[]).forEach(function(c){h+=cmHtml(c,false);((c.replies&&c.replies.data)||[]).forEach(function(r){h+=cmHtml(r,true)})});$("cm-list").innerHTML=h||"<p class='muted'>No comments yet.</p>";
 Array.prototype.forEach.call(document.querySelectorAll("#cm-list button"),function(b){b.onclick=function(){var id=b.dataset.id,a=b.dataset.a;
  if(a==="reply"){var t=prompt("Reply text:");if(t)api("comments/reply",{comment:id,message:t}).then(function(r){if(r.ok){toast("Reply published");loadComments()}})}
  if(a==="hide"||a==="unhide")api("comments/hide",{comment:id,hide:a==="hide"}).then(function(r){if(r.ok){toast(a==="hide"?"Comment hidden":"Comment visible again");loadComments()}});
  if(a==="delete")api("comments/delete",{comment:id}).then(function(r){if(r.ok){toast("Comment deleted");loadComments()}})}})})}
$("cm-add").onclick=function(){var t=$("cm-new").value.trim();if(!t||!SEL_MEDIA)return;api("comments/create",{media:SEL_MEDIA,message:t}).then(function(r){if(r.ok){$("cm-new").value="";toast("Comment published (id "+r.id+")");loadComments()}})};
$("cm-reload").onclick=loadComments;
function peerOf(c){var me=(ME&&ME.pages||[]).filter(function(x){return x.id===ME.sel})[0];var mine=me?me.ig_username:"";var ps=(c.participants&&c.participants.data)||c||[];return ps.filter(function(p){return p.username!==mine})[0]||ps[0]||{}}
function loadConvs(quiet){api("conversations").then(function(d){var cs=d.conversations||[];$("ms-list").innerHTML=cs.length?cs.map(function(c){var p=peerOf(c);var last=(c.messages&&c.messages.data&&c.messages.data[0])||{};return"<div class='conv"+(c.id===SEL_CONV?" sel":"")+"' data-id='"+e(c.id)+"' data-peer='"+e(p.id)+"' data-user='"+e(p.username)+"' title='Open this conversation'><b>@"+e(p.username||p.id)+"</b><br><span class='muted'>"+e((last.message||"").slice(0,50))+"</span><br><span class='muted' style='font-size:11.5px'>"+dt(c.updated_time)+"</span></div>"}).join(""):"<p class='muted' style='padding:12px'>No recent conversations. When someone sends a Direct message to the account, the conversation appears here.</p>";
 Array.prototype.forEach.call(document.querySelectorAll(".conv"),function(x){x.onclick=function(){SEL_CONV=x.dataset.id;SEL_PEER=x.dataset.peer;$("ms-title").textContent="Conversation with @"+x.dataset.user;$("ms-text").disabled=false;$("ms-send").disabled=false;loadConvs(true);loadThread()}})})}
function loadThread(quiet){var id=SEL_CONV;api("thread?id="+encodeURIComponent(id)).then(function(d){if(id!==SEL_CONV)return;var th=$("ms-thread");var atBottom=th.scrollHeight-th.scrollTop-th.clientHeight<40;
 th.innerHTML=(d.messages||[]).slice().reverse().map(function(m){var out=m.from&&m.from.id===d.ig_id;return"<div class='msg "+(out?"out":"in")+"'><b>@"+e(m.from&&m.from.username)+"</b><br>"+e(m.message||(m.attachments?"[attachment]":""))+"<small>"+dt(m.created_time)+(out?" · sent":" · received")+"</small></div>"}).join("");
 if(!quiet||atBottom)th.scrollTop=th.scrollHeight})}
function send(){var t=$("ms-text").value.trim();if(!t||!SEL_PEER)return;$("ms-send").disabled=true;api("send",{to:SEL_PEER,text:t}).then(function(r){$("ms-send").disabled=false;if(r.ok){$("ms-text").value="";toast("Message sent · AI assistant paused for this conversation (24 h)");setTimeout(loadThread,1200)}})}
$("ms-send").onclick=send;$("ms-text").onkeydown=function(ev){if(ev.key==="Enter")send()};
function loadEng(){api("page").then(function(d){var p=d.page||{};$("en-page").innerHTML="<p><b>"+e(p.name)+"</b> · "+e(p.category)+"<br>Followers: <b>"+e(p.followers_count)+"</b> · Likes: <b>"+e(p.fan_count)+"</b></p>";
 var ig=d.instagram||{};$("en-ig").innerHTML=ig.username?"<p><b>@"+e(ig.username)+"</b> · "+e(ig.name)+"<br>Followers: <b>"+e(ig.followers_count)+"</b> · Posts: <b>"+e(ig.media_count)+"</b></p>":"<p class='muted'>No Instagram account.</p>";
 $("en-posts").innerHTML=(d.posts||[]).map(function(x){return"<tr><td><a target='_blank' href='"+e(x.permalink_url)+"'>"+e((x.message||"(no text)").slice(0,80))+"</a></td><td>"+dt(x.created_time)+"</td><td>"+e(x.reactions&&x.reactions.summary&&x.reactions.summary.total_count)+"</td><td>"+e(x.comments&&x.comments.summary&&x.comments.summary.total_count)+"</td></tr>"}).join("")||"<tr><td colspan=4 class='muted'>"+e(d.posts_error||"No Page posts.")+"</td></tr>"});
 api("media").then(function(d){$("en-media").innerHTML=(d.media||[]).map(function(m){return"<tr><td><a target='_blank' href='"+e(m.permalink)+"'>"+e((m.caption||"(no caption)").slice(0,80))+"</a></td><td>"+dt(m.timestamp)+"</td><td>"+e(m.like_count)+"</td><td>"+e(m.comments_count)+"</td></tr>"}).join("")})}
$("en-refresh").onclick=loadEng;
loadMe().then(function(){tab("overview")});
</script></body></html>`;
