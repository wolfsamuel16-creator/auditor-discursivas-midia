# Rodadas de Discursiva — sistema (aprovado pelo Samuel em 11/11/2026)

Série semanal de aulas gratuitas em PDF, 3 trilhas × 5 rodadas = 15 rodadas, 1 por semana, alternando Controle → Fiscal → Policial.
Cada rodada = mini-aula da trilha (método, "aula bacana" baseada nas aulas já enviadas) + **2 temas inéditos**, cada um com enunciado, esqueleto, padrão de resposta, espelho e **texto definitivo completo** + palavra final com CTA de recurso.

## Calendário (publicação sexta 18h; story 18h15; anúncio sáb 18h47, R$ 20/dia × 5 dias, Mensagens, semelhantes aos seguidores, Brasil)
| # | Data | Trilha | Rodada | Tema 1 | Tema 2 |
|---|---|---|---|---|---|
| 1 | 13/11/2026 | Controle | 1 | Controle externo e interno na CF (arts. 70–75) | Governança pública (Dec. 9.203/2017) e das contratações (Lei 14.133, art. 11) |
| 2 | 20/11/2026 | Fiscal | 1 | Reforma tributária do consumo (EC 132/2023: IBS, CBS, IS, princípios) | Planejamento tributário × evasão (CTN, art. 116, p. ú.) |
| 3 | 27/11/2026 | Policial | 1 | Violência contra a mulher e a atuação policial (Lei 11.340/2006) | Câmeras corporais: transparência e proteção do policial |
| 4 | 04/12/2026 | Controle | 2 | Transparência pública (LAI + LRF, arts. 48 e 48-A) | LRF: despesa com pessoal e limitação de empenho |
| 5 | 11/12/2026 | Fiscal | 2 | Transação tributária (Lei 13.988/2020) | Conformidade cooperativa e o novo perfil da fiscalização |
| 6 | 18/12/2026 | Policial | 2 | Crime organizado e integração (Susp, Lei 13.675/2018) | Saúde mental do policial |
| 7 | 28/12/2026 (seg, por causa do Natal) | Controle | 3 | Planejamento das contratações (ETP, matriz de riscos, PCA) | Responsabilização: improbidade (Lei 14.230/2021) e tomada de contas especial |
| 8 | 04/01/2027 (seg, por causa do Ano-Novo) | Fiscal | 3 | Guerra fiscal do ICMS (LC 160/2017) e seu fim com o IBS | Tributação, progressividade e desigualdade |
| 9 | 08/01/2027 | Policial | 3 | Tecnologia na segurança pública (reconhecimento facial × privacidade) | Polícia comunitária e prevenção |
| 10 | 15/01/2027 | Controle | 4 | Avaliação de políticas públicas (CF, art. 37, § 16) | Auditoria governamental: achados (condição, critério, causa, efeito) e evidência |
| 11 | 22/01/2027 | Fiscal | 4 | Fiscalização com dados (NF-e, cruzamentos, IA) | Sigilo fiscal e compartilhamento de informações (CTN, art. 198) |
| 12 | 29/01/2027 | Policial | 4 | Sistema prisional e reincidência | Uso progressivo da força (Lei 13.060/2014) |
| 13 | 05/02/2027 | Controle | 5 | Gestão de riscos e controles internos (COSO, três linhas) | Integridade: Lei 12.846/2013 e programas de integridade |
| 14 | 12/02/2027 | Fiscal | 5 | Federalismo fiscal e o Comitê Gestor do IBS | Renúncia de receita (LRF, art. 14) |
| 15 | 19/02/2027 | Policial | 5 | Integração das forças de segurança (Susp) | Juventude, violência e prevenção |
Temas são o plano aprovado; a tarefa pode trocar um tema se o assunto ficar desatualizado (lei nova), registrando o motivo.

## Arquivos
- `build_aula.py conteudo/<area>_<n>.py` → `saida/<area>-<n>.pdf` (+ .html). Confere que o texto definitivo cabe nas linhas.
- `areas/<area>.py` → mini-aula da trilha (NOME, PALAVRA, SUBTITULO, PUBLICO, FORMATO_CURTO, PADRAO_BANCA, NOTA_DESCONTO, aula()). `controle.py` pronto. **fiscal.py** (base: docs/aulas/sefazsp.pdf e sefazal.pdf — estudo de caso/questão técnica de 30 l., FCC/Cebraspe/FGV) e **policial.py** (base: docs/aulas/pmsc.pdf e fontes/aula-pmsc-2026 — redação dissertativo-argumentativa de 20–30 l. com proposta, AOCP/Cebraspe/FGV) são criados na 1.ª rodada de cada trilha e reaproveitados depois (pode variar o recorte da mini-aula a cada rodada).
- `conteudo/<area>_<n>.py` → AREA, N_AREA, N_GERAL, DATA, PROXIMA, TEMAS (2), FONTES. Modelo: `conteudo/controle_1.py`.
- `carrossel/<area>-<n>.html` → 5 slides 1080×1350 + 1 story 1080×1920; `python3 render_carrossel.py carrossel/<area>-<n>.html <saida> foto.jpg` (fontes em /home/claude/carrossel/fonts — baixar Poppins/Lato do google/fonts se faltar). Modelo: `carrossel/controle-1.html` (capa navy com selo AULA GRATUITA · PDF, temas, calendário das trilhas, o que tem, prévia de conteúdo, CTA com foto).

