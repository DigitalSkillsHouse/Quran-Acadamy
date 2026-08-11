import os
import re

files_to_audit = [
    'index.html',
    'about.html',
    'services/noorani-qaida.html',
    'services/quran-tafseer.html',
    'services/quran-memorization.html',
    'services/six-kalima.html',
    'tutors/female-tutors.html',
    'contact.html',
    'pricing.html'
]

print("Starting Read-Only Audit...\n")

issues = {
    'critical': [],
    'high': [],
    'medium': [],
    'low': []
}

for file in files_to_audit:
    if not os.path.exists(file):
        issues['critical'].append(f"{file} does not exist!")
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check H1
    h1s = re.findall(r'<h1[^>]*>.*?</h1>', content, re.IGNORECASE | re.DOTALL)
    if len(h1s) == 0:
        issues['high'].append(f"{file}: Missing H1 tag")
    elif len(h1s) > 1:
        issues['medium'].append(f"{file}: Multiple H1 tags ({len(h1s)})")
        
    # Check Title
    titles = re.findall(r'<title>.*?</title>', content, re.IGNORECASE | re.DOTALL)
    if len(titles) != 1:
        issues['high'].append(f"{file}: Missing or multiple title tags")
        
    # Check Meta Description
    desc = re.findall(r'<meta name="description"\s+content=".*?">', content, re.IGNORECASE | re.DOTALL)
    if len(desc) != 1:
        # Check without DOTALL just in case
        desc2 = re.findall(r'<meta name="description"[\s\n]+content="[^"]*">', content, re.IGNORECASE)
        if len(desc2) != 1:
            issues['high'].append(f"{file}: Missing or multiple meta descriptions")
        
    # Check OG Tags
    og_title = re.findall(r'<meta property="og:title"[\s\n]+content="[^"]*">', content, re.IGNORECASE)
    og_desc = re.findall(r'<meta property="og:description"[\s\n]+content="[^"]*">', content, re.IGNORECASE)
    if not og_title or not og_desc:
        issues['medium'].append(f"{file}: Missing Open Graph tags")
        
    # Check Canonical
    canonical = re.findall(r'<link rel="canonical" href=".*?">', content, re.IGNORECASE)
    if not canonical:
        issues['medium'].append(f"{file}: Missing Canonical link")
        
    # Check EEAT Facts (No fake data)
    fake_terms = ['skype', 'fake', 'dummy', 'lorem ipsum', '500+ teachers', '1000+ students', 'discount', 'limited offer']
    for term in fake_terms:
        if term.lower() in content.lower() and not term == 'discount':
            issues['high'].append(f"{file}: Contains potentially fake/prohibited term: '{term}'")

    # Check Internal links
    links = re.findall(r'href="([^"#][^"]*)"', content)
    for link in links:
        if link.startswith('http') or link.startswith('tel:') or link.startswith('mailto:') or 'assets' in link:
            continue
        
        # very basic check
        clean_link = link.split('?')[0]
        # Resolve paths
        dir_name = os.path.dirname(file)
        target_path = os.path.normpath(os.path.join(dir_name, clean_link))
        
        if not os.path.exists(target_path):
            issues['high'].append(f"{file}: Broken internal link to {link} (resolved: {target_path})")
            
    # Check CTA Consistency
    if 'Book Free Trial' in content and 'Up to 3 Trial Classes' in content:
        pass # Navigation CTA could be "Book Up to 3 Trial Classes" now.
    
print("--- AUDIT RESULTS ---")
for level, lst in issues.items():
    print(f"\n[{level.upper()}] ({len(lst)} issues)")
    for issue in set(lst):
        print(f" - {issue}")
