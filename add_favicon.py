import os
import glob

html_files = glob.glob('*.html')
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<link rel="icon"' not in content:
        content = content.replace('</head>', '    <link rel="icon" type="image/png" href="Nox Audios Logo.png">\n</head>')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Added favicon to {file_path}')
    else:
        print(f'Favicon already exists in {file_path}')
