import os
import glob

html_files = glob.glob('*.html')

old_logo = '''                    <a href="index.html" class="text-2xl font-extrabold tracking-tighter text-white hover:text-zinc-300 transition-colors">
                        4NOX WAV
                    </a>'''

old_logo_alt = '''                    <a href="index.html" class="text-2xl font-extrabold tracking-tighter text-white hover:text-zinc-300 transition-colors">
                        4NOX WAV
                    </a>'''

new_logo = '''                    <a href="index.html" class="flex items-center gap-3">
                        <img src="Nox Audios Logo.png" alt="4NOX WAV Logo" class="h-10 w-auto">
                        <span class="text-xl font-extrabold tracking-tighter text-white hover:text-zinc-300 transition-colors hidden sm:block">4NOX WAV</span>
                    </a>'''

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try multiple ways in case of weird whitespace
    # Using simple replace for exact match
    if old_logo in content:
        content = content.replace(old_logo, new_logo)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed logo in {file_path}')
    else:
        # regex approach for flexible whitespace
        import re
        pattern = re.compile(r'<a\s+href="index\.html"\s+class="text-2xl\s+font-extrabold\s+tracking-tighter\s+text-white\s+hover:text-zinc-300\s+transition-colors">\s*4NOX\s*WAV\s*</a>', re.IGNORECASE)
        new_content, count = pattern.subn(new_logo, content)
        if count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed logo (regex) in {file_path}')
        else:
            print(f'Logo already correct or not found in {file_path}')
