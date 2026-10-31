# -*- coding: utf-8 -*-
import textwrap, html, re
from content_rodadas import RODADAS

CSS = open('base.css').read() + """
.texto{border-left:3pt solid var(--lar);background:#fffdf9;padding:6pt 10pt;margin:0 0 8pt;font-size:9.6pt}
.texto .tt{font-family:Poppins;font-weight:700;color:var(--navy);font-size:8.6pt;letter-spacing:.06em;text-transform:uppercase;display:block;margin-bottom:3pt}
.texto p{margin:0 0 4pt}
.texto .fonte{font-size:8pt;color:var(--mu);font-style:italic;margin:2pt 0 0}
.comando{background:var(--navy);color:#fff;border-radius:7pt;padding:10pt 13pt;margin:8pt 0 0;font-size:10.2pt}
.comando b{color:#ffb39e}
.npr td:nth-child(n+2){text-align:center}
.rep td.k{width:30%}
.rep{font-size:8.5pt}.rep td{padding:3.5pt 6pt}.rep td:last-child{width:24%;font-size:8.2pt;color:#3a4452}
.esq,.pad,.esp{font-size:8.6pt}.esq td,.pad td,.esp td{padding:3pt 6pt}.pad li,.chk li{margin-bottom:1pt}
section.sol h3{margin:9pt 0 4pt}
"""

FOTO = open('foto_uri.txt').read().strip()

def folha(pars, width=67):
    lines = []
    for p in pars:
        # primeira linha com recuo: largura menor
        words = p.split()
        cur = ''
        first = True
        plines = []
        for w in words:
            lim = width - 4 if first else width
            cand = (cur + ' ' + w).strip()
            if len(cand) <= lim:
                cur = cand
            else:
                plines.append((cur, first))
                first = False
                cur = w
        plines.append((cur, first))
        for i, (t, f) in enumerate(plines):
            cls = []
            if f: cls.append('ini')
            if i == len(plines) - 1: cls.append('fim')
            lines.append((t, ' '.join(cls)))
    n = len(lines)
    out = []
    for i in range(30):
        if i < n:
            t, c = lines[i]
            out.append(f'<div class="ln"><span class="nr">{i+1}</span><span class="t {c}">{html.escape(t)}</span></div>')
        else:
            out.append(f'<div class="ln"><span class="nr">{i+1}</span><span class="t fim">&nbsp;</span></div>')
    return n, '\n'.join(out)

AUTOR = f'''<div class="autor"><div class="foto" style="background-image:url({FOTO})"></div>
<div><div class="nm">Samuel Wolf</div><div class="at">@auditor_discursivas</div><ul>
<li>Auditor de Controle Externo do TCE-RJ</li><li>Engenheiro de Infraestrutura Aeronáutica formado pelo ITA</li>
<li>Nomeado Auditor Fiscal da SEFAZ-RS e da SEFIN Manaus</li><li>Trabalha com discursivas há mais de seis anos</li></ul></div></div>'''

parts = []
A = parts.append

# ---------------- CAPA
A('''<section class="capa"><div class="barra"></div><div class="wm">AUDITOR DISCURSIVAS</div>
<div class="eyebrow" style="color:#ffb39e;margin-top:30mm">Aula especial · Instituto AOCP · Temas propostos</div>
<h1 style="margin-top:6mm">Redação da<br><span>PM-SC</span> 2026</h1>
<div class="sub">A dissertação de 20 a 30 linhas sobre Ordem Pública: o que o edital e o Instituto AOCP avaliam, como a nota é calculada, planejamento, estrutura e cinco rodadas com temas inéditos, critérios de correção e texto completo.</div>
<div class="tag">SOLDADO DO QUADRO DE PRAÇAS POLICIAL MILITAR · QPPM</div>
<div class="data">PROVA EM 13 DE DEZEMBRO DE 2026</div>
<div class="rod"><span>Banca Instituto AOCP · PM-SC 2026 · Edital n.º 002/CCP/2026 – CFP</span><span>@auditor_discursivas</span></div></section>''')

# ---------------- AUTOR
A(f'''<section class="pb"><span class="eyebrow">Antes de começar</span><h2 class="sec">Por que fiz esta aula gratuita</h2>
{AUTOR}
<p>Eu sou o Samuel. Passei por concursos com prova discursiva e sei na prática o quanto ela pesa — e o quanto assusta. Hoje, além do trabalho de auditor, ajudo concurseiros a escrever melhor na prova, com aulas e com recursos contra a nota da discursiva.</p>
<p>Fiz esta aula de graça por um motivo simples: quero ajudar. Na PM-SC, a redação vale 20 dos 80 pontos da primeira fase — um quarto da nota —, elimina quem fizer menos de 10 e tem uma vantagem rara: o edital já diz de onde sai o tema. Ele será escolhido dentro do conteúdo de <b>Ordem Pública</b> do Anexo II. Ou seja, dá para treinar com foco.</p>
<p>Aqui está o mesmo jeito que eu uso para analisar provas e preparar recursos: olhar o que a banca realmente cobra, planejar antes de escrever e construir um texto com tese clara, argumentos fundamentados e proposta no fim. Nada de fórmula mágica — método e treino.</p>
<div class="box lr"><span class="eyebrow">Combinado?</span>Leia com calma, escreva as rodadas na folha antes de olhar as soluções e, se tiver dúvida ou quiser compartilhar o que achou, me chama no <b>@auditor_discursivas</b>. Bons estudos!</div>
</section>''')

