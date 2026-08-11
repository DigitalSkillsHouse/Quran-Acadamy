import os
from pathlib import Path
import re

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")

def analyze_headers():
    files_with_issues = []
    
    # 1. Read master header from index.html (or just assume we want them all to match)
    with open(BASE_DIR / 'index.html', 'r', encoding='utf-8') as f:
        master_content = f.read()
        
    master_header_match = re.search(r'(<div class="top-info-bar".*?</header>)', master_content, re.DOTALL)
    if not master_header_match:
        print("Could not find master header in index.html")
        return
        
    master_header = master_header_match.group(1)
    
    # Check for missing stylesheets or inline overrides
    for filepath in BASE_DIR.rglob("*.html"):
        if "backup" in filepath.parts or ".history" in filepath.parts or ".antigravity" in filepath.parts:
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        issues = []
        
        # Check stylesheet links
        if "style.min.css" not in content and "style.css" not in content:
            issues.append("Missing global stylesheet (style.css/style.min.css)")
            
        # Check inline styles targeting nav or header
        if re.search(r'<style[^>]*>.*?(?:\.nav-links|\.header|\.nav-cta|\.hero).*?</style>', content, re.DOTALL):
            issues.append("Contains local <style> block potentially overriding global layout")
            
        # Check if header matches (rough check: does it have Book Up to 3 Trial Classes?)
        if "Book Up to 3 Trial Classes" not in content:
            issues.append("Outdated CTA text in file")
            
        # Check for inline styles on the header or nav-cta
        if 'class="nav-cta" style=' in content or "style=" in re.findall(r'<header[^>]*>', content):
            issues.append("Inline style attribute on header or CTA")
            
        if issues:
            files_with_issues.append((filepath.name, issues))
            
    if files_with_issues:
        print("Found issues in the following files:")
        for name, issues in files_with_issues:
            print(f"- {name}: {', '.join(issues)}")
    else:
        print("All HTML files look clean regarding header, stylesheets, and CTA text!")

if __name__ == "__main__":
    analyze_headers()
