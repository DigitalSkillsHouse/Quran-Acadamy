import os
from pathlib import Path
import shutil

BASE_DIR = Path(r"e:\quran academy\Quran-Acadamy")
CSS_DIR = BASE_DIR / "assets" / "css"
BACKUP_DIR = BASE_DIR / "backup" / "luxury_ui_batch15"

BACKUP_DIR.mkdir(parents=True, exist_ok=True)

LUXURY_CSS = """

/* ============================================================
   BATCH 15: LUXURY HEADER & FOOTER REDESIGN (QATAR ELITE)
   ============================================================ */

/* 1. TOP ANNOUNCEMENT BAR */
.top-info-bar {
  background: linear-gradient(135deg, #1A1A1A 0%, #0A3A2A 100%) !important;
  color: #F8F9FA !important;
  padding: 12px 0 !important;
  border-bottom: 1px solid rgba(212, 175, 55, 0.2) !important;
}
.top-info-bar a {
  color: #F8F9FA !important;
  transition: color 0.3s ease !important;
}
.top-info-bar a:hover {
  color: #D4AF37 !important;
}
.info-icon {
  color: #D4AF37 !important;
  margin-right: 6px !important;
}

/* 2. MAIN NAVIGATION HEADER */
.header {
  background: rgba(255, 255, 255, 0.98) !important;
  backdrop-filter: blur(10px) !important;
  -webkit-backdrop-filter: blur(10px) !important;
  box-shadow: 0 10px 30px rgba(10, 58, 42, 0.08) !important;
  padding: 16px 0 !important;
  border-bottom: 2px solid #D4AF37 !important;
  transition: all 0.4s ease !important;
}
.nav-links a:not(.nav-cta) {
  font-weight: 600 !important;
  color: #1A1A1A !important;
  padding: 8px 16px !important;
  transition: color 0.3s ease !important;
  position: relative !important;
}
.nav-links a:not(.nav-cta):hover {
  color: #0A3A2A !important;
}
.nav-links a:not(.nav-cta)::after {
  content: "" !important;
  position: absolute !important;
  bottom: 0 !important;
  left: 50% !important;
  width: 0% !important;
  height: 2px !important;
  background-color: #D4AF37 !important;
  transition: all 0.3s ease !important;
  transform: translateX(-50%) !important;
}
.nav-links a:not(.nav-cta):hover::after {
  width: 80% !important;
}

/* DROPDOWN ANIMATIONS */
.dropdown {
  background: #ffffff !important;
  border-radius: 8px !important;
  box-shadow: 0 15px 35px rgba(0,0,0,0.1) !important;
  border-top: 3px solid #D4AF37 !important;
  padding: 10px 0 !important;
  opacity: 0 !important;
  visibility: hidden !important;
  transform: translateY(15px) !important;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
  display: block !important;
  pointer-events: none !important;
}
.has-dropdown:hover .dropdown {
  opacity: 1 !important;
  visibility: visible !important;
  transform: translateY(0) !important;
  pointer-events: auto !important;
}
.dropdown a {
  padding: 12px 24px !important;
  font-weight: 500 !important;
  border-bottom: 1px solid rgba(0,0,0,0.03) !important;
  transition: all 0.3s ease !important;
}
.dropdown a:hover {
  background: rgba(212, 175, 55, 0.05) !important;
  color: #0A3A2A !important;
  padding-left: 28px !important;
}
.dropdown a::after {
  display: none !important;
}

/* 3. CTA BUTTON */
.nav-cta {
  background: linear-gradient(135deg, #0A3A2A 0%, #0d543c 100%) !important;
  color: #D4AF37 !important;
  border: 1px solid #D4AF37 !important;
  font-weight: 700 !important;
  padding: 12px 28px !important;
  border-radius: 30px !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2) !important;
  transition: all 0.4s ease !important;
}
.nav-cta:hover {
  background: #D4AF37 !important;
  color: #0A3A2A !important;
  border-color: #0A3A2A !important;
  box-shadow: 0 8px 25px rgba(212, 175, 55, 0.4) !important;
  transform: translateY(-2px) !important;
}

/* 4. FOOTER UPGRADE */
.footer-v2 {
  background-color: #0A3A2A !important;
  background-image: radial-gradient(circle at top right, rgba(212, 175, 55, 0.05) 0%, transparent 40%) !important;
  color: #F8F9FA !important;
  padding: 80px 0 20px 0 !important;
  border-top: 4px solid #D4AF37 !important;
}
.footer-v2-grid {
  gap: 60px !important;
}
.footer-v2-col h4 {
  color: #D4AF37 !important;
  font-family: 'Amiri', serif !important;
  font-size: 1.4rem !important;
  margin-bottom: 24px !important;
  position: relative !important;
  padding-bottom: 12px !important;
}
.footer-v2-col h4::after {
  content: "" !important;
  position: absolute !important;
  bottom: 0 !important;
  left: 0 !important;
  width: 50px !important;
  height: 2px !important;
  background-color: #D4AF37 !important;
}
.footer-v2-col p {
  color: #DDE2DF !important;
  line-height: 1.8 !important;
  font-size: 0.95rem !important;
}
.footer-v2-links li a, .footer-v2-contact li a, .footer-v2-contact li {
  color: #DDE2DF !important;
  font-size: 0.95rem !important;
  transition: all 0.3s ease !important;
}
.footer-v2-links li a:hover, .footer-v2-contact li a:hover {
  color: #D4AF37 !important;
  transform: translateX(5px) !important;
  display: inline-block !important;
}
.footer-v2-contact li svg {
  color: #D4AF37 !important;
  margin-right: 12px !important;
  width: 20px !important;
  height: 20px !important;
}
.footer-v2-bottom {
  border-top: 1px solid rgba(255,255,255,0.08) !important;
  margin-top: 60px !important;
  padding-top: 24px !important;
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  flex-wrap: wrap !important;
}
.footer-v2-bottom p {
  color: #A0B0A8 !important;
  font-size: 0.85rem !important;
  margin: 0 !important;
}
.footer-v2-legal {
  display: flex !important;
  gap: 20px !important;
  list-style: none !important;
  margin: 0 !important;
  padding: 0 !important;
}
.footer-v2-legal li a {
  color: #A0B0A8 !important;
  font-size: 0.85rem !important;
  text-decoration: none !important;
  transition: color 0.3s ease !important;
}
.footer-v2-legal li a:hover {
  color: #D4AF37 !important;
}
@media (max-width: 768px) {
  .footer-v2-bottom {
    flex-direction: column !important;
    text-align: center !important;
    gap: 16px !important;
  }
}
"""

def append_luxury_css(filepath):
    # Backup
    shutil.copy2(filepath, BACKUP_DIR / filepath.name)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Avoid appending multiple times
    if "BATCH 15: LUXURY HEADER & FOOTER REDESIGN" not in content:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(LUXURY_CSS)
        print(f"Appended luxury CSS to {filepath.name}")
    else:
        print(f"CSS already exists in {filepath.name}")

append_luxury_css(CSS_DIR / "style.css")
append_luxury_css(CSS_DIR / "style.min.css")