# ---------------- PALAVRA INICIAL + SUMÁRIO
rod_sum = ''.join(f"<tr><td class='n'>▸</td><td>Rodada {i+1} · {r['titulo']}</td></tr>" for i, r in enumerate(RODADAS))
A(f'''<section class="pb"><span class="eyebrow">Palavra inicial</span><h2 class="sec">Um tema, trinta linhas, uma tese</h2>
<p class="lead">A redação da PM-SC é uma dissertação de 20 a 30 linhas, feita a partir de textos motivadores, sobre um tema de Ordem Pública. Ela é aplicada junto com a prova objetiva, no mesmo período de cinco horas, e só é corrigida para quem passa na objetiva e fica entre os 2.000 primeiros.</p>
<p>A aula segue essa lógica. A Parte 1 mostra a prova, como a nota é calculada, o que o tema pode cobrar, um repertório pronto para usar, o roteiro de planejamento e a estrutura que pontua. A Parte 2 traz cinco rodadas completas, uma para cada eixo do Anexo II. A Parte 3 fecha com o dia da prova e o checklist.</p>
<div class="box nv"><span class="eyebrow">Regra central</span>Introdução com <b>tese clara</b>; um <b>argumento por parágrafo</b> de desenvolvimento, com fundamento (Constituição, lei, fato) aplicado ao tema; conclusão que retoma a tese com uma <b>proposta</b> concreta. E tudo dentro do recorte do tema: na AOCP, quem foge do tema tira zero (item 11.13, a).</div>
<h3>Sumário</h3>
<table class="sum"><tbody>
<tr class="pt"><td colspan="2">Parte 1 · Visão geral da prova</td></tr>
<tr><td class="n">01</td><td>A prova de redação da PM-SC 2026</td></tr>
<tr><td class="n">02</td><td>Como a nota é calculada</td></tr>
<tr><td class="n">03</td><td>De onde sai o tema: Ordem Pública no Anexo II</td></tr>
<tr><td class="n">04</td><td>Repertório de bolso para Ordem Pública</td></tr>
<tr><td class="n">05</td><td>Roteiro de planejamento em cinco passos</td></tr>
<tr><td class="n">06</td><td>A estrutura que pontua</td></tr>
<tr class="pt"><td colspan="2">Parte 2 · Cinco rodadas com temas inéditos</td></tr>
<tr><td class="n">07</td><td>Como usar as rodadas</td></tr>{rod_sum}
<tr class="pt"><td colspan="2">Parte 3 · O dia da prova</td></tr>
<tr><td class="n">08</td><td>As cinco horas da prova</td></tr>
<tr><td class="n">09</td><td>Checklist do dia da prova</td></tr>
</tbody></table>
<p class="nota">Fontes: Edital de Concurso Público n.º 002/CCP/2026 – CFP (PMSC/Instituto AOCP); cronograma e conteúdo do Anexo II conferidos em fontes secundárias; legislação citada em cada rodada. Os temas e as resoluções desta aula são material do curso e não constituem padrão oficial da banca.</p>
</section>''')

# ---------------- PARTE 1 · 01
A('''<section class="pb"><div class="parte"><span class="eyebrow">Parte 1</span><h2>Visão geral da prova</h2><p>Formato, cálculo da nota, conteúdo do tema, repertório, planejamento e estrutura.</p></div>
<span class="eyebrow">01</span><h2 class="sec">A prova de redação da PM-SC 2026</h2>
<div class="stats"><div class="stat"><div class="v">20</div><div class="l">pontos</div></div><div class="stat"><div class="v">10</div><div class="l">nota mínima</div></div><div class="stat"><div class="v">20–30</div><div class="l">linhas</div></div><div class="stat"><div class="v">2.000</div><div class="l">redações corrigidas</div></div><div class="stat"><div class="v">5 h</div><div class="l">objetiva + redação</div></div></div>
<p>A redação é aplicada em <b>13 de dezembro de 2026</b>, junto com a prova objetiva de 60 questões, em cidades de Santa Catarina. O tema é escolhido no conteúdo de Ordem Pública do Anexo II e baseia-se em um ou mais textos motivadores; a tipologia exigida é a dissertação (itens 11.1 e 11.2).</p>
<table><thead><tr><th>Ponto do edital</th><th>O que isso significa para você</th></tr></thead><tbody>
<tr><td class="k">Peso na nota</td><td>A primeira fase vale 80 pontos: 60 da objetiva e 20 da redação (Tabela 8.1). A redação é um quarto da nota e soma na classificação.</td></tr>
<tr><td class="k">Quem tem a redação corrigida</td><td>Só quem atinge o mínimo da objetiva — 50% dos pontos, sem zerar área — e está até a 2.000.ª posição, incluídos os empatados com o último. Os demais são eliminados (itens 11.1.1 a 11.1.3).</td></tr>
<tr><td class="k">Nota mínima</td><td>Quem tirar menos de 10,00 na redação está eliminado (item 11.4).</td></tr>
<tr><td class="k">Extensão</td><td>Mínimo de 20 e máximo de 30 linhas. O que passar da 30.ª linha ou ficar fora do espaço é desconsiderado; cada linha que faltar para 20 custa 0,20 ponto (itens 11.5, d e g, e 11.7).</td></tr>
<tr><td class="k">Folha e caneta</td><td>Só a Folha de Redação Definitiva vale; o rascunho não é corrigido. Caneta esferográfica de material transparente, tinta azul ou preta, letra legível (itens 11.6 e 11.8).</td></tr>
<tr><td class="k">Consulta</td><td>Nada pode ser consultado, exceto o texto de apoio da própria prova (item 11.11).</td></tr>
</tbody></table>
<div class="box bad"><span class="eyebrow">Nota zero e eliminação (item 11.13)</span>Não desenvolver o tema proposto; letra ilegível ou outro meio que não o determinado; desestruturação textual acentuada ou texto que atente contra o pudor; escrever a lápis ou com tinta de outra cor; não entregar a folha definitiva, entregá-la em branco ou com espaçamento excessivo e margens irregulares; identificar-se de qualquer forma — nome, números, letras, sinais, desenhos ou códigos. A folha também não pode ser assinada nem rubricada fora do local próprio (item 11.9).</div>
</section>''')

