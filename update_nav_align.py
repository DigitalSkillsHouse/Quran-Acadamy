import os
from pathlib import Path
import shutil

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
CSS_DIR = BASE_DIR / "assets" / "css"
BACKUP_DIR = BASE_DIR / "backup" / "nav_align_batch18"

BACKUP_DIR.mkdir(parents=True, exist_ok=True)

NAV_CSS = """

/* ============================================================
   BATCH 18: NAV VERTICAL ALIGNMENT FIX
   ============================================================ */

/* 1. Flexbox Centering for the Navigation Wrapper */
.nav-links {
  display: flex !important;
  align-items: center !important;
  margin: 0 !important;
}

/* 2. Normalize children elements & remove conflicting margins */
.nav-links > a:not(.nav-cta),
.nav-links > .has-dropdown,
.nav-links > .has-dropdown > a {
  display: inline-flex !important;
  align-items: center !important;
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}

/* 3. Dropdown Icon & Text Alignment */
/* Making the anchor tags inline-flex vertically centers all text and symbols (like ▾) inside them automatically */
.nav-links a:not(.nav-cta) {
  line-height: 1.2 !important;
  vertical-align: middle !important;
}

/* 4. Ensure CTA button isn't misaligned by stray margins */
.nav-cta {
  margin-top: 0 !important;
  margin-bottom: 0 !important;
  vertical-align: middle !important;
}
"""

def append_nav_css(filepath):
    # Backup
    shutil.copy2(filepath, BACKUP_DIR / filepath.name)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Avoid appending multiple times
    if "BATCH 18: NAV VERTICAL ALIGNMENT" not in content:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(NAV_CSS)
        print(f"Appended nav alignment CSS to {filepath.name}")
    else:
        print(f"CSS already exists in {filepath.name}")

if __name__ == "__main__":
    append_nav_css(CSS_DIR / "style.css")
    append_nav_css(CSS_DIR / "style.min.css")
    print("Batch 18 nav alignment fix completed.")
