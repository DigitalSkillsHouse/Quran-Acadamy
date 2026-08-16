/* ===== Qurana Academy — Main JavaScript ===== */
(function(){
  'use strict';

  /* ---------- Header Scroll + Info Bar ---------- */
  const header = document.querySelector('.header');
  const topInfoBar = document.querySelector('.top-info-bar');
  const scrollThreshold = 60;
  function handleScroll(){
    if(!header) return;
    const scrolled = window.scrollY > scrollThreshold;
    header.classList.toggle('scrolled', scrolled);
    // Hide info bar on scroll and move header up
    if(topInfoBar){
      topInfoBar.classList.toggle('hidden', scrolled);
      header.style.top = scrolled ? '0' : '';
    }
    const btt = document.querySelector('.back-to-top');
    if(btt) btt.classList.toggle('show', window.scrollY > 400);
  }
  window.addEventListener('scroll', handleScroll, {passive:true});

  /* ---------- Mobile Nav ---------- */
  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');
  const overlay = document.querySelector('.mobile-overlay');

  function toggleNav(){
    hamburger?.classList.toggle('active');
    navLinks?.classList.toggle('open');
    overlay?.classList.toggle('show');
    const isOpen = navLinks?.classList.contains('open');
    if (hamburger) hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    document.body.style.overflow = isOpen ? 'hidden' : '';
  }
  hamburger?.addEventListener('click', toggleNav);
  overlay?.addEventListener('click', toggleNav);
  navLinks?.querySelectorAll('a:not(.has-dropdown > a)').forEach(function(link){
    link.addEventListener('click', function(){
      if(navLinks.classList.contains('open')) toggleNav();
    });
  });

  /* ---------- FAQ Accordion ---------- */
  document.querySelectorAll('.faq-question').forEach(function(btn){
    btn.addEventListener('click', function(){
      const item = this.closest('.faq-item');
      const answer = item.querySelector('.faq-answer');
      const isActive = item.classList.contains('active');
      document.querySelectorAll('.faq-item.active').forEach(function(el){
        el.classList.remove('active');
        el.querySelector('.faq-answer').style.maxHeight = null;
      });
      if(!isActive){
        item.classList.add('active');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  /* ---------- Testimonials Slider ---------- */
  const track = document.querySelector('.testimonials-track');
  const prevBtn = document.querySelector('.slider-prev');
  const nextBtn = document.querySelector('.slider-next');
  if(track && prevBtn && nextBtn){
    let idx = 0;
    function getPerView(){
      if(window.innerWidth >= 1024) return 3;
      if(window.innerWidth >= 768) return 2;
      return 1;
    }
    function slideCount(){
      return track.children.length;
    }
    function update(){
      const perView = getPerView();
      const maxIdx = Math.max(0, slideCount() - perView);
      if(idx > maxIdx) idx = maxIdx;
      const pct = (100 / slideCount()) * idx;
      track.style.transform = 'translateX(-' + pct + '%)';
    }
    prevBtn.addEventListener('click', function(){ if(idx > 0){ idx--; update(); } });
    nextBtn.addEventListener('click', function(){
      const perView = getPerView();
      if(idx < slideCount() - perView){ idx++; update(); }
    });
    window.addEventListener('resize', update);
  }

  /* ---------- Modal ---------- */
  const modal = document.querySelector('.modal-overlay');
  const modalClose = document.querySelector('.modal-close');
  const openModalBtns = document.querySelectorAll('[data-modal="open"]');

  function openModal(){ modal?.classList.add('active'); document.body.style.overflow = 'hidden'; }
  function closeModal(){ modal?.classList.remove('active'); document.body.style.overflow = ''; }

  openModalBtns.forEach(function(b){ b.addEventListener('click', function(e){ e.preventDefault(); openModal(); }); });
  modalClose?.addEventListener('click', closeModal);
  modal?.addEventListener('click', function(e){ if(e.target === modal) closeModal(); });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') closeModal(); });

  if(modal && !sessionStorage.getItem('modalShown')){
    setTimeout(openModal, 4000);
    sessionStorage.setItem('modalShown', '1');
  }

  /* ---------- Contact Form Validation ---------- */
  const contactForm = document.getElementById('contactForm');
  if(contactForm){
    contactForm.addEventListener('submit', function(e){
      e.preventDefault();
      let valid = true;
      contactForm.querySelectorAll('[required]').forEach(function(field){
        const group = field.closest('.form-group');
        if(!field.value.trim()){
          group?.classList.add('error');
          valid = false;
        } else {
          group?.classList.remove('error');
        }
        if(field.type === 'email' && field.value){
          const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if(!emailRe.test(field.value)){
            group?.classList.add('error');
            valid = false;
          }
        }
      });
      if(valid){
        const btn = contactForm.querySelector('button[type="submit"]');
        if(btn){
          btn.textContent = 'Message Sent ✓';
          btn.disabled = true;
          setTimeout(function(){
            btn.textContent = 'Send Message';
            btn.disabled = false;
            contactForm.reset();
          }, 3000);
        }
      }
    });
    contactForm.querySelectorAll('[required]').forEach(function(field){
      field.addEventListener('input', function(){
        this.closest('.form-group')?.classList.remove('error');
      });
    });
  }

  /* ---------- Modal Form Validation ---------- */
  const trialForm = document.getElementById('trialForm');
  if(trialForm){
    trialForm.addEventListener('submit', function(e){
      e.preventDefault();
      let valid = true;
      trialForm.querySelectorAll('[required]').forEach(function(field){
        const group = field.closest('.form-group');
        if(!field.value.trim()){ group?.classList.add('error'); valid = false; }
        else { group?.classList.remove('error'); }
      });
      if(valid){
        const btn = trialForm.querySelector('button[type="submit"]');
        if(btn){
          btn.textContent = 'Submitted ✓';
          btn.disabled = true;
          setTimeout(closeModal, 2000);
        }
      }
    });
  }

  /* ---------- Scroll Animations ---------- */
  function animateOnScroll(){
    document.querySelectorAll('.fade-in,.fade-in-left,.fade-in-right').forEach(function(el){
      const rect = el.getBoundingClientRect();
      if(rect.top < window.innerHeight - 60){
        requestAnimationFrame(() => el.classList.add('visible'));
      }
    });
  }
  window.addEventListener('scroll', animateOnScroll, {passive:true});
  window.addEventListener('load', animateOnScroll);

  /* ---------- Back to Top ---------- */
  document.querySelector('.back-to-top')?.addEventListener('click', function(e){
    e.preventDefault();
    window.scrollTo({top:0, behavior:'smooth'});
  });

  /* ---------- Active Nav Link ---------- */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(function(link){
    const href = link.getAttribute('href');
    if(href && (href === currentPage || href.endsWith('/' + currentPage))){
      link.classList.add('active');
    }
  });

  /* ---------- Smooth Scroll for Anchor Links ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click', function(e){
      const target = document.querySelector(this.getAttribute('href'));
      if(target){
        e.preventDefault();
        target.scrollIntoView({behavior:'smooth', block:'start'});
      }
    });
  });

})();

// --- LEADS TRACKING SYSTEM ---
document.addEventListener('DOMContentLoaded', () => {
    // 1. Form tracking
    const forms = document.querySelectorAll('form[action="thank-you.html"]');
    forms.forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = form.querySelector('button[type="submit"]') || form.querySelector('input[type="submit"]');
            if (btn) btn.disabled = true;

            try {
                const formData = new FormData(form);
                const data = {
                    event_type: 'FORM_SUBMISSION',
                    name: formData.get('name') || formData.get('parentName') || formData.get('studentName') || '',
                    email: formData.get('email') || '',
                    phone: formData.get('phone') || formData.get('whatsappNumber') || '',
                    course: formData.get('course') || '',
                    message: formData.get('message') || formData.get('preferredTime') || '',
                    source_url: window.location.href,
                    referrer: document.referrer
                };

                const res = await fetch('/api/track.php', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                });
                const result = await res.json();
                if (res.ok && result.success) {
                    window.location.href = form.action || 'thank-you.html';
                } else {
                    alert('Submission failed. Please try again or contact us via WhatsApp.');
                    if (btn) btn.disabled = false;
                }
            } catch (error) {
                console.error(error);
                alert('Connection error. Please try again or contact us via WhatsApp.');
                if (btn) btn.disabled = false;
            }
        });
    });

    // 2. Phone / WhatsApp Click Tracking
    const trackClick = (eventType) => {
        const data = {
            event_type: eventType,
            source_url: window.location.href,
            referrer: document.referrer
        };
        // Use sendBeacon so it doesn't block navigation
        if (navigator.sendBeacon) {
            navigator.sendBeacon('/api/track.php', JSON.stringify(data));
        } else {
            fetch('/api/track.php', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data),
                keepalive: true
            }).catch(() => {});
        }
    };

    document.querySelectorAll('a[href^="tel:"]').forEach(a => {
        a.addEventListener('click', () => trackClick('PHONE_CLICK'));
    });

    document.querySelectorAll('a[href^="https://wa.me"], a[href^="https://api.whatsapp.com"]').forEach(a => {
        a.addEventListener('click', () => trackClick('WHATSAPP_CLICK'));
    });
});
