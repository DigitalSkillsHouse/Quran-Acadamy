import os
import re
import json
import shutil
from html.parser import HTMLParser

HTML_DIR = r"E:\quran academy\Quran-Acadamy"
BACKUP_DIR = r"E:\quran academy\Quran-Acadamy\backup"

class BasicHTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr', '!doctype'}
        self.error = False
        self.error_msg = ""

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        # Allow some flexibility for unclosed p or li in older html, but main, div, section etc should match
        if not self.stack:
            self.error = True
            self.error_msg = f"Unexpected end tag <{tag}>"
            return
        
        # Check if the closing tag matches the last opened tag
        if self.stack[-1] == tag:
            self.stack.pop()
        else:
            # Simple recovery/check for mismatched div/main/header
            if tag in {'main', 'div', 'section', 'header', 'footer'}:
                if tag in self.stack:
                    self.error = True
                    self.error_msg = f"Mismatched end tag <{tag}>, expected <{self.stack[-1]}>"

def validate_html(content):
    parser = BasicHTMLValidator()
    parser.feed(content)
    return not parser.error, parser.error_msg

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.strip():
        return False, "Empty file"

    orig_content = content
    rel_path = os.path.relpath(filepath, HTML_DIR).replace('\\', '/')
    filename = os.path.basename(filepath)
    
    # 1. Skip to main content
    if 'class="skip-link"' not in content:
        skip_link = '\n<a href="#main" class="skip-link" style="position:absolute;left:-9999px;z-index:999;padding:1em;background-color:white;color:black;opacity:0;" onfocus="this.style.left=\'50%\';this.style.opacity=\'1\'" onblur="this.style.left=\'-9999px\';this.style.opacity=\'0\'">Skip to main content</a>\n'
        content = re.sub(r'(<body[^>]*>)', r'\1' + skip_link, content, count=1)

    # 2. Main landmark
    if '<main id="main">' not in content:
        header_end = content.find('</header>')
        if header_end != -1:
            overlay_end = content.find('<div class="mobile-overlay"></div>', header_end)
            insert_pos = overlay_end + len('<div class="mobile-overlay"></div>') if overlay_end != -1 else header_end + len('</header>')
            content = content[:insert_pos] + '\n<main id="main">\n' + content[insert_pos:]
        
        footer_start = content.find('<footer')
        if footer_start != -1:
            content = content[:footer_start] + '\n</main>\n' + content[footer_start:]

    # 3. Canonical and Meta tags
    head_end = content.find('</head>')
    if head_end != -1:
        injections = ""
        domain = "https://[YOUR-PRODUCTION-DOMAIN.COM]"
        url = f"{domain}/{rel_path}" if rel_path != "index.html" else f"{domain}/"
        
        if '<link rel="canonical"' not in content:
            injections += f'\n  <link rel="canonical" href="{url}">\n'
        if '<meta property="og:title"' not in content:
            injections += f'  <meta property="og:title" content="Qurana Academy - {filename}">\n'
            injections += f'  <meta property="og:type" content="website">\n'
            injections += f'  <meta property="og:url" content="{url}">\n'
        if '<meta name="twitter:card"' not in content:
            injections += f'  <meta name="twitter:card" content="summary_large_image">\n'
        
        if '"@type": "EducationalOrganization"' not in content:
            org_schema = {
                "@context": "https://schema.org",
                "@type": "EducationalOrganization",
                "name": "Qurana Academy",
                "url": domain,
                "logo": f"{domain}/assets/images/logo.png"
            }
            injections += f"  <!-- Schema -->\n  <script type=\"application/ld+json\">\n  {json.dumps(org_schema)}\n  </script>\n"

        content = content[:head_end] + injections + content[head_end:]

    # 4. Image lazy loading
    img_tags = list(re.finditer(r'<img[^>]+>', content))
    for i, match in enumerate(img_tags):
        img_str = match.group(0)
        if i == 0: continue
        if 'loading=' not in img_str:
            new_img = img_str.replace('<img ', '<img loading="lazy" ')
            content = content.replace(img_str, new_img)

    if content != orig_content:
        # Validate
        is_valid, err = validate_html(content)
        if not is_valid:
            # Restore from backup logic: we don't save the bad content
            return False, f"Validation failed: {err}. File restored/unmodified."
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Successfully modified and validated."
    
    return False, "No modifications needed."

def main():
    report = {}
    for root, dirs, files in os.walk(HTML_DIR):
        if 'backup' in root.lower(): continue
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, HTML_DIR)
                changed, msg = process_file(filepath)
                report[rel_path] = {"changed": changed, "message": msg}
    
    with open(os.path.join(HTML_DIR, 'batch2_report.json'), 'w') as f:
        json.dump(report, f, indent=2)
    print("Batch 2 processing complete. Report saved.")

if __name__ == "__main__":
    main()
