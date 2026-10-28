# -*- coding: utf-8 -*-
import pathlib

aqui = pathlib.Path(r"D:\projetos\perfil-github")
src_dir = aqui / "src"
src_dir.mkdir(exist_ok=True)

# ==============================================================================
# 1. HEADER.SVG — CYBERDECK HUD & NEURAL INTERFACE
# ==============================================================================
header_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-label="Phillipe Barros - AI Solutions Architect &amp; Full Stack Engineer">
  <defs>
    <style>
      /*FONTS*/
      .font-cyber { font-family: 'CP', 'Chakra Petch', 'Segoe UI', system-ui, sans-serif; font-weight: 700; }
      .font-cyber-mid { font-family: 'CPm', 'Chakra Petch', 'Segoe UI', system-ui, sans-serif; font-weight: 500; }
      .font-mono { font-family: 'STM', 'Share Tech Mono', 'JetBrains Mono', Consolas, monospace; }

      .t-hero { font-size: 76px; letter-spacing: 4px; }
      .t-sub { font-size: 15px; letter-spacing: 5px; fill: #38bdf8; }
      .t-telemetry { font-size: 11px; letter-spacing: 2px; fill: #64748b; }
      .t-card-id { font-size: 11px; letter-spacing: 2px; fill: #00f0ff; }
      .t-card-title { font-size: 14.5px; letter-spacing: 1px; fill: #f8fafc; font-weight: 700; }
      .t-card-stack { font-size: 12px; letter-spacing: 0.8px; fill: #94a3b8; }

      .cursor { animation: cur-blink 1s steps(1) infinite; }
      @keyframes cur-blink { 50% { opacity: 0; } }

      .pulse-slow { animation: pulse 3.5s ease-in-out infinite; }
      @keyframes pulse { 0%, 100% { opacity: 0.45; } 50% { opacity: 1; } }

      .glow-react { animation: react-glow 4s ease-in-out infinite; }
      @keyframes react-glow {
        0%, 100% { filter: drop-shadow(0 0 12px rgba(0, 240, 255, 0.35)); }
        50% { filter: drop-shadow(0 0 25px rgba(99, 102, 241, 0.55)); }
      }

      .scan-beam { animation: scan 6s linear infinite; }
      @keyframes scan { 0% { transform: translateY(-40px); } 100% { transform: translateY(440px); } }

      .circuit-flow { stroke-dasharray: 8 12; animation: flow 18s linear infinite; }
      @keyframes flow { to { stroke-dashoffset: -400; } }
    </style>

    <linearGradient id="bg-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#04060a"/>
      <stop offset="60%" stop-color="#070b14"/>
      <stop offset="100%" stop-color="#0a1020"/>
    </linearGradient>

    <radialGradient id="cyan-ambient" cx="30%" cy="35%" r="45%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="indigo-ambient" cx="75%" cy="45%" r="50%">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#6366f1" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="scan-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00f0ff" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
    </linearGradient>

    <pattern id="cyber-grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#1e293b" stroke-opacity="0.35" stroke-width="0.8"/>
    </pattern>

    <linearGradient id="card-glass" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f172a" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="#090d16" stop-opacity="0.88"/>
    </linearGradient>
  </defs>

  <!-- Background Layers -->
  <rect width="1200" height="420" fill="url(#bg-grad)"/>
  <rect width="1200" height="420" fill="url(#cyber-grid)"/>
  <rect width="1200" height="420" fill="url(#cyan-ambient)"/>
  <rect width="1200" height="420" fill="url(#indigo-ambient)"/>
  <rect class="scan-beam" width="1200" height="40" fill="url(#scan-grad)"/>

  <!-- HUD Corner Brackets -->
  <g stroke="#00f0ff" stroke-width="1.5" fill="none" opacity="0.75">
    <path d="M 20 40 L 20 20 L 40 20"/>
    <path d="M 1180 40 L 1180 20 L 1160 20"/>
    <path d="M 20 380 L 20 400 L 40 400"/>
    <path d="M 1180 380 L 1180 400 L 1160 400"/>
  </g>

  <!-- Outer HUD Frame Line -->
  <rect x="20" y="20" width="1160" height="380" fill="none" stroke="#1e293b" stroke-width="1" opacity="0.6"/>

  <!-- Top Telemetry Bar -->
  <g class="font-mono">
    <circle cx="42" cy="38" r="4" fill="#10b981" class="pulse-slow"/>
    <text x="54" y="42" class="t-telemetry"><tspan fill="#10b981">ONLINE</tspan> // PROTOCOLO: S&#195;O PAULO, BR // KERNEL: NEXT.JS 15 x FASTAPI</text>
    <text x="1156" y="42" text-anchor="end" class="t-telemetry">SYS_LATENCY: 0.12ms // ZERO-TRUST // DECK: ACTIVE</text>
    <line x1="30" y1="54" x2="1170" y2="54" stroke="#1e293b" stroke-width="1"/>
  </g>

  <!-- Decorative Target Crosshair -->
  <g stroke="#00f0ff" stroke-opacity="0.3" stroke-width="1">
    <line x1="50" y1="160" x2="70" y2="160"/>
    <line x1="60" y1="150" x2="60" y2="170"/>
    <circle cx="60" cy="160" r="14" fill="none"/>
  </g>

  <!-- Hero Title & Identity -->
  <g transform="translate(96, 175)">
    <!-- Chromatic Underlayer (Violet/Indigo) -->
    <text x="2" y="2" class="font-cyber t-hero glow-react" fill="#6366f1" fill-opacity="0.7">PHILLIPE BARROS</text>
    <!-- Crisp Foreground Layer -->
    <text x="0" y="0" class="font-cyber t-hero" fill="#f8fafc">PHILLIPE BARROS</text>
  </g>

  <!-- Subtitle with Cyberpunk Badges -->
  <g transform="translate(98, 216)" class="font-mono">
    <text x="0" y="0" class="t-sub">AI SOLUTIONS ARCHITECT  //  FULL-STACK ENGINEER</text>
    <text x="470" y="0" class="t-telemetry" fill="#64748b">[MULTI-AGENT &amp; CLOUD PLATFORMS]</text>
  </g>

  <!-- Live Command Simulation Line -->
  <g transform="translate(98, 252)" class="font-mono">
    <rect x="0" y="-15" width="510" height="24" rx="3" fill="#070b14" stroke="#1e293b" stroke-width="1"/>
    <text x="12" y="1" font-size="12" fill="#38bdf8">&gt; init --orchestrate=langgraph --cloud=gcp --stream=sse <tspan fill="#00f0ff" class="cursor">&#9608;</tspan></text>
  </g>

  <!-- Bottom 3 Cyberdeck Architecture Cards -->
  <!-- Card 1: Cognitive Core -->
  <g transform="translate(44, 292)">
    <polygon points="0,0 350,0 366,16 366,88 16,88 0,72" fill="url(#card-glass)" stroke="#1e293b" stroke-width="1"/>
    <line x1="0" y1="0" x2="40" y2="0" stroke="#00f0ff" stroke-width="2"/>
    <circle cx="22" cy="24" r="3.5" fill="#00f0ff" class="pulse-slow"/>
    <text x="34" y="28" class="font-mono t-card-id">01 // N&#218;CLEO COGNITIVO</text>
    <text x="22" y="50" class="font-cyber t-card-title">Sistemas Ag&#234;nticos &amp; IA</text>
    <text x="22" y="72" class="font-mono t-card-stack">LangGraph &#183; Claude MCP &#183; Gemini API &#183; RAG</text>
  </g>

  <!-- Card 2: Reactive Interface -->
  <g transform="translate(424, 292)">
    <polygon points="0,0 350,0 366,16 366,88 16,88 0,72" fill="url(#card-glass)" stroke="#1e293b" stroke-width="1"/>
    <line x1="0" y1="0" x2="40" y2="0" stroke="#61dafb" stroke-width="2"/>
    <circle cx="22" cy="24" r="3.5" fill="#61dafb" class="pulse-slow"/>
    <text x="34" y="28" class="font-mono t-card-id" fill="#61dafb">02 // INTERFACE REATIVA</text>
    <text x="22" y="50" class="font-cyber t-card-title">Frontend &amp; Gr&#225;ficos</text>
    <text x="22" y="72" class="font-mono t-card-stack">React 19 &#183; Next.js 15 &#183; TypeScript &#183; WebGL</text>
  </g>

  <!-- Card 3: Cloud & Scale -->
  <g transform="translate(804, 292)">
    <polygon points="0,0 350,0 366,16 366,88 16,88 0,72" fill="url(#card-glass)" stroke="#1e293b" stroke-width="1"/>
    <line x1="0" y1="0" x2="40" y2="0" stroke="#818cf8" stroke-width="2"/>
    <circle cx="22" cy="24" r="3.5" fill="#818cf8" class="pulse-slow"/>
    <text x="34" y="28" class="font-mono t-card-id" fill="#818cf8">03 // NUVEM &amp; DADOS</text>
    <text x="22" y="50" class="font-cyber t-card-title">Infraestrutura Escal&#225;vel</text>
    <text x="22" y="72" class="font-mono t-card-stack">GCP Cloud Run &#183; BigQuery &#183; Postgres &#183; Docker</text>
  </g>
</svg>"""

(src_dir / "header.svg").write_text(header_svg, encoding="utf-8")
print("ok header.svg")

# ==============================================================================
# 2. DEUS_EX.SVG — DEUS EX MACHINA // SYSTEMIC AUGMENTATIONS & STACK
# ==============================================================================
deus_ex_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 580" width="1200" height="580" role="img" aria-label="Deus Ex Machina - Systemic Augmentations &amp; Engineering Stack">
  <defs>
    <style>
      /*FONTS*/
      .font-cyber { font-family: 'CP', 'Chakra Petch', 'Segoe UI', system-ui, sans-serif; font-weight: 700; }
      .font-cyber-mid { font-family: 'CPm', 'Chakra Petch', 'Segoe UI', system-ui, sans-serif; font-weight: 500; }
      .font-mono { font-family: 'STM', 'Share Tech Mono', 'JetBrains Mono', Consolas, monospace; }

      .ttl-dx { font-size: 34px; letter-spacing: 5px; fill: #e5a93c; }
      .sub-dx { font-size: 12.5px; letter-spacing: 3px; fill: #a1824a; }
      .badge-dx { font-size: 11px; letter-spacing: 2px; fill: #e5a93c; }

      .aug-num { font-size: 11px; letter-spacing: 2.5px; fill: #e5a93c; }
      .aug-cat { font-size: 18px; letter-spacing: 2px; fill: #f8fafc; font-weight: 700; }
      .aug-sub { font-size: 11px; letter-spacing: 1.5px; fill: #94a3b8; }
      .aug-item { font-size: 13.5px; letter-spacing: 1px; fill: #e2e8f0; }
      .aug-status { font-size: 10px; letter-spacing: 2px; fill: #00f0ff; }

      .pulse-gold { animation: p-gold 3s ease-in-out infinite; }
      @keyframes p-gold { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; } }

      .scan-gold { animation: s-gold 8s linear infinite; }
      @keyframes s-gold { 0% { transform: translateY(-60px); } 100% { transform: translateY(620px); } }

      .hex-glow { animation: h-glow 5s ease-in-out infinite; }
      @keyframes h-glow { 0%, 100% { stroke-opacity: 0.12; } 50% { stroke-opacity: 0.28; } }
    </style>

    <linearGradient id="dx-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#08080c"/>
      <stop offset="60%" stop-color="#0d0e14"/>
      <stop offset="100%" stop-color="#06070a"/>
    </linearGradient>

    <!-- Deus Ex Carbon Hexagonal Lattice -->
    <pattern id="hex-mesh" width="32" height="55.4" patternUnits="userSpaceOnUse" patternTransform="scale(1.1)">
      <path d="M16 0 L32 9.24 V27.7 L16 36.94 L0 27.7 V9.24 Z M16 36.94 V55.4" fill="none" stroke="#e5a93c" class="hex-glow" stroke-width="0.9"/>
    </pattern>

    <linearGradient id="dx-feixe" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e5a93c" stop-opacity="0"/>
      <stop offset="50%" stop-color="#e5a93c" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#e5a93c" stop-opacity="0"/>
    </linearGradient>

    <!-- Deus Ex Chamfered Card Component -->
    <symbol id="dx-card" viewBox="0 0 356 195">
      <polygon points="0,18 18,0 356,0 356,177 338,195 0,195" fill="#0b0c12" fill-opacity="0.88" stroke="#2a2318" stroke-width="1.2"/>
      <!-- Top-Left Accent Notch -->
      <polyline points="0,40 0,18 18,0 50,0" fill="none" stroke="#e5a93c" stroke-width="2.2"/>
      <!-- Bottom-Right Accent Notch -->
      <polyline points="356,155 356,177 338,195 306,195" fill="none" stroke="#e5a93c" stroke-width="2.2"/>
      <!-- Internal grid accent -->
      <line x1="20" y1="62" x2="336" y2="62" stroke="#1f232d" stroke-width="1"/>
    </symbol>
  </defs>

  <!-- Background Canvas -->
  <rect width="1200" height="580" fill="url(#dx-bg)"/>
  <rect width="1200" height="580" fill="url(#hex-mesh)"/>
  <rect class="scan-gold" width="1200" height="60" fill="url(#dx-feixe)"/>

  <!-- Top Banner Section -->
  <g transform="translate(44, 48)">
    <!-- Iconic Deus Ex Geometric Triangle Motif -->
    <polygon points="0,0 14,24 28,0" fill="#e5a93c" opacity="0.8"/>
    <polygon points="28,0 42,24 56,0" fill="#e5a93c" opacity="0.45"/>
    <polygon points="14,24 28,48 42,24" fill="#e5a93c" opacity="0.95"/>
    
    <text x="74" y="24" class="font-cyber ttl-dx">DEUS EX MACHINA</text>
    <text x="76" y="44" class="font-mono sub-dx">SARIF DYNAMICS // MATRIZ DE AUMENTOS CIBERN&#201;TICOS // ARQUITETURA DE SISTEMAS</text>

    <!-- Live Telemetry Tag Right -->
    <circle cx="1104" cy="22" r="4.5" fill="#e5a93c" class="pulse-gold"/>
    <text x="1092" y="26" text-anchor="end" class="font-mono badge-dx">STATUS: 100% SINCRONIZADO // ZERO REJEI&#199;&#195;O</text>
  </g>

  <line x1="44" y1="108" x2="1156" y2="108" stroke="#2a2318" stroke-width="1.2"/>

  <!-- ROW 1 OF AUGMENTATION MODULES -->
  <!-- AUG-01: Cognitive Core -->
  <g transform="translate(44, 126)">
    <use href="#dx-card" width="356" height="195"/>
    <text x="24" y="32" class="font-mono aug-num">AUG-01 // COGNITIVE CORE</text>
    <text x="24" y="54" class="font-cyber aug-cat">C&#211;RTEX NEURAL</text>
    <text x="280" y="32" text-anchor="end" class="font-mono aug-status">SYNC_OK</text>

    <text x="24" y="86" class="font-mono aug-item"><tspan fill="#e5a93c">&#9656;</tspan> LangGraph &#183; Multi-Agent Workflows</text>
    <text x="24" y="110" class="font-mono aug-item"><tspan fill="#e5a93c">&#9656;</tspan> Claude MCP (Model Context Protocol)</text>
    <text x="24" y="134" class="font-mono aug-item"><tspan fill="#e5a93c">&#9656;</tspan> Gemini 2.5 API &#183; RAG &amp; Embeddings</text>
    <text x="24" y="158" class="font-mono aug-item"><tspan fill="#e5a93c">&#9656;</tspan> LangChain &#183; Fine-Grained Prompting</text>
  </g>

  <!-- AUG-02: Ocular Interface -->
  <g transform="translate(422, 126)">
    <use href="#dx-card" width="356" height="195"/>
    <text x="24" y="32" class="font-mono aug-num">AUG-02 // OCULAR INTERFACE</text>
    <text x="24" y="54" class="font-cyber aug-cat">&#211;PTICA REATIVA</text>
    <text x="280" y="32" text-anchor="end" class="font-mono aug-status" fill="#61dafb">120Hz_HDR</text>

    <text x="24" y="86" class="font-mono aug-item"><tspan fill="#00f0ff">&#9656;</tspan> React 19 &#183; Next.js 15 (App Router)</text>
    <text x="24" y="110" class="font-mono aug-item"><tspan fill="#00f0ff">&#9656;</tspan> TypeScript 5 &#183; Tipagem Estrita</text>
    <text x="24" y="134" class="font-mono aug-item"><tspan fill="#00f0ff">&#9656;</tspan> Three.js / WebGL &#183; Shaders &amp; Canvas</text>
    <text x="24" y="158" class="font-mono aug-item"><tspan fill="#00f0ff">&#9656;</tspan> PixiJS (Lip-Sync) &#183; Tailwind / CSS Puro</text>
  </g>

  <!-- AUG-03: Neural Spinal -->
  <g transform="translate(800, 126)">
    <use href="#dx-card" width="356" height="195"/>
    <text x="24" y="32" class="font-mono aug-num">AUG-03 // NEURAL SPINAL</text>
    <text x="24" y="54" class="font-cyber aug-cat">CONDUTO DORSAL</text>
    <text x="280" y="32" text-anchor="end" class="font-mono aug-status" fill="#10b981">0ms_BUFFER</text>

    <text x="24" y="86" class="font-mono aug-item"><tspan fill="#10b981">&#9656;</tspan> Python 3.12 &#183; FastAPI &#183; AsyncIO</text>
    <text x="24" y="110" class="font-mono aug-item"><tspan fill="#10b981">&#9656;</tspan> SSE Streaming Real-Time (sem buffer)</text>
    <text x="24" y="134" class="font-mono aug-item"><tspan fill="#10b981">&#9656;</tspan> Node.js &#183; Webhooks &#183; Proxy Reverso</text>
    <text x="24" y="158" class="font-mono aug-item"><tspan fill="#10b981">&#9656;</tspan> Concurrency Limiting &amp; Resili&#234;ncia</text>
  </g>

  <!-- ROW 2 OF AUGMENTATION MODULES -->
  <!-- AUG-04: Synaptic Memory -->
  <g transform="translate(44, 342)">
    <use href="#dx-card" width="356" height="195"/>
    <text x="24" y="32" class="font-mono aug-num">AUG-04 // SYNAPTIC MEMORY</text>
    <text x="24" y="54" class="font-cyber aug-cat">MATRIZ SIN&#193;PTICA</text>
    <text x="280" y="32" text-anchor="end" class="font-mono aug-status">PERSIST_OK</text>

    <text x="24" y="86" class="font-mono aug-item"><tspan fill="#e5a93c">&#9656;</tspan> Google BigQuery on-demand (DW)</text>
    <text x="24" y="110" class="font-mono aug-item"><tspan fill="#e5a93c">&#9656;</tspan> PostgreSQL (pg-grom) &#183; MySQL</text>
    <text x="24" y="134" class="font-mono aug-item"><tspan fill="#e5a93c">&#9656;</tspan> n8n Workflows Orquestrados (self-hosted)</text>
    <text x="24" y="158" class="font-mono aug-item"><tspan fill="#e5a93c">&#9656;</tspan> Redis Cache &#183; Modelos Vetoriais</text>
  </g>

  <!-- AUG-05: Cloud Exoskeleton -->
  <g transform="translate(422, 342)">
    <use href="#dx-card" width="356" height="195"/>
    <text x="24" y="32" class="font-mono aug-num">AUG-05 // CLOUD EXOSKELETON</text>
    <text x="24" y="54" class="font-cyber aug-cat">EXOMALHA NUVEM</text>
    <text x="280" y="32" text-anchor="end" class="font-mono aug-status" fill="#a855f7">AUTO_SCALE</text>

    <text x="24" y="86" class="font-mono aug-item"><tspan fill="#a855f7">&#9656;</tspan> Google Cloud Run (Serverless Multi-Stage)</text>
    <text x="24" y="110" class="font-mono aug-item"><tspan fill="#a855f7">&#9656;</tspan> Docker Alpine &#183; Nginx Hardening</text>
    <text x="24" y="134" class="font-mono aug-item"><tspan fill="#a855f7">&#9656;</tspan> GCP Secret Manager &#183; IAM Least Priv.</text>
    <text x="24" y="158" class="font-mono aug-item"><tspan fill="#a855f7">&#9656;</tspan> CI/CD Automatizado &#183; Linux &amp; PowerShell</text>
  </g>

  <!-- AUG-06: Security & Protocol -->
  <g transform="translate(800, 342)">
    <use href="#dx-card" width="356" height="195"/>
    <text x="24" y="32" class="font-mono aug-num">AUG-06 // SECURITY PROTOCOL</text>
    <text x="24" y="54" class="font-cyber aug-cat">QUEBRA &amp; CIFRA</text>
    <text x="280" y="32" text-anchor="end" class="font-mono aug-status" fill="#ef4444">ZERO_TRUST</text>

    <text x="24" y="86" class="font-mono aug-item"><tspan fill="#ef4444">&#9656;</tspan> Google Workspace OAuth2 &amp; SSO por Grupo</text>
    <text x="24" y="110" class="font-mono aug-item"><tspan fill="#ef4444">&#9656;</tspan> CSP com Nonce per-request &amp; HSTS</text>
    <text x="24" y="134" class="font-mono aug-item"><tspan fill="#ef4444">&#9656;</tspan> HMAC-SHA256 Sess&#245;es HTTP-only</text>
    <text x="24" y="158" class="font-mono aug-item"><tspan fill="#ef4444">&#9656;</tspan> OWASP Top 10 &#183; Defesa contra Inje&#231;&#227;o</text>
  </g>

  <!-- Footer quote inside Deus Ex card -->
  <text x="600" y="558" text-anchor="middle" class="font-mono sub-dx" fill="#64748b">SARIF INDUSTRIES // "O FUTURO N&#195;O &#201; ALGO QUE ESPERAMOS. &#201; ALGO QUE CONSTRU&#205;MOS."</text>
</svg>"""

(src_dir / "deus_ex.svg").write_text(deus_ex_svg, encoding="utf-8")
# Also overwrite augs.svg with this masterpiece so old links keep working
(src_dir / "augs.svg").write_text(deus_ex_svg, encoding="utf-8")
print("ok deus_ex.svg and augs.svg")

# ==============================================================================
# 3. TENET.SVG — CHRISTOPHER NOLAN // TEMPORAL INVERSION & SATOR SQUARE
# ==============================================================================
tenet_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-label="TENET - Temporal Inversion Engine &amp; Sator Square">
  <defs>
    <style>
      /*FONTS*/
      .font-cyber { font-family: 'CP', 'Chakra Petch', 'Segoe UI', system-ui, sans-serif; font-weight: 700; }
      .font-mono { font-family: 'STM', 'Share Tech Mono', 'JetBrains Mono', Consolas, monospace; }

      .ttl-tenet { font-size: 38px; letter-spacing: 8px; font-weight: 700; }
      .sub-tenet { font-size: 12px; letter-spacing: 3px; fill: #94a3b8; }
      .quote-tenet { font-size: 16px; letter-spacing: 3px; fill: #f8fafc; }
      .sator-cell { font-size: 26px; font-weight: 700; letter-spacing: 2px; }

      .flux-red { animation: flux-r 3s linear infinite; }
      @keyframes flux-r { 0% { transform: translateY(-40px); opacity: 0; } 50% { opacity: 0.8; } 100% { transform: translateY(400px); opacity: 0; } }

      .flux-blue { animation: flux-b 3s linear infinite; }
      @keyframes flux-b { 0% { transform: translateY(400px); opacity: 0; } 50% { opacity: 0.8; } 100% { transform: translateY(-40px); opacity: 0; } }

      .pulse-red { animation: p-red 2.5s ease-in-out infinite; }
      @keyframes p-red { 0%, 100% { opacity: 0.5; } 50% { opacity: 1; } }

      .pulse-blue { animation: p-blue 2.5s ease-in-out infinite; }
      @keyframes p-blue { 0%, 100% { opacity: 0.5; } 50% { opacity: 1; } }

      .glow-center { animation: g-center 4s ease-in-out infinite; }
      @keyframes g-center { 0%, 100% { filter: drop-shadow(0 0 10px rgba(0, 240, 255, 0.3)); } 50% { filter: drop-shadow(0 0 25px rgba(239, 68, 68, 0.4)); } }
    </style>

    <linearGradient id="tenet-bg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#140608"/>
      <stop offset="42%" stop-color="#07090f"/>
      <stop offset="50%" stop-color="#0b0e14"/>
      <stop offset="58%" stop-color="#07090f"/>
      <stop offset="100%" stop-color="#06101c"/>
    </linearGradient>

    <linearGradient id="beam-red" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0"/>
      <stop offset="50%" stop-color="#ef4444" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="beam-blue" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00f0ff" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="480" fill="url(#tenet-bg)"/>

  <!-- Grid overlay -->
  <g stroke="#1e293b" stroke-opacity="0.3" stroke-width="0.8">
    <line x1="0" y1="60" x2="1200" y2="60"/>
    <line x1="0" y1="420" x2="1200" y2="420"/>
    <line x1="600" y1="0" x2="600" y2="480" stroke="#38bdf8" stroke-opacity="0.5" stroke-dasharray="4 6"/>
  </g>

  <!-- Flowing Particles / Entropy Streams -->
  <!-- Red side: Forward Entropy (Falling Downward) -->
  <g class="flux-red">
    <circle cx="160" cy="0" r="2.5" fill="#ef4444"/>
    <circle cx="280" cy="50" r="3" fill="#f87171"/>
    <circle cx="420" cy="20" r="2" fill="#ef4444"/>
    <circle cx="210" cy="120" r="3" fill="#fca5a5"/>
    <line x1="320" y1="40" x2="320" y2="90" stroke="url(#beam-red)" stroke-width="2"/>
    <line x1="180" y1="160" x2="180" y2="230" stroke="url(#beam-red)" stroke-width="2"/>
  </g>

  <!-- Blue side: Inverted Entropy (Rising Upward Against Time) -->
  <g class="flux-blue">
    <circle cx="780" cy="0" r="2" fill="#00f0ff"/>
    <circle cx="920" cy="30" r="3.5" fill="#38bdf8"/>
    <circle cx="1040" cy="80" r="2" fill="#60a5fa"/>
    <circle cx="850" cy="140" r="3" fill="#00f0ff"/>
    <line x1="880" y1="60" x2="880" y2="130" stroke="url(#beam-blue)" stroke-width="2"/>
    <line x1="1020" y1="180" x2="1020" y2="260" stroke="url(#beam-blue)" stroke-width="2"/>
  </g>

  <!-- Top Header Bar -->
  <g transform="translate(600, 42)" text-anchor="middle">
    <text class="font-cyber ttl-tenet" fill="#f8fafc">T E N E T</text>
    <text y="24" class="font-mono sub-tenet">TEMPORAL INVERSION ENGINE // PROTOCOLO DE FLUXO ENTROPICO BIDIRECIONAL</text>
  </g>

  <!-- LEFT CHAMBER: RED TEAM (FORWARD) -->
  <g transform="translate(100, 110)">
    <rect width="360" height="280" rx="4" fill="#18080a" fill-opacity="0.82" stroke="#7f1d1d" stroke-width="1.2"/>
    <line x1="0" y1="0" x2="60" y2="0" stroke="#ef4444" stroke-width="3"/>
    <circle cx="24" cy="28" r="4" fill="#ef4444" class="pulse-red"/>
    <text x="36" y="32" class="font-mono" font-size="12" letter-spacing="2" fill="#ef4444">RED TEAM // FLUXO DIRETO</text>
    <text x="24" y="66" class="font-cyber" font-size="20" fill="#f8fafc">ENTROPIA POSITIVA (t &gt; 0)</text>

    <!-- Tactical Telemetry -->
    <text x="24" y="104" class="font-mono" font-size="12" fill="#fca5a5"><tspan fill="#ef4444">&#9656;</tspan> Dire&#231;&#227;o: Tempo Linear Padr&#227;o (+10 min)</text>
    <text x="24" y="130" class="font-mono" font-size="12" fill="#fca5a5"><tspan fill="#ef4444">&#9656;</tspan> Termodin&#226;mica: dS/dt &gt; 0 (Crescente)</text>
    <text x="24" y="156" class="font-mono" font-size="12" fill="#fca5a5"><tspan fill="#ef4444">&#9656;</tspan> Causa precede o Efeito</text>
    <text x="24" y="182" class="font-mono" font-size="12" fill="#fca5a5"><tspan fill="#ef4444">&#9656;</tspan> Pipeline: Ingestion &amp; Live Streaming</text>

    <!-- Code Block -->
    <rect x="20" y="208" width="320" height="52" rx="3" fill="#0c0405" stroke="#450a0a" stroke-width="1"/>
    <text x="32" y="230" class="font-mono" font-size="11" fill="#ef4444">&gt; stream.forward(payload)</text>
    <text x="32" y="248" class="font-mono" font-size="11" fill="#991b1b">&gt; timeline.advance(delta_t = +10)</text>
  </g>

  <!-- CENTER: THE SATOR SQUARE (5x5 PALINDROME) -->
  <g transform="translate(600, 250)" class="glow-center">
    <!-- Square Monolith Background -->
    <rect x="-115" y="-135" width="230" height="270" rx="6" fill="#070910" fill-opacity="0.94" stroke="#334155" stroke-width="1.5"/>
    <text x="0" y="-112" text-anchor="middle" class="font-mono" font-size="10" letter-spacing="3" fill="#94a3b8">ROTAS QUADRATUS</text>

    <!-- SATOR Row 1 -->
    <text x="-80" y="-72" class="font-mono sator-cell" fill="#ef4444">S</text>
    <text x="-40" y="-72" class="font-mono sator-cell" fill="#e2e8f0">A</text>
    <text x="0"   y="-72" class="font-mono sator-cell" fill="#e2e8f0">T</text>
    <text x="40"  y="-72" class="font-mono sator-cell" fill="#e2e8f0">O</text>
    <text x="80"  y="-72" class="font-mono sator-cell" fill="#00f0ff">R</text>

    <!-- AREPO Row 2 -->
    <text x="-80" y="-24" class="font-mono sator-cell" fill="#e2e8f0">A</text>
    <text x="-40" y="-24" class="font-mono sator-cell" fill="#f87171">R</text>
    <text x="0"   y="-24" class="font-mono sator-cell" fill="#e2e8f0">E</text>
    <text x="40"  y="-24" class="font-mono sator-cell" fill="#38bdf8">P</text>
    <text x="80"  y="-24" class="font-mono sator-cell" fill="#e2e8f0">O</text>

    <!-- TENET Row 3 (Highlighted Palindrome Heart) -->
    <rect x="-95" y="-1" width="190" height="34" rx="4" fill="#0f172a" stroke="#00f0ff" stroke-width="1.2"/>
    <text x="-80" y="24" class="font-mono sator-cell" fill="#38bdf8">T</text>
    <text x="-40" y="24" class="font-mono sator-cell" fill="#67e8f9">E</text>
    <text x="0"   y="24" class="font-mono sator-cell" fill="#f8fafc" font-size="30">N</text>
    <text x="40"  y="24" class="font-mono sator-cell" fill="#67e8f9">E</text>
    <text x="80"  y="24" class="font-mono sator-cell" fill="#38bdf8">T</text>

    <!-- OPERA Row 4 -->
    <text x="-80" y="70" class="font-mono sator-cell" fill="#e2e8f0">O</text>
    <text x="-40" y="70" class="font-mono sator-cell" fill="#f87171">P</text>
    <text x="0"   y="70" class="font-mono sator-cell" fill="#e2e8f0">E</text>
    <text x="40"  y="70" class="font-mono sator-cell" fill="#38bdf8">R</text>
    <text x="80"  y="70" class="font-mono sator-cell" fill="#e2e8f0">A</text>

    <!-- ROTAS Row 5 -->
    <text x="-80" y="116" class="font-mono sator-cell" fill="#ef4444">R</text>
    <text x="-40" y="116" class="font-mono sator-cell" fill="#e2e8f0">O</text>
    <text x="0"   y="116" class="font-mono sator-cell" fill="#e2e8f0">T</text>
    <text x="40"  y="116" class="font-mono sator-cell" fill="#e2e8f0">A</text>
    <text x="80"  y="116" class="font-mono sator-cell" fill="#00f0ff">S</text>
  </g>

  <!-- RIGHT CHAMBER: BLUE TEAM (REVERSE) -->
  <g transform="translate(740, 110)">
    <rect width="360" height="280" rx="4" fill="#06121e" fill-opacity="0.82" stroke="#0369a1" stroke-width="1.2"/>
    <line x1="300" y1="0" x2="360" y2="0" stroke="#00f0ff" stroke-width="3"/>
    <circle cx="336" cy="28" r="4" fill="#00f0ff" class="pulse-blue"/>
    <text x="324" y="32" text-anchor="end" class="font-mono" font-size="12" letter-spacing="2" fill="#00f0ff">BLUE TEAM // TEMPO REVERSO</text>
    <text x="24" y="66" class="font-cyber" font-size="20" fill="#f8fafc">ENTROPIA INVERTIDA (t &lt; 0)</text>

    <!-- Tactical Telemetry -->
    <text x="24" y="104" class="font-mono" font-size="12" fill="#bae6fd"><tspan fill="#00f0ff">&#9656;</tspan> Dire&#231;&#227;o: Movimento Regressivo (-10 min)</text>
    <text x="24" y="130" class="font-mono" font-size="12" fill="#bae6fd"><tspan fill="#00f0ff">&#9656;</tspan> Termodin&#226;mica: dS/dt &lt; 0 (Invertida)</text>
    <text x="24" y="156" class="font-mono" font-size="12" fill="#bae6fd"><tspan fill="#00f0ff">&#9656;</tspan> O Efeito antecede a Causa</text>
    <text x="24" y="182" class="font-mono" font-size="12" fill="#bae6fd"><tspan fill="#00f0ff">&#9656;</tspan> Pipeline: Rollback &amp; Speculative Sync</text>

    <!-- Code Block -->
    <rect x="20" y="208" width="320" height="52" rx="3" fill="#030c14" stroke="#0c4a6e" stroke-width="1"/>
    <text x="32" y="230" class="font-mono" font-size="11" fill="#00f0ff">&gt; state.reconcile(reverse = True)</text>
    <text x="32" y="248" class="font-mono" font-size="11" fill="#0284c7">&gt; timeline.invert(delta_t = -10)</text>
  </g>

  <!-- Bottom Nolan Quote & Philosophy -->
  <g transform="translate(600, 448)" text-anchor="middle" class="font-mono">
    <text class="quote-tenet">"N&#195;O TENTE ENTENDER. SINTA."</text>
    <text y="20" font-size="11" letter-spacing="2.5" fill="#64748b">PIN&#199;A TEMPORAL // O QUE ACONTECEU, ACONTECEU. &#201; UMA EXPRESS&#195;O DE F&#201; NA MEC&#194;NICA DO MUNDO.</text>
  </g>
</svg>"""

(src_dir / "tenet.svg").write_text(tenet_svg, encoding="utf-8")
print("ok tenet.svg")

# ==============================================================================
# 4. LEIS.SVG — ASIMOV ROBOTICS & AGENT GOVERNANCE (IDE WINDOW)
# ==============================================================================
leis_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 390" width="1200" height="390" role="img" aria-label="As Leis da Rob&#243;tica de Isaac Asimov - Governan&#231;a de Sistemas de IA">
  <defs>
    <style>
      /*FONTS*/
      .font-mono { font-family: 'STM', 'Share Tech Mono', 'JetBrains Mono', Consolas, monospace; }
      .font-cyber { font-family: 'CP', 'Chakra Petch', 'Segoe UI', system-ui, sans-serif; }

      text { font-size: 15px; }
      .ln { fill: #334155; }
      .cm { fill: #64748b; font-style: italic; }
      .kw { fill: #38bdf8; font-weight: 700; }
      .fn { fill: #a855f7; }
      .str { fill: #fde047; }
      .op { fill: #f43f5e; }
      .tx { fill: #e2e8f0; }

      .cursor { animation: cur 1s steps(1) infinite; }
      @keyframes cur { 50% { opacity: 0; } }
    </style>
  </defs>

  <!-- Editor Window Frame -->
  <rect width="1200" height="390" rx="8" fill="#090d16" stroke="#1e293b" stroke-width="1.2"/>
  
  <!-- Editor Titlebar -->
  <path d="M0,8 Q0,0 8,0 L1192,0 Q1200,0 1200,8 L1200,40 L0,40 Z" fill="#0f172a"/>
  
  <!-- Window Traffic Lights -->
  <circle cx="24" cy="20" r="6" fill="#ef4444"/>
  <circle cx="44" cy="20" r="6" fill="#eab308"/>
  <circle cx="64" cy="20" r="6" fill="#10b981"/>

  <!-- Active Tab -->
  <polygon points="90,40 100,10 270,10 280,40" fill="#090d16"/>
  <text x="120" y="27" class="font-mono" font-size="13" fill="#38bdf8">&#9881; asimov_governance.py</text>
  
  <!-- Inactive Tab -->
  <text x="310" y="27" class="font-mono" font-size="13" fill="#475569">agent_safety.rs</text>
  <text x="1170" y="26" text-anchor="end" class="font-mono" font-size="11.5" fill="#64748b">U.S. ROBOTS &amp; MECHANICAL MEN, INC. // ZERO-LOSS</text>

  <!-- Code Body with 100% Valid UTF-8 Accents -->
  <g transform="translate(0, 70)" class="font-mono">
    <!-- Line 1 -->
    <text x="24" class="ln">01</text>
    <text x="68" class="cm"># Isaac Asimov, 1942. A Lei Zero foi estabelecida em "Os Rob&#243;s e o Imp&#233;rio" (1985).</text>

    <!-- Line 2 -->
    <text x="24" y="28" class="ln">02</text>
    <text x="68" y="28"><tspan class="kw">from</tspan><tspan class="tx"> dataclasses </tspan><tspan class="kw">import</tspan><tspan class="tx"> dataclass</tspan></text>

    <!-- Line 3 -->
    <text x="24" y="56" class="ln">03</text>

    <!-- Line 4 -->
    <text x="24" y="84" class="ln">04</text>
    <text x="68" y="84"><tspan class="kw">LEIS_DA_ROB&#211;TICA</tspan><tspan class="tx">: list[str] </tspan><tspan class="op">=</tspan><tspan class="tx"> [</tspan></text>

    <!-- Line 5 -->
    <text x="24" y="112" class="ln">05</text>
    <text x="96" y="112" class="str">"0. Um rob&#243; n&#227;o pode causar mal &#224; humanidade ou, por omiss&#227;o, permitir que a humanidade sofra dano.",</text>

    <!-- Line 6 -->
    <text x="24" y="140" class="ln">06</text>
    <text x="96" y="140" class="str">"1. Um rob&#243; n&#227;o pode ferir um ser humano ou, por ina&#231;&#227;o, permitir que um ser humano sofra algum mal.",</text>

    <!-- Line 7 -->
    <text x="24" y="168" class="ln">07</text>
    <text x="96" y="168" class="str">"2. Um rob&#243; deve obedecer &#224;s ordens de seres humanos, exceto quando conflitarem com a Lei Maior.",</text>

    <!-- Line 8 -->
    <text x="24" y="196" class="ln">08</text>
    <text x="96" y="196" class="str">"3. Um rob&#243; deve proteger a pr&#243;pria exist&#234;ncia, desde que isso n&#227;o conflite com as Leis anteriores."</text>

    <!-- Line 9 -->
    <text x="24" y="224" class="ln">09</text>
    <text x="68" y="224"><tspan class="tx">]</tspan></text>

    <!-- Line 10 -->
    <text x="24" y="252" class="ln">10</text>
    <text x="68" y="252"><tspan class="kw">assert</tspan><tspan class="tx"> all(verify_safety(lei) </tspan><tspan class="kw">for</tspan><tspan class="tx"> lei </tspan><tspan class="kw">in</tspan><tspan class="tx"> LEIS_DA_ROB&#211;TICA)  </tspan><tspan class="cm"># Protocolo de Alinhamento Ativo</tspan><tspan fill="#00f0ff" class="cursor"> &#9608;</tspan></text>
  </g>
</svg>"""

(src_dir / "leis.svg").write_text(leis_svg, encoding="utf-8")
print("ok leis.svg")

# ==============================================================================
# 5. RODAPE.SVG — BLADE RUNNER MONOLITH (ROY BATTY MONOLOGUE)
# ==============================================================================
rodape_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 190" width="1200" height="190" role="img" aria-label="Blade Runner - Roy Batty: Todos esses momentos se perder&#227;o no tempo">
  <defs>
    <style>
      /*FONTS*/
      .font-cyber { font-family: 'CPm', 'Chakra Petch', 'Segoe UI', system-ui, sans-serif; font-weight: 500; }
      .font-mono { font-family: 'STM', 'Share Tech Mono', 'JetBrains Mono', Consolas, monospace; }

      .quote-batty { font-size: 27px; letter-spacing: 2px; fill: #f1f5f9; }
      .sub-batty { font-size: 12px; letter-spacing: 3.5px; fill: #38bdf8; }

      .rain { animation: drop 1.1s linear infinite; }
      @keyframes drop { from { transform: translate(0, -200px); } to { transform: translate(-30px, 0); } }

      .breathe { animation: br 5s ease-in-out infinite; }
      @keyframes br { 0%, 100% { opacity: 0.65; } 50% { opacity: 1; } }
    </style>

    <linearGradient id="rodape-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#04060a"/>
      <stop offset="60%" stop-color="#090e18"/>
      <stop offset="100%" stop-color="#020306"/>
    </linearGradient>

    <pattern id="rain-pattern" width="60" height="200" patternUnits="userSpaceOnUse">
      <line x1="10" y1="0" x2="4" y2="30" stroke="#38bdf8" stroke-opacity="0.22" stroke-width="1"/>
      <line x1="38" y1="70" x2="32" y2="100" stroke="#38bdf8" stroke-opacity="0.16" stroke-width="1"/>
      <line x1="52" y1="140" x2="46" y2="170" stroke="#38bdf8" stroke-opacity="0.2" stroke-width="1"/>
    </pattern>
  </defs>

  <rect width="1200" height="190" fill="url(#rodape-bg)"/>
  <g class="rain"><rect x="-40" y="0" width="1280" height="390" fill="url(#rain-pattern)"/></g>
  
  <!-- Neon Horizon line -->
  <line x1="0" y1="1" x2="1200" y2="1" stroke="#00f0ff" stroke-opacity="0.45" stroke-width="1.5"/>

  <!-- Monologue -->
  <text x="600" y="86" text-anchor="middle" class="font-cyber quote-batty breathe">"Todos esses momentos se perder&#227;o no tempo, como l&#225;grimas na chuva."</text>
  <text x="600" y="128" text-anchor="middle" class="font-mono sub-batty">ROY BATTY  ::  NEXUS-6  ::  BLADE RUNNER  ::  LOS ANGELES, 2019 &#8594; S&#195;O PAULO, 2026</text>
  <text x="600" y="156" text-anchor="middle" class="font-mono" font-size="10" letter-spacing="3" fill="#64748b">[SIGNAL ENCRYPTED // END OF TRANSMISSION]</text>
</svg>"""

(src_dir / "rodape.svg").write_text(rodape_svg, encoding="utf-8")
print("ok rodape.svg")

print("TODOS OS SVGS FORAM GERADOS COM SUCESSO!")