# ---------------- 02 nota
A('''<section class="pb"><span class="eyebrow">02</span><h2 class="sec">Como a nota é calculada</h2>
<p>O Instituto AOCP corrige a redação em duas frentes: o <b>conteúdo</b> e o <b>domínio da língua escrita</b> (item 11.3). O conteúdo gera uma nota de até 20 pontos; os erros de português entram como desconto, proporcional ao tamanho do texto (item 11.5).</p>
<div class="formula">Nota da redação = <span>Nota de conteúdo</span> − (<span>nº de erros</span> ÷ <span>nº de linhas escritas</span>)</div>
<table><thead><tr><th>Sigla do edital</th><th>O que é</th></tr></thead><tbody>
<tr><td class="k">NC · Nota de conteúdo (até 20)</td><td>Atendimento ao tema proposto; desenvolvimento do tema; coesão; coerência; estrutura do texto dissertativo-argumentativo e dos parágrafos.</td></tr>
<tr><td class="k">NE · Número de erros</td><td>Erros de ortografia, morfossintaxe (concordância, regência, crase, colocação) e pontuação.</td></tr>
<tr><td class="k">TL · Total de linhas</td><td>Linhas efetivamente escritas pelo candidato.</td></tr>
</tbody></table>
<h3>Três exemplos, com a mesma nota de conteúdo (16)</h3>
<table class="npr"><thead><tr><th>Situação</th><th>Erros</th><th>Linhas</th><th>Desconto</th><th>Nota final</th></tr></thead><tbody>
<tr><td class="k">Texto completo</td><td>6</td><td>30</td><td>0,20</td><td>15,80</td></tr>
<tr><td class="k">Texto no mínimo</td><td>6</td><td>20</td><td>0,30</td><td>15,70</td></tr>
<tr><td class="k">Texto curto demais</td><td>6</td><td>18</td><td>0,33 + 0,40 (2 linhas faltando)</td><td>15,27</td></tr>
</tbody></table>
<div class="box nv"><span class="eyebrow">O que isso muda na sua estratégia</span>Quase toda a nota está no <b>conteúdo</b>: tema bem atendido, argumentos desenvolvidos, texto coeso e bem estruturado. Por isso, o tempo de planejamento vale ouro. O desconto por erro é pequeno por erro isolado, mas não se engane: erros em excesso também prejudicam a clareza e a coesão, que estão dentro da nota de conteúdo — e um texto ilegível ou com desestruturação acentuada vai a zero.</div>
<div class="box lr"><span class="eyebrow">Meta de extensão</span>Escreva entre <b>26 e 30 linhas</b>. Abaixo de 20 você perde 0,20 por linha e ainda dá menos espaço para argumentar; acima de 30, o texto é cortado. Treine na folha pautada para conhecer o seu número de palavras por linha.</div>
</section>''')

