#!/usr/bin/env python3
"""
Import scraped units from JSON into Python config files
"""

import json
import re
from pathlib import Path


def generate_unit_id(name):
    """Generate a unit_id from unit name"""
    # Remove special characters and convert to lowercase
    unit_id = re.sub(r'[^a-z0-9]', '', name.lower().replace(' ', '').replace('-', ''))
    return unit_id


def format_weapon(weapon):
    """Format weapon as Python code"""
    dice = weapon['dice']
    keywords = weapon.get('keywords', {})
    name = weapon.get('name', 'Unknown')

    # Build weapon arguments
    args = [str(dice)]

    # Handle supported keywords in consistent order
    # Note: blast, lethal, suppressive not yet implemented in Weapon class
    if keywords.get('impacts') or keywords.get('impact'):
        args.append(f"impacts={keywords.get('impacts') or keywords.get('impact')}")
    if keywords.get('criticals') or keywords.get('critical'):
        args.append(f"criticals={keywords.get('criticals') or keywords.get('critical')}")
    if keywords.get('pierce'):
        args.append(f"pierce={keywords['pierce']}")

    # Add weapon name as last parameter (use double quotes to handle apostrophes)
    args.append(f'name="{name}"')

    return f"Weapon({', '.join(args)})"


def format_unit(unit_id, unit_data):
    """Format unit data as Python config entry"""
    lines = []
    lines.append(f"    '{unit_id}': {{")
    lines.append(f"        Props.NAME: '{unit_data['name']}',")
    lines.append(f"        Props.RANK: '{unit_data.get('rank', 'unknown')}',")
    lines.append(f"        Props.SIZE: {unit_data['size']},")

    # Weapons
    if unit_data['weapons']:
        lines.append(f"        Props.WEAPONS: [")
        for weapon in unit_data['weapons']:
            comment = f"  # {weapon['name']}"
            lines.append(f"            {format_weapon(weapon)},{comment}")
        lines.append(f"        ],")
    else:
        lines.append(f"        Props.WEAPONS: [],")

    # Defense die
    defense = 'DefenseDice.RED' if unit_data['defense_die'] == 'red' else 'DefenseDice.WHITE'
    lines.append(f"        Props.SAVES: {defense},")

    # Surge conversions
    if unit_data.get('surge_hit'):
        lines.append(f"        Props.HIT_SURGES: UNLIMITED_TOKENS,")
    if unit_data.get('surge_crit'):
        lines.append(f"        Props.CRIT_SURGES: UNLIMITED_TOKENS,")
    if unit_data.get('surge_block'):
        lines.append(f"        Props.BLOCK_SURGES: UNLIMITED_TOKENS,")

    # Other properties
    if unit_data.get('armor', 0) > 0:
        lines.append(f"        Props.ARMOR: {unit_data['armor']},")
    if unit_data.get('shields', 0) > 0:
        lines.append(f"        Props.SHIELDS: {unit_data['shields']},")
    if unit_data.get('dodges', 0) > 0:
        lines.append(f"        Props.DODGES: {unit_data['dodges']},")
    if unit_data.get('cover_improvement', 0) > 0:
        lines.append(f"        Props.COVER_IMPROVEMENT: {unit_data['cover_improvement']},")
    if unit_data.get('impervious'):
        lines.append(f"        Props.IMPERVIOUS: True,")
    if unit_data.get('immune_pierce'):
        lines.append(f"        Props.IMMUNE_PIERCE: True,")

    # Add comment for warnings if any
    if unit_data.get('warnings'):
        warnings_str = ", ".join(unit_data['warnings'][:2])  # Limit to first 2
        lines.append(f"        # Warnings: {warnings_str}")

    lines.append(f"    }},")

    return '\n'.join(lines)


def update_config_file(config_path, json_path, faction_name):
    """Update a config file with data from JSON"""
    print(f"\n{'='*60}")
    print(f"Updating {config_path.name}")
    print(f"{'='*60}")

    # Load JSON data
    with open(json_path) as f:
        json_data = json.load(f)

    # Read existing config
    with open(config_path) as f:
        config_content = f.read()

    # Find existing unit IDs
    existing_ids = set(re.findall(r"'([a-z0-9]+)':\s*{", config_content))

    # Generate new units
    new_units = []
    for unit_id, unit_data in json_data.items():
        if unit_id not in existing_ids:
            new_units.append((unit_id, unit_data))

    if not new_units:
        print(f"  No new units to add (all {len(json_data)} units already exist)")
        return

    print(f"  Found {len(new_units)} new units to add (out of {len(json_data)} total)")

    # Find the closing brace of the config dict
    last_brace_pos = config_content.rfind('}')
    if last_brace_pos == -1:
        print("  ERROR: Could not find closing brace")
        return

    # Insert new units before the closing brace
    new_content = config_content[:last_brace_pos]

    # Add newline if needed
    if not new_content.rstrip().endswith(','):
        new_content = new_content.rstrip() + '\n'

    # Group units by rank for organization
    ranks = {}
    for unit_id, unit_data in new_units:
        rank = unit_data.get('rank', 'unknown')
        if rank not in ranks:
            ranks[rank] = []
        ranks[rank].append((unit_id, unit_data))

    # Add units organized by rank
    for rank in ['commander', 'operative', 'corps', 'special forces', 'support', 'heavy']:
        if rank in ranks:
            new_content += f"\n    # ===== {rank.upper()} =====\n"
            for unit_id, unit_data in ranks[rank]:
                print(f"  + {unit_data['name']} ({rank})")
                new_content += format_unit(unit_id, unit_data) + '\n'

    # Add any remaining ranks
    for rank in ranks:
        if rank not in ['commander', 'operative', 'corps', 'special forces', 'support', 'heavy']:
            new_content += f"\n    # ===== {rank.upper()} =====\n"
            for unit_id, unit_data in ranks[rank]:
                print(f"  + {unit_data['name']} ({rank})")
                new_content += format_unit(unit_id, unit_data) + '\n'

    new_content += '}\n'

    # Write updated config
    with open(config_path, 'w') as f:
        f.write(new_content)

    print(f"  ✓ Updated {config_path.name}")


def main():
    base_dir = Path(__file__).parent

    # Map JSON files to config files
    updates = [
        ('empire_units.json', 'empire_config.py', 'empire'),
        ('rebel_units.json', 'rebel_config.py', 'rebel'),
        ('republic_units.json', 'republic_config.py', 'republic'),
        ('separatist_units.json', 'separatist_config.py', 'separatist'),
        ('mercenary_units.json', 'mercenary_config.py', 'mercenary'),
    ]

    for json_file, config_file, faction in updates:
        json_path = base_dir / json_file
        config_path = base_dir / config_file

        if not json_path.exists():
            print(f"WARNING: {json_file} not found, skipping")
            continue

        if not config_path.exists():
            print(f"WARNING: {config_file} not found, skipping")
            continue

        update_config_file(config_path, json_path, faction)

    print(f"\n{'='*60}")
    print("Import complete!")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
