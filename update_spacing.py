import os
from pathlib import Path
import shutil

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
CSS_DIR = BASE_DIR / "assets" / "css"
BACKUP_DIR = BASE_DIR / "backup" / "spacing_fix_batch16"

BACKUP_DIR.mkdir(parents=True, exist_ok=True)

SPACING_CSS = """

/* ============================================================
   BATCH 16: GLOBAL SPACING & HERO ALIGNMENT FIX
   ============================================================ */

/* Prevent hero sections from hiding under the fixed header */
.hero,
.course-v2-hero,
.page-hero,
.main-hero,
main > section:first-of-type,
body > section:first-of-type {
  padding-top: 180px !important;
  padding-bottom: 80px !important;
}

/* General section breathing room (Consistency) */
.section,
.course-v2-overview,
.course-v2-curriculum,
.course-v2-outcomes,
.course-v2-methodology,
.course-v2-trust,
.course-v2-faq,
.final-cta {
  padding: 80px 0 !important;
}

/* Ensure mobile feels spacious too but proportional */
@media (max-width: 768px) {
  .hero,
  .course-v2-hero,
  .page-hero,
  .main-hero,
  main > section:first-of-type,
  body > section:first-of-type {
    padding-top: 150px !important;
    padding-bottom: 60px !important;
  }
  .section,
  .course-v2-overview,
  .course-v2-curriculum,
  .course-v2-outcomes,
  .course-v2-methodology,
  .course-v2-trust,
  .course-v2-faq,
  .final-cta {
    padding: 60px 0 !important;
  }
}
"""

def append_spacing_css(filepath):
    # Backup
    shutil.copy2(filepath, BACKUP_DIR / filepath.name)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Avoid appending multiple times
    if "BATCH 16: GLOBAL SPACING" not in content:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(SPACING_CSS)
        print(f"Appended spacing CSS to {filepath.name}")
    else:
        print(f"CSS already exists in {filepath.name}")

append_spacing_css(CSS_DIR / "style.css")
append_spacing_css(CSS_DIR / "style.min.css")