# ---------------- 03 tema
A('''<section class="pb"><span class="eyebrow">03</span><h2 class="sec">De onde sai o tema: Ordem Pública no Anexo II</h2>
<p>O edital reservou um bloco de conteúdo <b>só para a redação</b>: Ordem Pública. O tema da prova será escolhido dentro dele (item 11.2). Isso é uma vantagem enorme: em vez de “atualidades” em geral, você sabe exatamente quais assuntos treinar.</p>
<table><thead><tr><th>Eixo do Anexo II</th><th>O que dominar</th><th>Temas possíveis</th></tr></thead><tbody>
<tr><td class="k">Sistema de justiça criminal</td><td>Os órgãos e a sequência (polícia → Ministério Público → Judiciário → execução penal); prisão em flagrante e audiência de custódia; termo circunstanciado; sistema prisional</td><td>Integração dos órgãos, reincidência, superlotação, celeridade da resposta ao crime</td></tr>
<tr><td class="k">Políticas públicas de ordem pública e cidadania</td><td>Segurança como “responsabilidade de todos”; polícia comunitária; prevenção; Susp (Lei n.º 13.675/2018); programas da PMSC; tecnologia e transparência</td><td>Polícia comunitária, prevenção da violência, violência contra a mulher, tecnologia e transparência, juventude</td></tr>
<tr><td class="k">Ordem Pública na CF/1988</td><td>Competências das polícias militares (art. 144, § 5.º); força auxiliar e reserva do Exército (art. 144, § 6.º); hierarquia e disciplina (art. 42); Lei Orgânica Nacional (Lei n.º 14.751/2023)</td><td>Papel da PM, policiamento ostensivo, hierarquia e disciplina na democracia, legitimidade da atuação policial</td></tr>
</tbody></table>
<h3>Como o Instituto AOCP propõe o tema</h3>
<p>O edital da PM-SC descreve o formato: um <b>tema proposto</b>, apoiado em <b>um ou mais textos motivadores</b>, e um texto na tipologia <b>dissertação</b>. Nas redações de Polícia Militar da AOCP que circulam em bancos de propostas (PMDF e PMPE, por exemplo), o tema costuma vir como uma frase nominal que já indica o recorte: “Desafios para...”, “Obstáculos para...”. Por isso, duas rodadas desta aula usam esse formato, e as outras variam o recorte (a importância de algo, a relação entre dois conceitos), para você treinar a leitura de recortes diferentes. Confira também, no caderno, se a banca pede título: o edital não exige, mas a instrução da prova prevalece.</p>
<div class="box cre"><span class="eyebrow">Leia o recorte, não só o assunto</span>“Polícia Militar” é assunto. “<b>Desafios para</b> a preservação da ordem pública pela Polícia Militar” é tema, com recorte. Um texto que só elogia a PM, sem apontar desafios, fala do assunto e foge do recorte — e o edital prevê nota zero para quem não desenvolve o tema proposto.</div>
<p>No concurso anterior, de 2023, organizado pelo Cebraspe, a discursiva de Soldado também foi um texto dissertativo de 20 a 30 linhas sobre tema relacionado à ordem pública. A banca mudou, mas o eixo do conteúdo se manteve.</p>
<div class="box lr"><span class="eyebrow">Use os textos motivadores do jeito certo</span>Eles dão pistas do recorte e trazem dados, mas a argumentação precisa ser sua. Não copie frases: reescreva a ideia com suas palavras e acrescente o que você sabe. Lembre: você escreve sobre o <b>tema</b>, não sobre os textos.</div>
</section>''')

# ---------------- 04 repertório
A('''<section class="pb"><span class="eyebrow">04</span><h2 class="sec">Repertório de bolso para Ordem Pública</h2>
<p>Repertório é aquilo que você traz de fora para fundamentar o argumento. Para esta prova, o melhor repertório é jurídico e institucional — e cabe em quase qualquer tema do Anexo II. Memorize a ideia central e o número do dispositivo.</p>
<table class="rep"><thead><tr><th>Referência</th><th>O que diz (em resumo)</th><th>Serve para temas sobre</th></tr></thead><tbody>
<tr><td class="k">CF, art. 144, caput</td><td>Segurança pública é dever do Estado, direito e responsabilidade de todos, exercida para preservar a ordem pública e a incolumidade das pessoas e do patrimônio</td><td>Qualquer tema; participação cidadã</td></tr>
<tr><td class="k">CF, art. 144, § 5.º</td><td>Às polícias militares cabem a polícia ostensiva e a preservação da ordem pública</td><td>Papel da PM, prevenção</td></tr>
<tr><td class="k">CF, art. 144, § 6.º</td><td>PMs e bombeiros militares são forças auxiliares e reserva do Exército e se subordinam aos governadores</td><td>Natureza militar, controle civil</td></tr>
<tr><td class="k">CF, art. 42 e § 1.º</td><td>PMs são instituições organizadas com base na hierarquia e disciplina; aos militares estaduais aplicam-se regras do art. 142, como a proibição de greve e sindicalização</td><td>Hierarquia, disciplina, continuidade do serviço</td></tr>
<tr><td class="k">Lei n.º 14.751/2023</td><td>Lei Orgânica Nacional das PMs e CBMs: princípios (hierarquia, disciplina, direitos humanos, legalidade, transparência, participação comunitária) e diretrizes (integração, evidências, tecnologia, uso racional da força)</td><td>Quase todos os temas</td></tr>
<tr><td class="k">Lei n.º 13.675/2018</td><td>Cria o Susp e a Política Nacional de Segurança Pública e Defesa Social: atuação integrada dos entes, em articulação com a sociedade</td><td>Integração, políticas públicas</td></tr>
<tr><td class="k">CPP, art. 310</td><td>Audiência de custódia em até 24 horas após a prisão em flagrante</td><td>Justiça criminal, direitos fundamentais</td></tr>
<tr><td class="k">Lei n.º 9.099/1995, art. 69 · STF, ADI 5.637</td><td>Termo circunstanciado para infrações de menor potencial ofensivo; o STF admitiu sua lavratura pela PM</td><td>Integração, eficiência do policiamento</td></tr>
<tr><td class="k">CF, art. 129, VII · CPM, art. 38, § 2.º</td><td>O Ministério Público exerce o controle externo da atividade policial; o subordinado que cumpre ordem manifestamente criminosa também responde</td><td>Hierarquia, legalidade, controle</td></tr>
<tr><td class="k">STF, ADPF 347 (2015 e 2023)</td><td>“Estado de coisas inconstitucional” no sistema prisional; determinou a realização das audiências de custódia</td><td>Sistema prisional, reincidência, facções</td></tr>
<tr><td class="k">Rede de Vizinhos (PMSC, 2016)</td><td>Grupos de moradores e comerciantes com os policiais da área, baseados na polícia comunitária</td><td>Prevenção, participação cidadã</td></tr>
<tr><td class="k">Rede Catarina · Patrulha Maria da Penha (PMSC)</td><td>Proteção à mulher, com visitas e acompanhamento de mulheres em situação de violência</td><td>Violência doméstica, prevenção</td></tr>
<tr><td class="k">Lei Maria da Penha, art. 12-C · STF, ADI 6.138</td><td>Em risco à vida ou à integridade da mulher, o agressor é afastado do lar pelo juiz, pelo delegado (sem comarca) ou pelo policial (sem comarca e sem delegado); juiz comunicado em 24 h</td><td>Violência doméstica, resposta imediata</td></tr>
</tbody></table>
<p class="nota"><b>Como citar:</b> cite e aplique na mesma frase. Se não tiver certeza do número do artigo, cite só a lei (“a Constituição Federal”, “a Lei Orgânica Nacional das Polícias Militares”).</p>
</section>''')

