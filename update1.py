import re

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

def update_line(line):
    # Free trial variants
    line = line.replace('Free Trial', 'Up to 3 Trial Classes')
    line = line.replace('free trial', 'up to 3 trial classes')
    line = line.replace('Free trial', 'Up to 3 trial classes')
    
    # Platforms
    line = line.replace('Zoom or Skype', 'Zoom or Google Meet')
    line = line.replace('via Zoom or Skype', 'via Zoom or Google Meet')
    
    # Social Media
    if 'Facebook' in line or 'Instagram' in line or 'YouTube' in line:
        # if it's an SVG icon link in footer, we can remove the whole link
        if '<a href="#" aria-label="Facebook">' in line:
            return ''
        if '<a href="#" aria-label="Instagram">' in line:
            return ''
        if '<a href="#" aria-label="YouTube">' in line:
            return ''
        
    return line

new_lines = []
for i, line in enumerate(lines):
    line_num = i + 1
    # Do NOT touch Hero section (approx 143 to 212)
    # The hero section is contained in <section class="hero-v2" id="hero"> to </section>
    # Let's say lines 143 to 211
    if 143 <= line_num <= 211:
        new_lines.append(line)
        continue
    
    line = update_line(line)
    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
