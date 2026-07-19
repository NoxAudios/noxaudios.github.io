import sys

filepath = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\portfolio.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_tags_1 = '''<div class="release-platforms">
                                <span class="release-platform">Spotify</span>
                               
                            </div>'''
new_tags_1 = '''<div style="margin-top: 10px;">
                                <span class="project-tag">Mix</span>
                                <span class="project-tag">Mastering</span>
                                <span class="project-tag">Produkcja</span>
                                <span class="project-tag">Spotify</span>
                            </div>'''

old_tags_2 = '''<div class="release-platforms">
                                <span class="release-platform">YouTube</span>
                               
                            </div>'''
new_tags_2 = '''<div style="margin-top: 10px;">
                                <span class="project-tag">Mix</span>
                                <span class="project-tag">Mastering</span>
                                <span class="project-tag">Produkcja</span>
                                <span class="project-tag">YouTube</span>
                            </div>'''

content = content.replace(old_tags_1, new_tags_1)
content = content.replace(old_tags_2, new_tags_2)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
    
print("Updated tags in portfolio.html")
