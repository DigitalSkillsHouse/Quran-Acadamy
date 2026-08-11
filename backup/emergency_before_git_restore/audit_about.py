import re

file_path = 'about.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Split file at header and footer safely
header_match = re.search(r'</header>', text)
footer_match = re.search(r'<footer[^>]*>', text)

if not header_match or not footer_match:
    print("Error: header or footer not found!")
    exit(1)

header_end = header_match.end()
footer_start = footer_match.start()

head_and_header = text[:header_end]
main_content = text[header_end:footer_start]
bottom_content = text[footer_start:] # Contains footer and modal

# SEO & Meta (Head)
head_and_header = head_and_header.replace('a Free Trial', 'up to 3 trial classes')
head_and_header = head_and_header.replace('5,000+ students across Qatar', 'families across Qatar')
head_and_header = head_and_header.replace('premium', 'trusted')

# Fix main_content
# EEAT / Factual wording
main_content = main_content.replace('premium online Quran academy', 'trusted online Quran academy')
main_content = main_content.replace('Premium Hero', 'Trusted Hero')
main_content = main_content.replace('premium educational platform', 'trusted educational platform')

# CTAs
main_content = main_content.replace('Book Free Trial', 'Book Up to 3 Trial Classes')
main_content = main_content.replace('WhatsApp Us', 'Talk on WhatsApp')
main_content = main_content.replace('Start Your Online Quran Journey', 'Begin Your Quran Journey')

# Founder Section
# Remove unverified: "Taught students internationally" and "Specialist in Online Quran classes"
main_content = re.sub(r'<li><svg[^>]*><polyline[^>]*></polyline></svg>\s*Taught students internationally</li>\n?', '', main_content)
main_content = re.sub(r'<li><svg[^>]*><polyline[^>]*></polyline></svg>\s*Specialist in Online Quran classes</li>\n?', '', main_content)
# Add "Growing team of 3 female teachers" to list
main_content = main_content.replace('<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg> Fluent in Urdu & English</li>',
                                    '<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg> Fluent in Urdu & English</li>\n            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg> Growing team of 3 female teachers</li>')

# Founder Story (Add paragraph)
founder_story = """
          <p class="founder-story">With a deep passion for teaching the Holy Quran, Shagufta Rehan founded Al-Tajweed ul Quran Academy to help students learn with proper Tajweed and sincere understanding. Drawing on her education from Madinah and experience with Al-Huda, she leads a growing team of 3 female teachers dedicated to guiding families in Qatar through consistent, patient, and personalized online education.</p>
"""
main_content = main_content.replace('<ul class="founder-specs">', founder_story + '          <ul class="founder-specs">')

# Mission & Vision
new_mission = "<p>To provide authentic online Quran education through qualified female teachers, ensuring a safe and patient learning environment rooted in Islamic values.</p>"
new_vision = "<p>To foster a lifelong connection to the Holy Quran for Muslim families in Qatar through consistent and sincere educational support.</p>"

main_content = re.sub(r'<h2>Our Mission</h2>\s*<p>.*?</p>', f'<h2>Our Mission</h2>\n          {new_mission}', main_content, flags=re.DOTALL)
main_content = re.sub(r'<h2>Our Vision</h2>\s*<p>.*?</p>', f'<h2>Our Vision</h2>\n          {new_vision}', main_content, flags=re.DOTALL)

# Trust Cards
main_content = main_content.replace('Qualified Female Tutors', 'Female Quran Tutors')
main_content = main_content.replace('Flexible Schedule', 'Flexible Scheduling')
main_content = main_content.replace('Progress Tracking', 'Student Progress')

# Methodology
main_content = main_content.replace('<h3>Live Classes</h3>\n           <p>Interactive 1-on-1 online sessions.</p>', '<h3>Regular Classes</h3>\n           <p>Interactive 1-on-1 online sessions.</p>')

# Bottom content (Modal + Footer)
# DO NOT touch footer content. The footer in about.html ends at </footer>. Let's isolate the modal.
footer_end = bottom_content.find('</footer>') + 9
footer_part = bottom_content[:footer_end]
modal_part = bottom_content[footer_end:]

# Modifying Modal only
modal_part = modal_part.replace('Book Free Trial', 'Book Up to 3 Trial Classes')
modal_part = modal_part.replace('Start Your Free Trial', 'Start Your Up to 3 Trial Classes')
modal_part = modal_part.replace('Experience a free Quran class', 'Experience up to 3 Quran trial classes')

# Ensure we don't end up with duplicate class attributes like class="btn btn-primary" class="..."
modal_part = modal_part.replace('style="width:100%;justify-content:center"', 'class="modal-submit-btn"')

bottom_content = footer_part + modal_part

# Accessibility and Performance (Inline CSS removal)
css_to_add = """
  <style>
    .skip-link { position:absolute;left:-9999px;z-index:999;padding:1em;background-color:white;color:black;opacity:0; }
    .skip-link:focus { left:50%; opacity:1; }
    .founder-story { margin-top: 16px; margin-bottom: 24px; font-size: 1.1rem; line-height: 1.6; color: var(--text-dark); }
    .modal-submit-btn { width: 100%; justify-content: center; }
  </style>
</head>
"""

head_and_header = head_and_header.replace('</head>', css_to_add)
head_and_header = head_and_header.replace('style="position:absolute;left:-9999px;z-index:999;padding:1em;background-color:white;color:black;opacity:0;" onfocus="this.style.left=\'50%\';this.style.opacity=\'1\'" onblur="this.style.left=\'-9999px\';this.style.opacity=\'0\'"', '')

final_text = head_and_header + main_content + bottom_content

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_text)
