import sys

def update_skills(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ableton Live: 2 filled, 3 empty
    old_ableton = '''<span class="skill-name">Ableton Live</span>
    <div class="dots">
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot"></span>
    </div>'''
    
    new_ableton = '''<span class="skill-name">Ableton Live</span>
    <div class="dots">
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot"></span>
      <span class="dot"></span>
      <span class="dot"></span>
    </div>'''

    # FL Studio: all filled
    old_fl = '''<span class="skill-name">FL Studio</span>
  <div class="dots vertical">
    <span class="dot filled"></span>
    <span class="dot filled"></span>
    <span class="dot filled"></span>
    <span class="dot filled"></span>
    <span class="dot"></span>
  </div>'''
  
    new_fl = '''<span class="skill-name">FL Studio</span>
  <div class="dots vertical">
    <span class="dot filled"></span>
    <span class="dot filled"></span>
    <span class="dot filled"></span>
    <span class="dot filled"></span>
    <span class="dot filled"></span>
  </div>'''

    # Aranżacja: all filled
    old_aran = '''<span class="skill-name">Aranżacja</span>
    <div class="dots">
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot"></span>
    </div>'''

    new_aran = '''<span class="skill-name">Aranżacja</span>
    <div class="dots">
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
    </div>'''

    # Mastering: 4 filled, 1 empty
    old_mast = '''<span class="skill-name">Mastering</span>
    <div class="dots">
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
    </div>'''
    
    new_mast = '''<span class="skill-name">Mastering</span>
    <div class="dots">
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot filled"></span>
      <span class="dot"></span>
    </div>'''

    content = content.replace(old_ableton, new_ableton)
    content = content.replace(old_fl, new_fl)
    content = content.replace(old_aran, new_aran)
    content = content.replace(old_mast, new_mast)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated skills in {filepath}")

update_skills(r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\portfolio-muzyczne.html')
update_skills(r'd:\Github\samplix\Tools\SamplixWebsite\noxaudios.github.io\portfolio.html')
