# CLAUDE.md — ViscusbearWeb

Instruções para qualquer agente trabalhando neste repositório. Leia antes de tocar
em qualquer arquivo.

## O que é

`viscusbear.com.br` — o site pessoal de Vixtor, publicado sob a persona
**Viscusbear**. Não é um blog com tema retrô: **o site é a obra**. A estética é a
web brasileira do começo dos anos 2000 (portais UOL/Terra, orkut, fotolog, MSN)
rodando sobre uma toolchain estática de 2026.

Dois nomes, e a distinção importa: **Viscusbear é a persona** (a pele, o avatar, o
domínio, os enfeites); **Vixtor é quem escreve** (o texto, o colofão, as notas do
arquivo, os commits). A persona é uma fantasia, não um narrador — as palavras são
sempre de Vixtor.

O site guarda todas as suas versões vivas: cada edição publicada fica congelada e
navegável para sempre em `/versoes/vN/`.

## A regra que domina todas as outras

**Nunca escreva uma linha da próxima edição antes da atual estar congelada.**

Congelar = criar a tag `vN` e conferir que `/versoes/vN/` abre. O `congelar.yml`
constrói a tag **uma única vez** e commita o HTML resultante; ele se recusa a
sobrescrever uma edição já arquivada. Uma edição não congelada a tempo simplesmente
deixa de existir — não há como reconstruí-la depois.

Corolário: **tudo que entra numa edição vira arqueologia permanente.** Um link
quebrado, uma data errada ou um bug de mobile congelam junto e ficam visíveis para
sempre. Na dúvida, corte — o que não entra nesta edição entra na próxima sem custo.

## Estado atual (21/09/2026)

- **v1 "Em construção" está congelada**: tag `v1` criada, `/versoes/v1/` commitada pelo
  `congelar.yml` (commit "congela v1", 01/09/2026).
- **v2 "O portal" está no `main`** (21/09/2026), ainda **sem tag**. Ela traz:
  - portal em três colunas: esquerda (perfil, comunidades, redes sociais), centro
    (últimas entradas / comunidades / entrada aberta), direita (camada viva, arquivo);
  - **entradas** em `_posts/` (texto e foto juntos — o antigo diário + fotolog), layout
    `entrada`, URL `/entradas/<slug>/`; modelo em `_drafts/modelo-de-entrada.md` (local);
  - **comunidades** = tags das entradas, em `/comunidades/` (só a lista; `#tag` abre as
    entradas daquela tag via `:target`, sem JS);
  - fotos preparadas por `ferramentas/foto.py` (tira todo metadado, 1000px + mini 480px)
    em `assets/img/entradas/`;
  - "tocando agora" em `_data/tocando.yml`; projetos em `_data/projetos.yml`;
  - `/vixtor/` voltou a ser a da v1 (pele e texto), fora do menu — acessível por
    "um site de Vixtor" e "quem é o Vixtor".
- Antes de `git tag v2`: medir o peso publicado e trocar `a medir` e `data: ""` em
  `_data/versoes.yml`.

## Stack e publicação

- **Jekyll 4.4 / Ruby 3.3**, sem JavaScript no cliente. Conteúdo em markdown/HTML
  no repositório.
- **Cloudflare** constrói e publica direto do `main` (`wrangler.jsonc`, assets em
  `_site`). DNS, TLS e hospedagem, tudo num painel só. Custo total do projeto:
  R$ 40/ano (só o domínio no registro.br).
- `.github/workflows/build.yml` está **inativo** — é só o caminho de volta para o
  GitHub Pages. Não reative sem motivo.
- `.github/workflows/congelar.yml` roda em tags `v*` e é a peça de que o arquivo
  permanente depende. É um GitHub Action de verdade e continua necessário.
- `_headers` (servido pela Cloudflare) dá cache longo em ícones/assets e
  `X-Robots-Tag: noindex` em `/versoes/*`.

> ⚠️ `README.md` e `PROJECT_CONTEXT.md` ainda falam em GitHub Pages. Estão
> desatualizados desde a migração de 31/08/2026. Este arquivo é a fonte correta.

## Mapa do repositório

```
_layouts/default.html      documento, metadados, fontes, favicons, faixa de arquivo
_includes/janela-v1.html   a janela compartilhada pela home e pelos stubs
assets/css/site.css        todo o sistema visual + responsivo/contraste/print
_data/versoes.yml          a tabela de edições (nome, data, peso, nota)
_data/vixtor.yml           o conteúdo de /vixtor/ (data, corpo, assinatura)
_config_arquivo.yml        liga `site.arquivo` — a faixa "você está na versão N"
icones/                    PNGs entregues pelo design; v1 usa viscus-v1.png
ferramentas/urso.py        gera o urso em box-shadow a partir de um grid
versoes/                   as edições congeladas — HTML committado de propósito
```

Design e handoff hi-fi ficam **fora deste repositório**, em
`D:\Projetos\ViscusbearDesign`.

## Regras invioláveis

1. **Sem JavaScript, sem analytics, sem contador de visitas** na v1.
2. **Silkscreen 400 é a única webfont**, e só em 8px (desktop) / 16px (celular) —
   uma fonte de pixel só renderiza nítida no tamanho de projeto ou em múltiplos
   inteiros. A **única exceção documentada** é o aviso de construção da home, em
   16/32px (2× em cada breakpoint). Ninguém "conserta" essa exceção depois.
   O wordmark é Verdana/Geneva pesada com sombra âmbar dura — nunca a fonte pixel.
3. **Disciplina de pixel:** grade inteira, sem `border-radius`, sem sombra borrada
   (offset duro), xadrez pontilhado onde outra paleta usaria gradiente.
