#!/usr/bin/env python3
"""Debug script to examine HTML structure of upgrade pages"""

import requests
from bs4 import BeautifulSoup

url = "https://starwarslegion.fandom.com/wiki/Super_Commando_Jetpack_Rockets"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all dice images
print("="*60)
print("SEARCHING FOR DICE IMAGES")
print("="*60)

for img in soup.find_all('img'):
    img_name = img.get('data-image-name', '').lower()
    if 'attack_die' in img_name or 'die' in img_name:
        print(f"\nFound dice image: {img.get('data-image-name')}")

        # The image is in an <a> tag, so check the <a> tag's siblings
        a_tag = img.parent
        print(f"Image parent (<a> tag): {a_tag.name}")

        # Check the <a> tag's siblings
        print("\n<a> tag's next siblings:")
        for i, sibling in enumerate(a_tag.next_siblings):
            if i >= 10:
                break
            sibling_text = str(sibling)[:200] if sibling else "None"
            print(f"  {i}: {repr(sibling_text)}")

        # Check grandparent
        grandparent = a_tag.parent
        print(f"\nGrandparent: {grandparent.name} - {grandparent.get('class', [])}")
        print(f"Grandparent HTML:\n{grandparent}")
        print("\n" + "-"*60)

# Also look for the full paragraph containing weapon info
print("\n" + "="*60)
print("SEARCHING FOR WEAPON INFO PARAGRAPH")
print("="*60)

content = soup.find('div', {'class': 'mw-parser-output'})
if content:
    # Find paragraphs that contain "Range:"
    for p in content.find_all('p'):
        if 'Range:' in p.get_text():
            print(f"\nFound paragraph with Range:")
            print(p)
            print(f"\nText: {p.get_text()}")
