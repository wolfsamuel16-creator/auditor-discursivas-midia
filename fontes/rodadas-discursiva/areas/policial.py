# -*- coding: utf-8 -*-
# Trilha POLICIAL — mini-aula (baseada na aula gratuita da PM-SC 2026 (Instituto AOCP), docs/aulas/pmsc.pdf)
NOME = 'Policial'
PALAVRA = 'POLICIAL'
SUBTITULO = 'Treino de redação para PM, PC, PP, PRF e PF.'
PUBLICO = 'SOLDADO · OFICIAL · AGENTE E ESCRIVÃO · POLÍCIA PENAL · PRF · PF'
FORMATO_CURTO = 'redação dissertativo-argumentativa'
PADRAO_BANCA = 'padrão AOCP/Cebraspe'
NOTA_DESCONTO = ('Depois da nota de conteúdo, os erros de língua entram como desconto proporcional às linhas escritas. '
                 'Exemplo do edital da PM-SC 2026 (Instituto AOCP, redação de 20 pontos): Nota = NC − NE ÷ TL, '
                 'e cada linha que faltar para 20 custa 0,20 ponto. Confira a fórmula no edital do seu concurso.')

def aula():
    return [
'''<section class="pb"><div class="parte"><span class="eyebrow">Mini-aula · Trilha Policial</span><h2>Como a redação policial pontua</h2><p>O formato da prova, como a nota é calculada, o planejamento e a estrutura que o corretor procura.</p></div>
<span class="eyebrow">01</span><h2 class="sec">O que as provas policiais cobram</h2>
<p>Nas carreiras policiais, a discursiva costuma ser uma <b>redação dissertativo-argumentativa</b> de 20 a 30 linhas, feita a partir de textos motivadores, sobre um tema de segurança pública. Não é texto escolar: o corretor quer <b>tese clara</b>, argumentos com <b>fundamento</b> (Constituição, lei, dado) e uma <b>proposta</b> concreta no fim.</p>
<table><thead><tr><th>Prova</th><th>Formato</th><th>O que vale observar</th></tr></thead><tbody>
<tr><td class="k">PM-SC 2026 · Soldado (AOCP)</td><td>Dissertação de 20 a 30 l., 20 pontos, nota mínima 10</td><td>Tema escolhido no conteúdo de Ordem Pública do edital; fuga ao tema = zero</td></tr>
<tr><td class="k">PM-SC 2023 · Soldado (Cebraspe)</td><td>Texto dissertativo de 20 a 30 l.</td><td>Tema ligado à ordem pública: a banca mudou, o eixo ficou</td></tr>
<tr><td class="k">Redações de PM da AOCP (PMDF, PMPE)</td><td>Tema em frase nominal, com recorte</td><td>“Desafios para...”, “Obstáculos para...”: o recorte define a tese</td></tr>
</tbody></table>
<div class="box nv"><span class="eyebrow">Assunto × tema</span>“Violência contra a mulher” é <b>assunto</b>. “Desafios para a efetividade das medidas protetivas” é <b>tema</b>, com recorte. Um texto que fala bem do assunto, mas não responde ao recorte, foge do tema — e, na AOCP, fuga ao tema é nota zero.</div>
<h3>Repertório de bolso</h3>
<table><thead><tr><th>Referência</th><th>O que diz (em resumo)</th></tr></thead><tbody>
<tr><td class="k">CF, art. 144, caput</td><td>Segurança pública é dever do Estado, direito e responsabilidade de todos</td></tr>
<tr><td class="k">CF, art. 144, § 5.º</td><td>Às polícias militares cabem a polícia ostensiva e a preservação da ordem pública</td></tr>
<tr><td class="k">CF, art. 129, VII</td><td>O Ministério Público exerce o controle externo da atividade policial</td></tr>
<tr><td class="k">Lei n.º 13.675/2018 (Susp)</td><td>Atuação integrada dos entes federados, em articulação com a sociedade</td></tr>
<tr><td class="k">Lei n.º 14.751/2023</td><td>Lei Orgânica Nacional das PMs e dos CBMs: princípios e diretrizes da atuação</td></tr>
</tbody></table>
<p class="nota">Fonte: Edital n.º 002/CCP/2026 – CFP (PMSC/Instituto AOCP) e legislação citada, reunidos na aula gratuita da PM-SC 2026 do @auditor_discursivas.</p>
</section>''',
'''<section class="pb"><span class="eyebrow">02</span><h2 class="sec">Como a nota é calculada</h2>
<p>Quase toda a nota está no <b>conteúdo</b>: atendimento ao tema, desenvolvimento, coesão, coerência e estrutura. Os erros de língua entram depois, como desconto dividido pelas linhas escritas — por isso, texto curto pesa duas vezes.</p>
<div class="formula">Nota = <span>NC</span> (conteúdo) − <span>NE</span> (erros) ÷ <span>TL</span> (linhas)</div>
<table><thead><tr><th>Situação (NC = 16)</th><th>Erros</th><th>Linhas</th><th>Nota final</th></tr></thead><tbody>
<tr><td class="k">Texto completo</td><td>6</td><td>30</td><td>15,80</td></tr>
<tr><td class="k">Texto no mínimo</td><td>6</td><td>20</td><td>15,70</td></tr>
<tr><td class="k">Texto curto demais</td><td>6</td><td>18</td><td>15,27 (−0,40 pelas 2 linhas que faltam)</td></tr>
</tbody></table>
<div class="box lr"><span class="eyebrow">Meta de extensão</span>Escreva entre <b>26 e 30 linhas</b>. Abaixo de 20 há desconto por linha e menos espaço para argumentar; acima de 30, o texto é cortado. Treine na folha pautada para saber quantas palavras cabem na sua linha.</div>
<span class="eyebrow">03</span><h2 class="sec">Roteiro de planejamento em cinco passos</h2>
<div class="passo"><div class="bn">1</div><div><h4>Sublinhe tema e recorte</h4>Separe o assunto (“câmeras corporais”) do recorte (“transparência e proteção do policial”). A tese precisa responder ao recorte inteiro.</div></div>
<div class="passo"><div class="bn">2</div><div><h4>Leia os textos motivadores</h4>Marque a ideia central e os dados úteis de cada um. Eles dão pistas, mas a argumentação é sua: não copie frases.</div></div>
<div class="passo"><div class="bn">3</div><div><h4>Tese em uma frase</h4>Responda ao recorte e anuncie os dois argumentos: “Torná-la efetiva exige superar dois desafios: X e Y.”</div></div>
<div class="passo"><div class="bn">4</div><div><h4>Dois argumentos, um repertório cada</h4>Um argumento por parágrafo, com fundamento (CF, lei, dado oficial) e consequência concreta.</div></div>
<div class="passo"><div class="bn">5</div><div><h4>Esqueleto e linhas</h4>Introdução 5–6 · desenvolvimento 7–8 · desenvolvimento 7–8 · conclusão 5–6. Palavras-chave de cada parágrafo, e só então o texto.</div></div>
</section>''',
'''<section class="pb"><span class="eyebrow">04</span><h2 class="sec">A estrutura que pontua</h2>
<p>Quatro parágrafos resolvem a prova com folga. O corretor encontra cada parte da estrutura dissertativa onde espera — e cada parte vale pontos no espelho.</p>
<div class="formula">Contexto + <span>Tese</span> → Argumento + Fundamento (×2) → Retomada + <span>Proposta</span></div>
<table><thead><tr><th>Parágrafo</th><th>O que faz</th><th>Exemplo de abertura</th></tr></thead><tbody>
<tr><td class="k">Introdução</td><td>Situa o tema com um dado ou norma e apresenta a tese</td><td>“A Constituição define a segurança pública como dever do Estado... Cumpri-lo, contudo, exige...”</td></tr>
<tr><td class="k">Desenvolvimento 1</td><td>Primeiro argumento: tópico frasal, explicação, fundamento</td><td>“Em primeiro lugar, ...”</td></tr>
<tr><td class="k">Desenvolvimento 2</td><td>Segundo argumento, diferente do primeiro</td><td>“Além disso, ...” / “Por outro lado, ...”</td></tr>
<tr><td class="k">Conclusão</td><td>Retoma a tese e propõe solução ligada aos argumentos</td><td>“Portanto, ... Cabe a [agente] [ação], por meio de [meio], a fim de [finalidade].”</td></tr>
</tbody></table>
<div class="box bad"><span class="eyebrow">Assim não pontua</span>“Nos dias de hoje, a violência é um tema de extrema importância, e todos devem refletir sobre ele, pois ela está cada vez maior.” — genérico, sem tese, serve para qualquer tema.</div>
<div class="box good"><span class="eyebrow">Assim pontua</span>“Em 2025, o Brasil registrou 1.571 feminicídios, novo recorde. Tornar efetivas as medidas protetivas exige superar dois desafios: a fiscalização insuficiente e a demora da resposta ao descumprimento.” — dado, recorte e argumentos anunciados.</div>
<h3>Proposta completa em uma frase</h3>
<p><b>Agente</b> (governo estadual, Polícia Militar, Judiciário, municípios) + <b>ação</b> (ampliar, capacitar, regulamentar) + <b>meio</b> (“por meio de...”) + <b>finalidade</b> (“a fim de que...”). Evite propostas vagas, como “conscientizar a população”, sem dizer quem faz e como.</p>
<h3>Conectivos que organizam</h3>
<p><b>Abrir argumentos:</b> “Em primeiro lugar”, “Além disso”, “Por outro lado”. <b>Explicar:</b> “Isso ocorre porque”, “Prova disso é”. <b>Concluir:</b> “Portanto”, “Dessa forma”. Varie: repetir o mesmo conectivo empobrece a coesão.</p>
</section>''',
    ]
