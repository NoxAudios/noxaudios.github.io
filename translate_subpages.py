import os
import re

files = ['SotD.html', 'EL.html', 'hexforest.html', 'marsfall.html', 'spirit.html', 'rapid01.html', 'forestmaze.html', 'orbsandspirits.html']
base_dir = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io'

nav_en_desktop = '''<div class="hidden md:flex space-x-10">
                    <a href="portfolio.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio</a>
                    <a href="index.html#socials" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Socials</a>
                    <a href="contact.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Contact</a>
                </div>'''
                
nav_pl_desktop = '''<div class="hidden md:flex space-x-10">
                    <a href="portfolio.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Game Dev</a>
                    <a href="portfolio-muzyczne.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio Muzyczne</a>
                    <a href="creators.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Twórcy</a>
                    <a href="index.html#socials" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Social Media</a>
                    <a href="contact.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Kontakt</a>
                </div>'''

nav_en_mobile = '''<div id="mobile-menu" class="hidden md:hidden bg-black border-b border-zinc-900">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio</a>
                <a href="index.html#socials" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Socials</a>
                <a href="contact.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white tracking-widest uppercase">Contact</a>
            </div>
        </div>'''
        
nav_pl_mobile = '''<div id="mobile-menu" class="hidden md:hidden bg-black border-b border-zinc-900">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Game Dev</a>
                <a href="portfolio-muzyczne.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio Muzyczne</a>
                <a href="creators.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Twórcy</a>
                <a href="index.html#socials" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Social Media</a>
                <a href="contact.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white tracking-widest uppercase">Kontakt</a>
            </div>
        </div>'''

