import os
import re
from pathlib import Path

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
HTML_FILE = BASE_DIR / "index.html"
CSS_FILE = BASE_DIR / "assets" / "css" / "style.css"
MIN_CSS_FILE = BASE_DIR / "assets" / "css" / "style.min.css"

def update_html():
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define a regex to find the #why-choose-us section
    pattern = r'(<section class="section premium-section bg-light" id="why-choose-us">.*?</section>)'
    
    new_html = """<section class="why-choose-split" id="why-choose-us">
    <div class="wc-left fade-in">
      <h2 class="wc-title">Why Choose Al-Tajweed ul Quran Academy in Qatar?</h2>
      <p class="wc-subtitle">Providing the best online Islamic education for families in Doha, Al Rayyan, and Lusail with a focus on Tajweed excellence and personalized learning.</p>
      
      <div class="wc-narrative-flow">
        <div class="wc-item">
          <div class="wc-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          </div>
          <div class="wc-content">
            <h3>Qualified Female Quran Tutors</h3>
            <p>Mothers and sisters in Qatar trust our dedicated female Quran teachers. We offer a safe, comfortable environment where women and children can learn the Holy Quran with privacy, respect, and deep understanding.</p>
            <a href="tutors/female-tutors.html" class="wc-link">Meet Our Teachers →</a>
          </div>
        </div>

        <div class="wc-item">
          <div class="wc-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          </div>
          <div class="wc-content">
            <h3>Personalized One-to-One Learning</h3>
            <p>Unlike crowded group sessions, our online Quran classes provide 100% focused attention. This direct tutor-to-student approach ensures faster progress, immediate correction of mistakes, and a curriculum adapted to your learning speed.</p>
          </div>
        </div>

        <div class="wc-item">
          <div class="wc-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          </div>
          <div class="wc-content">
            <h3>Strong Tajweed Foundation</h3>
            <p>Correct pronunciation is obligatory. Our structured Tajweed classes focus on Makharij (articulation points) and Sifat (attributes of letters), ensuring every student recites the Holy Quran exactly as it was revealed.</p>
            <a href="services/quran-tafseer.html" class="wc-link">Explore Tajweed →</a>
          </div>
        </div>

        <div class="wc-item">
          <div class="wc-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          </div>
          <div class="wc-content">
            <h3>Flexible Class Timings</h3>
            <p>We understand the busy schedules of families in Al Wakrah and Doha. Book your online Islamic education sessions at times that suit you best, with tutors available morning, afternoon, and evening to fit your lifestyle.</p>
          </div>
        </div>
        
        <div class="wc-item">
          <div class="wc-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          </div>
          <div class="wc-content">
            <h3>Safe Islamic Learning Environment</h3>
            <p>We provide a secure, ad-free online platform dedicated solely to Quranic studies. Parents can monitor their kids Quran classes easily, ensuring a spiritually enriching and entirely safe educational experience.</p>
          </div>
        </div>

        <div class="wc-item">
          <div class="wc-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          </div>
          <div class="wc-content">
            <h3>15+ Years Teaching Experience</h3>
            <p>Benefit from over a decade and a half of proven teaching methodologies. Our experienced tutors have successfully guided many students from beginners to fluent reciters and Hafiz-e-Quran.</p>
            <a href="about.html" class="wc-link">Read Our Story →</a>
          </div>
        </div>

      </div>
    </div>
    <div class="wc-right fade-in-right">
      <div class="wc-gradient-overlay"></div>
      <div class="wc-pattern-overlay"></div>
    </div>
  </section>"""
    
    # We use re.sub with re.DOTALL so .* matches newlines
    updated_content = re.sub(pattern, new_html, content, flags=re.DOTALL)
    
    if content != updated_content:
        with open(HTML_FILE, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Updated HTML structure in index.html.")
    else:
        print("Regex did not find a match. Ensure the section exists exactly as expected.")


def update_css():
    elite_css = """
/* ============================================================
   WHY CHOOSE US - EDITORIAL SPLIT
   ============================================================ */
.why-choose-split {
  display: flex;
  min-height: 800px;
  background: #0A3A2A; /* Deep Emerald */
  color: #FFFFFF;
  position: relative;
  overflow: hidden;
}

.wc-left {
  flex: 1;
  padding: 100px 8%;
  display: flex;
  flex-direction: column;
}

.wc-title {
  font-family: 'Amiri', serif;
  font-size: 3.5rem;
  line-height: 1.2;
  color: #D4AF37; /* Matte Gold */
  margin-bottom: 20px;
}

.wc-subtitle {
  font-family: 'Inter', sans-serif;
  font-size: 1.15rem;
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.85);
  margin-bottom: 50px;
  max-width: 600px;
  font-weight: 300;
}

.wc-narrative-flow {
  display: flex;
  flex-direction: column;
}

.wc-item {
  display: flex;
  align-items: flex-start;
  gap: 24px;
  padding: 40px 0;
  border-bottom: 1px solid rgba(212, 175, 55, 0.2);
}

.wc-item:first-child {
  border-top: 1px solid rgba(212, 175, 55, 0.2);
}

.wc-icon {
  flex: 0 0 32px;
  color: #D4AF37;
}

.wc-icon svg {
  width: 32px;
  height: 32px;
}

.wc-content h3 {
  font-family: 'Amiri', serif;
  font-size: 1.8rem;
  color: #D4AF37;
  margin-bottom: 12px;
  margin-top: -5px;
}

.wc-content p {
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.75);
  margin-bottom: 16px;
  font-weight: 300;
}

.wc-link {
  display: inline-block;
  font-family: 'Inter', sans-serif;
  color: #D4AF37;
  font-weight: 500;
  font-size: 0.95rem;
  text-decoration: none;
  position: relative;
  transition: opacity 0.3s ease;
}

.wc-link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 1px;
  background: #D4AF37;
  transition: transform 0.3s ease;
  transform-origin: right;
  transform: scaleX(0);
}

.wc-link:hover::after {
  transform-origin: left;
  transform: scaleX(1);
}

.wc-link:hover {
  opacity: 0.8;
}

.wc-right {
  flex: 1;
  position: relative;
  background: url('../images/female-quran-teacher-hijab-hero.webp') center/cover no-repeat;
}

/* Dark Gradient Overlay to blend with emerald */
.wc-gradient-overlay {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(90deg, #0A3A2A 0%, rgba(10,58,42,0.4) 50%, rgba(10,58,42,0.1) 100%);
  pointer-events: none;
}

/* Islamic Geometric 8-Point Star Pattern Overlay */
.wc-pattern-overlay {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 100 100"><path d="M50 0 L60 40 L100 50 L60 60 L50 100 L40 60 L0 50 L40 40 Z" fill="none" stroke="%23D4AF37" stroke-width="1" opacity="0.15"/></svg>');
  background-size: 60px 60px;
  pointer-events: none;
  z-index: 2;
}

/* Mobile Responsive */
@media (max-width: 1024px) {
  .why-choose-split {
    flex-direction: column-reverse;
  }
  
  .wc-left {
    padding: 60px 5%;
  }

  .wc-title {
    font-size: 2.8rem;
  }

  .wc-right {
    min-height: 400px;
    background-position: top center;
  }
  
  .wc-gradient-overlay {
    background: linear-gradient(0deg, #0A3A2A 0%, rgba(10,58,42,0.4) 50%, rgba(10,58,42,0.1) 100%);
  }
}
"""

    for css_file in [CSS_FILE, MIN_CSS_FILE]:
        with open(css_file, 'a', encoding='utf-8') as f:
            f.write(elite_css)
        print(f"Appended Elite CSS to {css_file.name}")

if __name__ == "__main__":
    update_html()
    update_css()
    print("Redesign successfully applied.")