# ---------------- 05 roteiro
A('''<section class="pb"><span class="eyebrow">05</span><h2 class="sec">Roteiro de planejamento em cinco passos</h2>
<p>Com cinco horas para 60 questões e a redação, há tempo para planejar com calma. O planejamento leva de 15 a 20 minutos e evita o pior erro da prova: fugir do recorte do tema.</p>
<div class="passo"><div class="bn">1</div><div><h4>Sublinhe o tema e o recorte</h4>Separe o assunto (“ordem pública”) do recorte (“desafios para...”, “a importância de...”, “o papel de...”). O recorte define o que a sua tese precisa responder.</div></div>
<div class="passo"><div class="bn">2</div><div><h4>Leia os textos motivadores</h4>Marque a ideia central de cada um e os dados úteis. Pergunte: que pista cada texto dá para um argumento?</div></div>
<div class="passo"><div class="bn">3</div><div><h4>Escreva a tese em uma frase</h4>A tese responde ao recorte e anuncia os dois argumentos: “Cumpri-la exige superar dois desafios: X e Y.”</div></div>
<div class="passo"><div class="bn">4</div><div><h4>Escolha dois argumentos e um repertório para cada</h4>Um argumento por parágrafo, cada um com fundamento (CF, lei, decisão, programa) e um exemplo ou consequência concreta.</div></div>
<div class="passo"><div class="bn">5</div><div><h4>Monte o esqueleto e distribua as linhas</h4>Palavras-chave de cada parágrafo e quantas linhas ele terá. Escreva o rascunho seguindo o esqueleto e passe a limpo com folga de tempo.</div></div>
<h3>Texto escolar × redação de concurso</h3>
<table><thead><tr><th>Critério</th><th>Redação escolar</th><th>Redação da PM-SC</th></tr></thead><tbody>
<tr><td class="k">Abertura</td><td>Longa, com frases de efeito</td><td>Contexto curto e tese já na introdução</td></tr>
<tr><td class="k">Repertório</td><td>Citações filosóficas e históricas</td><td>Constituição, leis, decisões e programas de segurança pública</td></tr>
<tr><td class="k">Desenvolvimento</td><td>Ideias soltas</td><td>Um argumento por parágrafo, com fundamento e exemplo</td></tr>
<tr><td class="k">Tom</td><td>Opinativo, emotivo</td><td>Técnico, institucional e equilibrado</td></tr>
<tr><td class="k">Fechamento</td><td>Resumo do texto</td><td>Retomada da tese + proposta: quem faz, o quê, como e para quê</td></tr>
</tbody></table>
</section>''')

