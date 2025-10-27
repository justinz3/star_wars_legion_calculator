#!/usr/bin/env python3
"""Test upgrade scraping on a single unit"""

from scrape_legion_units import LegionWikiScraper
import json

scraper = LegionWikiScraper(verbose=True, rate_limit=0.5)

# Test on Mandalorian Super Commandos (known to have upgrades)
unit = scraper.scrape_unit(
    "Mandalorian Super Commandos",
    "https://starwarslegion.fandom.com/wiki/Mandalorian_Super_Commandos",
    "mercenary",
    "special forces"
)

print("\n" + "="*60)
print("UNIT DATA")
print("="*60)
print(f"Name: {unit['name']}")
print(f"Size: {unit['size']}")
print(f"Base weapons: {len(unit['weapons'])}")
for w in unit['weapons']:
    print(f"  - {w['name']}: {w['dice']} {w.get('keywords', {})}")

print(f"\nUpgrades found: {len(unit.get('upgrades', []))}")
for u in unit.get('upgrades', []):
    print(f"  - {u['name']}")

# Now scrape the upgrades
if unit.get('upgrades'):
    print("\n" + "="*60)
    print("SCRAPING UPGRADES")
    print("="*60)
    for upgrade in unit['upgrades']:
        if upgrade.get('url'):
            weapon = scraper.scrape_upgrade(upgrade['name'], upgrade['url'])
            if weapon:
                print(f"\n{weapon['name']}:")
                print(f"  Dice: {weapon['dice']}")
                print(f"  Keywords: {weapon.get('keywords', {})}")
                if weapon.get('warnings'):
                    print(f"  Warnings: {weapon['warnings']}")

                # Only add upgrades that have actual weapons (non-zero dice)
                if weapon['dice'] != [0, 0, 0]:
                    unit['weapons'].append(weapon)
                else:
                    print("  → Skipping (no weapon dice, likely personnel/gear upgrade)")

print("\n" + "="*60)
print("FINAL WEAPON COUNT")
print("="*60)
print(f"Total weapons (with upgrades): {len(unit['weapons'])}")
for w in unit['weapons']:
    print(f"  - {w['name']}: {w['dice']}")

# Save to JSON
with open('test_unit_with_upgrades.json', 'w') as f:
    json.dump({unit['name'].lower().replace(' ', ''): unit}, f, indent=2)

print("\n✓ Saved to test_unit_with_upgrades.json")
