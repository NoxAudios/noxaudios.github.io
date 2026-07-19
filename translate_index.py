import sys

filepath = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('<html lang="en" class="scroll-smooth">', '<html lang="pl" class="scroll-smooth">'),
    ('<title>4NOX WAV | Premium Sound Design</title>', '<title>4NOX WAV | Dźwięk Premium</title>'),
    ('Premium Sound Design & Audio Solutions for Games & Media', 'Wysokiej Klasy Sound Design i Rozwiązania Audio dla Gier i Mediów'),
    
    # Navigation Desktop
    ('''<div class="hidden md:flex space-x-8 lg:space-x-10">
                    <a href="portfolio.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio</a>
                    <a href="creators.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Creators</a>
                    <a href="#socials" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Socials</a>
                    <a href="contact.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Contact</a>
                </div>''', 
    '''<div class="hidden md:flex space-x-8 lg:space-x-10">
                    <a href="portfolio.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Game Dev</a>
                    <a href="portfolio-muzyczne.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Muzyczne</a>
                    <a href="creators.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Twórcy</a>
                    <a href="#socials" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Social Media</a>
                    <a href="contact.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Kontakt</a>
                </div>'''),

    # Navigation Mobile
    ('''<div id="mobile-menu" class="hidden md:hidden bg-black border-b border-zinc-900">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio</a>
                <a href="creators.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Creators</a>
                <a href="#socials" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Socials</a>
                <a href="contact.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white tracking-widest uppercase">Contact</a>
            </div>
        </div>''',
    '''<div id="mobile-menu" class="hidden md:hidden bg-black border-b border-zinc-900">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Game Dev</a>
                <a href="portfolio-muzyczne.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Muzyczne</a>
                <a href="creators.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Twórcy</a>
                <a href="#socials" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Social Media</a>
                <a href="contact.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white tracking-widest uppercase">Kontakt</a>
            </div>
        </div>'''),

    # Hero Section
    ('''Crafting Cinematic Soundscapes & Interactive Game Audio''', '''Tworzenie Kinowych Pejzaży Dźwiękowych i Interaktywnego Audio do Gier'''),
    ('''Elevate your digital experiences with meticulously crafted soundscapes, hard-hitting UI audio, and immersive Foley. Industry-standard quality, zero compromises.''', '''Wzbogać swoje cyfrowe doświadczenia dzięki pieczołowicie przygotowanym pejzażom dźwiękowym, mocnemu audio UI i immersyjnym efektom Foley. Jakość branżowych standardów, zero kompromisów.'''),
    ('''Explore Sounds''', '''Eksploruj Dźwięki'''),
    ('''Get Support''', '''Uzyskaj Wsparcie'''),

    # Portfolio Section
    ('''Featured Audio''', '''Wyróżnione Projekty'''),
    ('''Curated collections designed for modern game engines and high-end media productions.''', '''Wyselekcjonowane kolekcje stworzone dla nowoczesnych silników gier i wysokiej klasy produkcji multimedialnych.'''),
    ('''Immersive horror game soundtrack and unsettling atmospheric sound design.''', '''Immersyjna ścieżka dźwiękowa do horroru i niepokojący atmosferyczny sound design.'''),
    ('''View Project''', '''Zobacz Projekt'''),
    ('''Fantasy adventure soundtrack with dynamic music production and FMOD implementation.''', '''Ścieżka dźwiękowa do przygodowej gry fantasy z dynamiczną produkcją muzyki i implementacją FMOD.'''),
    ('''Music Production''', '''Produkcja Muzyczna'''),
    ('''Jelly Jam 2024 - Strategy game audio featuring organic nature sounds and magical elements.''', '''Jelly Jam 2024 - Audio do gry strategicznej zawierające organiczne dźwięki natury i magiczne elementy.'''),
    ('''Project RAPID of 8bit jelly team. High-octane arcade racing sound effects and driving music.''', '''Projekt RAPID od ekipy 8bit jelly. Wysokooktanowe efekty dźwiękowe do wyścigów zręcznościowych i muzyka do jazdy.'''),
    ('''Jelly Jam 2024 - Atmospheric game featuring ethereal ambient tracks and subtle foley interactions.''', '''Jelly Jam 2024 - Atmosferyczna gra zawierająca eteryczne ścieżki ambientowe i subtelne interakcje foley.'''),
    
    # Creators Section
    ('''The Minds Behind 4NOX''', '''Twórcy 4NOX'''),
    ('''<p class="text-zinc-500 text-sm uppercase tracking-widest mb-4">Owner</p>''', '''<p class="text-zinc-500 text-sm uppercase tracking-widest mb-4">Właściciel</p>'''),
    ('''Lead visionary specialized in immersive soundscapes and shaping overarching audio direction.''', '''Główny wizjoner specjalizujący się w immersyjnych pejzażach dźwiękowych i kształtowaniu ogólnego kierunku audio.'''),
    ('''<p class="text-zinc-500 text-sm uppercase tracking-widest mb-4">Co-Owner</p>''', '''<p class="text-zinc-500 text-sm uppercase tracking-widest mb-4">Współwłaściciel</p>'''),
    ('''Dedicated audio specialist focused on meticulous Foley recording and interactive UI sound synthesis.''', '''Dedykowany specjalista ds. audio skupiający się na skrupulatnym nagrywaniu efektów Foley i interaktywnej syntezie dźwięku UI.'''),
    ('''Meet The Team ''', '''Poznaj Zespół '''),

    # Social Links Section
    ('''<h2 class="text-3xl font-bold tracking-tight text-white mb-16">Network</h2>''', '''<h2 class="text-3xl font-bold tracking-tight text-white mb-16">Social Media</h2>'''),

    # Support Center Section
    ('''Support Center''', '''Centrum Wsparcia'''),
    ('''Asset store verification hub & frequently asked questions.''', '''Centrum weryfikacji asset store i często zadawane pytania.'''),
    ('''What does the commercial license cover?''', '''Co obejmuje licencja komercyjna?'''),
    ('''Our standard commercial license allows you to use the audio assets in unlimited commercial projects, including video games, films, YouTube videos, and podcasts. You may not resell, redistribute, or re-package the raw audio files as standalone assets.''', '''Nasza standardowa licencja komercyjna pozwala na wykorzystanie zasobów audio w nieograniczonej liczbie projektów komercyjnych, w tym grach wideo, filmach, filmach na YouTube i podcastach. Nie możesz odsprzedawać, redystrybuować ani przepakowywać surowych plików audio jako samodzielnych zasobów.'''),
    ('''What formats are the audio files delivered in?''', '''W jakich formatach dostarczane są pliki audio?'''),
    ('''All our asset packs are delivered in industry-standard 24-bit / 96kHz or 44.1kHz WAV format for maximum fidelity. We also provide optimized OGG formats where applicable for direct game engine integration (Unity, Unreal Engine, Godot).''', '''Wszystkie nasze pakiety są dostarczane w standardowym dla branży formacie 24-bit / 96kHz lub 44.1kHz WAV, aby zapewnić maksymalną wierność. Tam gdzie to możliwe, udostępniamy również zoptymalizowane formaty OGG do bezpośredniej integracji z silnikami gier (Unity, Unreal Engine, Godot).'''),
    ('''What is your refund policy?''', '''Jaka jest wasza polityka zwrotów?'''),
    ('''Due to the digital nature of our products, we generally do not offer refunds once the files have been downloaded. However, if you experience technical issues with the files or accidental duplicate purchases, please contact our support team to resolve the matter.''', '''Ze względu na cyfrowy charakter naszych produktów, generalnie nie oferujemy zwrotów po pobraniu plików. Jeśli jednak napotkasz problemy techniczne z plikami lub omyłkowo dokonasz podwójnego zakupu, skontaktuj się z naszym zespołem wsparcia, abyśmy mogli rozwiązać sprawę.'''),
    ('''Direct Contact''', '''Bezpośredni Kontakt'''),

    # Footer
    ('''All rights reserved.''', '''Wszelkie prawa zastrzeżone.'''),
    
    ('''4NOX WAV - Profesjonalny sound design dla gier i produkcji filmowych. Immersyjne dźwięki, muzyka i implementacja FMOD/Unity. Sprawdź nasze portfolio!''', '''4NOX WAV - Profesjonalny sound design dla gier i produkcji filmowych. Immersyjne dźwięki, muzyka i implementacja FMOD/Unity. Sprawdź nasze portfolio!''')
]

for old, new in replacements:
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done index.html")
