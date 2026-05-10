import os
import re

base_dir = r"c:\Users\ALVIN THOMAS\Documents\Kudumbayogam\html-website"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

def extract_section(name):
    # Regex to match the section until the next <!-- \d+\.
    # Note: we use lookahead to not consume the next section marker
    pattern = r"(<!-- \d+\. " + name + r" SECTION -->.*?)(?=<!-- \d+\.)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1)
    
    # If it's the last section before footer
    pattern_end = r"(<!-- \d+\. " + name + r" SECTION -->.*?)(?=<!-- \d+\. FOOTER)"
    match = re.search(pattern_end, content, re.DOTALL)
    if match:
        return match.group(1)
    
    return ""

sections = {
    'HERO': extract_section('HERO'),
    'FAMILY STATISTICS': extract_section('FAMILY STATISTICS'),
    'ABOUT': extract_section('ABOUT'),
    'FAMILY TREE': extract_section('FAMILY TREE'),
    'EVENTS': extract_section('EVENTS'),
    'GALLERY': extract_section('GALLERY'),
    'ANNOUNCEMENTS': extract_section('ANNOUNCEMENTS'),
    'DONATIONS': extract_section('DONATIONS'),
    'CONTACT': extract_section('CONTACT'),
}

head_template = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Edathara Kudumbayogam</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        maroon: '#800000',
                        gold: '#FFD700',
                        darkgreen: '#006400',
                        cream: '#FFFDD0',
                        lightgold: '#FFE55C'
                    }},
                    fontFamily: {{
                        sans: ['Poppins', 'sans-serif'],
                        heading: ['Outfit', 'sans-serif'],
                    }},
                    boxShadow: {{
                        'glass': '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ font-family: 'Poppins', sans-serif; background-color: #faf9f6; }}
        h1, h2, h3, h4, h5, h6 {{ font-family: 'Outfit', sans-serif; }}
        .glass {{ background: rgba(255, 255, 255, 0.25); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.18); }}
        .glass-dark {{ background: rgba(0, 0, 0, 0.6); backdrop-filter: blur(8px); border: 1px solid rgba(255, 255, 255, 0.1); }}
        .glass-card {{ background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.3); box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1); }}
        .fade-in {{ opacity: 0; transform: translateY(20px); transition: opacity 0.8s ease-out, transform 0.8s ease-out; }}
        .fade-in.visible {{ opacity: 1; transform: translateY(0); }}
        .hover-lift {{ transition: transform 0.3s ease, box-shadow 0.3s ease; }}
        .hover-lift:hover {{ transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.15); }}
        .masonry {{ column-count: 1; column-gap: 1rem; }}
        @media (min-width: 640px) {{ .masonry {{ column-count: 2; }} }}
        @media (min-width: 1024px) {{ .masonry {{ column-count: 3; }} }}
        .masonry-item {{ break-inside: avoid; margin-bottom: 1rem; }}
        .no-scrollbar::-webkit-scrollbar {{ display: none; }}
        .no-scrollbar {{ -ms-overflow-style: none; scrollbar-width: none; }}
    </style>
</head>
<body class="text-gray-800 antialiased selection:bg-maroon selection:text-gold flex flex-col min-h-screen">
"""

navbar_home = """
    <!-- NAVBAR (HOME) -->
    <nav id="navbar" class="fixed w-full z-50 transition-all duration-300 bg-white/10 backdrop-blur-md border-b border-white/20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <div class="flex-shrink-0 flex items-center">
                    <a href="index.html" class="text-xl md:text-2xl font-heading font-bold text-white tracking-wider flex items-center gap-2 drop-shadow-md transition-colors" id="nav-brand">
                        <i class="fa-solid fa-leaf text-gold"></i>
                        EDATHARA <span class="hidden sm:inline">KUDUMBAYOGAM</span>
                    </a>
                </div>
                <div class="hidden lg:flex space-x-1 items-center">
                    <a href="index.html" class="nav-link text-white hover:text-gold px-3 py-2 rounded-md text-sm font-medium transition-colors">Home</a>
                    <a href="about.html" class="nav-link text-white hover:text-gold px-3 py-2 rounded-md text-sm font-medium transition-colors">About</a>
                    <a href="family-tree.html" class="nav-link text-white hover:text-gold px-3 py-2 rounded-md text-sm font-medium transition-colors">Family Tree</a>
                    <a href="events.html" class="nav-link text-white hover:text-gold px-3 py-2 rounded-md text-sm font-medium transition-colors">Events</a>
                    <a href="gallery.html" class="nav-link text-white hover:text-gold px-3 py-2 rounded-md text-sm font-medium transition-colors">Gallery</a>
                    <a href="announcements.html" class="nav-link text-white hover:text-gold px-3 py-2 rounded-md text-sm font-medium transition-colors">Announcements</a>
                    <a href="donations.html" class="nav-link text-white hover:text-gold px-3 py-2 rounded-md text-sm font-medium transition-colors">Donations</a>
                    <a href="contact.html" class="bg-maroon text-white hover:bg-maroon/90 px-5 py-2 rounded-full text-sm font-medium transition-all shadow-lg shadow-maroon/30 ml-2">Contact</a>
                </div>
                <div class="lg:hidden flex items-center">
                    <button id="mobile-menu-btn" class="text-white hover:text-gold focus:outline-none p-2">
                        <i class="fa-solid fa-bars text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
        <div id="mobile-menu" class="hidden lg:hidden bg-white/95 backdrop-blur-xl border-t border-gray-200 absolute w-full shadow-2xl">
            <div class="px-4 pt-2 pb-6 space-y-1">
                <a href="index.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">Home</a>
                <a href="about.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">About</a>
                <a href="family-tree.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">Family Tree</a>
                <a href="events.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">Events</a>
                <a href="gallery.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">Gallery</a>
                <a href="announcements.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">Announcements</a>
                <a href="donations.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">Donations</a>
                <a href="contact.html" class="mobile-link block px-3 py-3 text-base font-medium text-maroon font-bold hover:bg-cream rounded-md">Contact</a>
            </div>
        </div>
    </nav>
