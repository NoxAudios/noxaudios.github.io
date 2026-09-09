import re
import glob

nav_template = """    <!-- Navigation Header -->
    <nav class="fixed w-full z-50 bg-black/85 backdrop-blur-md border-b border-zinc-900 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <!-- Logo -->
                <div class="flex-shrink-0 flex items-center">
                    <a href="index.html" class="flex items-center gap-3 group">
                        <img src="Nox Audios Logo.png" alt="4NOX WAV Logo" class="h-10 w-auto transition-transform duration-300 group-hover:scale-105">
                        <span class="text-xl font-extrabold tracking-tighter text-white hover:text-zinc-300 transition-colors hidden sm:block">4NOX WAV</span>
                    </a>
                </div>
                
                <!-- Desktop Menu -->
                <div class="hidden md:flex items-center space-x-6 lg:space-x-8">
                    <!-- Rozwijane Portfolio -->
                    <div class="nav-dropdown py-2">
                        <button class="flex items-center gap-1.5 text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium focus:outline-none cursor-pointer group">
                            <span>Portfolio</span>
                            <svg class="w-3.5 h-3.5 text-zinc-500 group-hover:text-white transition-transform duration-200 group-hover:translate-y-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                            </svg>
                        </button>
                        <div class="nav-dropdown-menu py-2">
                            <a href="portfolio-muzyczne.html" class="block px-5 py-3 text-xs tracking-widest uppercase text-zinc-300 hover:text-white hover:bg-zinc-900 transition-colors border-b border-zinc-900/60">
                                ♫ Muzyczne
                            </a>
                            <a href="portfolio.html" class="block px-5 py-3 text-xs tracking-widest uppercase text-zinc-300 hover:text-white hover:bg-zinc-900 transition-colors">
                                🎮 Game Dev
                            </a>
                        </div>
                    </div>

                    <a href="index.html#cennik" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Oferta</a>
                    <a href="creators.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Twórcy</a>
                    <a href="index.html#socials" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Social Media</a>
                    <a href="contact.html" class="text-zinc-400 hover:text-white transition-colors duration-300 text-sm tracking-widest uppercase font-medium">Kontakt</a>
                </div>
                
                <!-- Mobile Menu Button -->
                <div class="md:hidden flex items-center">
                    <button id="mobile-menu-btn" class="text-zinc-400 hover:text-white focus:outline-none p-2" aria-label="Otwórz menu mobilne">
                        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path id="menu-icon" stroke-linecap="square" stroke-linejoin="miter" stroke-width="1.5" d="M4 6h16M4 12h16M4 18h16"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Mobile Menu Panel -->
        <div id="mobile-menu" class="hidden md:hidden bg-black border-b border-zinc-900">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <!-- Mobile Portfolio Collapsible/Group -->
                <div class="border-b border-zinc-900 pb-2">
                    <span class="block py-2 text-xs uppercase tracking-widest text-zinc-500 font-mono">Portfolio</span>
                    <a href="portfolio-muzyczne.html" class="mobile-link block py-2.5 pl-3 text-sm font-medium text-zinc-300 hover:text-white tracking-widest uppercase">♫ Muzyczne</a>
                    <a href="portfolio.html" class="mobile-link block py-2.5 pl-3 text-sm font-medium text-zinc-300 hover:text-white tracking-widest uppercase">🎮 Game Dev</a>
                </div>
                <a href="index.html#cennik" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Oferta</a>
                <a href="creators.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Twórcy</a>
                <a href="index.html#socials" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white border-b border-zinc-900 tracking-widest uppercase">Social Media</a>
                <a href="contact.html" class="mobile-link block py-3 text-base font-medium text-zinc-400 hover:text-white tracking-widest uppercase">Kontakt</a>
            </div>
        </div>
    </nav>"""

html_files = glob.glob("*.html")
for filename in html_files:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(r"<nav[\s\S]*?</nav>", nav_template, content, count=1)
    if new_content != content:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated nav in: {filename}")
print("All files updated successfully.")
