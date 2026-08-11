# Qurana Academy Website - Features, Functions, and SEO Implementations

Last updated: 2026-04-30

## 1) Current Website Structure

- Core pages implemented:
  - `index.html` (homepage)
  - `about.html`
  - `pricing.html`
  - `faq.html`
  - `reviews.html`
  - `contact.html`
  - `blog/index.html`
- Service pages implemented:
  - `services/noorani-qaida.html`
  - `services/quran-tafseer.html`
  - `services/quran-memorization.html`
  - `services/six-kalima.html`
- Tutor pages implemented:
  - `tutors/male-tutors.html`
  - `tutors/female-tutors.html`
- Shared assets:
  - `assets/css/style.css`
  - `assets/js/main.js`

## 2) Implemented Frontend Features

### A. Global Navigation and Layout
- Responsive header with desktop navigation and mobile hamburger menu.
- Services and Tutors dropdown menus in primary navigation.
- Top info bar with phone, email, and working hours.
- Mobile overlay support when nav drawer is open.
- Footer with quick links, course links, contact info, and service locations.

### B. Homepage Content Modules
- Hero section with trust indicators and conversion CTAs.
- About section with long-form institutional content.
- Services grid with dedicated course cards and page links.
- Why choose us section with value proposition cards.
- Tutor showcase cards.
- Pricing preview cards and full pricing page link.
- Testimonials carousel/slider.
- FAQ accordion section.
- CTA section for free trial conversion.

### C. Conversion and Contact Features
- Free trial modal accessible from multiple CTA buttons (`data-modal="open"`).
- Free trial form with required field validation.
- Contact form validation flow on contact page (`contactForm` support in JS).
- Click-to-call (`tel:`), click-to-email (`mailto:`), and WhatsApp links.
- Floating WhatsApp button.

### D. UX and Accessibility-Related Features
- Back-to-top button with smooth scroll behavior.
- Smooth scrolling for in-page anchor links.
- Header style change on scroll.
- Basic ARIA usage (navigation labels, button labels, content roles).
- Keyboard close support for modal (`Escape` key).
- Overlay click support to close modal/nav.

## 3) JavaScript Functions Implemented (`assets/js/main.js`)

### A. Scroll/Visibility Functions
- `handleScroll()`
  - Adds/removes header `scrolled` state.
  - Hides top info bar on scroll.
  - Toggles visibility of back-to-top button after threshold.
- `animateOnScroll()`
  - Adds `visible` class to fade animation elements once in viewport.

### B. Mobile Navigation Functions
- `toggleNav()`
  - Toggles hamburger state, nav open state, mobile overlay.
  - Locks/unlocks body scroll while nav is open.
- Auto-close nav when a navigation link is clicked on mobile.

### C. FAQ Interaction
- Accordion behavior for `.faq-question`.
- Single-open-item logic with dynamic `maxHeight` expansion.

### D. Testimonials Slider
- Responsive slide-per-view logic (`getPerView()`).
- Slide count and bounds logic (`slideCount()` and `update()`).
- Prev/next button controls.
- Resize listener to keep slider state valid across breakpoints.

### E. Modal and Form Functions
- `openModal()` and `closeModal()`
  - Opens/closes free trial modal.
  - Locks/unlocks body scroll.
- Auto modal trigger after 4 seconds on first session load.
- Trial form validation (`trialForm`) with submit-state feedback.
- Contact form validation (`contactForm`) including email regex check.

### F. Navigation Enhancement
- Active navigation highlighting based on current path.

## 4) SEO Implementations Completed

### A. Technical On-Page SEO (All Main Pages)
- Unique `<title>` tags.
- Meta description tags.
- Meta keyword tags.
- `robots` meta set to `index, follow`.
- Canonical URL tags on each page.
- Correct viewport and charset tags.
- `lang="en"` and `dir="ltr"` configured in HTML.

### B. Social Metadata
- Open Graph tags on pages:
  - `og:title`
  - `og:description`
  - `og:type`
  - `og:url`
  - `og:locale`
- Homepage additionally includes:
  - `og:site_name`
  - Twitter card tags (`twitter:card`, `twitter:title`, `twitter:description`)

### C. Structured Data (Schema.org)
- Homepage includes `EducationalOrganization` JSON-LD schema.
  - Includes organization info, service area, contact language, course catalog.
- Homepage includes FAQ `FAQPage` JSON-LD schema.
- `faq.html` also contains FAQ schema implementation.

### D. Content SEO
- Keyword-targeted content for Qatar market across pages.
- Local intent targeting for cities: Doha, Al Wakrah, Al Khor, Lusail, Al Rayyan.
- Long-form informational sections supporting topical relevance.
- Internal linking between homepage, service pages, tutors, pricing, FAQ, and blog.
- Multiple conversion anchors (free trial, WhatsApp, contact paths).

## 5) Implemented Internal Linking Strategy

- Header navigation links to all major money/intent pages.
- Homepage cards deep-link to course detail pages.
- Footer links reinforce crawl paths to all major sections.
- FAQ answers and pricing area include contextual internal links.
- Blog is exposed in global navigation and footer.

## 6) Current SEO Gaps / Next Improvements (Recommended)

These are not missing features from development quality, but high-impact next steps:

- Add `sitemap.xml` and `robots.txt` files if not already deployed.
- Add image Open Graph tags (`og:image`, `twitter:image`) for richer sharing.
- Ensure every page has explicit single `h1` and image `alt` attributes where images exist.
- Add `BreadcrumbList` schema on service/tutor detail pages.
- Add `WebSite` schema with potential search action.
- Improve Core Web Vitals:
  - Optimize and lazy-load non-critical media.
  - Preload critical assets as needed.
- Replace placeholder WhatsApp values (`974XXXXXXXX`) with real production number.
- Connect forms to backend/CRM endpoint (currently front-end validation and UX flow only).
- Add analytics and conversion tracking (GA4, Search Console verification, Meta Pixel as needed).

## 7) Quick Project Status Summary

- Website pages and user-facing frontend are implemented and navigable.
- Interactive features are present via shared JavaScript.
- Strong baseline on-page SEO and schema are already in place.
- Project is ready for next phase:
  - technical SEO hardening,
  - performance optimization,
  - real lead capture integrations,
  - and ongoing content growth.