"""

navbar_inner = """
    <!-- NAVBAR (INNER) -->
    <nav id="navbar" class="fixed w-full z-50 transition-all duration-300 bg-white shadow-md border-b border-gray-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <div class="flex-shrink-0 flex items-center">
                    <a href="index.html" class="text-xl md:text-2xl font-heading font-bold text-maroon tracking-wider flex items-center gap-2 drop-shadow-sm transition-colors" id="nav-brand">
                        <i class="fa-solid fa-leaf text-gold"></i>
                        EDATHARA <span class="hidden sm:inline">KUDUMBAYOGAM</span>
                    </a>
                </div>
                <div class="hidden lg:flex space-x-1 items-center">
                    <a href="index.html" class="nav-link text-gray-700 hover:text-maroon px-3 py-2 rounded-md text-sm font-medium transition-colors">Home</a>
                    <a href="about.html" class="nav-link text-gray-700 hover:text-maroon px-3 py-2 rounded-md text-sm font-medium transition-colors">About</a>
                    <a href="family-tree.html" class="nav-link text-gray-700 hover:text-maroon px-3 py-2 rounded-md text-sm font-medium transition-colors">Family Tree</a>
                    <a href="events.html" class="nav-link text-gray-700 hover:text-maroon px-3 py-2 rounded-md text-sm font-medium transition-colors">Events</a>
                    <a href="gallery.html" class="nav-link text-gray-700 hover:text-maroon px-3 py-2 rounded-md text-sm font-medium transition-colors">Gallery</a>
                    <a href="announcements.html" class="nav-link text-gray-700 hover:text-maroon px-3 py-2 rounded-md text-sm font-medium transition-colors">Announcements</a>
                    <a href="donations.html" class="nav-link text-gray-700 hover:text-maroon px-3 py-2 rounded-md text-sm font-medium transition-colors">Donations</a>
                    <a href="contact.html" class="bg-maroon text-white hover:bg-maroon/90 px-5 py-2 rounded-full text-sm font-medium transition-all shadow-lg shadow-maroon/30 ml-2">Contact</a>
                </div>
                <div class="lg:hidden flex items-center">
                    <button id="mobile-menu-btn" class="text-gray-800 hover:text-maroon focus:outline-none p-2">
                        <i class="fa-solid fa-bars text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
        <div id="mobile-menu" class="hidden lg:hidden bg-white/95 backdrop-blur-xl border-t border-gray-200 absolute w-full shadow-2xl">
            <div class="px-4 pt-2 pb-6 space-y-1">
                <a href="index.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">Home</a>
                <a href="about.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">About</a>
                <a href="family-tree.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">Family Tree</a>
                <a href="events.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">Events</a>
                <a href="gallery.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">Gallery</a>
                <a href="announcements.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">Announcements</a>
                <a href="donations.html" class="mobile-link block px-3 py-3 text-base font-medium text-gray-800 hover:text-maroon hover:bg-cream rounded-md">Donations</a>
                <a href="contact.html" class="mobile-link block px-3 py-3 text-base font-medium text-maroon font-bold hover:bg-cream rounded-md">Contact</a>
            </div>
        </div>
    </nav>
"""

inner_header_template = """
    <!-- HEADER -->
    <div class="pt-32 pb-10 bg-cream">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center fade-in">
            <h1 class="text-4xl md:text-5xl font-heading font-bold text-gray-900">{title}</h1>
            <div class="w-24 h-1 bg-gold mx-auto mt-4 rounded-full"></div>
        </div>
    </div>
