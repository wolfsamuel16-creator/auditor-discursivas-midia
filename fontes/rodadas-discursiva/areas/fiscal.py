# -*- coding: utf-8 -*-
# Trilha FISCAL — mini-aula (baseada nas aulas gratuitas da SEFAZ-SP 2026 (FCC) e da SEFAZ-AL 2026 (Cebraspe))
NOME = 'Fiscal'
PALAVRA = 'FISCAL'
SUBTITULO = 'Treino de discursiva para Receita, SEFAZs e fiscos municipais.'
PUBLICO = 'RECEITA FEDERAL · SEFAZs · SEFINs · AUDITOR FISCAL · ANALISTA DO TESOURO'
FORMATO_CURTO = 'estudo de caso com questionamentos'
PADRAO_BANCA = 'padrão Cebraspe'
NOTA_DESCONTO = ('Depois da nota de conteúdo, o Cebraspe desconta os erros de língua em proporção às linhas escritas. '
                 'Exemplo do edital da SEFAZ-AL 2026 (questões de 30 linhas valendo 10 pontos): NQ = NC − 2 × NE ÷ TL. '
                 'Neste treino, com espelho de 30 pontos, a lógica é a mesma. Confira a fórmula no edital do seu concurso.')

def aula():
    return [
'''<section class="pb"><div class="parte"><span class="eyebrow">Mini-aula · Trilha Fiscal</span><h2>Como a discursiva fiscal pontua</h2><p>O formato das bancas, o que a correção valoriza e o parágrafo que responde ao caso.</p></div>
<span class="eyebrow">01</span><h2 class="sec">O que as bancas fiscais cobram</h2>
<p>Na área fiscal, a discursiva quase sempre é <b>caso concreto</b>: um contribuinte, um estado, uma operação, com datas e valores, e perguntas que pedem uma posição — é regular? é devido? pode ser feito? o que recomendar? Quem só define conceitos e cita lei, sem aplicar ao caso, perde pontos.</p>
<table><thead><tr><th>Prova</th><th>Formato</th><th>O que vale observar</th></tr></thead><tbody>
<tr><td class="k">SEFAZ-AL 2021 · Auditor (Cebraspe)</td><td>Dois estudos de caso de até 30 l.</td><td>Auditoria fiscal e legislação tributária estadual aplicadas a casos</td></tr>
<tr><td class="k">SEFAZ-AC 2024 · Auditor (Cebraspe)</td><td>Texto com quatro aspectos</td><td>Ceticismo profissional, autenticidade documental e risco de fraude</td></tr>
<tr><td class="k">SEFAZ-PI 2025 (FCC)</td><td>Estudos de caso com itens (a, b, c...)</td><td>Caso narrado com fatos numerados; resposta por item</td></tr>
<tr><td class="k">SEFAZ-AL 2026 · Auditor (Cebraspe)</td><td>4 questões de 30 l., 10 pontos cada</td><td>Eixos fixos: ciência de dados, auditoria fiscal, finanças públicas e reforma tributária</td></tr>
<tr><td class="k">SEFAZ-SP 2026 · APOFP (FCC)</td><td>1 estudo de caso de 30 l., 120 pontos</td><td>Edital: “a mera citação de legislação ou de definições” não é valorada por si só</td></tr>
</tbody></table>
<div class="box nv"><span class="eyebrow">O que se repete</span>Três padrões aparecem prova após prova: <b>caso com dados</b> (use todos os números do enunciado), <b>itens duplos</b> (“é válido? por quê?”, “conceitue e aplique”) e <b>norma aplicada</b>, e não teoria pura. Os temas giram em torno de <b>reforma tributária</b>, <b>CTN e lançamento</b>, <b>auditoria e fiscalização com dados</b> e <b>finanças públicas e LRF</b> — as cinco rodadas da trilha passam por todos eles.</div>
<p class="nota">Fonte: editais e cadernos de prova da FCC e do Cebraspe, reunidos nas aulas gratuitas da SEFAZ-SP 2026 e da SEFAZ-AL 2026 do @auditor_discursivas.</p>
</section>''',
'''<section class="pb"><span class="eyebrow">02</span><h2 class="sec">Como a correção funciona</h2>
<p>As duas grandes bancas da área corrigem por <b>item do comando</b>. No Cebraspe, o espelho tem um quesito de apresentação e um quesito por item, com conceitos graduados (0, 1, 2, 3...), e depois vem o desconto dos erros de língua, dividido pelas linhas escritas. Na FCC, a <b>grade de correção</b> traz a abordagem esperada e os pontos de cada item, e só aparece na vista da prova.</p>
<div class="formula">Nota = <span>NC</span> (conteúdo, por item) − <span>peso</span> × <span>NE</span> (erros) ÷ <span>TL</span> (linhas)</div>
<table><thead><tr><th>Banca</th><th>Como o comando aparece</th><th>O que isso pede de você</th></tr></thead><tbody>
<tr><td class="k">Cebraspe</td><td>“Redija um texto... abordando, necessariamente” ou “responda aos questionamentos”, com o valor de cada item</td><td>Um parágrafo por item, linhas proporcionais ao valor, perto do limite</td></tr>
<tr><td class="k">FCC</td><td>Caso narrado + “responda, justificadamente:” e itens com letra</td><td>Veredito na 1.ª frase de cada item e proposta de solução no fim</td></tr>
</tbody></table>
<div class="box lr"><span class="eyebrow">O que isso muda na estratégia</span>Cada item vale pontos próprios: <b>nunca troque um item por introdução</b>. E todo dado do caso tem uma razão de estar ali — dado do enunciado que não aparece na sua resposta costuma ser requisito da grade que ficou de fora.</div>
<span class="eyebrow">03</span><h2 class="sec">Roteiro de planejamento em cinco passos</h2>
<div class="passo"><div class="bn">1</div><div><h4>Perguntas antes do caso</h4>Leia primeiro os itens. Conte quantas perguntas há dentro de cada um: “é válida? por quê?” são duas marcas no rascunho.</div></div>
<div class="passo"><div class="bn">2</div><div><h4>Tipo de cada pergunta</h4>Sim ou não, conceito, regularidade de um fato, cálculo ou recomendação. O tipo decide como a primeira frase do parágrafo começa.</div></div>
<div class="passo"><div class="bn">3</div><div><h4>Linhas por item</h4>Um parágrafo por item, com linhas proporcionais ao valor. Em 30 linhas com 3 itens: 9 + 9 + 9, e 0 a 2 de fecho.</div></div>
<div class="passo"><div class="bn">4</div><div><h4>Caso marcado</h4>Só agora leia o caso. Marque datas, percentuais, valores e palavras como “antes”, “depois”, “sem” e “inclusive”, e ligue cada dado ao item que ele responde.</div></div>
<div class="passo"><div class="bn">5</div><div><h4>Esqueleto em palavras-chave</h4>Para cada item: resposta · fundamento · fato do caso · solução. Nada de rascunho integral: o tempo vai para o texto definitivo.</div></div>
</section>''',
'''<section><span class="eyebrow" style="display:block;margin-top:14pt">04</span><h2 class="sec">O parágrafo que responde ao caso</h2>
<p>Na área fiscal, o parágrafo que pontua tem quatro partes. As três primeiras são obrigatórias; a quarta é a que separa a nota boa da nota máxima, porque mostra que você sabe o que fazer com o caso.</p>
<div class="formula">Resposta direta + <span>Fundamento</span> + Fato do caso + <span>Solução</span></div>
<table><thead><tr><th>Parte</th><th>O que é</th><th>Exemplo</th></tr></thead><tbody>
<tr><td class="k">1. Resposta direta</td><td>A primeira frase já dá o veredito, com as palavras do item</td><td>“A promessa do governador é inconstitucional.”</td></tr>
<tr><td class="k">2. Fundamento</td><td>A norma ou o conceito que sustenta o veredito</td><td>“...pois o IBS não pode ser objeto de incentivos e benefícios fiscais (CF, art. 156-A, § 1.º, X).”</td></tr>
<tr><td class="k">3. Fato do caso</td><td>O dado do enunciado que se encaixa na norma</td><td>“A redução de 80% prometida à montadora é benefício desse tipo.”</td></tr>
<tr><td class="k">4. Solução</td><td>O que fazer, em uma frase</td><td>“Recomenda-se atrair o investimento por infraestrutura e logística.”</td></tr>
</tbody></table>
<div class="box bad"><span class="eyebrow">Assim não pontua</span>“A reforma tributária é um marco histórico para o Brasil, que há décadas convive com um sistema complexo e injusto, sendo de suma importância discutir seus impactos...” — não responde a nenhum item e não usa nenhum dado do caso.</div>
<div class="box good"><span class="eyebrow">Assim pontua</span>“A promessa é inconstitucional. O IBS não pode ser objeto de incentivos e benefícios fiscais (CF, art. 156-A, § 1.º, X), e a redução de 80% prometida à montadora é exatamente isso.” — veredito, fundamento e fato em duas frases.</div>
<h3>Como citar normas</h3>
<ul><li>Primeira menção completa (“Emenda Constitucional n.º 132/2023”, “Lei Complementar n.º 214/2025”); depois, “a mesma emenda”.</li>
<li>Artigo só com certeza: número errado tira mais credibilidade do que número ausente. Na dúvida, cite a lei e o conteúdo.</li>
<li>Não invente julgado. Sem o número exato, cite o entendimento: “conforme o STF”.</li></ul>
<h3>Conectivos que organizam</h3>
<p><b>Fundamentar:</b> “Nos termos do...”, “Conforme o...”. <b>Aplicar ao caso:</b> “No caso,...”, “Na situação narrada,...”. <b>Propor:</b> “Recomenda-se...”, “Cabe ao fisco...”. <b>Fechar:</b> “Assim,...”, “Portanto,...”.</p>
</section>''',
    ]
