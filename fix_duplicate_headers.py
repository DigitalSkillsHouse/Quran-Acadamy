import re
from pathlib import Path

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")

def fix_duplicate_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all header blocks
    headers = list(re.finditer(r'<header\b[^>]*>.*?</header>', content, re.DOTALL | re.IGNORECASE))
    
    if len(headers) > 1:
        print(f"Found {len(headers)} headers in {filepath.name}. Removing duplicates...")
        # Keep the first one, remove the second (and any others)
        # Iterate backwards to safely remove from string
        new_content = content
        for i in range(len(headers)-1, 0, -1):
            match = headers[i]
            new_content = new_content[:match.start()] + new_content[match.end():]
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully cleaned {filepath.name}")
    else:
        print(f"{filepath.name} only has {len(headers)} header(s). No fix needed.")

if __name__ == "__main__":
    fix_duplicate_header(BASE_DIR / "terms-and-conditions.html")
    fix_duplicate_header(BASE_DIR / "refund-policy.html")
