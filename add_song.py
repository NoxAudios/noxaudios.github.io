import sys
import re

def update_portfolio_muzyczne():
    filepath = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\portfolio-muzyczne.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    placeholder_card = '''<div class="project-card">
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
                    </div>'''

    new_card = '''<div class="project-card">
                        <div class="project-image">
                            <img src="https://img.youtube.com/vi/sm2nsd6EOOs/maxresdefault.jpg" alt="Iskiereczka">
                            <div class="project-overlay">
                                <a href="https://www.youtube.com/watch?v=sm2nsd6EOOs" target="_blank" class="btn btn-primary">Słuchaj na YouTube</a>
                            </div>
                        </div>
                        <div class="project-content">
                            <h3>Iskiereczka</h3>
                            <p>Diya ft Hexit Rely, Davsky, BRTK</p>
                            <span class="project-tag">Pełna produkcja</span>
                            <span class="project-tag">YouTube</span>
                        </div>
                    </div>'''

    content = content.replace(placeholder_card, new_card)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
def update_index_and_portfolio(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    old_card_youtube = '''<div class="release-card">
                        <div class="release-image">
                            <img src="hexit/mmtlddiya.png"" alt="Diya My Mother Told ME">
                            <div class="release-overlay">
                                <a href="https://www.youtube.com/watch?v=5m4mH2_ReVY" target="_blank" class="btn btn-primary">Słuchaj Teraz</a>
                            </div>
                        </div>
                        <div class="release-content">
                            <h3>DIYA - MY MOTHER TOLD ME</h3>
                            <p>Słowiański Cover</p>
                            <div class="flex flex-wrap gap-2 mb-8">
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Mix</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Mastering</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Produkcja</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">YouTube</span>
                            </div>
                        </div>
                    </div>'''
                    
    old_card_youtube_portfolio = '''<div class="release-card">
                        <div class="release-image">
                            <img src="hexit/mmtlddiya.png"" alt="Diya My Mother Told ME">
                            <div class="release-overlay">
                                <a href="https://www.youtube.com/watch?v=5m4mH2_ReVY" target="_blank" class="btn btn-primary">Słuchaj Teraz</a>
                            </div>
                        </div>
                        <div class="release-content">
                            <h3>DIYA - MY MOTHER TOLD ME</h3>
                            <p>Słowiański Cover</p>
                            <div style="margin-top: 10px;">
                                <span class="project-tag">Mix</span>
                                <span class="project-tag">Mastering</span>
                                <span class="project-tag">Produkcja</span>
                                <span class="project-tag">YouTube</span>
                            </div>
                        </div>
                    </div>'''
                    
    new_card_index = '''<div class="release-card">
                        <div class="release-image">
                            <img src="https://img.youtube.com/vi/sm2nsd6EOOs/maxresdefault.jpg" alt="Iskiereczka">
                            <div class="release-overlay">
                                <a href="https://www.youtube.com/watch?v=sm2nsd6EOOs" target="_blank" class="btn btn-primary">Słuchaj Teraz</a>
                            </div>
                        </div>
                        <div class="release-content">
                            <h3>Iskiereczka</h3>
                            <p>Diya ft Hexit Rely, Davsky, BRTK</p>
                            <div class="flex flex-wrap gap-2 mb-8">
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Pełna produkcja</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">YouTube</span>
                            </div>
                        </div>
                    </div>'''
                    
    new_card_portfolio = '''<div class="release-card">
                        <div class="release-image">
                            <img src="https://img.youtube.com/vi/sm2nsd6EOOs/maxresdefault.jpg" alt="Iskiereczka">
                            <div class="release-overlay">
                                <a href="https://www.youtube.com/watch?v=sm2nsd6EOOs" target="_blank" class="btn btn-primary">Słuchaj Teraz</a>
                            </div>
                        </div>
                        <div class="release-content">
                            <h3>Iskiereczka</h3>
                            <p>Diya ft Hexit Rely, Davsky, BRTK</p>
                            <div style="margin-top: 10px;">
                                <span class="project-tag">Pełna produkcja</span>
                                <span class="project-tag">YouTube</span>
                            </div>
                        </div>
                    </div>'''

    if filepath.endswith('index.html'):
        content = content.replace(old_card_youtube, new_card_index)
    else:
        content = content.replace(old_card_youtube_portfolio, new_card_portfolio)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_portfolio_muzyczne()
update_index_and_portfolio(r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\index.html')
update_index_and_portfolio(r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\portfolio.html')
print("Songs updated.")
