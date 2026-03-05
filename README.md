<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Israr Hussain — AI Engineer</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet"/>
<style>
  :root {
    --bg: #080e14;
    --surface: #0d1821;
    --surface2: #111d2a;
    --border: #1a2d3f;
    --teal: #2aa889;
    --teal2: #599cab;
    --teal3: #99d1ce;
    --mint: #a8f0e0;
    --text: #c9d8e3;
    --muted: #5a7a8a;
    --white: #eef4f7;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Animated grid background */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(42,168,137,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(42,168,137,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .container {
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 24px 80px;
    position: relative;
    z-index: 1;
  }

  /* ── HERO ── */
  .hero {
    text-align: center;
    padding: 60px 0 48px;
    position: relative;
  }

  .hero-glow {
    position: absolute;
    top: 0; left: 50%;
    transform: translateX(-50%);
    width: 600px; height: 300px;
    background: radial-gradient(ellipse at center, rgba(42,168,137,0.12) 0%, transparent 70%);
    pointer-events: none;
  }

  .status-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(42,168,137,0.08);
    border: 1px solid rgba(42,168,137,0.25);
    border-radius: 100px;
    padding: 6px 16px;
    font-size: 11px;
    color: var(--teal3);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 28px;
    animation: fadeDown 0.6s ease both;
  }

  .status-dot {
    width: 7px; height: 7px;
    background: var(--teal);
    border-radius: 50%;
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
  }

  .hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(42px, 8vw, 72px);
    font-weight: 800;
    color: var(--white);
    line-height: 1;
    letter-spacing: -0.03em;
    animation: fadeDown 0.6s 0.1s ease both;
  }

  .hero h1 span {
    background: linear-gradient(135deg, var(--teal) 0%, var(--teal3) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .hero-subtitle {
    font-family: 'Syne', sans-serif;
    font-size: 14px;
    font-weight: 600;
    color: var(--muted);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-top: 12px;
    animation: fadeDown 0.6s 0.2s ease both;
  }

  /* Typewriter summary */
  .hero-summary {
    max-width: 580px;
    margin: 28px auto 0;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 24px;
    text-align: left;
    animation: fadeDown 0.6s 0.3s ease both;
    position: relative;
    overflow: hidden;
  }

  .hero-summary::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--teal), transparent);
  }

  .terminal-header {
    display: flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--border);
  }

  .dot { width: 10px; height: 10px; border-radius: 50%; }
  .dot.red { background: #ff5f57; }
  .dot.yellow { background: #febc2e; }
  .dot.green { background: #28c840; }
  .terminal-title { font-size: 10px; color: var(--muted); margin-left: 8px; letter-spacing: 0.05em; }

  .terminal-line {
    font-size: 12px;
    line-height: 1.9;
    color: var(--text);
  }

  .terminal-line .prompt { color: var(--teal); }
  .terminal-line .key { color: var(--teal3); }
  .terminal-line .val { color: #e8c77d; }
  .terminal-line .str { color: #a8d8a8; }
  .terminal-line .bool { color: #f4a261; }
  .terminal-line .comment { color: var(--muted); }

  /* Social links */
  .social-row {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 28px;
    flex-wrap: wrap;
    animation: fadeDown 0.6s 0.4s ease both;
  }

  .social-btn {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 9px 18px;
    border-radius: 8px;
    font-family: 'Syne', sans-serif;
    font-size: 12px;
    font-weight: 600;
    text-decoration: none;
    letter-spacing: 0.04em;
    transition: transform 0.2s, box-shadow 0.2s;
    border: 1px solid transparent;
  }

  .social-btn:hover { transform: translateY(-2px); }
  .social-btn.github { background: #181717; border-color: #333; color: #fff; }
  .social-btn.github:hover { box-shadow: 0 4px 20px rgba(255,255,255,0.1); }
  .social-btn.linkedin { background: #0a66c2; color: #fff; }
  .social-btn.linkedin:hover { box-shadow: 0 4px 20px rgba(10,102,194,0.4); }
  .social-btn.email { background: transparent; border-color: var(--teal); color: var(--teal); }
  .social-btn.email:hover { background: rgba(42,168,137,0.08); box-shadow: 0 4px 20px rgba(42,168,137,0.2); }

  /* ── SECTIONS ── */
  section { margin-top: 56px; }

  .section-label {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 24px;
  }

  .section-label h2 {
    font-family: 'Syne', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--teal);
  }

  .section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border), transparent);
  }

  /* ── ABOUT CARDS ── */
  .about-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }

  .about-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.25s, transform 0.25s;
  }

  .about-card:hover {
    border-color: var(--teal);
    transform: translateY(-3px);
  }

  .about-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at top left, rgba(42,168,137,0.06), transparent 60%);
    pointer-events: none;
  }

  .card-icon { font-size: 22px; margin-bottom: 10px; }
  .card-title {
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 700;
    color: var(--white);
    margin-bottom: 6px;
  }
  .card-body { font-size: 11px; line-height: 1.8; color: var(--muted); }

  /* ── STACK ── */
  .stack-tabs {
    display: flex;
    gap: 6px;
    margin-bottom: 20px;
    flex-wrap: wrap;
  }

  .tab-btn {
    padding: 7px 16px;
    border-radius: 8px;
    border: 1px solid var(--border);
    background: transparent;
    color: var(--muted);
    font-family: 'Syne', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.06em;
    cursor: pointer;
    transition: all 0.2s;
  }

  .tab-btn:hover { border-color: var(--teal2); color: var(--teal2); }
  .tab-btn.active { background: var(--teal); border-color: var(--teal); color: #fff; }

  .stack-panel { display: none; }
  .stack-panel.active { display: flex; flex-wrap: wrap; gap: 10px; }

  .tech-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    font-size: 11px;
    color: var(--text);
    cursor: default;
    transition: all 0.2s;
    position: relative;
  }

  .tech-badge:hover {
    border-color: var(--teal);
    background: var(--surface2);
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(42,168,137,0.15);
  }

  .tech-badge img { width: 16px; height: 16px; object-fit: contain; }

  /* ── PROJECTS ── */
  .projects-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }

  .project-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    position: relative;
    overflow: hidden;
    transition: all 0.25s;
    cursor: pointer;
  }

  .project-card:hover {
    border-color: var(--teal);
    transform: translateY(-3px);
    box-shadow: 0 8px 32px rgba(42,168,137,0.12);
  }

  .project-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--teal), var(--teal3));
    opacity: 0;
    transition: opacity 0.25s;
  }

  .project-card:hover::before { opacity: 1; }

  .project-icon { font-size: 24px; margin-bottom: 10px; }
  .project-title {
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 700;
    color: var(--white);
    margin-bottom: 6px;
  }
  .project-desc { font-size: 11px; line-height: 1.7; color: var(--muted); margin-bottom: 14px; }

  .project-tags { display: flex; flex-wrap: wrap; gap: 6px; }
  .project-tag {
    font-size: 10px;
    padding: 3px 10px;
    border-radius: 100px;
    background: rgba(42,168,137,0.08);
    border: 1px solid rgba(42,168,137,0.2);
    color: var(--teal3);
    letter-spacing: 0.04em;
  }

  /* ── STATS ── */
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-bottom: 24px;
  }

  .stat-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    transition: all 0.25s;
  }

  .stat-card:hover { border-color: var(--teal); transform: translateY(-2px); }

  .stat-number {
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 800;
    color: var(--teal);
    line-height: 1;
  }

  .stat-label { font-size: 10px; color: var(--muted); margin-top: 6px; letter-spacing: 0.08em; text-transform: uppercase; }

  .github-imgs {
    display: flex;
    flex-direction: column;
    gap: 14px;
    align-items: center;
  }

  .github-imgs img { max-width: 100%; border-radius: 8px; }

  .github-row {
    display: flex;
    gap: 14px;
    width: 100%;
    justify-content: center;
    flex-wrap: wrap;
  }

  /* ── FOCUS ── */
  .focus-list { display: flex; flex-direction: column; gap: 10px; }

  .focus-item {
    display: flex;
    align-items: center;
    gap: 14px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 18px;
    transition: all 0.2s;
  }

  .focus-item:hover { border-color: var(--teal); background: var(--surface2); transform: translateX(4px); }
  .focus-icon { font-size: 18px; flex-shrink: 0; }
  .focus-text { font-size: 12px; color: var(--text); line-height: 1.5; }
  .focus-text strong { color: var(--white); font-family: 'Syne', sans-serif; }

  /* ── CTA ── */
  .cta {
    text-align: center;
    margin-top: 64px;
    padding: 40px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    position: relative;
    overflow: hidden;
  }

  .cta::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--teal), transparent);
  }

  .cta h3 {
    font-family: 'Syne', sans-serif;
    font-size: 22px;
    font-weight: 800;
    color: var(--white);
    margin-bottom: 10px;
  }

  .cta p { font-size: 12px; color: var(--muted); margin-bottom: 24px; line-height: 1.7; }

  .cta-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 13px 28px;
    background: var(--teal);
    color: #fff;
    border-radius: 10px;
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 700;
    text-decoration: none;
    letter-spacing: 0.04em;
    transition: all 0.2s;
  }

  .cta-btn:hover {
    background: var(--teal2);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(42,168,137,0.35);
  }

  /* ── ANIMATIONS ── */
  @keyframes fadeDown {
    from { opacity: 0; transform: translateY(-16px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .reveal {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }
  .reveal.visible { opacity: 1; transform: translateY(0); }

  /* scrollbar */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

  @media (max-width: 600px) {
    .about-grid, .projects-grid { grid-template-columns: 1fr; }
    .stats-grid { grid-template-columns: 1fr 1fr; }
    .github-row { flex-direction: column; align-items: center; }
  }
</style>
</head>
<body>

<div class="container">

  <!-- HERO -->
  <div class="hero">
    <div class="hero-glow"></div>

    <div class="status-pill">
      <span class="status-dot"></span>
      Available for Remote Opportunities
    </div>

    <h1>Israr<br/><span>Hussain</span></h1>
    <div class="hero-subtitle">Applied AI Engineer &nbsp;·&nbsp; Pakistan 🇵🇰</div>

    <!-- Terminal Summary -->
    <div class="hero-summary">
      <div class="terminal-header">
        <span class="dot red"></span>
        <span class="dot yellow"></span>
        <span class="dot green"></span>
        <span class="terminal-title">profile.py</span>
      </div>
      <div class="terminal-line">
        <span class="key">class</span> <span class="val">AIEngineer</span>:
      </div>
      <div class="terminal-line" style="padding-left:20px">
        <span class="prompt">name</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= <span class="str">"Israr Hussain"</span>
      </div>
      <div class="terminal-line" style="padding-left:20px">
        <span class="prompt">focus</span> &nbsp;&nbsp;&nbsp;&nbsp;= <span class="str">["LLM Systems", "RAG Pipelines", "FastAPI"]</span>
      </div>
      <div class="terminal-line" style="padding-left:20px">
        <span class="prompt">mission</span> &nbsp; = <span class="str">"Turn AI research into production systems"</span>
      </div>
      <div class="terminal-line" style="padding-left:20px">
        <span class="prompt">open_to</span> &nbsp; = <span class="str">"Remote · Freelance · Collaboration"</span>
      </div>
      <div class="terminal-line" style="padding-left:20px">
        <span class="prompt">available</span> = <span class="bool">True</span> <span class="comment"># Let's build something</span>
      </div>
    </div>

    <div class="social-row">
      <a class="social-btn github" href="https://github.com/israrhussain20110" target="_blank">
        <svg width="14" height="14" fill="white" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
        GitHub
      </a>
      <a class="social-btn linkedin" href="https://linkedin.com/in/israr-hussain-40561a299" target="_blank">
        <svg width="14" height="14" fill="white" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        LinkedIn
      </a>
      <a class="social-btn email" href="mailto:ahmedisrar20110@gmail.com">
        <svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 010 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z"/></svg>
        Email
      </a>
    </div>
  </div>

  <!-- ABOUT -->
  <section class="reveal">
    <div class="section-label">
      <h2>⚡ What I Do</h2>
      <div class="section-line"></div>
    </div>
    <div class="about-grid">
      <div class="about-card">
        <div class="card-icon">🔍</div>
        <div class="card-title">RAG & LLM Systems</div>
        <div class="card-body">Design and ship retrieval-augmented generation pipelines — semantic chunking, vector search, reranking, and streamed LLM responses at production scale.</div>
      </div>
      <div class="about-card">
        <div class="card-icon">⚡</div>
        <div class="card-title">FastAPI Microservices</div>
        <div class="card-body">Build async, high-throughput APIs with Redis caching, auth layers, and clean architecture patterns. 30%+ latency improvements through smart async design.</div>
      </div>
      <div class="about-card">
        <div class="card-icon">🤖</div>
        <div class="card-title">LLM Agent Orchestration</div>
        <div class="card-body">Engineer multi-step agents with tool use, memory, and reasoning chains using LangChain. From ReAct patterns to full autonomous pipelines.</div>
      </div>
      <div class="about-card">
        <div class="card-icon">🏥</div>
        <div class="card-title">Medical AI Background</div>
        <div class="card-body">Built diagnostic image classifiers (85% accuracy) and healthcare analytics APIs. Experience applying AI to high-stakes, real-world domains.</div>
      </div>
    </div>
  </section>

  <!-- STACK -->
  <section class="reveal">
    <div class="section-label">
      <h2>🧰 Tech Stack</h2>
      <div class="section-line"></div>
    </div>

    <div class="stack-tabs">
      <button class="tab-btn active" onclick="switchTab(this,'llm')">🧠 LLM & GenAI</button>
      <button class="tab-btn" onclick="switchTab(this,'ml')">⚙️ ML & Training</button>
      <button class="tab-btn" onclick="switchTab(this,'backend')">🚀 Backend</button>
      <button class="tab-btn" onclick="switchTab(this,'devops')">🐳 DevOps</button>
    </div>

    <div id="tab-llm" class="stack-panel active">
      <div class="tech-badge"><img src="https://img.shields.io/badge/-LangChain-1C3C3C?style=flat-square&logo=chainlink&logoColor=white&labelColor=1C3C3C" style="height:18px;width:auto"/>LangChain</div>
      <div class="tech-badge">🤗 HuggingFace</div>
      <div class="tech-badge">🔮 OpenAI API</div>
      <div class="tech-badge">📦 FAISS</div>
      <div class="tech-badge">🦙 LlamaIndex</div>
      <div class="tech-badge">🔗 Vector Search</div>
      <div class="tech-badge">📝 Prompt Engineering</div>
      <div class="tech-badge">🧪 RAG Pipelines</div>
    </div>

    <div id="tab-ml" class="stack-panel">
      <div class="tech-badge">🔥 PyTorch</div>
      <div class="tech-badge">🤗 Transformers</div>
      <div class="tech-badge">📊 scikit-learn</div>
      <div class="tech-badge">🔢 NumPy</div>
      <div class="tech-badge">🐼 Pandas</div>
      <div class="tech-badge">📈 Time-Series ML</div>
      <div class="tech-badge">🖼️ CNN / VGG16</div>
    </div>

    <div id="tab-backend" class="stack-panel">
      <div class="tech-badge">⚡ FastAPI</div>
      <div class="tech-badge">🐍 Python</div>
      <div class="tech-badge">🍃 MongoDB</div>
      <div class="tech-badge">🐘 PostgreSQL</div>
      <div class="tech-badge">🔴 Redis</div>
      <div class="tech-badge">🔐 Auth & JWT</div>
      <div class="tech-badge">📡 REST APIs</div>
    </div>

    <div id="tab-devops" class="stack-panel">
      <div class="tech-badge">🐳 Docker</div>
      <div class="tech-badge">⚙️ GitHub Actions</div>
      <div class="tech-badge">🐧 Linux</div>
      <div class="tech-badge">🌿 Git</div>
      <div class="tech-badge">📊 Monitoring & Logs</div>
    </div>
  </section>

  <!-- PROJECTS -->
  <section class="reveal">
    <div class="section-label">
      <h2>🚀 Featured Projects</h2>
      <div class="section-line"></div>
    </div>
    <div class="projects-grid">
      <div class="project-card">
        <div class="project-icon">🔍</div>
        <div class="project-title">AI Incident Root Cause Investigator</div>
        <div class="project-desc">Analyzes logs, Git commits & monitoring alerts to pinpoint production incident root causes using semantic search and LLM reasoning.</div>
        <div class="project-tags">
          <span class="project-tag">FastAPI</span>
          <span class="project-tag">LangChain</span>
          <span class="project-tag">Vector Search</span>
          <span class="project-tag">LLM Agents</span>
        </div>
      </div>
      <div class="project-card">
        <div class="project-icon">💬</div>
        <div class="project-title">Document Assistant Chatbot</div>
        <div class="project-desc">RAG system for querying large document collections. Embedding generation, FAISS retrieval, and streamed LLM responses. 100+ concurrent users.</div>
        <div class="project-tags">
          <span class="project-tag">FAISS</span>
          <span class="project-tag">Transformers</span>
          <span class="project-tag">FastAPI</span>
          <span class="project-tag">RAG</span>
        </div>
      </div>
      <div class="project-card">
        <div class="project-icon">📦</div>
        <div class="project-title">AI Inventory Forecast System</div>
        <div class="project-desc">ML pipeline predicting inventory demand from historical operational data. Automated time-series forecasting integrated into analytics workflows.</div>
        <div class="project-tags">
          <span class="project-tag">PyTorch</span>
          <span class="project-tag">Time-Series</span>
          <span class="project-tag">Python</span>
          <span class="project-tag">MLOps</span>
        </div>
      </div>
      <div class="project-card">
        <div class="project-icon">📝</div>
        <div class="project-title">Custom LLM Summarizer</div>
        <div class="project-desc">Hierarchical summarization of large documents via chunking and contextual prompting — handles documents too long for a single LLM context window.</div>
        <div class="project-tags">
          <span class="project-tag">Transformers</span>
          <span class="project-tag">NLP</span>
          <span class="project-tag">Chunking</span>
          <span class="project-tag">Python</span>
        </div>
      </div>
      <div class="project-card">
        <div class="project-icon">💊</div>
        <div class="project-title">Pharmacy Analytics Service</div>
        <div class="project-desc">Backend analytics platform generating KPI reports and operational insights. Reduced manual reporting by 50% with automated MongoDB aggregation pipelines.</div>
        <div class="project-tags">
          <span class="project-tag">FastAPI</span>
          <span class="project-tag">MongoDB</span>
          <span class="project-tag">Analytics</span>
          <span class="project-tag">Python</span>
        </div>
      </div>
      <div class="project-card">
        <div class="project-icon">🦴</div>
        <div class="project-title">Knee Osteoporosis Classifier</div>
        <div class="project-desc">Medical image analysis model achieving 85% accuracy on validation data. Reduced clinical evaluation time by 40% through automated pre-screening pipeline.</div>
        <div class="project-tags">
          <span class="project-tag">CNN</span>
          <span class="project-tag">VGG16</span>
          <span class="project-tag">PyTorch</span>
          <span class="project-tag">Medical AI</span>
        </div>
      </div>
    </div>
  </section>

  <!-- STATS -->
  <section class="reveal">
    <div class="section-label">
      <h2>📊 GitHub Stats</h2>
      <div class="section-line"></div>
    </div>

    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-number" data-target="5">0</div>
        <div class="stat-label">Projects Shipped</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" data-target="85">0</div>
        <div class="stat-label">Model Accuracy %</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" data-target="100">0</div>
        <div class="stat-label">Concurrent Users</div>
      </div>
    </div>

    <div class="github-imgs">
      <div class="github-row">
        <img src="https://github-readme-stats.vercel.app/api?username=israrhussain20110&show_icons=true&theme=github_dark&hide_border=true&include_all_commits=true&count_private=true&title_color=2aa889&icon_color=599cab" style="height:160px"/>
        <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=israrhussain20110&layout=compact&theme=github_dark&hide_border=true&langs_count=6&title_color=2aa889" style="height:160px"/>
      </div>
      <img src="https://github-readme-streak-stats.herokuapp.com/?user=israrhussain20110&theme=github-dark-blue&hide_border=true&ring=2aa889&fire=599cab&currStreakLabel=2aa889" style="max-width:500px;width:100%"/>
      <img src="https://github-readme-activity-graph.vercel.app/graph?username=israrhussain20110&bg_color=0d1117&color=2aa889&line=599cab&point=99d1ce&area=true&hide_border=true" style="width:100%;border-radius:8px"/>
    </div>
  </section>

  <!-- CURRENT FOCUS -->
  <section class="reveal">
    <div class="section-label">
      <h2>🎯 Current Focus</h2>
      <div class="section-line"></div>
    </div>
    <div class="focus-list">
      <div class="focus-item">
        <div class="focus-icon">🔭</div>
        <div class="focus-text"><strong>Scalable RAG Architectures</strong> — multi-stage retrieval, hybrid search, and reranking for production document systems</div>
      </div>
      <div class="focus-item">
        <div class="focus-icon">🤖</div>
        <div class="focus-text"><strong>LLM Orchestration Workflows</strong> — building reliable multi-agent systems with tool use, memory, and structured reasoning</div>
      </div>
      <div class="focus-item">
        <div class="focus-icon">⚡</div>
        <div class="focus-text"><strong>Production AI Microservices</strong> — high-throughput APIs with async patterns, caching, and observability baked in</div>
      </div>
      <div class="focus-item">
        <div class="focus-icon">🌱</div>
        <div class="focus-text"><strong>Vector Databases</strong> — going deep on Pinecone, Weaviate, and Qdrant for large-scale semantic retrieval systems</div>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <div class="cta reveal">
    <h3>Let's Build Something Together</h3>
    <p>Open to collaborating on applied AI systems, LLM infrastructure,<br/>and production AI engineering challenges.</p>
    <a class="cta-btn" href="mailto:ahmedisrar20110@gmail.com">
      <svg width="14" height="14" fill="white" viewBox="0 0 24 24"><path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 010 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z"/></svg>
      ahmedisrar20110@gmail.com
    </a>
  </div>

</div>

<script>
  // Tab switching
  function switchTab(btn, id) {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.stack-panel').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('tab-' + id).classList.add('active');
  }

  // Scroll reveal
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  // Counter animation
  function animateCounter(el) {
    const target = +el.dataset.target;
    const duration = 1200;
    const step = target / (duration / 16);
    let current = 0;
    const timer = setInterval(() => {
      current = Math.min(current + step, target);
      el.textContent = Math.floor(current) + (target === 85 ? '%' : '+');
      if (current >= target) clearInterval(timer);
    }, 16);
  }

  const counterObserver = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.querySelectorAll('[data-target]').forEach(animateCounter);
        counterObserver.unobserve(e.target);
      }
    });
  }, { threshold: 0.3 });
  document.querySelectorAll('.stats-grid').forEach(el => counterObserver.observe(el));
</script>
</body>
</html>
