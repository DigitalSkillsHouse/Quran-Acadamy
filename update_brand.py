import os
import re
import shutil
from pathlib import Path

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
ASSETS_DIR = BASE_DIR / "assets" / "images"
BACKUP_DIR = BASE_DIR / "backup" / "brand_identity_batch14"

ASSETS_DIR.mkdir(parents=True, exist_ok=True)
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

# 1. GENERATE SVGS
LOGO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 70" width="350" height="70">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@700&amp;family=Inter:wght@500;700&amp;display=swap');
      .arabic { font-family: 'Amiri', serif; font-size: 32px; fill: #0A3A2A; font-weight: 700; }
      .english-main { font-family: 'Inter', sans-serif; font-size: 15px; fill: #0A3A2A; font-weight: 700; letter-spacing: 1.5px; }
      .english-sub { font-family: 'Inter', sans-serif; font-size: 8px; fill: #D4AF37; font-weight: 500; letter-spacing: 3.5px; }
    </style>
  </defs>
  
  <g transform="translate(5, 5)">
    <!-- Arch -->
    <path d="M 25,0 C 25,0 0,15 0,38 L 0,60 L 50,60 L 50,38 C 50,15 25,0 25,0 Z" fill="none" stroke="#D4AF37" stroke-width="2.5"/>
    <!-- Inner Diamond -->
    <path d="M 25,18 L 32,28 L 25,38 L 18,28 Z" fill="#0A3A2A" />
    <circle cx="25" cy="28" r="2" fill="#D4AF37" />
  </g>
  
  <text x="65" y="32" class="english-main">AL-TAJWEED</text>
  <text x="200" y="36" class="arabic">التجويد</text>
  <text x="65" y="52" class="english-sub">UL QURAN ACADEMY</text>
</svg>"""

LOGO_WHITE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 70" width="350" height="70">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@700&amp;family=Inter:wght@500;700&amp;display=swap');
      .arabic { font-family: 'Amiri', serif; font-size: 32px; fill: #FFFFFF; font-weight: 700; }
      .english-main { font-family: 'Inter', sans-serif; font-size: 15px; fill: #FFFFFF; font-weight: 700; letter-spacing: 1.5px; }
      .english-sub { font-family: 'Inter', sans-serif; font-size: 8px; fill: #D4AF37; font-weight: 500; letter-spacing: 3.5px; }
    </style>
  </defs>
  
  <g transform="translate(5, 5)">
    <!-- Arch -->
    <path d="M 25,0 C 25,0 0,15 0,38 L 0,60 L 50,60 L 50,38 C 50,15 25,0 25,0 Z" fill="none" stroke="#D4AF37" stroke-width="2.5"/>
    <!-- Inner Diamond -->
    <path d="M 25,18 L 32,28 L 25,38 L 18,28 Z" fill="#FFFFFF" />
    <circle cx="25" cy="28" r="2" fill="#D4AF37" />
  </g>
  
  <text x="65" y="32" class="english-main">AL-TAJWEED</text>
  <text x="200" y="36" class="arabic">التجويد</text>
  <text x="65" y="52" class="english-sub">UL QURAN ACADEMY</text>
</svg>"""

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 60" width="60" height="60">
  <g transform="translate(5, 2.5)">
    <path d="M 25,0 C 25,0 0,15 0,38 L 0,55 L 50,55 L 50,38 C 50,15 25,0 25,0 Z" fill="#0A3A2A" stroke="#D4AF37" stroke-width="3"/>
    <path d="M 25,18 L 34,30 L 25,42 L 16,30 Z" fill="#D4AF37" />
  </g>
</svg>"""

with open(ASSETS_DIR / "logo.svg", "w", encoding="utf-8") as f: f.write(LOGO_SVG)
with open(ASSETS_DIR / "logo-white.svg", "w", encoding="utf-8") as f: f.write(LOGO_WHITE_SVG)
with open(ASSETS_DIR / "favicon.svg", "w", encoding="utf-8") as f: f.write(FAVICON_SVG)

print("Generated SVGs successfully.")

# 2. FILE PROCESSING
def process_html_file(filepath):
    rel_path = filepath.relative_to(BASE_DIR)
    
    # Calculate prefix for assets
    parts = list(rel_path.parts)
    if len(parts) > 1:
        prefix = "../" * (len(parts) - 1)
    else:
        prefix = ""
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 2a. Replace Header Logo
    header_logo_regex = re.compile(r'<a href="[^"]*index\.html"[^>]*class="logo"[^>]*>.*?</a>', re.DOTALL | re.IGNORECASE)
    
    new_header_logo = f"""<a href="{prefix}index.html" class="logo" aria-label="Al-Tajweed ul Quran Academy Home">
      <img src="{prefix}assets/images/logo.svg" alt="Al-Tajweed ul Quran Academy" width="280" height="56" style="height: 56px; width: auto; max-width: 100%; object-fit: contain;">
    </a>"""
    
    content = header_logo_regex.sub(new_header_logo, content)

    # 2b. Replace Footer Logo text
    footer_logo_regex = re.compile(r'<h4>Al-Tajweed ul Quran Academy</h4>', re.IGNORECASE)
    
    new_footer_logo = f"""<a href="{prefix}index.html" aria-label="Home" class="footer-logo">
            <img src="{prefix}assets/images/logo-white.svg" alt="Al-Tajweed ul Quran Academy" width="240" height="48" style="height: 48px; width: auto; max-width: 100%; margin-bottom: 16px;">
          </a>"""
    
    content = footer_logo_regex.sub(new_footer_logo, content)

    # 2c. Favicon insertion
    favicon_tag = f'<link rel="icon" type="image/svg+xml" href="{prefix}assets/images/favicon.svg">'
    content = re.sub(r'<link[^>]*rel="icon"[^>]*>\s*', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<link[^>]*rel="shortcut icon"[^>]*>\s*', '', content, flags=re.IGNORECASE)
    
    content = re.sub(r'</head>', f'  {favicon_tag}\n</head>', content, flags=re.IGNORECASE)
    
    # Backup and Save if changed
    if content != original_content:
        backup_name = str(rel_path).replace("\\", "_").replace("/", "_")
        shutil.copy2(filepath, BACKUP_DIR / backup_name)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {rel_path}")

# Run for all HTML files
for html_file in BASE_DIR.rglob("*.html"):
    if "backup" in html_file.parts or ".history" in html_file.parts or ".antigravity" in html_file.parts:
        continue
    process_html_file(html_file)

print("Brand identity update complete.")
