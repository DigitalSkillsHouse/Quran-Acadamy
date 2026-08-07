import re
import json

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
    
    # Remove Skype isolated
    if 'Skype' in line and 'Zoom' not in line:
        line = line.replace('Skype', 'Google Meet')
        
    # Social Media
    if 'Facebook' in line or 'Instagram' in line or 'YouTube' in line:
        if '<a href="#" aria-label="Facebook">' in line: return ''
        if '<a href="#" aria-label="Instagram">' in line: return ''
        if '<a href="#" aria-label="YouTube">' in line: return ''
        
    # Fake info
    line = line.replace('thousands of students', 'many students')
    line = line.replace('thousands of', 'many')
    line = line.replace('Hundreds of Teachers', 'A growing team of qualified female Quran teachers')
    line = line.replace('hundreds of teachers', 'our growing team of qualified female Quran teachers')
    
    # "Our team of expert teachers" -> "Our growing team of qualified female Quran teachers."
    line = line.replace('Our team of expert teachers', 'Our growing team of qualified female Quran teachers.')
    line = line.replace('Our academy has many teachers', 'Our growing team of qualified female Quran teachers.')
    
    # "Multiple Branches" -> ""
    line = line.replace('Multiple Branches', '')
    line = line.replace('Physical Campus', '')
    line = line.replace('Large Academy', '')

    return line

new_lines = []
for i, line in enumerate(lines):
    line_num = i + 1
    # Do NOT touch Hero section (approx 143 to 212)
    if 143 <= line_num <= 211:
        new_lines.append(line)
        continue
    
    # Testimonials section replacement (around line 522-604)
    # We will manually replace the testimonials in a different pass or do it directly if we find the names.
    # Replace "Parent in Doha" with "Parent from Doha" 
    line = line.replace('Parent in Doha', 'Parent from Doha')
    # Replace "Mother in Qatar" with "Mother of Two Students"
    line = line.replace('Mother in Qatar', 'Mother of Two Students')
    
    # The prompt asked for:
    # One testimonial should be based on this verified review:
    # "My daughter previously studied Quran for almost a year without much progress. After joining Al-Tajweed ul Quran Academy, she gradually started enjoying her lessons and improving with confidence. We are grateful for the patience, encouragement, and sincere teaching."
    
    # We will look for: "The teacher's patience with my son has been incredible. His Tajweed has improved significantly, and he actually looks forward to his classes now."
    if "The teacher's patience with my son has been incredible" in line:
        line = line.replace(
            "The teacher's patience with my son has been incredible. His Tajweed has improved significantly, and he actually looks forward to his classes now.",
            "My daughter previously studied Quran for almost a year without much progress. After joining Al-Tajweed ul Quran Academy, she gradually started enjoying her lessons and improving with confidence. We are grateful for the patience, encouragement, and sincere teaching."
        )
    
    # Also "Family in Al Wakrah" to something like "Parent from Qatar"
    line = line.replace('Family in Al Wakrah', 'Parent from Qatar')
    
    line = update_line(line)
    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
