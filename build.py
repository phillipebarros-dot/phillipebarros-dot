"""Monta os SVGs do perfil: troca /*FONTS*/ pelas fontes embutidas (o GitHub não carrega fonte de fora).
Uso: python build.py   (lê src/*.svg e fontes/*.woff2, grava assets/*.svg)"""
import base64
import pathlib

aqui = pathlib.Path(__file__).parent
FONTES = {"CP": "ChakraPetch700.woff2", "CPm": "ChakraPetch500.woff2", "STM": "ShareTechMono.woff2"}

blocos = []
for familia, arquivo in FONTES.items():
    dados = base64.b64encode((aqui / "fontes" / arquivo).read_bytes()).decode()
    blocos.append(f"@font-face {{ font-family:'{familia}'; src:url(data:font/woff2;base64,{dados}) format('woff2'); }}")
css = "\n      ".join(blocos)

(aqui / "assets").mkdir(exist_ok=True)
for svg in sorted((aqui / "src").glob("*.svg")):
    (aqui / "assets" / svg.name).write_text(svg.read_text(encoding="utf-8").replace("/*FONTS*/", css), encoding="utf-8")
    print("ok", svg.name)
