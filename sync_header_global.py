import os
import re
import shutil
from pathlib import Path

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
BACKUP_DIR = BASE_DIR / "backup" / "header_sync_batch21"
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

TARGET_FILES = [
    "about.html",
    "contact.html",
    "pricing.html",
    "privacy-policy.html",
    "terms-and-conditions.html",
    "refund-policy.html",
    "faq.html",
    "tutors/female-tutors.html",
    "services/noorani-qaida.html",
    "services/quran-tafseer.html",
    "services/quran-memorization.html",
    "services/six-kalima.html",
    "free-trial.html",
    "reviews.html",
    "thank-you.html",
    "404.html"
]

INDEX_HTML_PATH = BASE_DIR / "index.html"
HEADER_REGEX = re.compile(r'<header\b[^>]*>.*?</header>', re.DOTALL | re.IGNORECASE)

def extract_header():
    with open(INDEX_HTML_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    match = HEADER_REGEX.search(content)
    if not match:
        raise ValueError("Could not find master header in index.html")
    return match.group(0)

def adjust_links(header_html, is_nested):
    if not is_nested:
        return header_html

    def replace_src(match):
        src = match.group(1)
        if src.startswith('http') or src.startswith('data:'):
            return f'src="{src}"'
        return f'src="../{src}"'

    def replace_href(match):
        href = match.group(1)
        if href.startswith('http') or href.startswith('tel:') or href.startswith('mailto:') or href.startswith('#'):
            return f'href="{href}"'
        return f'href="../{href}"'

    html = re.sub(r'src="([^"]+)"', replace_src, header_html)
    html = re.sub(r'href="([^"]+)"', replace_href, html)
    return html

def main():
    master_header = extract_header()
    
    count = 0
    for file_rel in TARGET_FILES:
        target_path = BASE_DIR / file_rel
        if not target_path.exists():
            continue
            
        shutil.copy2(target_path, BACKUP_DIR / file_rel.replace('/', '_').replace('\\', '_'))
        
        with open(target_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        is_nested = "/" in file_rel or "\\" in file_rel
        header_to_use = adjust_links(master_header, is_nested)
        
        # Strip active class from master
        header_to_use = header_to_use.replace(' class="active"', '')
        header_to_use = header_to_use.replace('class="active"', '')
        
        # Add active class back conditionally
        if "about.html" in file_rel:
            header_to_use = re.sub(r'(href="[^"]*about\.html")', r'\1 class="active"', header_to_use)
        elif "contact.html" in file_rel:
            header_to_use = re.sub(r'(href="[^"]*contact\.html")', r'\1 class="active"', header_to_use)
        elif "pricing.html" in file_rel:
            header_to_use = re.sub(r'(href="[^"]*pricing\.html")', r'\1 class="active"', header_to_use)
        elif "faq.html" in file_rel:
            header_to_use = re.sub(r'(href="[^"]*faq\.html")', r'\1 class="active"', header_to_use)
        elif "tutors" in file_rel:
            header_to_use = header_to_use.replace('href="#">Tutors', 'href="#" class="active">Tutors')
        elif "services" in file_rel:
            header_to_use = header_to_use.replace('href="#">Services', 'href="#" class="active">Services')
            
        if not HEADER_REGEX.search(content):
            print(f"Skipping {file_rel} - no header tag found")
            continue
            
        new_content = HEADER_REGEX.sub(header_to_use, content)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Synced header in {file_rel}")
            
    print(f"Header sync complete. Updated {count} files.")

if __name__ == "__main__":
    main()
