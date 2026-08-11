import re

filepath = 'index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the img tag
old_img_str = '<img src="https://images.unsplash.com/photo-1601004696144-84511a54b387?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Online Quran Learning Placeholder" width="800" height="800" loading="eager" decoding="async" class="hero-v2-img">'

new_img_str = """<img
    src="assets/images/female-quran-teacher-hijab-hero.webp"
    alt="Female Quran Teacher conducting one-to-one online Quran class"
    class="hero-teacher-image"
    loading="eager"
    decoding="async"
    fetchpriority="high"
    width="560"
    height="700"
/>"""

content = content.replace(old_img_str, new_img_str)

# 2. Inject CSS before </head>
css_block = """
  <style>
    /* Scoped CSS for Hero Teacher Image */
    .hero-teacher-image {
      display: block;
      width: 100%;
      max-width: 540px;
      height: auto;
      object-fit: contain;
      margin-inline: auto;
    }
    
    .hero-v2-image-card {
      background: transparent !important;
      box-shadow: none !important;
      border: none !important;
      padding: 0 !important;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    @media (max-width: 1024px) {
      .hero-teacher-image {
        max-width: 420px;
      }
    }

    @media (max-width: 768px) {
      .hero-teacher-image {
        max-width: 300px;
        margin-top: 2rem;
      }
    }
  </style>
"""

content = content.replace('</head>', css_block + '</head>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero image inserted successfully.")
