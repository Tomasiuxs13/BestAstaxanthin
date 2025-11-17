#!/usr/bin/env python3
"""Add fo-verify meta tag to all HTML files."""

import re
from pathlib import Path

VERIFICATION_META = '    <meta name="fo-verify" content="567d86b3-91fe-4468-a318-f2cdef453c5e" />'

def add_verification_meta(filepath):
    """Add fo-verify meta tag to HTML file if not already present."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Check if already present
    content_str = ''.join(lines)
    if 'fo-verify' in content_str:
        return False
    
    # Find the line to insert after
    insert_line = None
    for i, line in enumerate(lines):
        # Try to find Google verification meta tag
        if 'google-site-verification' in line:
            insert_line = i
            break
        # Or robots meta tag
        elif 'name="robots"' in line and insert_line is None:
            insert_line = i
        # Or canonical link (fallback)
        elif 'rel="canonical"' in line and insert_line is None:
            insert_line = i
    
    if insert_line is not None:
        # Insert after the found line
        lines.insert(insert_line + 1, VERIFICATION_META + '\n')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        return True
    
    return False

def main():
    """Add verification meta tag to all HTML files."""
    base_dir = Path('.')
    html_files = list(base_dir.rglob('*.html'))
    
    updated = 0
    skipped = 0
    failed = []
    
    for html_file in html_files:
        try:
            if add_verification_meta(html_file):
                print(f"Updated: {html_file}")
                updated += 1
            else:
                content = html_file.read_text(encoding='utf-8')
                if 'fo-verify' in content:
                    print(f"Already has verification: {html_file}")
                    skipped += 1
                else:
                    failed.append(html_file)
        except Exception as e:
            print(f"Error with {html_file}: {e}")
            failed.append(html_file)
    
    print(f"\nTotal updated: {updated}")
    print(f"Total skipped: {skipped}")
    if failed:
        print(f"Failed to update: {len(failed)}")
        for f in failed[:5]:  # Show first 5
            print(f"  {f}")

if __name__ == '__main__':
    main()
