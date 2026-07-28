import os
import re
from html.parser import HTMLParser

HTML_DIR = r"E:\quran academy\Quran-Acadamy"
BACKUP_DIR = r"E:\quran academy\Quran-Acadamy\backup"

class BasicHTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr', '!doctype'}
        self.error = False

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.void_elements: return
        if not self.stack:
            self.error = True
            return
        if self.stack[-1] == tag:
            self.stack.pop()
        else:
            if tag in {'main', 'div', 'section', 'header', 'footer'}:
                if tag in self.stack:
                    self.error = True

def validate_html(content):
    parser = BasicHTMLValidator()
    parser.feed(content)
    return not parser.error

def get_template_parts():
    with open(os.path.join(HTML_DIR, 'about.html'), 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Head
    head_match = re.search(r'(<!DOCTYPE html>.*?</head>)', content, re.DOTALL)
    head_part = head_match.group(1) if head_match else ""
    
    # Extract Header (including body start and skip link)
    header_match = re.search(r'(<body[^>]*>.*?</header>)', content, re.DOTALL)
    header_part = header_match.group(1) if header_match else ""
    
    # Extract mobile-overlay if exists
    if '<div class="mobile-overlay"></div>' in content:
        header_part += '\n  <div class="mobile-overlay"></div>\n'

    # Extract Footer (including script and body end)
    footer_match = re.search(r'(<footer class="footer".*?</html>)', content, re.DOTALL)
    footer_part = footer_match.group(1) if footer_match else ""
    
    return head_part, header_part, footer_part

def generate_page(filename, title, content_html, head, header, footer):
    # Adjust title
    head_adj = re.sub(r'<title>.*?</title>', f'<title>{title} | Qurana Academy</title>', head)
    # Adjust canonical
    head_adj = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="https://[YOUR-PRODUCTION-DOMAIN.COM]/{filename}">', head_adj)
    # Adjust OG
    head_adj = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title} | Qurana Academy">', head_adj)
    head_adj = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="https://[YOUR-PRODUCTION-DOMAIN.COM]/{filename}">', head_adj)

    html = f"""{head_adj}
{header}
<main id="main">
  <section class="page-header" style="padding: 80px 0 40px; text-align: center; background: #f9f9f9;">
    <div class="container">
      <h1>{title}</h1>
    </div>
  </section>
  <section class="page-content" style="padding: 60px 0;">
    <div class="container">
{content_html}
    </div>
  </section>
</main>
{footer}
"""
    if validate_html(html):
        with open(os.path.join(HTML_DIR, filename), 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    return False

def generate_pages():
    head, header, footer = get_template_parts()
    
    pages = {
        "privacy-policy.html": {
            "title": "Privacy Policy",
            "content": """      <!-- TODO: Insert client-approved Privacy Policy content here -->
      <p>Last updated: [DATE]</p>
      <h2>1. Information We Collect</h2>
      <p>[PLACEHOLDER_TEXT]</p>
      <h2>2. How We Use Your Information</h2>
      <p>[PLACEHOLDER_TEXT]</p>
      <h2>3. Contact Us</h2>
      <p>If you have any questions, contact us at: <a href="mailto:info@[YOUR-PRODUCTION-DOMAIN.COM]">info@[YOUR-PRODUCTION-DOMAIN.COM]</a></p>"""
        },
        "terms-and-conditions.html": {
            "title": "Terms and Conditions",
            "content": """      <!-- TODO: Insert client-approved Terms and Conditions content here -->
      <p>Last updated: [DATE]</p>
      <h2>1. Acceptance of Terms</h2>
      <p>[PLACEHOLDER_TEXT]</p>
      <h2>2. Services Provided</h2>
      <p>[PLACEHOLDER_TEXT]</p>
      <h2>3. Payment and Refunds</h2>
      <p>[PLACEHOLDER_TEXT]</p>"""
        },
        "refund-policy.html": {
            "title": "Refund Policy",
            "content": """      <!-- TODO: Insert client-approved Refund Policy content here -->
      <p>Last updated: [DATE]</p>
      <h2>1. Eligibility for Refunds</h2>
      <p>[PLACEHOLDER_TEXT]</p>
      <h2>2. Process for Requesting a Refund</h2>
      <p>[PLACEHOLDER_TEXT]</p>"""
        },
        "thank-you.html": {
            "title": "Thank You",
            "content": """      <div style="text-align: center; max-width: 600px; margin: 0 auto;">
        <h2>Your Request Has Been Received</h2>
        <p>Thank you for contacting Qurana Academy. Our team will get back to you shortly.</p>
        <a href="index.html" class="btn btn-primary" style="margin-top: 20px; display: inline-block;">Return to Home</a>
      </div>"""
        },
        "404.html": {
            "title": "Page Not Found",
            "content": """      <div style="text-align: center; max-width: 600px; margin: 0 auto;">
        <h2>404 - Not Found</h2>
        <p>The page you are looking for does not exist or has been moved.</p>
        <a href="index.html" class="btn btn-primary" style="margin-top: 20px; display: inline-block;">Return to Home</a>
      </div>"""
        },
        "free-trial.html": {
            "title": "Start Your Free Trial",
            "content": """      <div style="max-width: 600px; margin: 0 auto;">
        <p style="text-align: center; margin-bottom: 30px;">Experience a free Quran class with our certified tutor. No commitment required.</p>
        <form action="thank-you.html" method="GET" class="trial-form">
          <!-- Form styling matches existing site logic -->
          <div class="form-group" style="margin-bottom: 20px;">
            <label for="ft-name" style="display:block; margin-bottom:8px; font-weight:600;">Full Name</label>
            <input type="text" id="ft-name" name="name" placeholder="Your Full Name" required style="width:100%; padding:12px; border:1px solid #ccc; border-radius:4px;" aria-required="true">
          </div>
          <div class="form-group" style="margin-bottom: 20px;">
            <label for="ft-email" style="display:block; margin-bottom:8px; font-weight:600;">Email Address</label>
            <input type="email" id="ft-email" name="email" placeholder="Email Address" required style="width:100%; padding:12px; border:1px solid #ccc; border-radius:4px;" aria-required="true">
          </div>
          <div class="form-group" style="margin-bottom: 20px;">
            <label for="ft-phone" style="display:block; margin-bottom:8px; font-weight:600;">WhatsApp Number</label>
            <input type="tel" id="ft-phone" name="phone" placeholder="e.g. +974..." required style="width:100%; padding:12px; border:1px solid #ccc; border-radius:4px;" aria-required="true">
          </div>
          <button type="submit" class="btn btn-primary" style="width:100%; padding:15px; font-size:16px;">Book Free Trial</button>
        </form>
      </div>"""
        }
    }
    
    for filename, data in pages.items():
        generate_page(filename, data["title"], data["content"], head, header, footer)

def update_forms():
    # Update forms in existing pages to have action="thank-you.html" and add aria-labels
    for root, dirs, files in os.walk(HTML_DIR):
        if 'backup' in root.lower(): continue
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                orig_content = content
                
                # Add action to forms
                # Only if form doesn't already have an action
                content = re.sub(r'<form((?!action)[^>]*)>', r'<form action="thank-you.html"\1>', content)
                
                # Add aria-label based on placeholder for inputs
                def add_aria_label(match):
                    full_match = match.group(0)
                    if 'aria-label=' not in full_match:
                        placeholder_match = re.search(r'placeholder="([^"]+)"', full_match)
                        if placeholder_match:
                            label_val = placeholder_match.group(1)
                            full_match = full_match.replace('<input ', f'<input aria-label="{label_val}" ')
                            full_match = full_match.replace('<textarea ', f'<textarea aria-label="{label_val}" ')
                    return full_match
                
                content = re.sub(r'<input[^>]+>', add_aria_label, content)
                content = re.sub(r'<textarea[^>]+>', add_aria_label, content)
                
                if content != orig_content:
                    if validate_html(content):
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)

if __name__ == "__main__":
    generate_pages()
    update_forms()
    print("Batch 3 complete.")