replacements = [
    ('<html lang="en">', '<html lang="pl">'),
    (nav_en_desktop, nav_pl_desktop),
    (nav_en_mobile, nav_pl_mobile),
    ('Back to Portfolio', 'Powrót do Portfolio'),
    ('About the Soundtrack', 'O Ścieżce Dźwiękowej'),
    ('About the Sound Design', 'O Sound Designie'),
    ('Soundtrack Samples', 'Próbki Ścieżki Dźwiękowej'),
    ('Songs and Ambients', 'Utwory i Ambienty'),
    ('Sound Effects', 'Efekty Dźwiękowe'),
    ('<h2 class="section-title">Soundtrack</h2>', '<h2 class="section-title">Ścieżka Dźwiękowa</h2>'),
    ('Game Screenshots', 'Zrzuty Ekranu z Gry'),
    ('<h2 class="section-title">Gameplay</h2>', '<h2 class="section-title">Rozgrywka</h2>'),
    ('Game Trailer', 'Zwiastun Gry'),
    ('Download Build', 'Pobierz Build'),
    ('Play on Steam', 'Zagraj na Steam'),
    ('Play on Itch.io', 'Zagraj na Itch.io'),
    ('Play on 8bitjelly', 'Zagraj na 8bitjelly'),
    ('Play Now', 'Zagraj Teraz'),
    ('Collaborator: Dawid Blacharski', 'Współtwórca: Dawid Blacharski'),
    ('Ready to Experience Marsfall?', 'Gotowy na Doświadczenie Marsfall?'),
    ('Dive into this atmospheric sci-fi adventure and experience the immersive sound design firsthand.', 'Zanurz się w tej klimatycznej przygodzie sci-fi i doświadcz z bliska immersyjnego sound designu.'),
    ('Your browser does not support the audio element.', 'Twoja przeglądarka nie obsługuje elementu audio.'),
    ('Our website uses cookies to improve the quality of services. Read our <a href="polityka.html">Privacy Policy</a>.', 'Nasza strona używa plików cookie, aby poprawić jakość usług. Przeczytaj naszą <a href="polityka.html">Politykę Prywatności</a>.'),
    ('<button id="acceptButton">Accept</button>', '<button id="acceptButton">Akceptuj</button>'),
    ('All rights reserved.', 'Wszelkie prawa zastrzeżone.'),
    
    # Specific texts from subpages
    ('Eerie and mysterious soundtrack for a horror adventure game', 'Niepokojąca i tajemnicza ścieżka dźwiękowa do przygodowego horroru'),
    ('The soundtrack "Fear" was created by my friend Dawid "Davsky" Blacharski with my support. Our goal was to create an eerie and mysterious sound that would let players experience the overall feeling of the game before clicking the PLAY button.', 'Ścieżka dźwiękowa "Fear" została stworzona przez mojego przyjaciela Dawida "Davsky\'ego" Blacharskiego z moim wsparciem. Naszym celem było stworzenie niepokojącego i tajemniczego brzmienia, które pozwoli graczom poczuć ogólny klimat gry przed kliknięciem przycisku GRAJ.'),
    ('Below you can listen to the atmospheric tracks and sound effects I contributed to this horror adventure.', 'Poniżej możesz posłuchać klimatycznych utworów i efektów dźwiękowych, które stworzyłem do tego horroru.'),
    
    ('Immersive soundtrack and sound design for an atmospheric puzzle adventure game', 'Immersyjna ścieżka dźwiękowa i sound design do klimatycznej przygodowej gry logicznej'),
    ('All soundtracks in this game were created with the support of my friend Dawid Blacharski. We started from scratch, crafting atmospheric sounds that enhance the mysterious and magical environment of the elemental labyrinth.', 'Wszystkie ścieżki dźwiękowe w tej grze powstały przy wsparciu mojego przyjaciela Dawida Blacharskiego. Zaczęliśmy od zera, tworząc klimatyczne dźwięki, które podkreślają tajemnicze i magiczne środowisko żywiołów.'),
    ('Below you can listen to the soundtracks I created for this immersive puzzle adventure.', 'Poniżej możesz posłuchać ścieżek dźwiękowych, które stworzyłem dla tej wciągającej gry logicznej.'),
    
    ('Hexagonal world sound design with nature and magical elements', 'Sound design heksagonalnego świata z elementami natury i magii'),
    ('All sounds in this game were created by me and my friend Dawid Blacharski. We crafted immersive nature sounds including trees, footsteps, magical elements, pickups, clicks, items, and much more for this unique hexagonal world.', 'Wszystkie dźwięki w tej grze zostały stworzone przeze mnie i mojego przyjaciela Dawida Blacharskiego. Stworzyliśmy immersyjne dźwięki natury, w tym drzewa, kroki, magiczne elementy, podnoszenie przedmiotów, kliknięcia i wiele więcej dla tego unikalnego heksagonalnego świata.'),
    ('Below you can listen to the sounds I created for this geometric forest adventure.', 'Poniżej możesz posłuchać dźwięków, które stworzyłem dla tej geometrycznej leśnej przygody.'),
    
    ('Sci-fi industrial sound design for a Brackeys Game Jam 2024 entry', 'Industrialny sound design sci-fi dla projektu Brackeys Game Jam 2024'),
    ('All sounds in this game were created by me and my friend Dawid Blacharski. We crafted immersive industrial sounds including pipes, ambients, cables, electricity, and much more for this sci-fi adventure.', 'Wszystkie dźwięki w tej grze zostały stworzone przeze mnie i mojego przyjaciela Dawida Blacharskiego. Stworzyliśmy wciągające dźwięki industrialne, w tym rury, ambienty, kable, elektryczność i wiele więcej dla tej przygody sci-fi.'),
    ('This project was created for the Brackeys Game Jam 2024, showcasing our ability to create atmospheric soundscapes for space-themed games.', 'Ten projekt został stworzony na Brackeys Game Jam 2024, pokazując naszą zdolność do tworzenia klimatycznych pejzaży dźwiękowych do gier w kosmosie.'),
    
    ('Mystical forest adventure with immersive nature sound design', 'Mistyczna leśna przygoda z immersyjnym dźwiękiem natury'),
    ('All sounds in this game were created by me and my friend Dawid Blacharski. We crafted immersive nature sounds including trees, footsteps, magical elements, pickups, clicks, items, and much more for this mystical forest adventure.', 'Wszystkie dźwięki w tej grze zostały stworzone przeze mnie i mojego przyjaciela Dawida Blacharskiego. Stworzyliśmy immersyjne dźwięki natury, w tym drzewa, kroki, elementy magiczne, podnoszenie przedmiotów i wiele więcej dla tej mistycznej leśnej przygody.'),
    ('Below you can listen to the sounds I created for this enchanting spirit-filled journey.', 'Poniżej możesz posłuchać dźwięków, które stworzyłem dla tej uroczej, pełnej duchów podróży.'),
    ('Arts by @hinneo', 'Grafika: @hinneo'),
    
    ('Project made in 8bit jelly team as RAPID Deadline 6 months', 'Projekt stworzony w zespole 8bit jelly jako RAPID z terminem 6 miesięcy'),
    ('In a futuristic neon-lit city, every turn is a battle against time, and every sound tells a story.', 'W futurystycznym, neonowym mieście każdy zakręt to walka z czasem, a każdy dźwięk opowiada historię.'),
    ('For Neon Rush, I crafted a full spectrum of sounds capturing the adrenaline and rhythm of high-speed arcade racing — from roaring turbo engines to synthetic UI elements and the atmospheric hum of a city alive at night.', 'Dla Neon Rush stworzyłem pełne spektrum dźwięków, oddając adrenalinę i rytm szybkich wyścigów zręcznościowych — od ryczących silników turbo po syntetyczne elementy UI i klimatyczny szum żyjącego nocą miasta.'),
    ('Dynamic audio layers react to acceleration, drifts, and collisions, creating a powerful sense of motion and energy. You can feel the rhythm of the asphalt, the screech of tires, and the echo of music bouncing off glass skyscrapers.', 'Dynamiczne warstwy audio reagują na przyspieszenie, drifty i kolizje, tworząc potężne poczucie ruchu i energii. Możesz poczuć rytm asfaltu, pisk opon i echo muzyki odbijające się od szklanych drapaczy chmur.'),
    ('The goal was to merge retro-futuristic aesthetics with modern cinematic sound design, so that speed could be heard as vividly as it’s seen.', 'Celem było połączenie retro-futurystycznej estetyki z nowoczesnym kinowym sound designem, tak aby prędkość można było usłyszeć równie wyraźnie, co zobaczyć.'),
    
    ('Nature-inspired sound design for a magical forest adventure game', 'Sound design inspirowany naturą dla magicznej przygodowej gry leśnej'),
    ('All sounds in this game were created by me and my friend Dawid Blacharski. We started from scratch, crafting immersive nature sounds including trees, footsteps, magical elements, pickups, clicks, items, and much more.', 'Wszystkie dźwięki w tej grze zostały stworzone przeze mnie i mojego przyjaciela Dawida Blacharskiego. Zaczęliśmy od zera, tworząc wciągające dźwięki natury, w tym drzewa, kroki, elementy magiczne, kliknięcia i wiele więcej.'),
    ('Below you can listen to the sounds I created for this enchanting forest adventure.', 'Poniżej możesz posłuchać dźwięków, które stworzyłem dla tej urokliwej leśnej przygody.'),
    
    ('Vibrant 3D platformer with immersive sound effects and music', 'Barwna platformówka 3D z immersyjnymi efektami dźwiękowymi i muzyką'),
    ('Together with Davsky, I create immersive sound effects and music for Orbs and Spirits, a vibrant 3D game world. We crafted unique audio that brings the colorful platformer to life through atmospheric sound design.', 'Razem z Davskym stworzyłem immersyjne efekty dźwiękowe i muzykę do Orbs and Spirits, pełnego życia świata gry 3D. Stworzyliśmy unikalne audio, które ożywia tę kolorową platformówkę poprzez klimatyczny sound design.'),
    ('Below you can listen to samples of my work for this enchanting adventure.', 'Poniżej możesz posłuchać próbek mojej pracy nad tą uroczą przygodą.')
]

for file in files:
    path = os.path.join(base_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
print("All subpages translated.")
