import re

filepath = 'contact.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_addition = """
    /* Hero Buttons Update */
    .c-hero-btns { display: flex; flex-direction: row; gap: 20px; justify-content: flex-start; margin-top: 40px; }
    .c-hero-btns a { flex: 1; text-align: center; display: flex; justify-content: center; align-items: center; }
    @media(max-width: 600px) {
      .c-hero-btns { flex-direction: column; gap: 16px; }
      .c-hero-btns a { width: 100%; }
    }
  </style>"""

content = content.replace('  </style>', css_addition)

# 2. Update Hero Section
old_hero_start = content.find('<!-- Section 1: Premium Hero -->')
old_hero_end = content.find('<!-- Section 2: Get in Touch -->')

if old_hero_start != -1 and old_hero_end != -1:
    new_hero = """<!-- Section 1: Premium Hero -->
  <section class="c-section c-bg-emerald" style="padding-top: 120px; padding-bottom: 100px; display: flex; align-items: center; min-height: 50vh;">
    <div class="c-container" style="max-width: 800px; margin: 0 auto; width: 100%;">
      <div class="c-arabic" style="text-align:left; color: var(--c-gold);">﴿ فَاسْأَلُوا أَهْلَ الذِّكْرِ إِن كُنتُمْ لَا تَعْلَمُونَ ﴾</div>
      <div class="c-arabic-translation" style="text-align:left; color: rgba(255,255,255,0.8);">"So ask the people of knowledge if you do not know."<br>(Quran 16:43)</div>
      <h1 class="c-h1" style="text-align:left; color: var(--c-white);">Let's Begin Your Quran Journey</h1>
      <p class="c-p" style="text-align:left; max-width:100%; color: rgba(255,255,255,0.9);">Contact our academy to discuss your child's learning needs and book up to 3 trial classes with our verified female Quran teachers.</p>
      
      <ul class="c-trust-bullets" style="justify-content:flex-start; gap:16px 24px;">
        <li style="color: var(--c-white);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg> Up to 3 Trial Classes</li>
        <li style="color: var(--c-white);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg> Female Quran Teachers</li>
        <li style="color: var(--c-white);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg> One-to-One Classes</li>
        <li style="color: var(--c-white);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg> Flexible Timings</li>
        <li style="color: var(--c-white);"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg> Qatar Friendly</li>
      </ul>

      <div class="c-hero-btns">
        <a href="#contact-form" class="c-btn-primary" style="background: var(--c-gold); color: var(--c-emerald);" aria-label="Book Up to 3 Trial Classes">Book Up to 3 Trial Classes</a>
        <a href="https://wa.me/974XXXXXXXX" class="c-btn-outline" style="border-color: var(--c-white); color: var(--c-white);" target="_blank" rel="noopener" aria-label="Talk on WhatsApp">Talk on WhatsApp</a>
      </div>
    </div>
  </section>

  """
    
    content = content[:old_hero_start] + new_hero + content[old_hero_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Contact Hero updated successfully.")
