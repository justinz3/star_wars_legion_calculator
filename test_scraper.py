#!/usr/bin/env python3
"""Quick test of the scraping logic on a few sample units"""

import sys
sys.path.insert(0, '.')

from scrape_legion_units import LegionWikiScraper
import json

# Test on just a few units
test_units = [
    ("Darth Vader", "https://starwarslegion.fandom.com/wiki/Darth_Vader", "empire", "commander"),
    ("Stormtroopers", "https://starwarslegion.fandom.com/wiki/Stormtroopers", "empire", "corps"),
    ("General Grievous", "https://starwarslegion.fandom.com/wiki/General_Grievous", "separatist", "commander"),
    ("Luke Skywalker", "https://starwarslegion.fandom.com/wiki/Luke_Skywalker", "rebel", "commander"),
]

scraper = LegionWikiScraper(verbose=True, rate_limit=0.5)

print("\n" + "="*60)
print("Testing unit scraping on sample units")
print("="*60)

results = {}

for name, url, faction, rank in test_units:
    print(f"\nScraping: {name}")
    unit_data = scraper.scrape_unit(name, url, faction, rank)

    if unit_data:
        unit_id = name.lower().replace(' ', '').replace('-', '')
        results[unit_id] = unit_data

        print(f"✓ {name}:")
        print(f"  Size: {unit_data['size']}")
        print(f"  Defense: {unit_data['defense_die']}")
        print(f"  Weapons: {len(unit_data['weapons'])}")
        print(f"  Warnings: {unit_data['warnings']}")

# Save results
output_file = "test_scrape_results.json"
with open(output_file, 'w') as f:
    json.dump(results, f, indent=2)

print(f"\n✓ Saved results to {output_file}")
print(f"\nTotal warnings: {scraper.total_warnings}")
