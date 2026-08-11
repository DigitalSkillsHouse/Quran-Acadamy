import re
from pathlib import Path

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
HTML_FILE = BASE_DIR / "index.html"
CSS_FILE = BASE_DIR / "assets" / "css" / "style.css"
MIN_CSS_FILE = BASE_DIR / "assets" / "css" / "style.min.css"

def update_html():
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # The current HTML has `<section class="section premium-section bg-light" id="faq">`
    pattern = r'(<section class="section premium-section bg-light" id="faq">.*?</section>)'
    
    new_html = """<section class="luxury-faq-section" id="faq">
    <div class="container">
      <div class="text-center">
        <h2 class="section-title fade-in" style="font-family: 'Amiri', serif; color: #0A3A2A;">Frequently Asked Questions</h2>
        <p class="section-subtitle fade-in" style="max-width: 600px; margin: 0 auto 48px; font-family: 'Inter', sans-serif;">Find quick answers to common questions about our online Quran classes in Qatar.</p>
      </div>
      
      <div class="luxury-faq-list fade-in">
        <details class="luxury-faq-item" name="faq-group">
          <summary>
            <span class="faq-question">How do online Quran classes work in Qatar?</span>
            <span class="faq-toggle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
          </summary>
          <div class="faq-content">
            <p>Our online Quran classes connect you with a certified tutor via Zoom or Google Meet for live 1-on-1 sessions. Students in Doha, Al Wakrah, Al Khor, Lusail, and across Qatar simply need a device with an internet connection. Classes are scheduled at your convenience, and each session includes interactive Quran reading, recitation practice, and personalized feedback from your dedicated tutor.</p>
          </div>
        </details>

        <details class="luxury-faq-item" name="faq-group">
          <summary>
            <span class="faq-question">Do you offer female Quran teachers in Qatar?</span>
            <span class="faq-toggle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
          </summary>
          <div class="faq-content">
            <p>Yes, Qurana Academy has a dedicated team of certified female Quran teachers available for women and girls in Qatar. Our female tutors are Ijazah-certified, fluent in Arabic, and experienced in teaching Tajweed, Hifz, and Noorani Qaida. Many families in Doha prefer female tutors for their daughters, and we ensure comfortable, professional learning environments.</p>
          </div>
        </details>

        <details class="luxury-faq-item" name="faq-group">
          <summary>
            <span class="faq-question">What age can children start online Quran classes?</span>
            <span class="faq-toggle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
          </summary>
          <div class="faq-content">
            <p>Children as young as 4 years old can begin their Quran learning journey with our Noorani Qaida program. Our tutors are specially trained to engage young learners with patience, interactive methods, and age-appropriate teaching techniques. We recommend starting with short 20-30 minute sessions for young children.</p>
          </div>
        </details>

        <details class="luxury-faq-item" name="faq-group">
          <summary>
            <span class="faq-question">Are there up to 3 trial classes available?</span>
            <span class="faq-toggle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
          </summary>
          <div class="faq-content">
            <p>Absolutely! We offer up to 3 trial classes with no commitment required. Simply fill out our enrollment form or message us on WhatsApp, and we will schedule your first trial class within 24 hours. This allows you to experience our teaching quality, meet your tutor, and decide if Qurana Academy is the right fit for your family.</p>
          </div>
        </details>

        <details class="luxury-faq-item" name="faq-group">
          <summary>
            <span class="faq-question">How much do Quran classes cost in Doha?</span>
            <span class="faq-toggle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
          </summary>
          <div class="faq-content">
            <p>Our online Quran classes start from just $30 per month for the Basic plan (2 classes per week). We offer three plans: Basic ($30/month), Standard ($50/month with 4 classes/week), and Premium ($80/month with 6 classes/week). All plans include 1-on-1 live sessions with certified tutors and progress reports.</p>
          </div>
        </details>

        <details class="luxury-faq-item" name="faq-group">
          <summary>
            <span class="faq-question">What Quran courses are available for students in Qatar?</span>
            <span class="faq-toggle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
          </summary>
          <div class="faq-content">
            <p>We offer a comprehensive range of courses including Noorani Qaida for beginners, Quran reading with Tajweed, Quran memorization (Hifz program), Quran Tafseer (interpretation), Six Kalima course, and Islamic studies. Each course is available for students of all ages and proficiency levels across Qatar.</p>
          </div>
        </details>

        <details class="luxury-faq-item" name="faq-group">
          <summary>
            <span class="faq-question">Can adults join online Quran classes in Qatar?</span>
            <span class="faq-toggle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
          </summary>
          <div class="faq-content">
            <p>Yes, our online Quran classes are designed for learners of all ages, from young children to adults. Many working professionals in Doha and across Qatar join our evening and weekend classes to learn Quran reading, improve their Tajweed, or begin their Hifz journey. We offer flexible scheduling to accommodate busy lifestyles.</p>
          </div>
        </details>

        <details class="luxury-faq-item" name="faq-group">
          <summary>
            <span class="faq-question">How do I enroll in Qurana Academy from Qatar?</span>
            <span class="faq-toggle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
          </summary>
          <div class="faq-content">
            <p>Enrolling is simple. You can fill out the up to 3 trial classes form on our website, message us directly on WhatsApp, or email us at info@qurana-academy.com. Our team will contact you within 24 hours to schedule your up to 3 trial classes class and discuss the best learning plan for you or your child.</p>
          </div>
        </details>
      </div>
    </div>
  </section>"""
    
    updated_content = re.sub(pattern, new_html, content, flags=re.DOTALL)
    
    if content != updated_content:
        with open(HTML_FILE, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Updated HTML structure for FAQ section.")
    else:
        print("Regex did not find a match for faq section.")

def append_css():
    css_content = """
/* ============================================================
   LUXURY FAQ ACCORDION (Light Editorial Style)
   ============================================================ */
.luxury-faq-section {
  background-color: #FAFAFA;
  padding: 80px 0 100px;
}

.luxury-faq-list {
  max-width: 840px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
}

.luxury-faq-item {
  border-bottom: 1px solid rgba(212, 175, 55, 0.3); /* Ultra-fine Matte Gold line */
  transition: all 0.3s ease;
}

.luxury-faq-item:first-child {
  border-top: 1px solid rgba(212, 175, 55, 0.3);
}

.luxury-faq-item summary {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 28px 0;
  cursor: pointer;
  list-style: none; /* Hide default triangle */
}

/* Hide default details marker in WebKit */
.luxury-faq-item summary::-webkit-details-marker {
  display: none;
}

.faq-question {
  font-family: 'Amiri', serif;
  font-size: 1.4rem;
  color: #333333;
  transition: color 0.3s ease;
  padding-right: 24px;
}

.faq-toggle {
  flex-shrink: 0;
  color: #D4AF37;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.faq-toggle svg {
  width: 100%;
  height: 100%;
}

.luxury-faq-item .faq-content {
  padding: 0 48px 32px 0;
  color: #555555;
  font-family: 'Inter', sans-serif;
  font-size: 1.05rem;
  line-height: 1.8;
}

/* Expanded State */
.luxury-faq-item[open] summary .faq-question {
  color: #0A3A2A; /* Shift to Deep Emerald on open */
}

.luxury-faq-item[open] summary .faq-toggle {
  transform: rotate(180deg);
}

/* Smooth padding expansion */
.luxury-faq-item[open] .faq-content {
  animation: faq-fade-in-down 0.4s ease-out forwards;
}

@keyframes faq-fade-in-down {
  0% { opacity: 0; transform: translateY(-10px); }
  100% { opacity: 1; transform: translateY(0); }
}

/* Hover State */
.luxury-faq-item:hover summary .faq-question {
  color: #0A3A2A;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .luxury-faq-section {
    padding: 60px 0;
  }
  
  .faq-question {
    font-size: 1.25rem;
  }
  
  .luxury-faq-item summary {
    padding: 22px 0;
  }
  
  .luxury-faq-item .faq-content {
    padding: 0 0 24px 0;
    font-size: 1rem;
  }
}
"""
    for css_file in [CSS_FILE, MIN_CSS_FILE]:
        with open(css_file, 'a', encoding='utf-8') as f:
            f.write(css_content)
        print(f"Appended Luxury FAQ CSS to {css_file.name}")

if __name__ == "__main__":
    update_html()
    append_css()
    print("FAQ redesign applied successfully.")
