# Contexto do projeto Viscusbear

## Resumo

`viscusbear.com.br` é o site pessoal de Vixtor. A proposta é que o site evolua em edições e preserve cada versão publicada como um arquivo permanente. A edição atual é a **v1 — Em construção**, em português, com estética de interface antiga/pixel art.

## Arquitetura

- Site estático gerado por Jekyll 4.4, sem JavaScript no cliente.
- Publicação no GitHub Pages pela action `.github/workflows/build.yml`.
- Domínio customizado `viscusbear.com.br` pelo arquivo `CNAME`.
- A action `.github/workflows/congelar.yml` congela tags `v*` em `/versoes/<tag>/` sem sobrescrever edições já arquivadas.
- `_config_arquivo.yml` ativa a faixa que identifica uma versão arquivada.
- `_layouts/default.html` concentra o documento, metadados, fontes, favicons e CSS.
- `_includes/janela-v1.html` concentra a janela compartilhada pela home e pelos stubs.
- `assets/css/site.css` contém o sistema visual e os modos responsivo, alto contraste, movimento reduzido e impressão.
- `icones/` contém os PNGs originais entregues pelo design; v1 usa `viscus-v1.png`.

## Experiência da v1

A home mostra, nesta ordem: barra de topo com o título clicável que leva à página inicial, avatar com capacete, aviso de construção, ícone de câmera que leva ao Instagram `@viscusbear`, link para o histórico e rodapé com a data 31/08/2026. `/vixtor/` é a página sobre quem escreve, com sprite animado e uma única entrada que será reescrita a cada versão. `/versoes/` e `/livro/` são stubs curtos com a mesma skin e link de volta.

## Regras que não devem ser quebradas

- Hi-fi definido em `ViscusbearDesign/prompt-codex-v1.md` e no handoff v1.
- Janela compacta e fixa de 430px no desktop, que passa a encolher apenas quando o viewport fica menor que sua largura. Entre 720px e 480px, tipografia, espaçamento e sombras interpolam fluidamente até o tratamento mobile, sem salto visual; em telefones muito estreitos, o aviso continua diminuindo de forma contínua.
- Silkscreen 400 é a única webfont; Verdana/Geneva no título.
- Sem JS, animação, analytics ou contador de visitas.
- Foco âmbar visível, alvos de toque de pelo menos 44px e nenhuma rolagem horizontal.
- Preservar `prefers-contrast`, `prefers-reduced-motion` e `@media print`.
- Não reamostrar ou recomprimir os PNGs.
- O conteúdo de `/vixtor/` vive em `_data/vixtor.yml` e expõe somente data, corpo e assinatura; não transformar a página em feed ou lista.

## Conteúdo e publicação pendentes

- Antes de criar a tag `v1`, substituir `a medir` em `_data/versoes.yml` pelo peso publicado observado.
- GitHub Pages deve usar GitHub Actions; HTTPS deve ser ativado quando disponível.
- Cabeçalhos `Cache-Control: public, max-age=31536000, immutable` para `icones/*.png` dependem da camada de hospedagem/CDN e não são configuráveis pelo HTML.