# ---------------- 06 estrutura
A('''<section class="pb"><span class="eyebrow">06</span><h2 class="sec">A estrutura que pontua</h2>
<p>Quatro parágrafos resolvem a prova com folga: introdução, dois de desenvolvimento e conclusão. Assim, o corretor encontra cada parte da estrutura dissertativa exatamente onde espera.</p>
<div class="formula">Contexto + <span>Tese</span> → Argumento + <span>Fundamento</span> + Exemplo (×2) → Retomada + <span>Proposta</span></div>
<table><thead><tr><th>Parágrafo</th><th>Linhas</th><th>O que faz</th><th>Exemplo de abertura</th></tr></thead><tbody>
<tr><td class="k">Introdução</td><td>5–6</td><td>Situa o tema com um dado ou norma e apresenta a tese</td><td>“A Constituição Federal atribui às polícias militares... Cumpri-la, contudo, exige...”</td></tr>
<tr><td class="k">Desenvolvimento 1</td><td>7–9</td><td>Primeiro argumento: tópico frasal, explicação, fundamento, exemplo</td><td>“Em primeiro lugar, ...”</td></tr>
<tr><td class="k">Desenvolvimento 2</td><td>7–9</td><td>Segundo argumento, diferente do primeiro</td><td>“Além disso, ...” / “Por outro lado, ...”</td></tr>
<tr><td class="k">Conclusão</td><td>5–6</td><td>Retoma a tese e propõe solução ligada aos argumentos</td><td>“Portanto, ... Cabe a [agente] [ação], a fim de que [finalidade].”</td></tr>
</tbody></table>
<div class="box bad"><span class="eyebrow">Assim não pontua</span>“Nos dias de hoje, a segurança pública é um tema de extrema importância na sociedade, e todos devem refletir sobre ele, pois a violência está cada vez maior.” — genérico, sem tese, serve para qualquer tema.</div>
<div class="box good"><span class="eyebrow">Assim pontua</span>“A Constituição Federal atribui às polícias militares a polícia ostensiva e a preservação da ordem pública (art. 144, § 5.º). Cumpri-la no Brasil atual, contudo, exige superar dois desafios: a insuficiência de efetivo e a distância entre a polícia e as comunidades.” — situa, fundamenta e anuncia os argumentos.</div>
<h3>Conectivos que organizam o texto</h3>
<p><b>Para abrir argumentos:</b> “Em primeiro lugar”, “Inicialmente”, “Além disso”, “Ademais”, “Por outro lado”. <b>Para explicar e exemplificar:</b> “Isso ocorre porque”, “Não por acaso”, “Prova disso é”, “Nesse sentido”. <b>Para concluir:</b> “Portanto”, “Logo”, “Conclui-se, portanto”, “Dessa forma”. Varie: repetir o mesmo conectivo empobrece a coesão.</p>
<div class="box cre"><span class="eyebrow">Proposta completa em uma frase</span><b>Agente</b> (governo estadual, Polícia Militar, municípios, escolas) + <b>ação</b> (recompor, capacitar, regulamentar, expandir) + <b>meio</b> (por meio de...) + <b>finalidade</b> (a fim de que...). Evite propostas vagas, como “conscientizar a população”, sem dizer quem faz e como.</div>
</section>''')

# ---------------- PARTE 2
A('''<section class="pb"><div class="parte"><span class="eyebrow">Parte 2</span><h2>Cinco rodadas com temas inéditos</h2><p>Uma rodada para cada eixo de Ordem Pública · formato Instituto AOCP · 20 a 30 linhas · 20 pontos</p></div>
<span class="eyebrow">07</span><h2 class="sec">Como usar as rodadas</h2>
<p>Cada rodada traz uma proposta inédita no formato do edital: tema, textos motivadores e comando. Na página seguinte vêm o esqueleto do planejamento, a abordagem esperada e os critérios de correção. Por fim, uma proposta de texto definitivo, na folha de 30 linhas, com armadilhas, erros comuns e dicas.</p>
<table><thead><tr><th>Rodada</th><th>Tema</th><th>Eixo do Anexo II</th></tr></thead><tbody>''' +
''.join(f"<tr><td class='k'>{i+1}</td><td>{r['tema']}</td><td>{r['eixo']}</td></tr>" for i, r in enumerate(RODADAS)) +
'''</tbody></table>
<div class="box nv"><span class="eyebrow">Faça antes de olhar</span>Planeje (15 min), escreva o rascunho (40 min) e passe a limpo à mão numa folha de 30 linhas (25 min). Só depois compare com a solução.</div>
<div class="box cre"><span class="eyebrow">Sobre os critérios de correção</span>O edital informa os critérios da nota de conteúdo (tema, desenvolvimento, coesão, coerência e estrutura), mas não divide os 20 pontos entre eles. A distribuição usada nas rodadas (5 + 7 + 4 + 4) é um <b>modelo didático</b> para você se autoavaliar. Os erros de língua entram depois, pela fórmula da seção 02. Trechos de lei são transcritos do texto oficial; os demais textos motivadores foram elaborados para o treino, com base nas fontes indicadas.</div>

</section>''')

