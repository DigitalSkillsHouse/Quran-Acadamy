import os
from pathlib import Path
import shutil

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
CSS_DIR = BASE_DIR / "assets" / "css"
BACKUP_DIR = BASE_DIR / "backup" / "cta_fix_batch20"

BACKUP_DIR.mkdir(parents=True, exist_ok=True)

CTA_CSS = """

/* ============================================================
   BATCH 20: CTA BUTTON PROPORTIONS FIX
   ============================================================ */

/* Restore the squished CTA button padding that was overridden by Batch 19 */
.nav-links .nav-cta,
.nav-cta {
  padding: 12px 28px !important;
  height: auto !important;
  align-self: center !important; /* Prevent stretching */
  white-space: nowrap !important; /* Keep text strictly on one line */
  font-size: 0.85rem !important;
  line-height: 1.2 !important;
  border-radius: 30px !important;
  display: inline-flex !important;
  justify-content: center !important;
  align-items: center !important;
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}
"""

def append_cta_css(filepath):
    # Backup
    shutil.copy2(filepath, BACKUP_DIR / filepath.name)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Avoid appending multiple times
    if "BATCH 20: CTA BUTTON PROPORTIONS FIX" not in content:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(CTA_CSS)
        print(f"Appended Batch 20 CSS to {filepath.name}")
    else:
        print(f"CSS already exists in {filepath.name}")

if __name__ == "__main__":
    append_cta_css(CSS_DIR / "style.css")
    append_cta_css(CSS_DIR / "style.min.css")
    print("Batch 20 CTA button fix completed.")
