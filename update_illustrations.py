import re

def update_about():
    filepath = 'about.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # SVG to replace in about.html
    svg_pattern = r'<div class="founder-illustration fade-in">.*?</div>'
    new_img_div = """<div class="founder-illustration fade-in" style="display:flex; justify-content:center; align-items:center;">
          <img
            src="assets/images/female-quran-teacher-hijab-hero.webp"
            alt="Founder and Female Quran Teacher Shagufta Rehan"
            class="about-founder-image"
            loading="lazy"
            decoding="async"
            width="520"
            height="650"
          />
        </div>"""
    content = re.sub(svg_pattern, new_img_div, content, flags=re.DOTALL)

    css_block = """
  <style>
    .about-founder-image {
      display: block;
      width: 100%;
      max-width: 460px;
      height: auto;
      object-fit: contain;
      margin-inline: auto;
    }
    @media (max-width: 768px) {
      .about-founder-image {
        max-width: 300px;
        margin: 0 auto 2rem;
      }
    }
  </style>
"""
    if '.about-founder-image' not in content:
        content = content.replace('</head>', css_block + '</head>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def update_tutors():
    filepath = 'tutors/female-tutors.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Hero SVG replace
    hero_svg_pattern = r'<!-- Elegant Faceless SVG Illustration -->.*?</svg>'
    hero_img = """<img
          src="../assets/images/female-quran-teacher-hijab-hero.webp"
          alt="Female Quran Teacher conducting one-to-one online Quran class"
          class="tutors-hero-image"
          loading="eager"
          decoding="async"
          width="520"
          height="650"
        />"""
    content = re.sub(hero_svg_pattern, hero_img, content, flags=re.DOTALL)

    # Founder SVG replace
    founder_svg_pattern = r'<!-- Elegant Star SVG Motif -->.*?</svg>'
    founder_img = """<img
          src="../assets/images/female-quran-teacher-hijab-hero.webp"
          alt="Founder and Female Quran Teacher Shagufta Rehan"
          class="tutors-founder-image"
          loading="lazy"
          decoding="async"
          width="520"
          height="650"
        />"""
    content = re.sub(founder_svg_pattern, founder_img, content, flags=re.DOTALL)

    # Add id to the founder section split to handle column-reverse
    content = content.replace('<div class="t-container t-split">\n      <div class="t-split-text">\n        <h2>Meet Our Founder</h2>', '<div class="t-container t-split" id="t-founder-split">\n      <div class="t-split-text">\n        <h2>Meet Our Founder</h2>')

    css_block = """
  <style>
    .tutors-hero-image,
    .tutors-founder-image {
      display: block;
      width: 100%;
      height: auto;
      object-fit: contain;
      margin-inline: auto;
    }
    .tutors-hero-image { max-width: 540px; }
    .tutors-founder-image { max-width: 460px; }
    
    @media (max-width: 768px) {
      .tutors-hero-image {
        max-width: 300px;
        margin: 2rem auto 0;
      }
      .tutors-founder-image {
        max-width: 300px;
        margin: 0 auto 2rem;
      }
      #t-founder-split {
        display: flex;
        flex-direction: column-reverse;
      }
    }
  </style>
"""
    if '.tutors-hero-image' not in content:
        content = content.replace('</head>', css_block + '</head>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_about()
update_tutors()
print("Images updated successfully.")
