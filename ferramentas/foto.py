#!/usr/bin/env python3
"""Prepara uma foto para uma entrada do site.

Uso:
    python ferramentas/foto.py CAMINHO_DA_FOTO titulo-curto [AAAA-MM-DD]

O que faz:
  - aplica a rotação do celular (orientação EXIF) nos pixels;
  - converte para sRGB e descarta TODO metadado: EXIF (localização/GPS,
    câmera, data), XMP, IPTC, perfil ICC, miniaturas;
  - reduz o lado maior para 1000px (e faz uma miniatura de 480px para as listas),
    JPEG progressivo, qualidade 78;
  - grava em assets/img/entradas/AAAA-MM-DD-titulo-curto.jpg e ...-mini.jpg
    (nunca sobrescreve);
  - imprime o bloco de front matter para colar no post.

Precisa de Pillow (pip install pillow).
"""
import io
import sys
from datetime import date
from pathlib import Path

from PIL import Image, ImageCms, ImageOps

LADO_MAX = 1000   # a página da entrada mostra a foto com até ~950px
LADO_MINI = 480   # miniatura das listas (início, comunidades)
QUALIDADE = 78


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    origem = Path(sys.argv[1])
    slug = sys.argv[2]
    dia = sys.argv[3] if len(sys.argv) > 3 else date.today().isoformat()

    raiz = Path(__file__).resolve().parent.parent
    destino = raiz / "assets" / "img" / "entradas" / f"{dia}-{slug}.jpg"
    mini = destino.with_name(f"{dia}-{slug}-mini.jpg")
    for f in (destino, mini):
        if f.exists():
            sys.exit(f"{f} já existe — assets são append-only, escolha outro nome.")
    destino.parent.mkdir(parents=True, exist_ok=True)

    im = Image.open(origem)
    im = ImageOps.exif_transpose(im)  # gira de verdade antes de jogar o EXIF fora

    icc = im.info.get("icc_profile")
    if icc:
        im = ImageCms.profileToProfile(
            im, ImageCms.ImageCmsProfile(io.BytesIO(icc)),
            ImageCms.createProfile("sRGB"), outputMode="RGB")
    im = im.convert("RGB")
    web = "/" + destino.relative_to(raiz).as_posix()
    web_mini = "/" + mini.relative_to(raiz).as_posix()
    for arquivo, lado in ((destino, LADO_MAX), (mini, LADO_MINI)):
        copia = im.copy()
        copia.thumbnail((lado, lado), Image.LANCZOS)
        # Copia só os pixels para uma imagem nova: nada do arquivo original sobrevive.
        limpa = Image.new("RGB", copia.size)
        limpa.paste(copia)
        limpa.save(arquivo, "JPEG", quality=QUALIDADE, optimize=True, progressive=True)

        conferida = Image.open(arquivo)
        sobrou = [k for k in conferida.info if k not in ("jfif", "jfif_version", "jfif_unit", "jfif_density", "progressive", "progression")]
        if len(conferida.getexif()) or sobrou:
            sys.exit(f"ATENÇÃO: sobrou metadado em {arquivo}: {sobrou}")
        print(f"ok: {arquivo.name} — {limpa.size[0]}x{limpa.size[1]}, {arquivo.stat().st_size // 1024} KB, sem metadados")

    print("\nfront matter:\n")
    print(f'foto: {web}\nfoto_mini: {web_mini}\nfoto_alt: "descreva a foto aqui"')


if __name__ == "__main__":
    main()