4. **Âmbar nunca carrega texto claro.** Branco sobre `#F5A623` dá 2.0:1. Sempre
   `--accent-ink: #2B1C10` (8.1:1).
5. **Celular é de primeira classe.** Reflow honesto: colunas empilham, tipo cresce,
   caixas ocupam a largura. Densidade vertical apertada (line-height ~1.45) — é o
   que separa 2003 de um blog com tema retrô. Nada de hambúrguer. Alvos de toque
   ≥44px, foco âmbar visível, zero rolagem horizontal.
6. **Preservar `prefers-contrast`, `prefers-reduced-motion` e `@media print`.**
   Não existe mais "versão moderna" para servir de rede de segurança — a pele camp
   carrega a acessibilidade sozinha. Essas regras são o único piso.
7. **Não reamostrar nem recomprimir os PNGs** entregues pelo design.
8. **Assets são append-only.** Nunca apague ou sobrescreva nada em
   `assets/` ou `icones/` — as edições antigas apontam para lá.
9. **Caminhos:** links, CSS e JS usam `| relative_url`. Loops e enfeites são
   caminhos absolutos de raiz, **sem** o filtro (são compartilhados, não duplicados
   por edição). Um link que precisa escapar da edição congelada usa
   `{% if site.arquivo %}/caminho/{% else %}{{ '/caminho/' | relative_url }}{% endif %}`.
10. **Português em tudo:** site, commits, comentários, nomes de arquivo.
11. **O cabeçalho é fixo.** Barra de título + navbar têm o mesmo tamanho e a mesma
    posição em todas as páginas do portal (início, comunidades, projetos, versões,
    entradas). Toda página v2 usa `_includes/topo-curta.html` + `navbar-v2.html`, janela
    de 1000px presa no topo. A única exceção é `/vixtor/`, que usa a pele da v1.

## Onde as decisões moram

O registro de decisões não está no repositório — está nos docs do projeto Claude
"Vixtor Website". Leia antes de propor qualquer mudança de rumo:

| doc | o que tem |
|---|---|
| `claude/decisoes-v0.md` | o registro completo: as 26 decisões travadas, a pele, o arquivo, o celular, o roadmap por fases |
| `claude/decisoes-v1-conteudo.md` | o conteúdo travado da v1 e o que foi cortado |
| `claude/fase-1-infra.md` | infraestrutura: Cloudflare, DNS, certificado, ordem de execução, armadilhas |
| `claude/peles-v1.md` | o estudo de paleta que escolheu a direção Habbo |
| `claude/prompt-codex-v1.md` · `claude/prompt-codex-vixtor-v1.md` | os prompts de implementação da v1 |
| `claude/prompt-claude-design.md` | o prompt de design |

Emendas posteriores valem sobre o documento original. Já aconteceram duas:

- **A decisão #26 caiu** (01/09/2026). Não existe mais uma `/vixtor` sóbria e sem
  pele — "o quarto onde a fantasia não é usada". A `/vixtor` com a pele completa é a
  definitiva. **Consequência em aberto:** a bio, o "onde já trabalhei", o contato e
  o colofão ficaram sem casa, e essa era a única página do site pensada para
  aparecer em busca. Precisa de destino na v2.
- **"melhor visualizado em 800×600" foi cortado em definitivo** — contradizia a
  regra de reflow honesto no único lugar em que ela era dita em voz alta.

## Comandos

```sh
bundle install
bundle exec jekyll serve          # http://localhost:4000
.\testar.ps1                      # no Windows, monta o Ruby portátil e sobe o serve

git tag v1 && git push origin v1  # congela a edição — irreversível
```

## Armadilhas, em ordem de custo

1. Começar a v2 sem ter congelado a v1 — a v1 deixa de existir.
2. `versoes/` no `.gitignore` — apaga o arquivo permanente no deploy seguinte, sem
   recuperação. `CNAME` idem: ignorado ou apagado, o site sai do ar no domínio.
3. Esquecer de renovar o domínio (R$ 40/ano). Ligar renovação automática.
4. Criar o registro de DNS na mão apontando para o `.pages.dev` — erro 522. O
   domínio se adiciona **pelo painel do Pages**, e a nuvem laranja aqui é o certo.
5. Apagar o projeto do Pages com o domínio ainda ligado nele.
6. Build falhando por versão de Ruby — `.ruby-version` tem só `3.3`.
7. Um link relativo que atravessa a edição congelada (ver regra 9).

## Limitações do ambiente (sessões Cowork)

Descobertas na prática, para não repetir a investigação:

- O shell no computador do Vix **não tem credencial do GitHub** — clone e commit
  funcionam, `push` não. O push é sempre dele.
- Esse shell **não consegue apagar arquivos** na pasta montada. O git tropeça nos
  próprios `index.lock`/`HEAD.lock`: contorne com `GIT_INDEX_FILE` fora do mount e
  movendo os `.lock` para `_to_delete/` (que é gitignored).
- O container em nuvem **não alcança o rubygems.org**, então não dá para rodar
  `bundle install` nem validar a build lá. Quem valida é a build da Cloudflare.
- Ruby local na VM é 3.0 e não tem bundler — não serve para testar o site.

## O risco nomeado

A pele é divertida demais de construir, e o site nunca é alimentado: uma casca
perfeita de época com quatro posts, abandonada em março. Duas features pioram isso —
**o arquivo** transforma toda redecoração num entregável de aparência legítima, e
**a persona** pode virar lugar de se esconder.

Defesa: publicar tem que ser um comando que dá para rodar cansado, e a camada viva
precisa manter o site em movimento nos dias em que nada é escrito. Quando estiver em
dúvida entre construir mais cromo e colocar conteúdo no ar, **coloque conteúdo no ar.**