## Publicação de cada rodada
1. PDF → `docs/rodadas/<area>-<n>.pdf` e cópia em `docs/rodadas/<area>.pdf` (link fixo da trilha, usado pela IA do direct); linha nova no topo de `<div id="rodadas">` em docs/index.html.
2. `posts/<data>-rodadas-<area>-<n>/` (slides, legenda.txt, post.json com palavra_chave) e `posts/<data>-story-rodadas-<area>-<n>/`.
3. Metricool (blogId 7469898): carrossel 18h, story 18h15, autoPublish true.
4. Planilha "Anúncios – controle semanal" (1niXBXQGUd0WHBea1JWwkjx4Q7Cmc-iUmtq09iZZz3A4): linha PLANEJADO — post da rodada, Mensagens, semelhantes aos seguidores (Brasil), R$ 20/dia × 5 dias, sobe no dia seguinte às 18h47.
5. Drive: Campanhas/Rodadas de Discursiva/<area>-<n>/ com o HTML do carrossel, a legenda e o PDF.

## Palavras-chave e entrega (fixas — não exigem mexer no InfluenciMax a cada semana)
CONTROLE → auditordiscursivas.com.br/rodadas/controle.pdf · FISCAL → /rodadas/fiscal.pdf · POLICIAL → /rodadas/policial.pdf. Todas as rodadas: auditordiscursivas.com.br (seção "Rodadas de Discursiva").
InfluenciMax (11/11/2026): comentários em qualquer post — RODADAS · CONTROLE 30771, RODADAS · FISCAL 30775, RODADAS · POLICIAL 30776 (resposta pública + DM com botão do link fixo + IA pós-aula). Direct: a Porta de entrada (26757) já reconhece CONTROLE/FISCAL/POLICIAL e manda o link. fiscal.pdf e policial.pdf são avisos provisórios até a 1.ª rodada de cada trilha.
Exceção da Rodada 1: anúncio sobe seg 16/11 18h47 (a semana 09–15/11 já estava no teto com o TCE-PE).

## Regras vigentes (prevalecem sobre o texto acima)
- **CTA (16/11/2026):** a Meta rejeitou o anúncio da Rodada 1 por "Comente CONTROLE ... de graça". Nenhuma peça (slides, story, Reel, legenda, 1.º comentário, PDF) usa "Comente <PALAVRA>": o CTA é sempre **"Mande <PALAVRA> no direct"**. A automação de comentários continua ligada. O build_aula.py já usa "mande <PALAVRA> no direct" (ajustado em 18/11/2026).
- **Anúncio (13/11 e 16/11/2026):** R$ 100 por rodada, divididos em R$ 50 no carrossel (R$ 10/dia × 5) e R$ 50 no Reel (R$ 10/dia × 5); cada um sobe NO DIA da sua publicação, na rodada das 18h47 da tarefa "Anúncios · acompanhamento diário". Teste de canal: Rodada 1 Controle = Gerenciador; Rodada 2 (Fiscal 1) = Turbinar. Depois vale o vencedor registrado na planilha.
- **Reel da rodada (16/11/2026):** vídeo dos 5 slides (1080×1920, 20–40 s, sem áudio próprio, música do Instagram via Metricool), publicado no dia seguinte ao carrossel às 12h (13h30 se houver outro post de feed/Reel a menos de 3 h), **fora da grade** (showReelOnFeed false), em posts/<data+1>-reel-rodadas-<area>-<n>/; anunciado pelo Gerenciador como publicação existente.
- **Horário (18/11/2026):** se houver outro post de feed a menos de 3 h das 18h no dia da rodada, o carrossel vai às 19h30 e o story às 19h45 (ex.: Fiscal 1, em 20/11, por causa do carrossel do catálogo de aulas às 18h).
- Modelo de carrossel com o CTA novo: carrossel/fiscal-1.html (controle-1.html é anterior à regra e ainda tem "Comente").
- Mini-aulas prontas: areas/controle.py, areas/fiscal.py (base: aulas SEFAZ-SP 2026 e SEFAZ-AL 2026) e areas/policial.py (base: aula PM-SC 2026; criada em 25/11/2026).
- Policial 1 (27/11/2026): Tema 1 recortado para "Desafios para a efetividade das medidas protetivas de urgência" (a aula PM-SC já tinha o papel da PM na violência doméstica; incorpora Lei 14.994/2024 e Lei 15.125/2025). Carrossel às 21h (story 21h15) porque 27/11 já tinha carrossel às 18h e Reel às 19h30 — quando 19h30 também estiver ocupado, usar o próximo horário livre à noite.
- Modelo de carrossel mais recente: carrossel/policial-1.html.
