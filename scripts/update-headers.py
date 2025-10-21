#!/usr/bin/env python3
"""Update all page headers to match the homepage header structure."""

import re
import os
from pathlib import Path

# Standard header from homepage (for blog pages - they need ../ paths)
BLOG_HEADER = '''    <!-- Skip to Content Link (Accessibility) -->
    <a href="#main-content" class="skip-link">Skip to main content</a>

    <!-- Header / Navigation -->
    <header class="header" role="banner">
        <nav class="nav-container" role="navigation" aria-label="Main navigation">
            <div class="logo">
                <a href="/" aria-label="Best Astaxanthin Home">
                    <i class="fas fa-flask"></i>
                    <span>Best Astaxanthin</span>
                </a>
            </div>

            <button class="menu-toggle" aria-label="Toggle navigation menu" aria-expanded="false">
                <span class="hamburger"></span>
            </button>

            <ul class="nav-menu" role="menubar">
                <li role="none"><a href="../index.html#top-10" role="menuitem">Top 10</a></li>
                <li role="none"><a href="../index.html#comparison" role="menuitem">Compare</a></li>
                <li class="dropdown" role="none">
                    <a href="../guides" role="menuitem" class="dropdown-toggle">Guides <i class="fas fa-chevron-down"></i></a>
                    <ul class="dropdown-menu" role="menu">
                        <li role="none"><a href="../guides/what-is-astaxanthin.html" role="menuitem">What is Astaxanthin?</a></li>
                        <li role="none"><a href="../guides/benefits.html" role="menuitem">Benefits Guide</a></li>
                        <li role="none"><a href="../guides/dosage.html" role="menuitem">Dosage Guide</a></li>
                        <li role="none"><a href="../guides/buying-guide.html" role="menuitem">Buying Guide</a></li>
                    </ul>
                </li>
                <li class="dropdown" role="none">
                    <a href="../reviews" role="menuitem" class="dropdown-toggle">Reviews <i class="fas fa-chevron-down"></i></a>
                    <ul class="dropdown-menu" role="menu">
                        <li role="none"><a href="../reviews/sports-research-astaxanthin-review.html" role="menuitem">#1: Sports Research</a></li>
                        <li role="none"><a href="../reviews/life-extension-astaxanthin-review.html" role="menuitem">#2: Life Extension</a></li>
                        <li role="none"><a href="../reviews/nutrex-hawaii-bioastin-review.html" role="menuitem">#3: NUTREX HAWAII BioAstin</a></li>
                        <li role="none"><a href="../reviews/microingredients-astaxanthin-review.html" role="menuitem">#4: Microingredients</a></li>
                        <li role="none"><a href="../reviews/double-wood-astaxanthin-review.html" role="menuitem">#5: Double Wood</a></li>
                        <li role="none"><a href="../reviews/nutricost-astaxanthin-review.html" role="menuitem">#6: Nutricost</a></li>
                        <li role="none"><a href="../reviews/vivonu-astaxanthin-review.html" role="menuitem">#7: Vivonu</a></li>
                        <li role="none"><a href="../reviews/now-foods-astaxanthin-review.html" role="menuitem">#8: NOW Foods</a></li>
                        <li role="none"><a href="../reviews/naturebell-astaxanthin-review.html" role="menuitem">#9: NatureBell</a></li>
                        <li role="none"><a href="../reviews/bulksupplements-astaxanthin-review.html" role="menuitem">#10: BulkSupplements</a></li>
                    </ul>
                </li>
                <li role="none"><a href="../about.html" role="menuitem">About</a></li>
                <li role="none"><a href="../contact.html" role="menuitem">Contact</a></li>
            </ul>
        </nav>
    </header>
'''

def update_blog_page(filepath):
    """Replace header in blog page with standard header."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find <body> tag
    body_match = re.search(r'<body>\s*', content)
    if not body_match:
        return False

    body_end = body_match.end()

    # Find the </header> tag
    header_match = re.search(r'</header>\s*', content[body_end:])
    if not header_match:
        return False

    # Calculate position after </header>
    header_end = body_end + header_match.end()

    # Build new content: everything before <body>, <body> tag, new header, everything after </header>
    new_content = content[:body_end] + '\n' + BLOG_HEADER + '\n' + content[header_end:]

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    """Update headers in all blog and guide pages."""
    blog_dir = Path('blog')
    guides_dir = Path('guides')

    blog_pages = [
        'astaxanthin-exercise-recovery.html',
        'astaxanthin-eye-health.html',
        'astaxanthin-for-skin.html',
        'best-time-to-take-astaxanthin.html',
        'index.html',
        'is-astaxanthin-worth-it.html'
    ]

    guide_pages = [
        'natural-vs-synthetic.html',
        'side-effects.html'
    ]

    updated = 0
    total = len(blog_pages) + len(guide_pages)

    print("Updating blog pages...")
    for page in blog_pages:
        filepath = blog_dir / page
        if filepath.exists():
            if update_blog_page(filepath):
                print(f"  Updated: {filepath}")
                updated += 1
            else:
                print(f"  No changes: {filepath}")
        else:
            print(f"  Not found: {filepath}")

    print("\nUpdating guide pages...")
    for page in guide_pages:
        filepath = guides_dir / page
        if filepath.exists():
            if update_blog_page(filepath):
                print(f"  Updated: {filepath}")
                updated += 1
            else:
                print(f"  No changes: {filepath}")
        else:
            print(f"  Not found: {filepath}")

    print(f"\nTotal updated: {updated}/{total}")

if __name__ == '__main__':
    main()
