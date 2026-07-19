import os
import glob
import re

html_files = glob.glob('*.html')
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove all existing <link rel="icon"...> tags
    content = re.sub(r'<link[^>]*rel=["\']icon["\'][^>]*>', '', content)
    
    # Add our new favicon right before </head>
    if '</head>' in content:
        content = content.replace('</head>', '    <link rel="icon" type="image/png" href="Nox Audios Logo.png">\n</head>')
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Replaced favicon in {file_path}')
