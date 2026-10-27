"""Gera src/matrix.svg: chuva de código verde (colunas fixas, semente fixa) e a escolha das pílulas."""
import pathlib
import random

random.seed(1999)
L, A = 1200, 360
CHARS = "0123456789ABCDEFZ:.=*+"  # só o que a fonte embutida tem e não quebra o XML

colunas = []
for i, x in enumerate(range(10, L, 22)):
    n = random.randint(10, 22)
    dur = round(random.uniform(4.5, 9.0), 2)
    atraso = round(-random.uniform(0, dur), 2)
    letras = "".join(
        f'<tspan x="{x}" dy="20" fill-opacity="{round(0.15 + 0.85 * (k / n), 2)}">{random.choice(CHARS)}</tspan>'
        for k in range(n)
    )
    cabeca = f'<tspan x="{x}" dy="20" class="cab">{random.choice(CHARS)}</tspan>'
    colunas.append(
        f'<text class="col" style="animation-duration:{dur}s; animation-delay:{atraso}s" y="0">{letras}{cabeca}</text>'
    )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {A}" width="{L}" height="{A}" role="img" aria-label="Matrix: pílula azul ou pílula vermelha">
  <defs>
    <style>
      /*FONTS*/
      .col {{ font-family:'STM', Consolas, monospace; font-size:16px; fill:#00ff66; animation-name:cai; animation-timing-function:linear; animation-iteration-count:infinite; }}
      .cab {{ fill:#d6ffe4; }}
      @keyframes cai {{ from {{ transform:translateY(-480px) }} to {{ transform:translateY({A + 40}px) }} }}
      .fala {{ font-family:'CPm'; font-size:19px; fill:#d8f5e1; }}
      .quem {{ font-family:'STM', Consolas, monospace; font-size:13px; letter-spacing:3px; fill:#00c853; }}
      .rot {{ font-family:'CP'; font-size:15px; letter-spacing:3px; }}
      .brilha {{ animation: brilha 2.4s ease-in-out infinite; }}
      @keyframes brilha {{ 0%,100% {{ opacity:.55 }} 50% {{ opacity:1 }} }}
    </style>
    <radialGradient id="vinheta" cx="50%" cy="50%" r="65%">
      <stop offset=".35" stop-color="#000" stop-opacity=".0"/>
      <stop offset="1" stop-color="#000" stop-opacity=".85"/>
    </radialGradient>
    <linearGradient id="azul" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6fa8ff"/><stop offset="1" stop-color="#1d4fd8"/></linearGradient>
    <linearGradient id="verm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff6b6b"/><stop offset="1" stop-color="#c3001b"/></linearGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="{L}" height="{A}" fill="#000"/>
  <g opacity=".55">
    {chr(10).join("    " + c for c in colunas)}
  </g>
  <rect width="{L}" height="{A}" fill="url(#vinheta)"/>

  <g transform="translate(160 70)">
    <rect width="880" height="220" rx="4" fill="#000" fill-opacity=".82" stroke="#00c853" stroke-opacity=".35"/>
    <text x="40" y="58" class="fala">Você toma a pílula azul: a história acaba, você acorda na sua cama</text>
    <text x="40" y="86" class="fala">e acredita no que quiser.</text>
    <text x="40" y="124" class="fala">Você toma a pílula vermelha: fica no País das Maravilhas, e eu te mostro</text>
    <text x="40" y="152" class="fala">até onde vai a toca do coelho.</text>
    <text x="40" y="192" class="quem">MORFEU  ::  MATRIX, 1999</text>

    <g transform="translate(640 176)">
      <rect x="0" y="0" width="58" height="22" rx="11" fill="url(#azul)" opacity=".75"/>
      <text x="29" y="-10" text-anchor="middle" class="rot" fill="#6fa8ff" fill-opacity=".7">AZUL</text>
      <g class="brilha" filter="url(#glow)">
        <rect x="120" y="0" width="58" height="22" rx="11" fill="url(#verm)"/>
      </g>
      <text x="149" y="-10" text-anchor="middle" class="rot" fill="#ff6b6b">VERMELHA</text>
    </g>
  </g>
</svg>
'''
pathlib.Path(__file__).with_name("src").joinpath("matrix.svg").write_text(svg, encoding="utf-8")
print("ok matrix.svg")
