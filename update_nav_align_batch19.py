import os
from pathlib import Path
import shutil

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
CSS_DIR = BASE_DIR / "assets" / "css"
BACKUP_DIR = BASE_DIR / "backup" / "nav_align_batch19"

BACKUP_DIR.mkdir(parents=True, exist_ok=True)

NAV_CSS = """

/* ============================================================
   BATCH 19: DEFINITIVE NAV VERTICAL ALIGNMENT FIX
   ============================================================ */

/* 1. Flex Container & Baseline Fix */
.nav-links {
  display: flex !important;
  align-items: center !important;
  margin: 0 !important;
  padding: 0 !important;
}

/* 2. Structure Normalization */
.nav-links > a,
.nav-links > .has-dropdown {
  display: flex !important;
  align-items: center !important;
  margin: 0 !important;
  padding: 0 !important;
  height: auto !important;
}

/* 3. Normalize Line-Height & Padding on Anchors */
.nav-links > a:not(.nav-cta),
.nav-links > .has-dropdown > a {
  display: flex !important;
  align-items: center !important;
  line-height: 1.5 !important;
  margin: 0 !important;
  padding: 8px 12px !important; /* Uniform padding */
  box-sizing: border-box !important;
}

/* 4. Dropdown Arrow Alignment */
/* By using display: flex on the anchor, text and the dropdown arrow are perfectly centered vertically on the same axis */
.nav-links > .has-dropdown > a {
  justify-content: center !important;
  gap: 4px !important;
}

/* Ensure the CTA stays perfectly centered */
.nav-links .nav-cta {
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}
"""

def append_nav_css(filepath):
    # Backup
    shutil.copy2(filepath, BACKUP_DIR / filepath.name)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Avoid appending multiple times
    if "BATCH 19: DEFINITIVE NAV VERTICAL ALIGNMENT FIX" not in content:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(NAV_CSS)
        print(f"Appended Batch 19 CSS to {filepath.name}")
    else:
        print(f"CSS already exists in {filepath.name}")

if __name__ == "__main__":
    append_nav_css(CSS_DIR / "style.css")
    append_nav_css(CSS_DIR / "style.min.css")
    print("Batch 19 nav alignment fix completed.")
