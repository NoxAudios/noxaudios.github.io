import sys
import re

filepath = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\portfolio.html'
outpath = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\portfolio-muzyczne.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Update title
content = content.replace('<title>Portfolio Game Dev - Hexit Rely</title>', '<title>Portfolio Muzyczne - Hexit Rely</title>')

# Update Navigation to make Portfolio Muzyczne active
content = content.replace(
    '''<a href="portfolio.html" class="text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Game Dev</a>
                    <a href="portfolio-muzyczne.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Muzyczne</a>''',
    '''<a href="portfolio.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Game Dev</a>
                    <a href="portfolio-muzyczne.html" class="text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Muzyczne</a>'''
)
content = content.replace(
    '''<a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Game Dev</a>
                <a href="portfolio-muzyczne.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Muzyczne</a>''',
    '''<a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Game Dev</a>
                <a href="portfolio-muzyczne.html" class="mobile-link block py-3 text-base font-medium text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Muzyczne</a>'''
)

# Hero Section
content = content.replace('<h1 class="hero-title">Moje Kreatywne Portfolio</h1>', '<h1 class="hero-title">Portfolio Muzyczne</h1>')
content = content.replace('<p class="hero-subtitle">Poznaj moje najnowsze projekty w dziedzinie audio do gier, produkcji muzyki i sound designu</p>', '<p class="hero-subtitle">Odkryj moje najnowsze produkcje muzyczne, miksy i mastering</p>')

# Replace skills section
skills_html = '''<section class="skills-section">
  <h2>Umiejętności</h2>

  <div class="skill">
    <i class="icon fas fa-sliders-h"></i>
    <span class="skill-name">Miksowanie</span>
    <div class="dots">
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
    </div>
  </div>

  <div class="skill">
    <i class="icon fas fa-wave-square"></i>
    <span class="skill-name">Mastering</span>
    <div class="dots">
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
    </div>
  </div>

  <div class="skill">
    <i class="icon fas fa-music"></i>
    <span class="skill-name">Produkcja Muzyczna</span>
    <div class="dots">
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
    </div>
  </div>

  <div class="skill">
    <i class="icon fas fa-guitar"></i>
    <span class="skill-name">Aranżacja</span>
    <div class="dots">
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot"></span>
    </div>
  </div>

  <div class="skill">
    <i class="icon fas fa-headphones"></i>
    <span class="skill-name">Ableton Live</span>
    <div class="dots">
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot"></span>
    </div>
  </div>

  <div class="skill">
  <i class="icon fas fa-drum"></i>
  <span class="skill-name">FL Studio</span>
  <div class="dots vertical">
    <span class="dot filled"></span>
    <span class="dot filled"></span>
    <span class="dot filled"></span>
    <span class="dot filled"></span>
    <span class="dot"></span>
  </div></div>

</section>'''
content = re.sub(r'<section class="skills-section">.*?</section>', skills_html, content, flags=re.DOTALL)

# Replace projects section
projects_html = '''<section class="projects-section">
            <div class="container">
                <h2 class="section-title">Produkcje Muzyczne i Mix/Mastering</h2>
                <div class="projects-grid">

                    <div class="project-card">
                        <div class="project-image">
                            <img src="hexit/mmtlddiya.png" alt="Diya My Mother Told ME">
                            <div class="project-overlay">
                                <a href="https://open.spotify.com/album/7DMzV5bFegW3tYEe6uf1kH" target="_blank" class="btn btn-primary">Słuchaj na Spotify</a>
                            </div>
                        </div>
                        <div class="project-content">
                            <h3>DIYA - MY MOTHER TOLD ME</h3>
                            <p>Słowiański Cover</p>
                            <span class="project-tag">Produkcja</span>
                            <span class="project-tag">Mix</span>
                            <span class="project-tag">Mastering</span>
                            <span class="project-tag">Spotify</span>
                            <span class="project-tag">YouTube</span>
                        </div>
                    </div>
                   
                    <div class="project-card">
                        <div class="project-image">
                            <img src="hexit/mmtlddiya.png" alt="Przykładowy Utwór">
                            <div class="project-overlay">
                                <a href="#" target="_blank" class="btn btn-primary">Słuchaj na SoundCloud</a>
                            </div>
                        </div>
                        <div class="project-content">
                            <h3>Tytuł Utworu (Placeholder)</h3>
                            <p>Opis utworu</p>
                            <span class="project-tag">Mix</span>
                            <span class="project-tag">Mastering</span>
                            <span class="project-tag">SoundCloud</span>
                            <span class="project-tag">iTunes</span>
                        </div>
                    </div>

                </div>
            </div>
        </section>'''
content = re.sub(r'<section class="projects-section">.*?</section>', projects_html, content, flags=re.DOTALL)

with open(outpath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Created portfolio-muzyczne.html")
