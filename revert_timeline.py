import re
from pathlib import Path

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
HTML_FILE = BASE_DIR / "index.html"
CSS_FILE = BASE_DIR / "assets" / "css" / "style.css"
MIN_CSS_FILE = BASE_DIR / "assets" / "css" / "style.min.css"

def revert_html():
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(<section class="luxury-timeline-section" id="how-it-works">.*?</section>)'
    
    old_html = """<section class="section bg-light" id="how-it-works">
    <div class="container text-center">
      <h2 class="section-title fade-in">How Our Online Quran Classes Work</h2>
      <p class="section-subtitle fade-in">A simple, transparent process to start your journey with the Holy Quran today.</p>
      
      <div class="timeline-grid fade-in">
        <div class="timeline-step">
          <div class="ts-number">1</div>
          <div class="ts-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          </div>
          <h3>Book Your Up to 3 Trial Classes</h3>
          <p>Sign up online in less than a minute. No credit card required.</p>
        </div>

        <div class="timeline-arrow">↓</div>

        <div class="timeline-step">
          <div class="ts-number">2</div>
          <div class="ts-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          </div>
          <h3>Choose Your Preferred Schedule</h3>
          <p>Select flexible timings that work best for your family in Qatar.</p>
        </div>

        <div class="timeline-arrow">↓</div>

        <div class="timeline-step">
          <div class="ts-number">3</div>
          <div class="ts-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          </div>
          <h3>Meet Your Female Quran Tutor</h3>
          <p>Connect 1-on-1 with your dedicated teacher in a secure environment.</p>
        </div>

        <div class="timeline-arrow">↓</div>

        <div class="timeline-step">
          <div class="ts-number">4</div>
          <div class="ts-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          </div>
          <h3>Start Your Quran Journey</h3>
          <p>Begin learning, tracking progress, and perfecting your recitation.</p>
        </div>
      </div>
      
      <div style="margin-top: 48px;" class="fade-in">
        <a href="#" class="btn btn-primary" data-modal="open" aria-label="Book Your Up to 3 Trial Classes">Get Started Now</a>
      </div>
    </div>
  </section>"""
    
    updated_content = re.sub(pattern, old_html, content, flags=re.DOTALL)
    
    if content != updated_content:
        with open(HTML_FILE, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Reverted HTML structure for How It Works timeline.")
    else:
        print("Regex did not find a match for luxury-timeline-section.")

def revert_css():
    for css_file in [CSS_FILE, MIN_CSS_FILE]:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # The appended CSS started with this exact string:
        css_header = r"/\* ============================================================\s*LUXURY TIMELINE SECTION \(How it Works\)\s*============================================================ \*/.*"
        
        updated_content = re.sub(css_header, '', content, flags=re.DOTALL)
        
        if content != updated_content:
            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Removed Timeline CSS from {css_file.name}")
        else:
            print(f"Timeline CSS not found in {css_file.name}")

if __name__ == "__main__":
    revert_html()
    revert_css()
    print("Revert completed successfully.")
