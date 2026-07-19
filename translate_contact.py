import sys

filepath = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\contact.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('<html lang="en">', '<html lang="pl">'),
    ('<title>Contact - 4NOX WAV</title>', '<title>Kontakt - 4NOX WAV</title>'),
    ('Contact 4NOX WAV for premium sound design and audio solutions.', 'Skontaktuj się z 4NOX WAV w sprawie wysokiej klasy sound designu i rozwiązań audio.'),
    
    # Navigation Desktop
    ('''<div class="hidden md:flex space-x-8 lg:space-x-10">
                    <a href="portfolio.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio</a>
                    <a href="creators.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Creators</a>
                    <a href="index.html#socials" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Socials</a>
                    <a href="contact.html" class="text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Contact</a>
                </div>''', 
    '''<div class="hidden md:flex space-x-8 lg:space-x-10">
                    <a href="portfolio.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Game Dev</a>
                    <a href="portfolio-muzyczne.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Muzyczne</a>
                    <a href="creators.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Twórcy</a>
                    <a href="index.html#socials" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Social Media</a>
                    <a href="contact.html" class="text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Kontakt</a>
                </div>'''),

    # Navigation Mobile
    ('''<div id="mobile-menu" class="hidden md:hidden bg-black border-b border-zinc-900">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio</a>
                <a href="creators.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Creators</a>
                <a href="index.html#socials" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Socials</a>
                <a href="contact.html" class="mobile-link block py-3 text-base font-medium text-white tracking-widest uppercase">Contact</a>
            </div>
        </div>''',
    '''<div id="mobile-menu" class="hidden md:hidden bg-black border-b border-zinc-900">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Game Dev</a>
                <a href="portfolio-muzyczne.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Muzyczne</a>
                <a href="creators.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Twórcy</a>
                <a href="index.html#socials" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Social Media</a>
                <a href="contact.html" class="mobile-link block py-3 text-base font-medium text-white tracking-widest uppercase">Kontakt</a>
            </div>
        </div>'''),

    ('''Get In Touch''', '''Skontaktuj Się z Nami'''),
    ('''Premium Sound Design & Audio Solutions''', '''Wysokiej Klasy Sound Design i Rozwiązania Audio'''),
    ('''Your Name''', '''Twoje Imię'''),
    ('''Your Email''', '''Twój Email'''),
    ('''Message''', '''Wiadomość'''),
    ('''How can we help?''', '''W czym możemy pomóc?'''),
    ('''Send Message''', '''Wyślij Wiadomość'''),
    ('''Copy Email''', '''Skopiuj Email'''),
    ('''All rights reserved.''', '''Wszelkie prawa zastrzeżone.''')
]

for old, new in replacements:
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done contact.html")
