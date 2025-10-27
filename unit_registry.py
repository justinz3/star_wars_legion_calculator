"""
Unit Registry - Organizes all units hierarchically by faction and type
"""

from republic_config import republic_config
from separatist_config import separatist_config
from empire_config import empire_config
from rebel_config import rebel_config
from mercenary_config import mercenary_config

# Define unit types in order
UNIT_TYPES = [
    'Commanders',
    'Operatives',
    'Corps',
    'Special Forces',
    'Support',
    'Heavy'
]

# Map rank names from JSON to GUI display names
RANK_TO_TYPE = {
    'commander': 'Commanders',
    'operative': 'Operatives',
    'corps': 'Corps',
    'special forces': 'Special Forces',
    'support': 'Support',
    'heavy': 'Heavy'
}

def get_units_by_faction():
    """
    Returns a hierarchical structure of all units organized by faction and type.
    Automatically loads all units from faction configs based on their rank.

    Returns:
        dict: {faction_name: {unit_type: [(unit_id, unit_name), ...]}}
    """
    from config import unit_config

    units_by_faction = {}

    # Define faction configs
    faction_configs = {
        'Republic': republic_config,
        'Separatist': separatist_config,
        'Empire': empire_config,
        'Rebel': rebel_config,
        'Mercenary': mercenary_config,
    }

    # Process each faction
    for faction_name, faction_config in faction_configs.items():
        units_by_faction[faction_name] = {}

        # Initialize empty lists for each unit type
        for unit_type in UNIT_TYPES:
            units_by_faction[faction_name][unit_type] = []

        # Iterate through all units in this faction's config
        for unit_id, unit_data in faction_config.items():
            # Get unit rank and convert to GUI type name
            rank = unit_data.get('rank', '').lower()
            unit_type = RANK_TO_TYPE.get(rank)

            if unit_type:
                unit_name = unit_data.get('name', unit_id)
                units_by_faction[faction_name][unit_type].append((unit_id, unit_name))
            else:
                # Unknown rank, skip or log warning
                print(f"Warning: Unknown rank '{rank}' for unit {unit_id}")

    return units_by_faction

def get_unit_weapons(unit_id):
    """
    Returns a list of weapon descriptions with dice profiles for a given unit.

    Args:
        unit_id: The unit's ID string

    Returns:
        list: List of weapon descriptions showing dice profile and keywords
    """
    from config import unit_config

    if unit_id not in unit_config:
        return []

    unit = unit_config[unit_id]
    weapons = unit.get('weapons', [])

    weapon_descriptions = []
    for i, weapon in enumerate(weapons):
        # Use weapon name if available, otherwise generate description
        if hasattr(weapon, 'name') and weapon.name:
            # Use weapon name with dice and keywords
            dice_counts = weapon.dice_counts
            white, black, red = dice_counts

            # Build dice profile string
            dice_parts = []
            if white > 0:
                dice_parts.append(f"{white}W")
            if black > 0:
                dice_parts.append(f"{black}B")
            if red > 0:
                dice_parts.append(f"{red}R")

            dice_str = "+".join(dice_parts) if dice_parts else "0 dice"

            # Get keywords
            keywords = []
            if weapon.impacts > 0:
                keywords.append(f"Impact {weapon.impacts}")
            if weapon.pierce > 0:
                keywords.append(f"Pierce {weapon.pierce}")
            if weapon.criticals > 0:
                keywords.append(f"Crit {weapon.criticals}")

            # Build description with name
            if keywords:
                desc = f"{weapon.name}: [{dice_str}] {', '.join(keywords)}"
            else:
                desc = f"{weapon.name}: [{dice_str}]"
        else:
            # Fallback to old format for weapons without names
            dice_counts = weapon.dice_counts
            white, black, red = dice_counts

            dice_parts = []
            if white > 0:
                dice_parts.append(f"{white}W")
            if black > 0:
                dice_parts.append(f"{black}B")
            if red > 0:
                dice_parts.append(f"{red}R")

            dice_str = "+".join(dice_parts) if dice_parts else "0 dice"

            keywords = []
            if weapon.impacts > 0:
                keywords.append(f"Impact {weapon.impacts}")
            if weapon.pierce > 0:
                keywords.append(f"Pierce {weapon.pierce}")
            if weapon.criticals > 0:
                keywords.append(f"Crit {weapon.criticals}")

            if keywords:
                desc = f"Weapon {i}: [{dice_str}] {', '.join(keywords)}"
            else:
                desc = f"Weapon {i}: [{dice_str}]"

        weapon_descriptions.append(desc)

    return weapon_descriptions