for i, r in enumerate(RODADAS):
    n = i + 1
    textos = ''.join(f'<div class="texto"><span class="tt">{t}</span>{c}<p class="fonte">{f}</p></div>' for t, c, f in r['textos'])
    A(f'''<section class="pb rod-h"><span class="eyebrow">Rodada {n} · Redação · 20 a 30 linhas · 20 pontos</span>
<h2><span class="rn">{n}.</span> {r['titulo']}</h2>
<div class="eixo"><b>Eixo do edital:</b> {r['eixo']}. Tema inédito, no formato do Instituto AOCP, elaborado para treino.</div>
<div class="enun"><span class="eyebrow">Proposta de redação · inédita · formato Instituto AOCP</span>
{textos}
<div class="comando">Com base nos textos motivadores e em seus conhecimentos, redija uma <b>dissertação</b>, de 20 a 30 linhas, sobre o tema: <b>“{r['tema']}”</b>.</div></div>
<div class="pare">Pare aqui. Planeje e escreva a sua redação em até 30 linhas, cronometrando cerca de 80 minutos, antes de virar a página. A solução começa na próxima página.</div>
</section>''')
    esq = ''.join(f'<tr><td class="k">{a}</td><td>{b}</td></tr>' for a, b in r['esqueleto'])
    abo = ''.join(f'<tr><td class="k">{a}</td><td><ul>' + ''.join(f'<li>{x}</li>' for x in b) + '</ul></td></tr>' for a, b in r['abordagem'])
    cri = ''.join(f'<tr><td class="q">{a}</td><td><ul class="chk">' + ''.join(f'<li>{x}</li>' for x in b) + f'</ul></td><td>{p}</td></tr>' for a, b, p in r['criterios'])
    A(f'''<section class="pb sol"><h3 style="margin-top:0">Como montar o esqueleto</h3>
<table class="esq"><thead><tr><th>Parágrafo</th><th>Palavras-chave do rascunho</th></tr></thead><tbody>{esq}</tbody></table>
<h3>Abordagem esperada (padrão do curso)</h3>
<table class="pad"><thead><tr><th>Parte</th><th>O que o texto deve conter</th></tr></thead><tbody>{abo}</tbody></table>
<h3>Critérios de correção (modelo didático) · nota de conteúdo · 20,00 pontos</h3>
<p class="nota">Distribuição didática dos critérios do item 11.5, a, do edital. Depois, aplica-se o desconto por erros: nota de conteúdo − (erros ÷ linhas).</p>
<table class="esp"><thead><tr><th>Critério</th><th>O que o corretor procura</th><th>Pontos</th></tr></thead><tbody>{cri}
<tr class="tot"><td>Total</td><td></td><td>20,00</td></tr></tbody></table>
</section>''')
    nl, fl = folha(r['redacao'])
    t1, t2, t3 = r['tri']
    ul = lambda xs: '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
    A(f'''<section class="pb"><h3 style="margin-top:0">Proposta de redação definitiva · {nl} de 30 linhas</h3>
<div class="folha"><span class="eyebrow">TEXTO DEFINITIVO · REDAÇÃO · 30 LINHAS</span>
{fl}
</div>
<p class="nota">Contagem simulada com cerca de 67 caracteres por linha. Em letra maior (cerca de 60 caracteres), o mesmo texto chega perto de 30 linhas: treine na folha.</p>
<div class="tri"><div class="t1"><span class="eyebrow">Armadilhas do tema</span>{ul(t1)}</div><div class="t2"><span class="eyebrow">Erros mais comuns</span>{ul(t2)}</div><div class="t3"><span class="eyebrow">Dicas estratégicas</span>{ul(t3)}</div></div>
</section>''')
    print(f'Rodada {n}: {nl} linhas')

# ---------------- PARTE 3
A('''<section class="pb"><div class="parte"><span class="eyebrow">Parte 3</span><h2>O dia da prova</h2><p>Gestão das cinco horas e conferência final</p></div>
<span class="eyebrow">08</span><h2 class="sec">As cinco horas da prova</h2>
<p>A prova objetiva (60 questões) e a redação são feitas no mesmo período de 5 horas, incluído o tempo de preencher a folha de respostas e a folha definitiva da redação, sem prorrogação (item 9.20). A saída da sala só é permitida depois de 60 minutos do início (item 9.16). Vale decidir antes de entrar como dividir o tempo. Uma sugestão:</p>
<table><thead><tr><th>Tempo</th><th>Etapa</th></tr></thead><tbody>
<tr><td class="k">10 min</td><td>Ler o tema e os textos motivadores logo no início: o cérebro trabalha no tema enquanto você faz a objetiva</td></tr>
<tr><td class="k">2 h 30</td><td>Prova objetiva (cerca de 2,5 minutos por questão)</td></tr>
<tr><td class="k">15–20 min</td><td>Planejamento: tese, dois argumentos, repertório e esqueleto com linhas</td></tr>
<tr><td class="k">40 min</td><td>Rascunho completo</td></tr>
<tr><td class="k">25–30 min</td><td>Passar a limpo na folha definitiva, com letra legível</td></tr>
<tr><td class="k">Restante</td><td>Revisão da redação e transcrição do gabarito, com folga</td></tr>
</tbody></table>
<div class="box lr"><span class="eyebrow">Não deixe a redação para o fim</span>A redação só é corrigida se você passar na objetiva, mas vale um quarto da nota e elimina abaixo de 10. Reserve pelo menos 1 h 20 para ela e fixe um horário-limite para parar a objetiva.</div>
<h3>Sete erros que custam a vaga</h3>
<ul><li>Fugir do recorte: escrever sobre “segurança pública” quando o tema pede “desafios para...” (item 11.13, a).</li>
<li>Introdução genérica, sem tese.</li>
<li>Copiar trechos dos textos motivadores em vez de argumentar.</li>
<li>Repertório decorado e solto, sem ligação com o argumento.</li>
<li>Conclusão sem proposta ou com proposta vaga (“é preciso conscientizar”).</li>
<li>Escrever menos de 20 linhas (−0,20 por linha) ou passar da 30.ª (texto cortado).</li>
<li>Assinar, escrever o nome ou deixar qualquer marca na folha definitiva (item 11.13, f).</li></ul>
</section>''')

