import sys
import re

filepath = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# For the first release card (Spotify)
old_tags_1 = '''<div class="release-platforms">
                                <span class="release-platform">Spotify</span>
                               
                            </div>'''
new_tags_1 = '''<div class="flex flex-wrap gap-2 mb-8">
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Mix</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Mastering</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Produkcja</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Spotify</span>
                            </div>'''

# For the second release card (YouTube)
old_tags_2 = '''<div class="release-platforms">
                                <span class="release-platform">YouTube</span>
                               
                            </div>'''
new_tags_2 = '''<div class="flex flex-wrap gap-2 mb-8">
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Mix</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Mastering</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">Produkcja</span>
                                <span class="px-2 py-1 text-xs font-medium text-zinc-400 border border-zinc-800">YouTube</span>
                            </div>'''

content = content.replace(old_tags_1, new_tags_1)
content = content.replace(old_tags_2, new_tags_2)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated tags in index.html")