"""

footer_template = """
    <footer class="bg-gray-900 text-white pt-16 pb-8 border-t-4 border-maroon mt-auto">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-12">
                <div class="space-y-4">
                    <a href="index.html" class="text-2xl font-heading font-bold text-white tracking-wider flex items-center gap-2">
                        <i class="fa-solid fa-leaf text-gold"></i>
                        EDATHARA
                    </a>
                    <p class="text-gray-400 text-sm leading-relaxed">
                        Preserving the rich heritage and traditions of our ancestors while fostering unity among the present and future generations.
                    </p>
                    <div class="flex space-x-4 pt-2">
                        <a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-gray-300 hover:bg-maroon hover:text-white transition-all"><i class="fa-brands fa-facebook-f"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-gray-300 hover:bg-maroon hover:text-white transition-all"><i class="fa-brands fa-instagram"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-gray-300 hover:bg-maroon hover:text-white transition-all"><i class="fa-brands fa-youtube"></i></a>
                    </div>
                </div>
                <div>
                    <h4 class="text-lg font-heading font-bold mb-6 text-gold relative inline-block">
                        Quick Links
                        <span class="absolute bottom-0 left-0 w-1/2 h-0.5 bg-maroon -mb-2"></span>
                    </h4>
                    <ul class="space-y-3">
                        <li><a href="about.html" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2"><i class="fa-solid fa-angle-right text-xs text-maroon"></i> About Us</a></li>
                        <li><a href="family-tree.html" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2"><i class="fa-solid fa-angle-right text-xs text-maroon"></i> Family Tree</a></li>
                        <li><a href="events.html" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2"><i class="fa-solid fa-angle-right text-xs text-maroon"></i> Events</a></li>
                        <li><a href="gallery.html" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2"><i class="fa-solid fa-angle-right text-xs text-maroon"></i> Photo Gallery</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-lg font-heading font-bold mb-6 text-gold relative inline-block">
                        Support
                        <span class="absolute bottom-0 left-0 w-1/2 h-0.5 bg-maroon -mb-2"></span>
                    </h4>
                    <ul class="space-y-3">
                        <li><a href="announcements.html" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2"><i class="fa-solid fa-angle-right text-xs text-maroon"></i> Announcements</a></li>
                        <li><a href="donations.html" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2"><i class="fa-solid fa-angle-right text-xs text-maroon"></i> Make a Donation</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2"><i class="fa-solid fa-angle-right text-xs text-maroon"></i> Privacy Policy</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white transition-colors flex items-center gap-2"><i class="fa-solid fa-angle-right text-xs text-maroon"></i> Terms of Use</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-lg font-heading font-bold mb-6 text-gold relative inline-block">
                        Family Motto
                        <span class="absolute bottom-0 left-0 w-1/2 h-0.5 bg-maroon -mb-2"></span>
                    </h4>
                    <blockquote class="italic text-gray-400 border-l-4 border-maroon pl-4 py-1 mb-6">
                        "United we stand, preserving our past, building our future."
                    </blockquote>
                    <p class="text-sm text-gray-400 mb-3">Subscribe to directory updates:</p>
                    <div class="flex">
                        <input type="email" placeholder="Email address" class="bg-white/5 border border-white/10 px-4 py-2 rounded-l-lg w-full focus:outline-none focus:border-maroon text-sm text-white">
                        <button class="bg-maroon hover:bg-red-800 px-4 py-2 rounded-r-lg transition-colors text-sm font-medium">Subscribe</button>
                    </div>
                </div>
            </div>
            <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center text-sm text-gray-500">
                <p>&copy; 2026 Edathara Kudumbayogam. All rights reserved.</p>
                <p class="mt-2 md:mt-0">Designed with <i class="fa-solid fa-heart text-maroon mx-1"></i> for the Family</p>
            </div>
        </div>
    </footer>
    <script type="module">
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
        import {{ getAnalytics }} from "https://www.gstatic.com/firebasejs/10.8.1/firebase-analytics.js";
        const firebaseConfig = {{
            apiKey: "AIzaSyAZNCPmlff0BXHouCDT3i42Vv0RJ_goPLw",
            authDomain: "cypher-projects-6cce3.firebaseapp.com",
            databaseURL: "https://cypher-projects-6cce3-default-rtdb.firebaseio.com",
            projectId: "cypher-projects-6cce3",
            storageBucket: "cypher-projects-6cce3.firebasestorage.app",
            messagingSenderId: "454711938195",
            appId: "1:454711938195:web:876fb3046d091061251166",
            measurementId: "G-WJF8L0C0YX"
        }};
        const app = initializeApp(firebaseConfig);
        try {{ const analytics = getAnalytics(app); }} catch(e) {{}}
    </script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const btn = document.getElementById('mobile-menu-btn');
            const menu = document.getElementById('mobile-menu');
            if (btn && menu) {{
                btn.addEventListener('click', () => menu.classList.toggle('hidden'));
            }}
            
            const navbar = document.getElementById('navbar');
            const isHome = window.location.pathname.endsWith('index.html') || window.location.pathname.endsWith('/');
            if (isHome && navbar) {{
                const navBrand = document.getElementById('nav-brand');
                const navLinks = document.querySelectorAll('.nav-link');
                const menuBtn = document.getElementById('mobile-menu-btn');
                
                window.addEventListener('scroll', () => {{
                    if (window.scrollY > 50) {{
                        navbar.classList.remove('bg-white/10', 'text-white', 'border-white/20');
                        navbar.classList.add('bg-white', 'shadow-md', 'border-gray-100');
                        if (navBrand) {{
                            navBrand.classList.remove('text-white', 'drop-shadow-md');
                            navBrand.classList.add('text-maroon');
                        }}
                        navLinks.forEach(link => {{
                            link.classList.remove('text-white');
                            link.classList.add('text-gray-700');
                        }});
                        if (menuBtn) {{
                            menuBtn.classList.remove('text-white');
                            menuBtn.classList.add('text-gray-800');
                        }}
                    }} else {{
                        navbar.classList.add('bg-white/10', 'text-white', 'border-white/20');
                        navbar.classList.remove('bg-white', 'shadow-md', 'border-gray-100');
                        if (navBrand) {{
                            navBrand.classList.add('text-white', 'drop-shadow-md');
                            navBrand.classList.remove('text-maroon');
                        }}
                        navLinks.forEach(link => {{
                            link.classList.add('text-white');
                            link.classList.remove('text-gray-700');
                        }});
                        if (menuBtn) {{
                            menuBtn.classList.add('text-white');
                            menuBtn.classList.remove('text-gray-800');
                        }}
                    }}
                }});
            }}

            const observer = new IntersectionObserver((entries, obs) => {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) {{
                        entry.target.classList.add('visible');
                        if (entry.target.classList.contains('counter') && !entry.target.classList.contains('counted')) {{
                            animateCounter(entry.target);
                            entry.target.classList.add('counted');
                        }}
                        const counters = entry.target.querySelectorAll('.counter:not(.counted)');
                        counters.forEach(counter => {{
                            animateCounter(counter);
                            counter.classList.add('counted');
                        }});
                        obs.unobserve(entry.target);
                    }}
                }});
            }}, {{ root: null, rootMargin: '0px', threshold: 0.1 }});
            document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

            function animateCounter(el) {{
                const target = parseInt(el.getAttribute('data-target'));
                const duration = 2000;
                const step = target / (duration / 16);
                let current = 0;
                const updateCounter = () => {{
                    current += step;
                    if (current < target) {{
                        el.innerText = Math.ceil(current) + "+";
                        requestAnimationFrame(updateCounter);
                    }} else {{
                        el.innerText = target + "+";
                    }}
                }};
                updateCounter();
            }}
        }});
    </script>
