import os
import re

HEAD_INJECT = """
    <!-- 4NOX WAV Theme Scripts & Styles -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;800&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        black: '#000000',
                        zinc: {
                            800: '#27272a',
                            900: '#18181b',
                            950: '#09090b',
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>
"""

NAVBAR = """
    <!-- Navigation -->
    <nav class="fixed w-full z-50 bg-black/80 backdrop-blur-md border-b border-zinc-900 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <div class="flex-shrink-0 flex items-center">
                    <a href="index.html" class="flex items-center gap-3">
                        <img src="Nox Audios Logo.png" alt="4NOX WAV Logo" class="h-10 w-auto">
                        <span class="text-xl font-extrabold tracking-tighter text-white hover:text-zinc-300 transition-colors hidden sm:block">4NOX WAV</span>
                    </a>
                </div>
                <div class="hidden md:flex space-x-8 lg:space-x-10">
                    <a href="portfolio.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Portfolio</a>
                    <a href="creators.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Creators</a>
                    <a href="index.html#socials" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Socials</a>
                    <a href="contact.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Contact</a>
                </div>
                <div class="md:hidden flex items-center">
                    <button id="mobile-menu-btn" class="text-zinc-400 hover:text-white focus:outline-none p-2">
                        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path id="menu-icon" stroke-linecap="square" stroke-linejoin="miter" stroke-width="1.5" d="M4 6h16M4 12h16M4 18h16"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        <div id="mobile-menu" class="hidden md:hidden bg-black border-b border-zinc-900">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="portfolio.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Portfolio</a>
                <a href="creators.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Creators</a>
                <a href="index.html#socials" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Socials</a>
                <a href="contact.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white tracking-widest uppercase">Contact</a>
            </div>
        </div>
    </nav>
"""

FOOTER = """
    <!-- Footer -->
    <footer class="bg-black py-10 border-t border-zinc-900 text-center mt-24">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col items-center">
            <div class="text-xl font-bold tracking-tighter text-zinc-700 mb-4">4NOX WAV</div>
            <p class="text-zinc-600 text-xs tracking-widest uppercase">
                &copy; <span id="year"></span> 4NOX WAV. All rights reserved.
            </p>
        </div>
    </footer>
"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if os.path.basename(filepath) == 'index.html':
        return

    # Replace <header ...> ... </header>
    content = re.sub(r'<header[^>]*>.*?</header>', NAVBAR, content, flags=re.DOTALL)
    
    # Replace <footer ...> ... </footer>
    content = re.sub(r'<footer[^>]*>.*?</footer>', FOOTER, content, flags=re.DOTALL)
    
    # Clean up old body attributes that might conflict
    content = re.sub(r'<body[^>]*>', r'<body class="antialiased selection:bg-zinc-800 selection:text-white bg-black text-white" style="font-family: \'Inter\', sans-serif;">', content)

    if '<link rel="stylesheet" href="styles.css">' not in content:
        content = content.replace('</head>', '    <link rel="stylesheet" href="styles.css">\n</head>')
    
    if '<script src="scripts.js"></script>' not in content:
        content = content.replace('</body>', '    <script src="scripts.js"></script>\n</body>')
        
    if 'tailwind.config =' not in content:
        content = content.replace('</head>', HEAD_INJECT + '\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filepath}")

directory = '.'
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        process_file(os.path.join(directory, filename))
