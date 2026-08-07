import os

css_addition = """
/* Header CTA Update */
.nav-cta,
.header-cta,
.header .btn-primary {
    color: #ffffff !important;
}

.nav-cta:hover,
.header-cta:hover,
.header .btn-primary:hover {
    background: #C8A24D !important;
    color: #0F5132 !important;
    border-color: #C8A24D !important;
    transition: all 0.3s ease;
    cursor: pointer;
    box-shadow: 0 8px 20px rgba(15,81,50,.15);
}
"""

css_files = [
    'assets/css/style.css',
    'assets/css/style.min.css'
]

for filepath in css_files:
    if os.path.exists(filepath):
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(css_addition)
        print(f"Appended CTA CSS to {filepath}")
    else:
        print(f"File not found: {filepath}")
