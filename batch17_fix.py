import os
import re
from pathlib import Path
import shutil

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
BACKUP_DIR = BASE_DIR / "backup" / "header_fix_batch17"

def fix_html_files():
    # Regex to find Book Free Trial inside elements with nav-cta
    # It looks for `nav-cta" ` followed by anything up to `>` then `Book Free Trial</a>`
    regex_cta = re.compile(r'(nav-cta"[^>]*>)Book Free Trial(</a>)', re.IGNORECASE)
    
    count = 0
    for filepath in BASE_DIR.rglob("*.html"):
        if "backup" in filepath.parts or ".history" in filepath.parts or ".antigravity" in filepath.parts:
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = regex_cta.sub(r'\1Book Up to 3 Trial Classes\2', content)
        
        if new_content != content:
            # Backup
            backup_name = str(filepath.relative_to(BASE_DIR)).replace("\\", "_").replace("/", "_")
            shutil.copy2(filepath, BACKUP_DIR / backup_name)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Updated CTA text in {filepath.name}")
            
    print(f"Updated {count} HTML files.")

if __name__ == "__main__":
    fix_html_files()
    print("HTML CTA text replacement completed.")
