import os
from pathlib import Path
import shutil

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
CSS_DIR = BASE_DIR / "assets" / "css"

def wrap_arrows():
    count = 0
    for filepath in BASE_DIR.rglob("*.html"):
        if "backup" in filepath.parts or ".history" in filepath.parts or ".antigravity" in filepath.parts:
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '<span class="nav-arrow">' in content:
            continue
            
        new_content = content.replace('Services ▾', 'Services <span class="nav-arrow">▾</span>')
        new_content = new_content.replace('Tutors ▾', 'Tutors <span class="nav-arrow">▾</span>')
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Wrapped dropdown arrows in {filepath.name}")
            
    print(f"Wrapped arrows in {count} HTML files.")

ARROW_CSS = """
/* ============================================================
   BATCH 22: NAV DROPDOWN ARROW WRAPPER FIX
   ============================================================ */

/* Explicitly wrap the dropdown arrow in a flex container so it NEVER breaks baseline */
.nav-arrow {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin-left: 4px !important;
  line-height: 1 !important;
  vertical-align: middle !important;
}

/* Ensure the parent anchor stays a clean flex row */
.nav-links > .has-dropdown > a {
  display: flex !important;
  align-items: center !important;
  white-space: nowrap !important; /* Prevent text wrapping */
}
"""

def append_arrow_css(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "BATCH 22: NAV DROPDOWN ARROW WRAPPER FIX" not in content:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write("\n" + ARROW_CSS)
        print(f"Appended Batch 22 CSS to {filepath.name}")

if __name__ == "__main__":
    wrap_arrows()
    append_arrow_css(CSS_DIR / "style.css")
    append_arrow_css(CSS_DIR / "style.min.css")