</body>
</html>
"""

pages = [
    {
        'filename': 'index.html',
        'title': 'Home',
        'content': navbar_home + sections['HERO'] + sections['FAMILY STATISTICS']
    },
    {
        'filename': 'about.html',
        'title': 'About Us',
        'content': navbar_inner + inner_header_template.format(title="About Us") + sections['ABOUT']
    },
    {
        'filename': 'family-tree.html',
        'title': 'Family Tree',
        'content': navbar_inner + inner_header_template.format(title="Family Tree") + sections['FAMILY TREE']
    },
    {
        'filename': 'events.html',
        'title': 'Events',
        'content': navbar_inner + inner_header_template.format(title="Events") + sections['EVENTS']
    },
    {
        'filename': 'gallery.html',
        'title': 'Gallery',
        'content': navbar_inner + inner_header_template.format(title="Photo Gallery") + sections['GALLERY']
    },
    {
        'filename': 'announcements.html',
        'title': 'Announcements',
        'content': navbar_inner + inner_header_template.format(title="Announcements") + sections['ANNOUNCEMENTS']
    },
    {
        'filename': 'donations.html',
        'title': 'Donations',
        'content': navbar_inner + inner_header_template.format(title="Make a Donation") + sections['DONATIONS']
    },
    {
        'filename': 'contact.html',
        'title': 'Contact Us',
        'content': navbar_inner + inner_header_template.format(title="Contact Us") + sections['CONTACT']
    }
]

for page in pages:
    page_path = os.path.join(base_dir, page['filename'])
    html_content = head_template.format(title=page['title']) + page['content'] + footer_template
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Generated all pages successfully!")
