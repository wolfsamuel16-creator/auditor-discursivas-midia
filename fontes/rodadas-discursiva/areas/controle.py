# -*- coding: utf-8 -*-
# Trilha CONTROLE — mini-aula (baseada na aula gratuita da CGU 2026, seções 03 a 08)
NOME = 'Controle'
PALAVRA = 'CONTROLE'
SUBTITULO = 'Treino de discursiva para tribunais de contas, CGU e controladorias.'
PUBLICO = 'TCU · TCEs · TCMs · CGU · CGEs · CONTROLE INTERNO E EXTERNO'
FORMATO_CURTO = 'texto dissertativo com aspectos'
PADRAO_BANCA = 'padrão Cebraspe'
NOTA_DESCONTO = ('Depois da nota de conteúdo, o Cebraspe desconta os erros de língua em proporção às linhas escritas. '
                 'Exemplo do edital da CGU 2026 para a questão de 30 linhas: nota = NC − 6 × NE ÷ TL. Confira a fórmula no edital do seu concurso.')

def aula():
    return [
'''<section class="pb"><div class="parte"><span class="eyebrow">Mini-aula · Trilha Controle</span><h2>Como a discursiva de controle pontua</h2><p>O que as bancas cobram, como corrigem e o parágrafo que soma pontos.</p></div>
<span class="eyebrow">01</span><h2 class="sec">O que as bancas de controle cobram</h2>
<p>Nas provas de tribunais de contas e controladorias, a discursiva quase nunca é redação de opinião. É <b>texto técnico</b>: a banca dá um tema, lista os aspectos que você deve abordar e corrige com um espelho em que cada aspecto vale um quesito.</p>
<table><thead><tr><th>Prova (Cebraspe)</th><th>Formato</th><th>O que foi cobrado</th></tr></thead><tbody>
<tr><td class="k">TCE-RJ 2021 · Analista</td><td>3 questões de 20 l. + parecer de 50 l.</td><td>Contas irregulares por dispensa indevida; três linhas de defesa</td></tr>
<tr><td class="k">TCDF 2021 · Auditor</td><td>2 questões de 20 l. + relatório de 50 l.</td><td>Custos no setor público; matriz de achados; controles internos (COSO)</td></tr>
<tr><td class="k">TCE-PB 2018 · Auditor</td><td>Texto de 30 l.</td><td>Mínimos da saúde na LOA; emendas parlamentares e orçamento impositivo</td></tr>
<tr><td class="k">CGE-RJ 2024 · Auditor</td><td>Texto de 30 l.</td><td>Materialidade, risco e relevância; requisitos dos achados; evidências</td></tr>
<tr><td class="k">TCE-MS 2025 · Auditor</td><td>3 questões de 20 l. + peça de 60 l.</td><td>Classificação da despesa; condição, critério, causa e efeito</td></tr>
</tbody></table>
<div class="box nv"><span class="eyebrow">O que se repete</span>Cinco blocos aparecem prova após prova: <b>controle interno e externo</b> (CF, arts. 70 a 75), <b>governança e riscos</b> (três linhas, COSO), <b>contratações</b> (Lei n.º 14.133/2021), <b>orçamento e LRF</b> e <b>auditoria governamental</b> (achados, evidência, materialidade). As cinco rodadas da trilha passam por todos eles.</div>
<p class="nota">Fonte: cadernos de prova e padrões de resposta publicados pelo Cebraspe, reunidos na aula gratuita da CGU 2026 do @auditor_discursivas.</p>
</section>''',
'''<section class="pb"><span class="eyebrow">02</span><h2 class="sec">Como a nota é calculada</h2>
<p>O corretor tem um <b>espelho</b>: um quesito de apresentação (legibilidade, margens, parágrafos) e um quesito para cada aspecto do comando, com conceitos graduados (0, 1, 2, 3...). Introdução e conclusão, em geral, <b>não são quesito</b>. Depois vem o desconto dos erros de língua, dividido pelas linhas escritas.</p>
<div class="formula">Nota = <span>NC</span> (conteúdo, por quesito) − <span>peso</span> × <span>NE</span> (erros) ÷ <span>TL</span> (linhas)</div>
<div class="box lr"><span class="eyebrow">O que isso muda na estratégia</span>Cada aspecto do comando vale pontos próprios: <b>nunca troque um aspecto por introdução</b>. E escreva perto do limite de linhas: o desconto por erro é dividido pelas linhas escritas, então um texto de 18 linhas paga mais caro por erro do que um de 29.</div>
<span class="eyebrow">03</span><h2 class="sec">Texto técnico × redação escolar</h2>
<table><thead><tr><th>Critério</th><th>Redação escolar</th><th>Discursiva de controle</th></tr></thead><tbody>
<tr><td class="k">Objetivo</td><td>Defender uma tese</td><td>Responder exatamente ao que o comando pede</td></tr>
<tr><td class="k">Abertura</td><td>Longa, com contextualização</td><td>Opcional e curta (1 a 2 linhas)</td></tr>
<tr><td class="k">Repertório</td><td>Cultural e histórico</td><td>Constituição, leis, decretos e conceitos técnicos</td></tr>
<tr><td class="k">Estrutura</td><td>Livre</td><td>Um parágrafo por aspecto, na ordem do comando</td></tr>
<tr><td class="k">Fechamento</td><td>Proposta de intervenção</td><td>Síntese técnica de 1 a 2 linhas, sem fato novo</td></tr>
</tbody></table>
<span class="eyebrow">04</span><h2 class="sec">Roteiro de planejamento em cinco passos</h2>
<div class="passo"><div class="bn">1</div><div><h4>Decomponha o comando</h4>Numere os aspectos, sublinhe o verbo (“explique”, “diferencie”, “cite três”) e circule o valor de cada um. Aspecto com duas partes recebe duas marcas.</div></div>
<div class="passo"><div class="bn">2</div><div><h4>Escolha o fundamento</h4>Ao lado de cada aspecto, anote a norma ou o conceito que o responde. Número de artigo só com certeza.</div></div>
<div class="passo"><div class="bn">3</div><div><h4>Distribua as linhas pelo valor</h4>Um parágrafo por aspecto, com linhas proporcionais ao valor. Em 30 linhas com 3 aspectos: 0–2 de abertura, 8 a 9 por aspecto, 1–2 de fecho.</div></div>
<div class="passo"><div class="bn">4</div><div><h4>Monte o esqueleto</h4>Para cada parágrafo, em palavras-chave: tópico frasal, fundamento, desenvolvimento e fechamento.</div></div>
<div class="passo"><div class="bn">5</div><div><h4>Escreva, revise, passe a limpo</h4>Rascunho seguindo o esqueleto, revisão de concordância e pontuação, e passagem a limpo com letra legível, sem marcas de identificação.</div></div>
</section>''',
'''<section><span class="eyebrow" style="display:block;margin-top:14pt">05</span><h2 class="sec">O parágrafo que pontua</h2>
<p>O parágrafo é onde a banca conta os pontos. Se cada um seguir a mesma sequência, o corretor encontra o quesito na primeira frase.</p>
<div class="formula">Tópico frasal + <span>Fundamento</span> + Desenvolvimento + <span>Fechamento</span></div>
<table><thead><tr><th>Parte</th><th>O que é</th><th>Exemplo</th></tr></thead><tbody>
<tr><td class="k">1. Tópico frasal</td><td>A primeira frase já responde ao aspecto, com as palavras do comando</td><td>“A titularidade do controle externo pertence ao Poder Legislativo.”</td></tr>
<tr><td class="k">2. Fundamento</td><td>A norma ou o conceito que sustenta a resposta</td><td>“...conforme o art. 71 da Constituição Federal.”</td></tr>
<tr><td class="k">3. Desenvolvimento</td><td>Explica, diferencia ou exemplifica</td><td>“Esse auxílio, contudo, não significa subordinação...”</td></tr>
<tr><td class="k">4. Fechamento</td><td>A consequência, em uma frase</td><td>“Assim, o tribunal atua com autonomia.”</td></tr>
</tbody></table>
<div class="box bad"><span class="eyebrow">Assim não pontua</span>“No mundo contemporâneo, em que a sociedade exige cada vez mais transparência, é de suma importância discutir o controle da administração pública...” — genérico, gasta linhas e não responde a nenhum aspecto.</div>
<div class="box good"><span class="eyebrow">Assim pontua</span>“Apreciar e julgar contas são competências distintas. As contas anuais do Presidente da República são apenas apreciadas pelo TCU, que emite parecer prévio (CF, art. 71, I)...” — responde na primeira frase e fundamenta na segunda.</div>
<h3>Como citar normas</h3>
<ul><li>Primeira menção completa (“Lei n.º 14.133/2021”); depois, “a mesma lei”.</li>
<li>Artigo só com certeza: número errado tira mais credibilidade do que número ausente.</li>
<li>Não invente acórdão. Sem o número exato, cite o entendimento sem número.</li></ul>
<h3>Conectivos que organizam</h3>
<p><b>Fundamentar:</b> “Nos termos do...”, “Conforme o...”. <b>Diferenciar:</b> “Já...”, “Por outro lado...”. <b>Fechar o parágrafo:</b> “Assim,...”, “Por isso,...”. <b>Fechar o texto:</b> “Conclui-se, portanto, que...”.</p>
</section>''',
    ]
