import os
import glob
import re

backup_dir = 'backup/global_sync'
files_to_restore = glob.glob(f'{backup_dir}/*.html')

for backup_file in files_to_restore:
    basename = os.path.basename(backup_file)
    # The backup files are named like 'services_noorani-qaida.html'
    if basename.startswith('services_'):
        live_file = 'services/' + basename.replace('services_', '')
    elif basename.startswith('tutors_'):
        live_file = 'tutors/' + basename.replace('tutors_', '')
    else:
        live_file = basename
        
    print(f"Restoring Header/Footer for {live_file} from {backup_file}")
    
    with open(backup_file, 'r', encoding='utf-8') as f:
        backup_content = f.read()
        
    with open(live_file, 'r', encoding='utf-8') as f:
        live_content = f.read()
        
    # 1. Extract Top Info Bar + Header from backup
    header_start_idx = backup_content.find('<!-- Top Info Bar -->')
    if header_start_idx == -1:
        header_start_idx = backup_content.find('<div class="top-info-bar">')
        
    header_end_idx = backup_content.find('</header>') + len('</header>')
    
    if header_start_idx != -1 and header_end_idx != -1:
        backup_header_block = backup_content[header_start_idx:header_end_idx]
        
        # Find same bounds in live file
        live_header_start = live_content.find('<!-- Top Info Bar -->')
        if live_header_start == -1:
            live_header_start = live_content.find('<div class="top-info-bar">')
            
        live_header_end = live_content.find('</header>') + len('</header>')
        
        if live_header_start != -1 and live_header_end != -1:
            live_content = live_content[:live_header_start] + backup_header_block + live_content[live_header_end:]
            print(f" -> Restored Header block.")
            
    # 2. Extract Footer + Modals from backup
    # Everything from <footer to the end of the file.
    footer_start_idx = backup_content.find('<footer')
    if footer_start_idx != -1:
        backup_footer_block = backup_content[footer_start_idx:]
        
        live_footer_start = live_content.find('<footer')
        if live_footer_start != -1:
            live_content = live_content[:live_footer_start] + backup_footer_block
            print(f" -> Restored Footer & Modal block.")
            
    # Write back to live file
    with open(live_file, 'w', encoding='utf-8') as f:
        f.write(live_content)

# 3. Clean up CSS
css_file = 'assets/css/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()
    
cta_css_idx = css_content.find('/* CTA Button Upgrade */')
if cta_css_idx != -1:
    css_content = css_content[:cta_css_idx]
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print(" -> Reverted CSS styling in style.css.")
    
print("Rollback completed successfully.")
