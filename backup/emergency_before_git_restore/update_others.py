import re

def fix_duplicate_class(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.replace('class="btn btn-primary" class="modal-submit-btn"', 'class="btn btn-primary modal-submit-btn"')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

fix_duplicate_class('services/noorani-qaida.html')

# Base templates for sections
who_for_template = """
        <!-- Who is this for -->
        <div class="who-for-box fade-in">
          <h2 class="section-title text-left" style="font-size:1.8rem;">Who is this course for?</h2>
          <div class="who-for-list">
            
            <div class="wf-item">
              <div class="wf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg></div>
              <div class="wf-text">
                <h4>Women & Girls</h4>
                <p>Comfortable one-to-one sessions with verified female Quran teachers.</p>
              </div>
            </div>
            <div class="wf-item">
              <div class="wf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg></div>
              <div class="wf-text">
                <h4>Children & Boys up to 15 years</h4>
                <p>Engaging methodology tailored to young learners.</p>
              </div>
            </div>
            <div class="wf-item">
              <div class="wf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg></div>
              <div class="wf-text">
                <h4>Beginners</h4>
                <p>Adults starting or continuing their Quran learning journey.</p>
              </div>
            </div>
          </div>
        </div>
"""

methodology_template = """
  <!-- 6. Teaching Methodology -->
  <section class="section course-v2-methodology bg-light">
    <div class="container text-center">
      <h2 class="section-title fade-in">Our Teaching Methodology</h2>
      <p class="section-subtitle fade-in">A proven workflow designed for effective online learning via Zoom and Google Meet.</p>
      
      <div class="cm-grid" style="display:grid;gap:24px;grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));text-align:left;margin-top:40px;">
        <div class="cm-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
          <div class="cm-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M14 2H6a2 2 0 0 0-2 2v16c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V8l-6-6z"></path><path d="M14 3v5h5M16 13H8M16 17H8M10 9H8"></path></svg></div>
          <h3 style="font-size:1.1rem;margin-bottom:8px;">1. Assessment</h3>
          <p style="font-size:0.9rem;color:var(--text-light);margin:0;">Evaluating the student's current proficiency.</p>
        </div>
        <div class="cm-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
          <div class="cm-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg></div>
          <h3 style="font-size:1.1rem;margin-bottom:8px;">2. Learning Plan</h3>
          <p style="font-size:0.9rem;color:var(--text-light);margin:0;">Customizing a structured path for improvement.</p>
        </div>
        <div class="cm-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
          <div class="cm-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg></div>
          <h3 style="font-size:1.1rem;margin-bottom:8px;">3. Regular Classes</h3>
          <p style="font-size:0.9rem;color:var(--text-light);margin:0;">One-to-one live classes with a dedicated tutor.</p>
        </div>
        <div class="cm-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
          <div class="cm-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg></div>
          <h3 style="font-size:1.1rem;margin-bottom:8px;">4. Practice</h3>
          <p style="font-size:0.9rem;color:var(--text-light);margin:0;">Applying principles accurately under supervision.</p>
        </div>
        <div class="cm-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
          <div class="cm-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><polyline points="1 4 1 10 7 10"></polyline><polyline points="23 20 23 14 17 14"></polyline><path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path></svg></div>
          <h3 style="font-size:1.1rem;margin-bottom:8px;">5. Revision</h3>
          <p style="font-size:0.9rem;color:var(--text-light);margin:0;">Consistent review to secure memorization and fluency.</p>
        </div>
        <div class="cm-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
          <div class="cm-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="24" height="24"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg></div>
          <h3 style="font-size:1.1rem;margin-bottom:8px;">6. Parent Updates</h3>
          <p style="font-size:0.9rem;color:var(--text-light);margin:0;">Regular progress communication via WhatsApp.</p>
        </div>
      </div>
    </div>
  </section>
"""

trust_template = """
  <!-- 7. Why Choose Us (EEAT) -->
  <section class="section course-v2-trust">
    <div class="container">
      <div class="trust-flex">
        <div class="trust-content fade-in">
          <h2 class="section-title text-left">Why Choose Al-Tajweed ul Quran Academy?</h2>
          <p>We are dedicated to providing authentic Islamic education for families in Qatar. Our foundation is built on trust, verified teaching expertise, and a strictly ad-free learning space.</p>
          <ul class="trust-list">
            <li><strong>Up to 3 Trial Classes:</strong> Experience our teaching methodology before committing.</li>
            <li><strong>Growing team of 3 female teachers:</strong> Ensuring a comfortable environment for women, girls, and children.</li>
            <li><strong>One-to-One Classes:</strong> Live, personalized instruction via Zoom or Google Meet.</li>
            <li><strong>Flexible Timings:</strong> Choose schedules that fit your family's routine.</li>
            <li><strong>Madinah Tajweed background:</strong> Authentic principles taught by experienced tutors.</li>
            <li><strong>Al-Huda teaching experience:</strong> Proven methodologies led by our founder.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
"""

faq_template = """
  <!-- 8. FAQ -->
  <section class="section course-v2-faq bg-light">
    <div class="container">
      <h2 class="section-title text-center fade-in">Frequently Asked Questions</h2>
      <div class="faq-accordion-grid fade-in" style="max-width:800px;margin:32px auto 0;">
        <details class="faq-accordion" name="faq-group">
          <summary>Do I need any prior knowledge for this course?</summary>
          <div class="faq-content">
            <p>Our female Quran teachers will assess your current level during your trial and create a learning plan tailored perfectly for you or your child.</p>
          </div>
        </details>
        <details class="faq-accordion" name="faq-group">
          <summary>Are all teachers female?</summary>
          <div class="faq-content">
            <p>Yes, our growing team consists strictly of verified female Quran teachers. We focus on providing a secure and comfortable learning environment for women, girls, and boys up to 15 years.</p>
          </div>
        </details>
        <details class="faq-accordion" name="faq-group">
          <summary>How do the online classes work?</summary>
          <div class="faq-content">
            <p>Classes are conducted live, one-to-one, using Zoom or Google Meet. We offer flexible Qatar timings, and parents receive regular progress updates directly via WhatsApp.</p>
          </div>
        </details>
        <details class="faq-accordion" name="faq-group">
          <summary>Can I take a trial class before paying?</summary>
          <div class="faq-content">
            <p>Yes. We offer up to 3 trial classes so you can experience our teaching methodology and meet your tutor before deciding to enroll. Reach out on WhatsApp to schedule yours.</p>
          </div>
        </details>
      </div>
    </div>
  </section>
"""

cta_template = """
  <!-- 9. Final CTA -->
  <section class="section final-cta text-center" id="contact">
    <div class="container">
      <div class="fade-in">
        <h2>Start Learning the Quran with Confidence</h2>
        <p>Book up to 3 trial classes and speak directly with our female Quran teachers.</p>
        <div class="final-cta-buttons">
          <a href="#" class="btn btn-primary" data-modal="open" aria-label="Book Up to 3 Trial Classes">Book Up to 3 Trial Classes</a>
          <a href="https://wa.me/974XXXXXXXX" class="btn btn-outline" target="_blank" rel="noopener" aria-label="WhatsApp">Talk on WhatsApp</a>
        </div>
      </div>
    </div>
  </section>
"""

def generate_hero(title, subtitle):
    return f"""
  <!-- 1. Premium Hero -->
  <section class="course-v2-hero">
    <div class="container text-center">
      <nav class="course-breadcrumb fade-in" aria-label="Breadcrumb">
        <a href="../index.html">Home</a>
        <span class="separator">&gt;</span>
        <span class="crumb">Courses</span>
        <span class="separator">&gt;</span>
        <span class="crumb current" aria-current="page">{title}</span>
      </nav>
      <h1 class="fade-in">{title}</h1>
      <p class="fade-in course-hero-desc">{subtitle}</p>
      
      <ul class="hero-trust-points fade-in" style="list-style: none; padding: 0; display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; margin: 24px 0; font-weight: 500; color: #fff;">
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:18px;height:18px;vertical-align:middle;margin-right:4px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Up to 3 Trial Classes</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:18px;height:18px;vertical-align:middle;margin-right:4px;"><polyline points="20 6 9 17 4 12"></polyline></svg> One-to-One Learning</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:18px;height:18px;vertical-align:middle;margin-right:4px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Female Quran Tutors</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:18px;height:18px;vertical-align:middle;margin-right:4px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Flexible Timings</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:18px;height:18px;vertical-align:middle;margin-right:4px;"><polyline points="20 6 9 17 4 12"></polyline></svg> Qatar</li>
      </ul>

      <div class="course-hero-btns fade-in">
        <a href="#" class="btn btn-primary btn-lg" data-modal="open" aria-label="Book Up to 3 Trial Classes">Book Up to 3 Trial Classes</a>
        <a href="https://wa.me/974XXXXXXXX" class="btn btn-outline btn-lg bg-white" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">Talk on WhatsApp</a>
      </div>
    </div>
  </section>
"""

def generate_outcomes(outcomes_list):
    lis = "".join([f'<span class="o-tag"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg> {o}</span>' for o in outcomes_list])
    return f"""
  <!-- 5. Learning Outcomes -->
  <section class="section course-v2-outcomes bg-emerald-light">
    <div class="container">
      <div class="outcomes-flex">
        <div class="outcomes-text fade-in text-center" style="max-width:800px;margin:0 auto;">
          <h2 class="section-title">Learning Outcomes</h2>
          <p class="section-subtitle">By the end of this program, students will achieve:</p>
          <div class="outcomes-tags">
            {lis}
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# ============================
# Tafseer (Nazra with Tajweed)
# ============================
with open('services/quran-tafseer.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace global texts
text = text.replace('Quran Tafseer Online', 'Nazra with Tajweed')
text = text.replace('Learn Tafseer', 'Nazra with Tajweed')
text = text.replace('Free Trial', 'Up to 3 Trial Classes')
text = text.replace('free trial', 'up to 3 trial classes')
text = text.replace('Skype', 'Google Meet')

header_end = text.find('</header>') + 9
footer_start = text.find('<footer')
head_header = text[:header_end]
main_content = text[header_end:footer_start]
footer_content = text[footer_start:]

# Inject new sections safely by replacing from one section to another.
# Hero
hero = generate_hero('Nazra with Tajweed', 'Enhance your Quran recitation by learning essential Tajweed rules and mastering beautiful, confident pronunciation with verified female tutors.')
main_content = re.sub(r'<section class="course-v2-hero">.*?</section>', hero, main_content, flags=re.DOTALL)

# Who for
main_content = re.sub(r'<!-- Who is this for -->.*?<!-- What you will learn -->', who_for_template + '\n        <!-- What you will learn -->', main_content, flags=re.DOTALL)

# What learn
what_learn_tafseer = """
        <!-- What you will learn -->
        <div class="what-learn-box fade-in">
          <h2 class="section-title text-left" style="font-size:1.8rem;">What Students Learn</h2>
          <ul class="what-learn-list">
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg> Recite the Quran fluently with correct Tajweed rules.</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg> Improve pronunciation and avoid common reading mistakes.</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg> Develop a consistent, daily Quran reading habit.</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg> Gain deep confidence in your recitation ability.</li>
          </ul>
        </div>
"""
main_content = re.sub(r'<!-- What you will learn -->.*?</div>\s*</div>\s*</section>', what_learn_tafseer + '\n      </div>\n    </div>\n  </section>', main_content, flags=re.DOTALL)

# Curriculum
curr_tafseer = """
  <!-- 4. Course Curriculum -->
  <section class="section course-v2-curriculum">
    <div class="container text-center">
      <span class="section-badge fade-in">Step-by-Step</span>
      <h2 class="section-title fade-in">Course Curriculum</h2>
      
      <div class="curriculum-grid" style="display:grid;gap:24px;grid-template-columns:repeat(auto-fit, minmax(250px, 1fr));text-align:left;margin-top:40px;">
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">1. Basic Tajweed</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Introduction to essential Tajweed principles.</p>
        </div>
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><circle cx="12" cy="12" r="10"></circle><path d="M12 8v4l3 3"></path></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">2. Articulation Points</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Mastering Makharij for exact pronunciation.</p>
        </div>
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">3. Fluent Recitation</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Reading chapters with proper flow and rhythm.</p>
        </div>
      </div>
    </div>
  </section>
"""
main_content = re.sub(r'<!-- 4\. Course Curriculum -->.*?(<!-- 5\. Learning Outcomes -->|<section class="section course-v2-outcomes)', curr_tafseer + '\n  <!-- 5. Learning Outcomes -->', main_content, flags=re.DOTALL)

outcomes = generate_outcomes(["Read Quran confidently", "Improve Tajweed", "Develop consistent Quran reading habits", "Improve pronunciation"])
main_content = re.sub(r'<!-- 5\. Learning Outcomes -->.*?(<!-- 6\. Teaching Methodology -->|<section class="section course-v2-methodology)', outcomes + '\n  <!-- 6. Teaching Methodology -->', main_content, flags=re.DOTALL)

main_content = re.sub(r'<!-- 6\. Teaching Methodology -->.*?(<!-- 7\. Why Choose Us \(EEAT\) -->|<section class="section course-v2-trust)', methodology_template + '\n  <!-- 7. Why Choose Us (EEAT) -->', main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- 7\. Why Choose Us \(EEAT\) -->.*?(<!-- 8\. FAQ -->|<section class="section course-v2-faq)', trust_template + '\n  <!-- 8. FAQ -->', main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- 8\. FAQ -->.*?(<!-- 9\. Final CTA -->|<section class="section final-cta)', faq_template + '\n  <!-- 9. Final CTA -->', main_content, flags=re.DOTALL)

# Handle cases where sections were named differently
main_content = re.sub(r'<!-- Result After Completion -->.*?</section>', '', main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- Local Relevance -->.*?</section>', '', main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- FAQ -->.*?</section>', faq_template, main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- CTA -->.*?</section>', cta_template, main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- 9\. Final CTA -->.*?</main>', cta_template + '\n</main>', main_content, flags=re.DOTALL)

css_to_add = """
  <style>
    .skip-link { position:absolute;left:-9999px;z-index:999;padding:1em;background-color:white;color:black;opacity:0; }
    .skip-link:focus { left:50%; opacity:1; }
    .modal-submit-btn { width: 100%; justify-content: center; }
  </style>
</head>
"""
head_header = head_header.replace('</head>', css_to_add)
head_header = head_header.replace('style="position:absolute;left:-9999px;z-index:999;padding:1em;background-color:white;color:black;opacity:0;" onfocus="this.style.left=\'50%\';this.style.opacity=\'1\'" onblur="this.style.left=\'-9999px\';this.style.opacity=\'0\'"', '')
footer_content = footer_content.replace('style="width:100%;justify-content:center"', 'class="btn btn-primary modal-submit-btn"')

with open('services/quran-tafseer.html', 'w', encoding='utf-8') as f:
    f.write(head_header + main_content + footer_content)

print("Tafseer (Nazra) updated.")


# ============================
# Quran Memorization (Hifz)
# ============================
with open('services/quran-memorization.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('Free Trial', 'Up to 3 Trial Classes')
text = text.replace('free trial', 'up to 3 trial classes')
text = text.replace('Skype', 'Google Meet')

header_end = text.find('</header>') + 9
footer_start = text.find('<footer')
head_header = text[:header_end]
main_content = text[header_end:footer_start]
footer_content = text[footer_start:]

hero = generate_hero('Quran Memorization (Hifz)', 'Commit the Holy Quran to memory through a structured, supportive, and highly personalized online learning plan with our expert female tutors.')
main_content = re.sub(r'<section class="course-v2-hero">.*?</section>', hero, main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- Who is this for -->.*?<!-- What you will learn -->', who_for_template + '\n        <!-- What you will learn -->', main_content, flags=re.DOTALL)

what_learn_hifz = """
        <!-- What you will learn -->
        <div class="what-learn-box fade-in">
          <h2 class="section-title text-left" style="font-size:1.8rem;">What Students Learn</h2>
          <ul class="what-learn-list">
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Memorize chapters of the Quran systematically.</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Retain memorization through dedicated revision techniques.</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Recite smoothly from memory with correct Tajweed.</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Build deep confidence in Hifz abilities.</li>
          </ul>
        </div>
"""
main_content = re.sub(r'<!-- What you will learn -->.*?</div>\s*</div>\s*</section>', what_learn_hifz + '\n      </div>\n    </div>\n  </section>', main_content, flags=re.DOTALL)

curr_hifz = """
  <!-- 4. Course Curriculum -->
  <section class="section course-v2-curriculum">
    <div class="container text-center">
      <span class="section-badge fade-in">Step-by-Step</span>
      <h2 class="section-title fade-in">Course Curriculum</h2>
      
      <div class="curriculum-grid" style="display:grid;gap:24px;grid-template-columns:repeat(auto-fit, minmax(250px, 1fr));text-align:left;margin-top:40px;">
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">1. Assessment</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Determining memorization capacity.</p>
        </div>
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><path d="M12 20h9"></path></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">2. Short Surahs</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Beginning with Juz 30.</p>
        </div>
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">3. Complete Hifz</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Progressing through the Quran systematically.</p>
        </div>
      </div>
    </div>
  </section>
"""
main_content = re.sub(r'<!-- 4\. Course Curriculum -->.*?(<!-- 5\. Learning Outcomes -->|<section class="section course-v2-outcomes)', curr_hifz + '\n  <!-- 5. Learning Outcomes -->', main_content, flags=re.DOTALL)

outcomes_hifz = generate_outcomes(["Memorize Quran completely", "Improve Tajweed retention", "Develop daily revision habits", "Build spiritual confidence"])
main_content = re.sub(r'<!-- 5\. Learning Outcomes -->.*?(<!-- 6\. Teaching Methodology -->|<section class="section course-v2-methodology)', outcomes_hifz + '\n  <!-- 6. Teaching Methodology -->', main_content, flags=re.DOTALL)

main_content = re.sub(r'<!-- 6\. Teaching Methodology -->.*?(<!-- 7\. Why Choose Us \(EEAT\) -->|<section class="section course-v2-trust)', methodology_template + '\n  <!-- 7. Why Choose Us (EEAT) -->', main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- 7\. Why Choose Us \(EEAT\) -->.*?(<!-- 8\. FAQ -->|<section class="section course-v2-faq)', trust_template + '\n  <!-- 8. FAQ -->', main_content, flags=re.DOTALL)

main_content = re.sub(r'<!-- Result After Completion -->.*?</section>', '', main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- Local Relevance -->.*?</section>', '', main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- FAQ -->.*?</section>', faq_template, main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- 8\. FAQ -->.*?(<!-- 9\. Final CTA -->|<section class="section final-cta)', faq_template + '\n  <!-- 9. Final CTA -->', main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- CTA -->.*?</section>', cta_template, main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- 9\. Final CTA -->.*?</main>', cta_template + '\n</main>', main_content, flags=re.DOTALL)

head_header = head_header.replace('</head>', css_to_add)
head_header = head_header.replace('style="position:absolute;left:-9999px;z-index:999;padding:1em;background-color:white;color:black;opacity:0;" onfocus="this.style.left=\'50%\';this.style.opacity=\'1\'" onblur="this.style.left=\'-9999px\';this.style.opacity=\'0\'"', '')
footer_content = footer_content.replace('style="width:100%;justify-content:center"', 'class="btn btn-primary modal-submit-btn"')

with open('services/quran-memorization.html', 'w', encoding='utf-8') as f:
    f.write(head_header + main_content + footer_content)
    
print("Hifz updated.")


# ============================
# Six Kalima (Basic Islamic Education)
# ============================
with open('services/six-kalima.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('Six Kalima Online', 'Basic Islamic Education')
text = text.replace('Six Kalima', 'Basic Islamic Education')
text = text.replace('Free Trial', 'Up to 3 Trial Classes')
text = text.replace('free trial', 'up to 3 trial classes')
text = text.replace('Skype', 'Google Meet')

header_end = text.find('</header>') + 9
footer_start = text.find('<footer')
head_header = text[:header_end]
main_content = text[header_end:footer_start]
footer_content = text[footer_start:]

hero = generate_hero('Basic Islamic Education', 'Equip your children and yourself with essential Islamic knowledge, including Duas, Kalimas, and daily Sunnahs, taught by experienced female tutors.')
main_content = re.sub(r'<section class="course-v2-hero">.*?</section>', hero, main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- Who is this for -->.*?<!-- What you will learn -->', who_for_template + '\n        <!-- What you will learn -->', main_content, flags=re.DOTALL)

what_learn_islamic = """
        <!-- What you will learn -->
        <div class="what-learn-box fade-in">
          <h2 class="section-title text-left" style="font-size:1.8rem;">What Students Learn</h2>
          <ul class="what-learn-list">
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Memorize daily Islamic Duas and the 6 Kalimas.</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Understand basic principles of Salah (Prayer).</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Learn essential Islamic etiquette and manners.</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Build a strong, authentic Islamic identity.</li>
          </ul>
        </div>
"""
main_content = re.sub(r'<!-- What you will learn -->.*?</div>\s*</div>\s*</section>', what_learn_islamic + '\n      </div>\n    </div>\n  </section>', main_content, flags=re.DOTALL)

curr_islamic = """
  <!-- 4. Course Curriculum -->
  <section class="section course-v2-curriculum">
    <div class="container text-center">
      <span class="section-badge fade-in">Step-by-Step</span>
      <h2 class="section-title fade-in">Course Curriculum</h2>
      
      <div class="curriculum-grid" style="display:grid;gap:24px;grid-template-columns:repeat(auto-fit, minmax(250px, 1fr));text-align:left;margin-top:40px;">
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">1. Core Beliefs</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Learning the fundamental pillars of Islam.</p>
        </div>
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><path d="M12 20h9"></path></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">2. Daily Duas</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Essential supplications for daily life.</p>
        </div>
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">3. Sunnah & Etiquette</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Manners and character building for Muslim children.</p>
        </div>
      </div>
    </div>
  </section>
"""
main_content = re.sub(r'<!-- 4\. Course Curriculum -->.*?(<!-- 5\. Learning Outcomes -->|<section class="section course-v2-outcomes)', curr_islamic + '\n  <!-- 5. Learning Outcomes -->', main_content, flags=re.DOTALL)

outcomes_islamic = generate_outcomes(["Build strong Islamic character", "Understand daily Sunnahs", "Improve confident prayer", "Learn essential Kalimas"])
main_content = re.sub(r'<!-- 5\. Learning Outcomes -->.*?(<!-- 6\. Teaching Methodology -->|<section class="section course-v2-methodology)', outcomes_islamic + '\n  <!-- 6. Teaching Methodology -->', main_content, flags=re.DOTALL)

main_content = re.sub(r'<!-- 6\. Teaching Methodology -->.*?(<!-- 7\. Why Choose Us \(EEAT\) -->|<section class="section course-v2-trust)', methodology_template + '\n  <!-- 7. Why Choose Us (EEAT) -->', main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- 7\. Why Choose Us \(EEAT\) -->.*?(<!-- 8\. FAQ -->|<section class="section course-v2-faq)', trust_template + '\n  <!-- 8. FAQ -->', main_content, flags=re.DOTALL)

main_content = re.sub(r'<!-- Result After Completion -->.*?</section>', '', main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- Local Relevance -->.*?</section>', '', main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- FAQ -->.*?</section>', faq_template, main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- 8\. FAQ -->.*?(<!-- 9\. Final CTA -->|<section class="section final-cta)', faq_template + '\n  <!-- 9. Final CTA -->', main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- CTA -->.*?</section>', cta_template, main_content, flags=re.DOTALL)
main_content = re.sub(r'<!-- 9\. Final CTA -->.*?</main>', cta_template + '\n</main>', main_content, flags=re.DOTALL)

head_header = head_header.replace('</head>', css_to_add)
head_header = head_header.replace('style="position:absolute;left:-9999px;z-index:999;padding:1em;background-color:white;color:black;opacity:0;" onfocus="this.style.left=\'50%\';this.style.opacity=\'1\'" onblur="this.style.left=\'-9999px\';this.style.opacity=\'0\'"', '')
footer_content = footer_content.replace('style="width:100%;justify-content:center"', 'class="btn btn-primary modal-submit-btn"')

with open('services/six-kalima.html', 'w', encoding='utf-8') as f:
    f.write(head_header + main_content + footer_content)

print("Basic Islamic Education updated.")
