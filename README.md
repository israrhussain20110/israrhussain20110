<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Israr Hussain — AI Engineer</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet"/>
<style>
:root{
--bg:#080e14; --surface:#0d1821; --surface2:#111d2a; --border:#1a2d3f;
--teal:#2aa889; --teal2:#599cab; --teal3:#99d1ce; --mint:#a8f0e0;
--text:#c9d8e3; --muted:#5a7a8a; --white:#eef4f7;
}
*{margin:0;padding:0;box-sizing:border-box;}
body{background:var(--bg); color:var(--text); font-family:'JetBrains Mono', monospace; min-height:100vh; overflow-x:hidden;}
body::before{content:'';position:fixed;inset:0;background-image:linear-gradient(rgba(42,168,137,0.03) 1px,transparent 1px), linear-gradient(90deg, rgba(42,168,137,0.03) 1px,transparent 1px); background-size:40px 40px;pointer-events:none;z-index:0;}
.container{max-width:900px;margin:0 auto;padding:40px 24px 80px;position:relative;z-index:1;}
.hero{text-align:center;padding:60px 0 48px;position:relative;}
.hero-glow{position:absolute;top:0;left:50%;transform:translateX(-50%);width:600px;height:300px;background:radial-gradient(ellipse at center, rgba(42,168,137,0.12) 0%, transparent 70%);pointer-events:none;}
.status-pill{display:inline-flex;align-items:center;gap:8px;background:rgba(42,168,137,0.08);border:1px solid rgba(42,168,137,0.25);border-radius:100px;padding:6px 16px;font-size:11px;color:var(--teal3);letter-spacing:0.08em;text-transform:uppercase;margin-bottom:28px;animation:fadeDown 0.6s ease both;}
.status-dot{width:7px;height:7px;background:var(--teal);border-radius:50%;animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1);}50%{opacity:0.5;transform:scale(0.8);}}
.hero h1{font-family:'Syne',sans-serif;font-size:clamp(42px,8vw,72px);font-weight:800;color:var(--white);line-height:1;letter-spacing:-0.03em;animation:fadeDown 0.6s 0.1s ease both;}
.hero h1 span{background:linear-gradient(135deg,var(--teal) 0%,var(--teal3) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.hero-subtitle{font-family:'Syne',sans-serif;font-size:14px;font-weight:600;color:var(--muted);letter-spacing:0.15em;text-transform:uppercase;margin-top:12px;animation:fadeDown 0.6s 0.2s ease both;}
.hero-summary{max-width:580px;margin:28px auto 0;background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:20px 24px;text-align:left;animation:fadeDown 0.6s 0.3s ease both;position:relative;overflow:hidden;}
.hero-summary::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg, transparent, var(--teal), transparent);}
.terminal-header{display:flex;align-items:center;gap:6px;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid var(--border);}
.dot{width:10px;height:10px;border-radius:50%;}.dot.red{background:#ff5f57;}.dot.yellow{background:#febc2e;}.dot.green{background:#28c840;}.terminal-title{font-size:10px;color:var(--muted);margin-left:8px;letter-spacing:0.05em;}
.terminal-line{font-size:12px;line-height:1.9;color:var(--text);}.terminal-line .prompt{color:var(--teal);}.terminal-line .key{color:var(--teal3);}.terminal-line .val{color:#e8c77d;}.terminal-line .str{color:#a8d8a8;}.terminal-line .bool{color:#f4a261;}.terminal-line .comment{color:var(--muted);}
.social-row{display:flex;justify-content:center;gap:10px;margin-top:28px;flex-wrap:wrap;animation:fadeDown 0.6s 0.4s ease both;}
.social-btn{display:inline-flex;align-items:center;gap:7px;padding:9px 18px;border-radius:8px;font-family:'Syne',sans-serif;font-size:12px;font-weight:600;text-decoration:none;letter-spacing:0.04em;transition:transform 0.2s,box-shadow 0.2s;border:1px solid transparent;}
.social-btn:hover{transform:translateY(-2px);}
.social-btn.github{background:#181717;border-color:#333;color:#fff;}.social-btn.github:hover{box-shadow:0 4px 20px rgba(255,255,255,0.1);}
.social-btn.linkedin{background:#0a66c2;color:#fff;}.social-btn.linkedin:hover{box-shadow:0 4px 20px rgba(10,102,194,0.4);}
.social-btn.email{background:transparent;border-color:var(--teal);color:var(--teal);}.social-btn.email:hover{background:rgba(42,168,137,0.08);box-shadow:0 4px 20px rgba(42,168,137,0.2);}
section{margin-top:56px;}
.section-label{display:flex;align-items:center;gap:12px;margin-bottom:24px;}
.section-label h2{font-family:'Syne',sans-serif;font-size:11px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:var(--teal);}
.section-line{flex:1;height:1px;background:linear-gradient(90deg, var(--border), transparent);}
.reveal{opacity:0;transform:translateY(20px);transition:opacity 0.5s ease, transform 0.5s ease;}
.reveal.visible{opacity:1;transform:translateY(0);}
.tech-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:16px;}
.tech-card{background:var(--surface2);border:1px solid var(--border);padding:12px 16px;border-radius:8px;text-align:center;font-size:12px;font-weight:600;transition:transform 0.2s;}
.tech-card:hover{transform:translateY(-2px);border-color:var(--teal);}
.project-grid{display:grid;grid-template-columns:1fr;gap:12px;}
.project-card{background:var(--surface2);border:1px solid var(--border);padding:12px 16px;border-radius:8px;transition:transform 0.2s;}
.project-card:hover{transform:translateY(-2px);border-color:var(--teal);}
.stats-grid{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;}
.stat-card{flex:1 1 120px;background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:12px 16px;text-align:center;font-weight:700;transition:transform 0.2s;}
.stat-card:hover{transform:translateY(-2px);border-color:var(--teal);}
@keyframes fadeDown{from{opacity:0;transform:translateY(-16px);}to{opacity:1;transform:translateY(0);}}
</style>
</head>
<body>
<div class="container">
  <!-- HERO -->
  <div class="hero">
    <div class="hero-glow"></div>
    <div class="status-pill"><span class="status-dot"></span> Available for Remote Opportunities</div>
    <h1>Israr<br/><span>Hussain</span></h1>
    <div class="hero-subtitle">Applied AI Engineer · Pakistan 🇵🇰</div>
    <div class="hero-summary">
      <div class="terminal-header">
        <span class="dot red"></span>
        <span class="dot yellow"></span>
        <span class="dot green"></span>
        <span class="terminal-title">profile.py</span>
      </div>
      <div class="terminal-line"><span class="key">class</span> <span class="val">AIEngineer</span>:</div>
      <div class="terminal-line" style="padding-left:20px"><span class="prompt">name</span> = <span class="str">"Israr Hussain"</span></div>
      <div class="terminal-line" style="padding-left:20px"><span class="prompt">focus</span> = <span class="str">["LLM Systems","RAG Pipelines","FastAPI"]</span></div>
      <div class="terminal-line" style="padding-left:20px"><span class="prompt">mission</span> = <span class="str">"Turn AI research into production systems"</span></div>
      <div class="terminal-line" style="padding-left:20px"><span class="prompt">open_to</span> = <span class="str">"Remote · Freelance · Collaboration"</span></div>
      <div class="terminal-line" style="padding-left:20px"><span class="prompt">available</span> = <span class="bool">True</span> <span class="comment"># Let's build something</span></div>
    </div>
    <div class="social-row">
      <a class="social-btn github" href="https://github.com/israrhussain20110" target="_blank">GitHub</a>
      <a class="social-btn linkedin" href="https://linkedin.com/in/israr-hussain-40561a299" target="_blank">LinkedIn</a>
      <a class="social-btn email" href="mailto:ahmedisrar20110@gmail.com">Email</a>
    </div>
  </div>

  <!-- TECH STACK -->
  <section class="reveal">
    <div class="section-label"><h2>Tech Stack</h2><div class="section-line"></div></div>
    <div class="tech-grid">
      <div class="tech-card">Python</div>
      <div class="tech-card">FastAPI</div>
      <div class="tech-card">LangChain</div>
      <div class="tech-card">RAG Pipelines</div>
      <div class="tech-card">LLMs / GPT</div>
      <div class="tech-card">SQL & NoSQL</div>
      <div class="tech-card">Docker / Kubernetes</div>
      <div class="tech-card">AWS / GCP</div>
      <div class="tech-card">Git & CI/CD</div>
      <div class="tech-card">NLP / ML</div>
    </div>
  </section>

  <!-- PROJECTS -->
  <section class="reveal">
    <div class="section-label"><h2>Projects</h2><div class="section-line"></div></div>
    <div class="project-grid">
      <div class="project-card"><strong>AI Incident Root Cause Investigator:</strong> Reconstructs timelines from logs & monitoring, suggests root causes using NLP + RAG.</div>
      <div class="project-card"><strong>Autonomous Job Application SaaS:</strong> System searches & applies to matching job posts, designed as scalable SaaS.</div>
      <div class="project-card"><strong>RAG Chatbot:</strong> Query & retrieve context-aware answers from structured/unstructured data with embeddings.</div>
    </div>
  </section>

  <!-- STATS -->
  <section class="reveal">
    <div class="section-label"><h2>Current Focus</h2><div class="section-line"></div></div>
    <div class="stats-grid">
      <div class="stat-card">🚀 LLM Optimization</div>
      <div class="stat-card">⚡ Production AI Pipelines</div>
      <div class="stat-card">📈 SaaS AI Tools</div>
      <div class="stat-card">🔗 RAG & Knowledge Graphs</div>
    </div>
  </section>

</div>
<script>
const observer=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible');});},{threshold:0.1});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
</script>
</body>
</html>
