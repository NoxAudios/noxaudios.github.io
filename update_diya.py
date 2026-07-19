import sys

def update_index_and_portfolio():
    # index.html
    filepath_index = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\index.html'
    with open(filepath_index, 'r', encoding='utf-8') as f:
        content_index = f.read()

    old_index = '''<div class="release-card">
                        <div class="release-image">
                            <img src="hexit/mmtlddiya.png"" alt="Diya My Mother Told ME">
                            <div class="release-overlay">
                                <a href="https://open.spotify.com/album/7DMzV5bFegW3tYEe6uf1kH" target="_blank" class="btn btn-primary">Słuchaj Teraz</a>
                            </div>
                        </div>
                        <div class="release-content">
                            <h3>DIYA - MY MOTHER TOLD ME</h3>
                            <p>Słowiański Cover</p>
                            <div class="flex flex-wrap gap-2 mb-8">
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Mix</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Mastering</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Produkcja</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Spotify</span>
                            </div>
                        </div>
                    </div>'''

    new_index = '''<div class="release-card">
                        <div class="release-image">
                            <img src="https://img.youtube.com/vi/5m4mH2_ReVY/maxresdefault.jpg" alt="Diya - My Mother Told Me">
                            <div class="release-overlay">
                                <a href="https://www.youtube.com/watch?v=5m4mH2_ReVY" target="_blank" class="btn btn-primary">Słuchaj Teraz</a>
                            </div>
                        </div>
                        <div class="release-content">
                            <h3>DIYA - MY MOTHER TOLD ME</h3>
                            <p>Słowiański Cover (ft. HexitRely, Davsky, BRTK)</p>
                            <div class="flex flex-wrap gap-2 mb-8">
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Pełna produkcja</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">YouTube</span>
                            </div>
                        </div>
                    </div>'''

    if old_index in content_index:
        content_index = content_index.replace(old_index, new_index)
        with open(filepath_index, 'w', encoding='utf-8') as f:
            f.write(content_index)
        print("Updated index.html")
    else:
        print("Block not found in index.html")

    # portfolio.html
    filepath_port = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\portfolio.html'
    with open(filepath_port, 'r', encoding='utf-8') as f:
        content_port = f.read()

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

    if old_port in content_port:
        content_port = content_port.replace(old_port, new_port)
        with open(filepath_port, 'w', encoding='utf-8') as f:
            f.write(content_port)
        print("Updated portfolio.html")
    else:
        print("Block not found in portfolio.html")

    # portfolio-muzyczne.html
    filepath_music = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\portfolio-muzyczne.html'
    with open(filepath_music, 'r', encoding='utf-8') as f:
        content_music = f.read()

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

    if old_music in content_music:
        content_music = content_music.replace(old_music, new_music)
        with open(filepath_music, 'w', encoding='utf-8') as f:
            f.write(content_music)
        print("Updated portfolio-muzyczne.html")
    else:
        print("Block not found in portfolio-muzyczne.html")

update_index_and_portfolio()
