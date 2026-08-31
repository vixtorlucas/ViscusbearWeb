# ViscusbearWeb

Fase 1 do site [viscusbear.com.br](https://viscusbear.com.br): a edição **v1 — Em construção**.

## Desenvolvimento local

Requisitos: Ruby 3.3 e Bundler.

```sh
bundle install
bundle exec jekyll serve
```

Neste workspace do Codex, Ruby e todas as dependências já estão instalados. No PowerShell, também é possível iniciar tudo com:

```powershell
.\testar.ps1
```

Depois, abra `http://localhost:4000`. Use `Ctrl+C` para encerrar.

## Publicação

O workflow `build.yml` publica a branch `main` pelo GitHub Pages usando Jekyll 4.4. O Pages deve estar configurado para usar **GitHub Actions** como fonte.

Para congelar a primeira edição, depois de conferir o site publicado:

```sh
git tag v1
git push origin v1
```

O workflow `congelar.yml` constrói a tag uma vez, remove cópias aninhadas do arquivo e grava o HTML final em `versoes/v1/` na branch `main`.

Antes de criar a tag, substitua `a medir` em `_data/versoes.yml` pelo peso total observado na versão publicada.
