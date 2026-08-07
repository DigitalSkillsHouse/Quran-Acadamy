import re

with open('services/noorani-qaida.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Protect Header/Footer
header_end = text.find('</header>') + 9
footer_start = text.find('<footer')

head_header = text[:header_end]
main_content = text[header_end:footer_start]
footer_content = text[footer_start:]

# 1. SEO & Meta (Head)
head_header = head_header.replace('Start learning Arabic and Quran reading with the best Noorani Qaida online classes in Qatar. One-to-one sessions with female Quran teachers. Book a free trial!', 'Start learning Arabic and Quran reading with authentic Noorani Qaida online classes in Qatar. One-to-one sessions with female Quran teachers. Book up to 3 trial classes.')
head_header = head_header.replace('Master Arabic alphabets and pronunciation with our Noorani Qaida online course. Certified tutors, 1-on-1 sessions. Free trial available.', 'Master Arabic alphabets and pronunciation with our Noorani Qaida online course. Female tutors, one-to-one sessions. Up to 3 trial classes available.')
head_header = head_header.replace('"description": "Start learning Arabic and Quran reading with the best Noorani Qaida online classes in Qatar. One-to-one sessions with female Quran teachers. Book a free trial!"', '"description": "Start learning Arabic and Quran reading with authentic Noorani Qaida online classes in Qatar. One-to-one sessions with female Quran teachers. Book up to 3 trial classes."')

# 2. Hero Section
# Keep layout, improve typography, add trust points, change CTAs
hero_replacement = """
  <!-- 1. Premium Hero -->
  <section class="course-v2-hero">
    <div class="container text-center">
      <nav class="course-breadcrumb fade-in" aria-label="Breadcrumb">
        <a href="../index.html">Home</a>
        <span class="separator">&gt;</span>
        <span class="crumb">Courses</span>
        <span class="separator">&gt;</span>
        <span class="crumb current" aria-current="page">Noorani Qaida</span>
      </nav>
      <h1 class="fade-in">Noorani Qaida Online Qatar</h1>
      <p class="fade-in course-hero-desc">The perfect starting point for kids and beginners to learn Arabic alphabets, pronunciation, and basic Quran reading.</p>
      
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
main_content = re.sub(r'<!-- 1\. Premium Hero -->.*?<!-- 2 & 3\. Who is this for & What you learn -->', hero_replacement + '\n  <!-- 2 & 3. Who is this for & What you learn -->', main_content, flags=re.DOTALL)

# 3. Who is this for
who_for_replacement = """
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
                <p>Gentle, engaging introduction to Arabic letters for young learners.</p>
              </div>
            </div>
            <div class="wf-item">
              <div class="wf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg></div>
              <div class="wf-text">
                <h4>Beginners</h4>
                <p>Adults starting their Quran learning journey from the very basics.</p>
              </div>
            </div>
          </div>
        </div>
"""
main_content = re.sub(r'<!-- Who is this for -->.*?<!-- What you will learn -->', who_for_replacement + '\n        <!-- What you will learn -->', main_content, flags=re.DOTALL)

# 4. What you will learn
what_learn_replacement = """
        <!-- What you will learn -->
        <div class="what-learn-box fade-in">
          <h2 class="section-title text-left" style="font-size:1.8rem;">What Students Learn</h2>
          <ul class="what-learn-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
              Recognize and confidently read Arabic letters with Harakat.
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
              Articulate complex letters from their correct origin points (Makharij).
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
              Connect individual letters seamlessly to form complete words.
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
              Apply essential foundational rules for accurate Quranic reading.
            </li>
          </ul>
        </div>
"""
main_content = re.sub(r'<!-- What you will learn -->.*?</div>\s*</div>\s*</section>', what_learn_replacement + '\n      </div>\n    </div>\n  </section>', main_content, flags=re.DOTALL)

# 5. Course Curriculum
curriculum_replacement = """
  <!-- 4. Course Curriculum -->
  <section class="section course-v2-curriculum">
    <div class="container text-center">
      <span class="section-badge fade-in">Step-by-Step</span>
      <h2 class="section-title fade-in">Course Curriculum</h2>
      <p class="section-subtitle fade-in">A structured pathway designed for consistent progress.</p>
      
      <div class="curriculum-grid" style="display:grid;gap:24px;grid-template-columns:repeat(auto-fit, minmax(250px, 1fr));text-align:left;margin-top:40px;">
        
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">1. The Alphabet</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Mastering the Arabic alphabet (Huroof e Mufradaat) with perfect pronunciation.</p>
        </div>
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><path d="M13.4 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-7.4"></path><path d="M2 6h4"></path><path d="M2 10h4"></path><path d="M2 14h4"></path><path d="M2 18h4"></path><path d="M21.4 2.6a2.12 2.12 0 0 1 3 3L16 14l-4 1 1-4 8.4-8.4z"></path></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">2. Joined Letters</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Learning how letters change shape when joined seamlessly together (Murakkabat).</p>
        </div>
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><circle cx="12" cy="12" r="10"></circle><path d="M12 8v4l3 3"></path></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">3. Movements & Vowels</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Understanding Harakat, Tanween, and basic short vowel sounds.</p>
        </div>
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><path d="M2 12h4l2-9 5 18 3-10h4"></path></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">4. Maddah & Leen</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Practicing correctly elongated sounds and soft letters.</p>
        </div>
        <div class="curr-card fade-in" style="background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,0.05);border-top:4px solid var(--primary-color);">
          <div class="curr-icon" style="color:var(--primary-color);margin-bottom:16px;"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="32" height="32"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
          <h3 style="font-size:1.2rem;margin-bottom:8px;">5. Sukoon & Shaddah</h3>
          <p style="font-size:0.95rem;color:var(--text-light);margin:0;">Mastering pausing and emphasized letters for fluent and natural reading.</p>
        </div>
      </div>
    </div>
  </section>
"""
main_content = re.sub(r'<!-- 4\. Course Curriculum -->.*?<!-- 5\. Learning Outcomes -->', curriculum_replacement + '\n  <!-- 5. Learning Outcomes -->', main_content, flags=re.DOTALL)

# 6. Learning Outcomes
outcomes_replacement = """
  <!-- 5. Learning Outcomes -->
  <section class="section course-v2-outcomes bg-emerald-light">
    <div class="container">
      <div class="outcomes-flex">
        <div class="outcomes-text fade-in text-center" style="max-width:800px;margin:0 auto;">
          <h2 class="section-title">Learning Outcomes</h2>
          <p class="section-subtitle">By the end of this program, students will be able to:</p>
          <div class="outcomes-tags">
            <span class="o-tag"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg> Read Quran confidently</span>
            <span class="o-tag"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg> Improve pronunciation</span>
            <span class="o-tag"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg> Build confidence</span>
            <span class="o-tag"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg> Develop consistent Quran reading habits</span>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
main_content = re.sub(r'<!-- 5\. Learning Outcomes -->.*?<!-- 6\. Teaching Methodology -->', outcomes_replacement + '\n  <!-- 6. Teaching Methodology -->', main_content, flags=re.DOTALL)

# 7. Teaching Methodology
methodology_replacement = """
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
main_content = re.sub(r'<!-- 6\. Teaching Methodology -->.*?<!-- 7\. Why Choose Us \(EEAT\) -->', methodology_replacement + '\n  <!-- 7. Why Choose Us (EEAT) -->', main_content, flags=re.DOTALL)

# 8. Trust Section (EEAT)
trust_replacement = """
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
main_content = re.sub(r'<!-- 7\. Why Choose Us \(EEAT\) -->.*?<!-- 8\. FAQ -->', trust_replacement + '\n  <!-- 8. FAQ -->', main_content, flags=re.DOTALL)

# 9. FAQ
faq_replacement = """
  <!-- 8. FAQ -->
  <section class="section course-v2-faq bg-light">
    <div class="container">
      <h2 class="section-title text-center fade-in">Frequently Asked Questions</h2>
      <div class="faq-accordion-grid fade-in" style="max-width:800px;margin:32px auto 0;">
        <details class="faq-accordion" name="faq-group">
          <summary>Do I need any prior knowledge for this course?</summary>
          <div class="faq-content">
            <p>Not at all. Our beginner courses start from scratch. Our female Quran teachers will patiently guide you or your child through the Arabic alphabet at a pace that ensures complete understanding.</p>
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
main_content = re.sub(r'<!-- 8\. FAQ -->.*?<!-- 9\. Final CTA -->', faq_replacement + '\n  <!-- 9. Final CTA -->', main_content, flags=re.DOTALL)

# 10. Final CTA
cta_replacement = """
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
main_content = re.sub(r'<!-- 9\. Final CTA -->.*?</main>', cta_replacement + '\n</main>', main_content, flags=re.DOTALL)

# Footer CTAs (in modal)
footer_content = footer_content.replace('Book Free Trial', 'Book Up to 3 Trial Classes')
footer_content = footer_content.replace('Start Your Free Trial', 'Start Your Up to 3 Trial Classes')
footer_content = footer_content.replace('Experience a free Noorani Qaida class', 'Experience up to 3 Noorani Qaida trial classes')
footer_content = footer_content.replace('style="width:100%;justify-content:center"', 'class="modal-submit-btn"')

# Remove any remaining Skype references
main_content = main_content.replace('Skype', 'Google Meet')
footer_content = footer_content.replace('Skype', 'Google Meet')

# Schema Sync (FAQ)
head_header = head_header.replace('"text": "Our beginners\' courses start from absolute scratch. If you\'re enrolling in an advanced course like Hifz or Tafseer, our tutors will first conduct a basic assessment to ensure it\'s the right fit for your current level."', '"text": "Not at all. Our beginner courses start from scratch. Our female Quran teachers will patiently guide you or your child through the Arabic alphabet at a pace that ensures complete understanding."')
head_header = head_header.replace('"text": "Yes, all our classes are conducted by highly qualified, verified female Quran teachers. We specialize in providing a comfortable and respectful learning environment for women, girls, and young children in Qatar."', '"text": "Yes, our growing team consists strictly of verified female Quran teachers. We focus on providing a secure and comfortable learning environment for women, girls, and boys up to 15 years."')
head_header = head_header.replace('"text": "Classes are held live, one-to-one, via Zoom or Skype. You just need a stable internet connection and a device (laptop, tablet, or smartphone). The tutor shares their screen to display the Quran or Qaida, making it easy to follow along."', '"text": "Classes are conducted live, one-to-one, using Zoom or Google Meet. We offer flexible Qatar timings, and parents receive regular progress updates directly via WhatsApp."')
head_header = head_header.replace('"text": "Absolutely. We offer a completely free, no-obligation trial class. This allows you to experience our teaching methodology and meet the tutor before deciding to enroll."', '"text": "Yes. We offer up to 3 trial classes so you can experience our teaching methodology and meet your tutor before deciding to enroll. Reach out on WhatsApp to schedule yours."')

# CSS fixes
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


final_text = head_header + main_content + footer_content

with open('services/noorani-qaida.html', 'w', encoding='utf-8') as f:
    f.write(final_text)

print("Noorani Qaida page updated successfully.")