A('''<section class="pb"><span class="eyebrow">09</span><h2 class="sec">Checklist do dia da prova</h2>
<div class="tri"><div class="t1"><span class="eyebrow">Antes de passar a limpo</span><ul><li>A tese responde ao recorte do tema?</li><li>Cada parágrafo de desenvolvimento tem um argumento diferente?</li><li>Há fundamento (CF, lei, programa) aplicado em cada argumento?</li><li>A conclusão tem agente, ação e finalidade?</li><li>O rascunho cabe entre 26 e 30 linhas?</li></ul></div>
<div class="t3"><span class="eyebrow">Depois de passar a limpo</span><ul><li>Nada além da linha 30 nem fora do espaço.</li><li>Nenhuma assinatura, nome ou marca.</li><li>Caneta azul ou preta, letra legível.</li><li>Acentos, crases, concordâncias e vírgulas revisados.</li><li>Nenhuma frase copiada dos textos motivadores.</li></ul></div></div>
<div class="box nv"><span class="eyebrow">Última palavra</span>Boa parte da nota depende de três coisas: entender o recorte do tema, sustentar a tese com dois argumentos bem fundamentados e fechar com uma proposta concreta. Treine até isso ficar automático.</div>
<h3>Fontes</h3>
<ul class="fontes">
<li>PMSC. Edital de Concurso Público n.º 002/CCP/2026 – CFP (Instituto AOCP), itens 8, 9.16, 9.20, 9.21 e 11.1 a 11.13 (cópia em cdn.direcaoconcursos.com.br; autenticidade: processo PMSC 00057417/2026).</li>
<li>Cronograma, Anexo II (Ordem Pública), nota final e critérios do item 11.5, a, conferidos em fontes secundárias: Você Concursado (“Concurso PM SC 2026: discursiva Instituto AOCP”), Gran Cursos Online e Nova Concursos (out. 2026).</li>
<li>Concurso de 2023 (Cebraspe): Você Concursado e Estratégia Concursos. Temas de PM do Instituto AOCP: banco de propostas do Projeto Agatha.</li>
<li>Constituição Federal (arts. 42, 129, 142 e 144); Código Penal Militar (art. 38); Lei n.º 14.751/2023; Lei n.º 13.675/2018; Lei n.º 9.099/1995; Código de Processo Penal (art. 310); STF, ADI 5.637 (2022) e ADPF 347 (medida cautelar de 2015 e mérito de 2023).</li>
<li>Rede de Vizinhos: Trevisan, dissertação de mestrado (UDESC, 2019); Jornal dos Condomínios (SC). Rede Catarina, Patrulha Maria da Penha e botão do pânico: documentos da ALESC, estudo publicado pela Univali e NSC Total. Lei n.º 11.340/2006 (art. 12-C, incluído pela Lei n.º 13.827/2019) e STF, ADI 6.138 (2022).</li>
</ul>
<p class="nota">O edital prevalece sobre qualquer resumo, inclusive este. Confira datas e regras no texto oficial e no site do Instituto AOCP.</p>
</section>''')

A(f'''<section class="pb"><span class="eyebrow">Uma palavra final</span><h2 class="sec">Obrigado por ter lido até aqui</h2>
{AUTOR}
<p>Eu sou o Samuel. Passei pelos dois lados da discursiva: como candidato, em concursos da área fiscal e de controle, e hoje como auditor que escreve textos técnicos todos os dias. Há mais de seis anos ajudo concurseiros a escrever melhor na prova — com aulas e com recursos contra a nota da discursiva.</p>
<p>Montei esta aula do mesmo jeito que analiso uma prova: olhando o que a banca realmente cobra e o que faz um texto ganhar ou perder pontos. Se ela te ajudou a enxergar a redação da PM-SC com mais clareza, já valeu.</p>
<div class="box lr"><span class="eyebrow">Gostou do material?</span>Comenta lá no <b>@auditor_discursivas</b> o que você achou. Parece pouco, mas cada comentário ajuda muito o meu trabalho e faz este material chegar a mais gente que está na mesma luta que você. Por lá eu sempre posto conteúdo sobre discursivas: estrutura, análise de provas e padrões das bancas.</div>
<p>Eu torço muito por você. Estude com método, treine na folha, cronometre os textos e chegue ao dia 13 de dezembro confiando no que você construiu.</p>
<div class="cta"><span class="eyebrow">E se a nota não vier como você esperava?</span>Não aceite a nota de cara. Pelo cronograma preliminar, o resultado da redação e a resposta padrão saem em <b>15/01/2027</b>, e o prazo de recurso é de <b>apenas dois dias: 18 e 19/01/2027</b>. O espelho da sua folha de redação fica disponível no site do Instituto AOCP durante esse prazo (item 9.21). Um recurso bem fundamentado mostra, critério por critério, o que o seu texto já trazia e não foi pontuado — e confere a contagem de erros e de linhas. Com nota mínima de 10 e a redação valendo um quarto da nota, isso pode ser a diferença entre a eliminação e a vaga.<br><br><b>Me chama no direct do @auditor_discursivas</b> que a gente analisa a sua prova juntos e prepara o recurso. A análise de viabilidade é gratuita.</div>
<p style="margin-top:12pt">Um abraço e boa prova,<br><b>Samuel Wolf</b></p>
</section>''')

doc = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Redação PM-SC 2026 · Auditor Discursivas</title>
<style>{CSS}</style></head><body>
{''.join(parts)}
</body></html>'''
open('aula_pmsc.html', 'w').write(doc)
print('ok', len(doc))
