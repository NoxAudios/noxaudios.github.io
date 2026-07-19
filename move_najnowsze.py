filepath = r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# The Najnowsze block starts with this comment and ends before the Creators comment
start_marker = '    <!-- Najnowsze Section -->'
end_marker = '    <!-- Creators Section -->'

# Extract the Najnowsze block
start_idx = content.index(start_marker)
end_idx = content.index(end_marker)
najnowsze_block = content[start_idx:end_idx]

# Remove it from current position
content = content[:start_idx] + content[end_idx:]

# Now insert right after hero section (before Portfolio section comment)
insert_before = '    <!-- Portfolio Section -->'
content = content.replace(insert_before, najnowsze_block + '    <!-- Portfolio Section -->', 1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done - Najnowsze moved after hero')
