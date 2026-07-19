import sys

filepath = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\portfolio.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('<html lang="en">', '<html lang="pl">'),
    ('<title>Portfolio - Hexit Rely</title>', '<title>Portfolio Game Dev - Hexit Rely</title>'),
    
    # Navigation Desktop
    ('''<div class="hidden md:flex space-x-10">
                    <a href="portfolio.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio</a>
                    <a href="index.html#socials" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Socials</a>
                    <a href="contact.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Contact</a>
                </div>''', 
    '''<div class="hidden md:flex space-x-10">
                    <a href="portfolio.html" class="text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Game Dev</a>
                    <a href="portfolio-muzyczne.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Muzyczne</a>
                    <a href="creators.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Twórcy</a>
                    <a href="index.html#socials" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Social Media</a>
                    <a href="contact.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Kontakt</a>
                </div>'''),

    # Navigation Mobile
    ('''<div id="mobile-menu" class="hidden md:hidden bg-black border-b border-zinc-900">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio</a>
                <a href="index.html#socials" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Socials</a>
                <a href="contact.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white tracking-widest uppercase">Contact</a>
            </div>
        </div>''',
    '''<div id="mobile-menu" class="hidden md:hidden bg-black border-b border-zinc-900">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Game Dev</a>
                <a href="portfolio-muzyczne.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Muzyczne</a>
                <a href="creators.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Twórcy</a>
                <a href="index.html#socials" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Social Media</a>
                <a href="contact.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white tracking-widest uppercase">Kontakt</a>
            </div>
        </div>'''),

    # Content
    ('''<h1 class="hero-title">My Creative Portfolio</h1>''', '''<h1 class="hero-title">Moje Kreatywne Portfolio</h1>'''),
    ('''<p class="hero-subtitle">Explore my latest projects in game audio, music production, and sound design</p>''', '''<p class="hero-subtitle">Poznaj moje najnowsze projekty w dziedzinie audio do gier, produkcji muzyki i sound designu</p>'''),
    ('''<h2 class="section-title">Featured Audio Work</h2>''', '''<h2 class="section-title">Wyróżnione Prace Audio</h2>'''),
    ('''<h3>Game Soundtracks</h3>''', '''<h3>Ścieżki Dźwiękowe do Gier</h3>'''),
    ('''<p>Immersive musical experiences for gaming</p>''', '''<p>Immersyjne doświadczenia muzyczne dla gier</p>'''),
    ('''Listen on YouTube''', '''Słuchaj na YouTube'''),
    ('''<p>Jelly Jam 2024 - Atmospheric Soundtrack</p>''', '''<p>Jelly Jam 2024 - Atmosferyczna Ścieżka Dźwiękowa</p>'''),
    ('''<p>Davsky Portfolio - Ambient Soundscape</p>''', '''<p>Portfolio Davsky - Ambientowy Pejzaż Dźwiękowy</p>'''),
    ('''<p>Hexit Rely - Cinematic Composition</p>''', '''<p>Hexit Rely - Kinowa Kompozycja</p>'''),
    ('''<h2 class="section-title">Latest Releases</h2>''', '''<h2 class="section-title">Najnowsze Wydania</h2>'''),
    ('''<p>Slavic Cover</p>''', '''<p>Słowiański Cover</p>'''),
    ('''Listen Now''', '''Słuchaj Teraz'''),
    ('''<h2>Skills</h2>''', '''<h2>Umiejętności</h2>'''),
    ('''<span class="skill-name">Mixing</span>''', '''<span class="skill-name">Miksowanie</span>'''),
    ('''<span class="skill-name">Mastering</span>''', '''<span class="skill-name">Mastering</span>'''),
    ('''<span class="skill-name">Audio Recording</span>''', '''<span class="skill-name">Nagrywanie Audio</span>'''),
    ('''<h2 class="section-title">Game Development Projects</h2>''', '''<h2 class="section-title">Projekty Game Dev</h2>'''),
    ('''View Project''', '''Zobacz Projekt'''),
    ('''<p>Project RAPID of 8bit jelly team</p>''', '''<p>Projekt RAPID od ekipy 8bit jelly</p>'''),
    ('''<p>VOXTEN - Horror Game Soundtrack</p>''', '''<p>VOXTEN - Ścieżka Dźwiękowa do Horroru</p>'''),
    ('''<p>Fantasy Adventure Soundtrack</p>''', '''<p>Ścieżka Dźwiękowa do Gry Przygodowej Fantasy</p>'''),
    ('''<p>8BitJelly - Platformer Game Audio</p>''', '''<p>8BitJelly - Audio do Platformówki</p>'''),
    ('''<p>Brackeys 2024 - Sci-Fi Game Audio</p>''', '''<p>Brackeys 2024 - Audio do Gry Sci-Fi</p>'''),
    ('''<p>Jelly Jam 2024 - Atmospheric Game</p>''', '''<p>Jelly Jam 2024 - Atmosferyczna Gra</p>'''),
    ('''<p>Jelly Jam 2024 - Puzzle Game Audio</p>''', '''<p>Jelly Jam 2024 - Audio do Gry Logicznej</p>'''),
    ('''<p>Jelly Jam 2024 - Strategy Game Audio</p>''', '''<p>Jelly Jam 2024 - Audio do Gry Strategicznej</p>'''),
    
    # Tags
    ('''<span class="project-tag">Sound Design</span>''', '''<span class="project-tag">Sound Design</span>'''),
    ('''<span class="project-tag">Music Production</span>''', '''<span class="project-tag">Produkcja Muzyczna</span>'''),
    ('''<span class="project-taggreen">commercial</span>''', '''<span class="project-taggreen">komercyjny</span>'''),
    ('''<span class="project-tagred">unfinished</span>''', '''<span class="project-tagred">niedokończony</span>'''),
    
    ('''<h2 class="section-title">Behind the Scenes</h2>''', '''<h2 class="section-title">Za Kulisami</h2>'''),
    
    ('''<p>This website uses cookies to improve your experience. <a href="polityka.html">Privacy Policy</a></p>''', '''<p>Ta strona używa plików cookie, aby poprawić Twoje wrażenia. <a href="polityka.html">Polityka Prywatności</a></p>'''),
    ('''<button id="acceptButton">Accept</button>''', '''<button id="acceptButton">Akceptuj</button>'''),
    ('''All rights reserved.''', '''Wszelkie prawa zastrzeżone.'''),
    ('''<p class="hero-subtitle">Explore my latest projects in game audio, music production, and sound design</p>''', '''<p class="hero-subtitle">Poznaj moje najnowsze projekty w dziedzinie audio do gier, produkcji muzyki i sound designu</p>''')
]

for old, new in replacements:
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done portfolio.html")
