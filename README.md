<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Israr Hussain — AI Engineer</title>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet"/>
  <style>
    /* all your CSS here, exactly as you had */
  </style>
</head>
<body>
  <div class="container">
    <!-- HERO SECTION -->
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
        <div class="terminal-line" style="padding-left:20px">
          <span class="prompt">name</span> = <span class="str">"Israr Hussain"</span>
        </div>
        <div class="terminal-line" style="padding-left:20px">
          <span class="prompt">focus</span> = <span class="str">["LLM Systems","RAG Pipelines","FastAPI"]</span>
        </div>
        <div class="terminal-line" style="padding-left:20px">
          <span class="prompt">mission</span> = <span class="str">"Turn AI research into production systems"</span>
        </div>
        <div class="terminal-line" style="padding-left:20px">
          <span class="prompt">open_to</span> = <span class="str">"Remote · Freelance · Collaboration"</span>
        </div>
        <div class="terminal-line" style="padding-left:20px">
          <span class="prompt">available</span> = <span class="bool">True</span> <span class="comment"># Let's build something</span>
        </div>
      </div>

      <div class="social-row">
        <a class="social-btn github" href="#">GitHub</a>
        <a class="social-btn linkedin" href="#">LinkedIn</a>
        <a class="social-btn email" href="#">Email</a>
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
        <div class="project-card"><strong>Autonomous Job Application SaaS:</strong> Searches & applies to matching job posts, designed as scalable SaaS.</div>
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
    const observer = new IntersectionObserver(entries => {
      entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('visible'); });
    }, { threshold: 0.1 });
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
  </script>
</body>
</html>
