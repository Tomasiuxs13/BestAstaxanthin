#!/usr/bin/env python3
"""Update affiliate links for all astaxanthin products."""

from pathlib import Path
import re

# Mapping of old links to new links
AFFILIATE_LINKS = {
    # Sports Research
    "https://amzn.to/4hnuA32": "https://click.linksynergy.com/link?id=BCyqzXXusRs&offerid=1663588.534126176833866128105820&type=2&murl=https%3a%2f%2fstore.sportsresearch.com%2fproducts%2fastaxanthin-12mg-60-veggie-softgels%3fvariant%3d52872601207155",
    "amzn.to/4hnuA32": "https://click.linksynergy.com/link?id=BCyqzXXusRs&offerid=1663588.534126176833866128105820&type=2&murl=https%3a%2f%2fstore.sportsresearch.com%2fproducts%2fastaxanthin-12mg-60-veggie-softgels%3fvariant%3d52872601207155",
    
    # Life Extension
    "https://amzn.to/496JLva": "https://amzn.to/3X5WQhb",
    "amzn.to/496JLva": "amzn.to/3X5WQhb",
    
    # Nutrex Hawaii
    "https://amzn.to/46T6I3E": "https://amzn.to/48nQu35",
    "amzn.to/46T6I3E": "amzn.to/48nQu35",
    
    # Microingredients
    "https://amzn.to/48tkT0t": "https://pboost.me/HLhk8cX9",
    "amzn.to/48tkT0t": "pboost.me/HLhk8cX9",
    
    # Double Wood
    "https://amzn.to/48taNg6": "https://amzn.to/49pbNSU",
    "amzn.to/48taNg6": "amzn.to/49pbNSU",
    
    # Nutricost
    "https://amzn.to/4qdljyn": "https://amzn.to/49pxsdL",
    "amzn.to/4qdljyn": "amzn.to/49pxsdL",
    
    # Vivonu
    "https://amzn.to/3W9BnDG": "https://amzn.to/43GWUI1",
    "amzn.to/3W9BnDG": "amzn.to/43GWUI1",
    
    # Now Foods
    "https://amzn.to/4nRruGL": "https://amzn.to/4oPJAcE",
    "amzn.to/4nRruGL": "amzn.to/4oPJAcE",
    
    # Naturebell
    "https://amzn.to/42IGTAK": "https://amzn.to/3X5X5c5",
    "amzn.to/42IGTAK": "amzn.to/3X5X5c5",
    
    # Bulk Supplements
    "https://amzn.to/4hkYC7C": "https://amzn.to/48bR2rF",
    "amzn.to/4hkYC7C": "amzn.to/48bR2rF",
}

def update_affiliate_links(filepath):
    """Update affiliate links in HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    updated = False
    
    # Replace all old links with new links
    for old_link, new_link in AFFILIATE_LINKS.items():
        if old_link in content:
            content = content.replace(old_link, new_link)
            updated = True
    
    if updated and content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Update affiliate links in all HTML files."""
    base_dir = Path('.')
    html_files = list(base_dir.rglob('*.html'))
    
    updated = 0
    skipped = 0
    
    for html_file in html_files:
        try:
            if update_affiliate_links(html_file):
                print(f"Updated: {html_file}")
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"Error with {html_file}: {e}")
    
    print(f"\nTotal updated: {updated}")
    print(f"Total skipped: {skipped}")

if __name__ == '__main__':
    main()

