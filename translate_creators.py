import sys

filepath = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\creators.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('<html lang="en">', '<html lang="pl">'),
    ('<title>Creators - 4NOX WAV</title>', '<title>Twórcy - 4NOX WAV</title>'),
    
    # Navigation Desktop
    ('''<div class="hidden md:flex space-x-8 lg:space-x-10">
                    <a href="portfolio.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio</a>
                    <a href="creators.html" class="text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Creators</a>
                    <a href="index.html#socials" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Socials</a>
                    <a href="contact.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Contact</a>
                </div>''', 
    '''<div class="hidden md:flex space-x-8 lg:space-x-10">
                    <a href="portfolio.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Game Dev</a>
                    <a href="portfolio-muzyczne.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Muzyczne</a>
                    <a href="creators.html" class="text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Twórcy</a>
                    <a href="index.html#socials" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Social Media</a>
                    <a href="contact.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Kontakt</a>
                </div>'''),

    # Navigation Mobile
    ('''<div id="mobile-menu" class="hidden md:hidden bg-black border-b border-zinc-900">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio</a>
                <a href="creators.html" class="mobile-link block py-3 text-base font-medium text-white border-b border-zinc-900 tracking-widest uppercase">Creators</a>
                <a href="index.html#socials" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Socials</a>
                <a href="contact.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white tracking-widest uppercase">Contact</a>
            </div>
        </div>''',
    '''<div id="mobile-menu" class="hidden md:hidden bg-black border-b border-zinc-900">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Game Dev</a>
                <a href="portfolio-muzyczne.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Muzyczne</a>
                <a href="creators.html" class="mobile-link block py-3 text-base font-medium text-white border-b border-zinc-900 tracking-widest uppercase">Twórcy</a>
                <a href="index.html#socials" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Social Media</a>
                <a href="contact.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white tracking-widest uppercase">Kontakt</a>
            </div>
        </div>'''),

    ('''The Minds Behind 4NOX''', '''Twórcy 4NOX'''),
    ('''Meet the audio visionaries crafting the next generation of sound design.''', '''Poznaj wizjonerów audio, którzy tworzą następną generację sound designu.'''),
    ('''Owner & Lead Audio Director''', '''Właściciel & Główny Reżyser Audio'''),
    ('''Founder and lead visionary at 4NOX. Specialized in immersive soundscapes, game audio engines, and electronic music production. Master of atmospheric tension, cinematic punch, and shaping the overarching audio direction for major projects.''', '''Założyciel i główny wizjoner w 4NOX. Specjalizuje się w immersyjnych pejzażach dźwiękowych, silnikach audio w grach oraz produkcji muzyki elektronicznej. Mistrz budowania atmosferycznego napięcia, kinowego uderzenia i nadawania głównego kierunku audio dla kluczowych projektów.'''),
    ('''Co-Owner & Sound Designer''', '''Współwłaściciel & Sound Designer'''),
    ('''Co-founder and dedicated audio specialist. Focused on meticulous Foley recording, interactive UI sound synthesis, and bringing digital environments to life through highly detailed auditory feedback.''', '''Współzałożyciel i dedykowany specjalista ds. audio. Skupiony na drobiazgowym nagrywaniu efektów Foley, interaktywnej syntezie dźwięku UI oraz ożywianiu cyfrowych środowisk poprzez wysoce szczegółowe sprzężenie zwrotne audio.'''),
    
    ('''All rights reserved.''', '''Wszelkie prawa zastrzeżone.'''),
    ('''Click to Copy''', '''Kliknij, aby skopiować''')
]

for old, new in replacements:
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done creators.html")
