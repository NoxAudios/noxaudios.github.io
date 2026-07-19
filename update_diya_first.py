import sys

def update_song(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # portfolio.html pattern
    old_port = '''<div class="release-card">
                        <div class="release-image">
                            <img src="hexit/mmtlddiya.png"" alt="Diya My Mother Told ME">
                            <div class="release-overlay">
                                <a href="https://open.spotify.com/album/7DMzV5bFegW3tYEe6uf1kH" target="_blank" class="btn btn-primary">Słuchaj Teraz</a>
                            </div>
                        </div>
                        <div class="release-content">
                            <h3>DIYA - MY MOTHER TOLD ME</h3>
                            <p>Słowiański Cover</p>
                            <div style="margin-top: 10px;">
                                <span class="project-tag">Mix</span>
                                <span class="project-tag">Mastering</span>
                                <span class="project-tag">Produkcja</span>
                                <span class="project-tag">Spotify</span>
                            </div>
                        </div>
                    </div>'''

    new_port = '''<div class="release-card">
                        <div class="release-image">
                            <img src="https://img.youtube.com/vi/5m4mH2_ReVY/maxresdefault.jpg" alt="Diya - My Mother Told Me">
                            <div class="release-overlay">
                                <a href="https://www.youtube.com/watch?v=5m4mH2_ReVY" target="_blank" class="btn btn-primary">Słuchaj Teraz</a>
                            </div>
                        </div>
                        <div class="release-content">
                            <h3>DIYA - MY MOTHER TOLD ME</h3>
                            <p>Słowiański Cover (ft. HexitRely, Davsky, BRTK)</p>
                            <div style="margin-top: 10px;">
                                <span class="project-tag">Pełna produkcja</span>
                                <span class="project-tag">YouTube</span>
                            </div>
                        </div>
                    </div>'''

    # portfolio-muzyczne.html pattern
    old_music = '''<div class="project-card">
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
                    </div>'''

    new_music = '''<div class="project-card">
                        <div class="project-image">
                            <img src="https://img.youtube.com/vi/5m4mH2_ReVY/maxresdefault.jpg" alt="Diya - My Mother Told Me">
                            <div class="project-overlay">
                                <a href="https://www.youtube.com/watch?v=5m4mH2_ReVY" target="_blank" class="btn btn-primary">Słuchaj na YouTube</a>
                            </div>
                        </div>
                        <div class="project-content">
                            <h3>DIYA - MY MOTHER TOLD ME</h3>
                            <p>Słowiański Cover (ft. HexitRely, Davsky, BRTK)</p>
                            <span class="project-tag">Pełna produkcja</span>
                            <span class="project-tag">YouTube</span>
                        </div>
                    </div>'''

    if old_port in content:
        content = content.replace(old_port, new_port)
        print("Updated " + filepath)
    elif old_music in content:
        content = content.replace(old_music, new_music)
        print("Updated " + filepath)
    else:
        print("Block not found in " + filepath)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_song(r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\portfolio.html')
update_song(r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\portfolio-muzyczne.html')
