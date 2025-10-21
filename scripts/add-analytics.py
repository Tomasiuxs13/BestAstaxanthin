#!/usr/bin/env python3
"""
Script to add Google Analytics 4 to all HTML files
Run this to add GA4 tracking to all pages
"""

import os
import re

# GA4 snippet to insert
GA4_SNIPPET = '''
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MYQXG1E7WY"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-MYQXG1E7WY');
    </script>
'''

def add_ga4_to_file(filepath):
    """Add GA4 snippet to a single HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if GA4 is already present
    if 'gtag' in content or 'G-MYQXG1E7WY' in content:
        print(f"✓ {filepath} already has GA4")
        return False

    # Find the canonical link or robots meta tag and insert after it
    if '<link rel="canonical"' in content:
        content = re.sub(
            r'(<link rel="canonical"[^>]*>)',
            r'\1' + GA4_SNIPPET,
            content,
            count=1
        )
        print(f"✓ Added GA4 to {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    elif '<meta name="robots"' in content:
        content = re.sub(
            r'(<meta name="robots"[^>]*>)',
            r'\1' + GA4_SNIPPET,
            content,
            count=1
        )
        print(f"✓ Added GA4 to {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    else:
        print(f"✗ Could not find insertion point in {filepath}")
        return False

def main():
    """Process all HTML files"""
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Directories to process
    directories = [
        '',  # root
        'guides',
        'reviews',
        'blog'
    ]

    total_processed = 0
    total_updated = 0

    for directory in directories:
        dir_path = os.path.join(base_dir, directory)
        if not os.path.exists(dir_path):
            continue

        for filename in os.listdir(dir_path):
            if filename.endswith('.html'):
                filepath = os.path.join(dir_path, filename)
                total_processed += 1
                if add_ga4_to_file(filepath):
                    total_updated += 1

    print(f"\n{'='*60}")
    print(f"Processed {total_processed} HTML files")
    print(f"Updated {total_updated} files with GA4")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
