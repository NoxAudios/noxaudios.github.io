import re

with open('rapid01.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles
content = content.replace('<title>Rapid 01</title>', '<title>Wiskers & Magic</title>')
content = content.replace('Arcade Race 3D', 'Wiskers & Magic')
content = content.replace('Projekt stworzony w zespole 8bit jelly jako RAPID z terminem 6 miesięcy', 'Projekt stworzony przez zespół 8bitJelly')
content = content.replace('https://drive.google.com/file/d/1sbhU_nOfer9ug0x8CDP_kHaREAvHKeaN/view?usp=sharing', 'https://voxten.itch.io/wiskers-and-magic')
content = content.replace('>Pobierz Build<', '>Zagraj (itch.io)<')

# Change main image
content = content.replace('hexit/rapid 01/image.png', 'hexit/wiskers/1.png')

# Strip out specific game contents
start = content.find('<section class="about-section">')
end = content.find('</main>')

new_body = '''<section class="about-section">
            <div class="container">
                <h2 class="section-title">O Projekcie</h2>
                <div class="about-content">
                    <div class="about-text">
                        <p>Wiskers & Magic to gra stworzona przez zespół 8bitJelly. Odpowiadaliśmy za przygotowanie kompletnej ścieżki dźwiękowej.</p>
                        <ul class="project-features">
                            <li><i class="fas fa-check"></i> Pełna produkcja muzyczna (Soundtrack)</li>
                            <li><i class="fas fa-check"></i> Współpraca w modelu Indie</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section class="gallery-section">
            <div class="container">
                <h2 class="section-title">Soundtrack</h2>
                <div class="compact-gallery">
                    <div style="margin: 0 auto; width: fit-content;">
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/_1Se26zpee8?list=PLcCHmkih2ansR-g3frV_qmlZJHtg9Clif" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
            </div>
        </section>

        <section class="gallery-section">
            <div class="container">
                <h2 class="section-title">Zrzuty Ekranu z Gry</h2>
                <div class="compact-gallery">
                    <img src="hexit/wiskers/1.png" alt="Wiskers 1">
                    <img src="hexit/wiskers/2.png" alt="Wiskers 2">
                    <img src="hexit/wiskers/3.png" alt="Wiskers 3">
                    <img src="hexit/wiskers/4.png" alt="Wiskers 4">
                    <img src="hexit/wiskers/5.png" alt="Wiskers 5">
                </div>
            </div>
        </section>
    '''

content = content[:start] + new_body + content[end:]

with open('wiskers.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('wiskers.html generated')
