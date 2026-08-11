import os
import re
import shutil
from pathlib import Path

# Paths configuration
BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
BACKUP_DIR = BASE_DIR / "backup" / "footer_sync_batch13"

# Ensure backup directory exists
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

# Files to update
TARGET_FILES = [
    "about.html",
    "contact.html",
    "pricing.html",
    "privacy-policy.html",
    "terms-and-conditions.html", # Used actual filename on disk
    "refund-policy.html",
    "faq.html",
    "tutors/female-tutors.html",
    "services/noorani-qaida.html",
    "services/quran-tafseer.html",
    "services/quran-memorization.html",
    "services/six-kalima.html"
]

INDEX_HTML_PATH = BASE_DIR / "index.html"

# Footer regex (non-greedy)
FOOTER_REGEX = re.compile(r'<footer\b[^>]*>.*?</footer>', re.DOTALL | re.IGNORECASE)

def extract_footer(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = FOOTER_REGEX.search(content)
    if not match:
        raise ValueError("Could not find footer in index.html")
    return match.group(0)

def adjust_links_for_subdirectories(footer_html):
    """
    Adjust relative paths for files nested one level deep (e.g., services/, tutors/).
    We prepend '../' to local html pages, directories like services/ and tutors/, and sitemap.xml.
    """
    # List of things to prefix with '../'
    # We must only match href="[local_path]" and not touch external links (tel:, mailto:, https:)
    
    def replace_href(match):
        href = match.group(1)
        # Skip external or anchor links
        if href.startswith('http') or href.startswith('tel:') or href.startswith('mailto:') or href.startswith('#'):
            return f'href="{href}"'
        
        # If it's a local file/path, prepend ../
        return f'href="../{href}"'

    adjusted_footer = re.sub(r'href="([^"]+)"', replace_href, footer_html)
    return adjusted_footer

def main():
    try:
        master_footer = extract_footer(INDEX_HTML_PATH)
        print("Successfully extracted master footer from index.html")
        
        # Pre-calculate adjusted footer for nested pages
        nested_footer = adjust_links_for_subdirectories(master_footer)
        
        for file_rel in TARGET_FILES:
            target_path = BASE_DIR / file_rel
            
            if not target_path.exists():
                print(f"Skipping {file_rel} - File not found")
                continue
                
            # Create backup
            # using relative parts to maintain uniqueness if names collide, but they don't here.
            # safe naming for backup
            backup_file_name = file_rel.replace('/', '_').replace('\\', '_')
            backup_file_path = BACKUP_DIR / backup_file_name
            shutil.copy2(target_path, backup_file_path)
            
            # Read content
            with open(target_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine which footer to use based on nesting
            is_nested = "/" in file_rel or "\\" in file_rel
            footer_to_use = nested_footer if is_nested else master_footer
            
            # Replace footer
            # Ensure there is a footer to replace
            if not FOOTER_REGEX.search(content):
                print(f"Warning: No footer found in {file_rel}, appending it before </main> or </body>")
                print(f"Skipping {file_rel} due to missing footer tag.")
                continue
            
            new_content = FOOTER_REGEX.sub(footer_to_use, content)
            
            # Write back
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"Successfully synced footer in {file_rel}")
            
        print("\nBatch 13 Footer Sync completed successfully.")
        
    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    main()
