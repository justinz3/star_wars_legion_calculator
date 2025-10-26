"""
Unit Registry - Organizes all units hierarchically by faction and type
"""

from republic_config import republic_config
from separatist_config import separatist_config
from empire_config import empire_config
from rebel_config import rebel_config

# Define unit types in order
UNIT_TYPES = [
    'Commanders',
    'Operatives',
    'Corps',
    'Special Forces',
    'Support',
    'Heavy'
]

# Manually map unit IDs to types based on the config files
# This could be automated by adding type info to configs, but manual mapping works for now
REPUBLIC_UNITS = {
    'Commanders': ['ob', 'anakin', 'yoda', 'rex', 'cody', 'ahsoka'],
    'Operatives': ['padme', 'r2d2'],
    'Corps': ['p1', 'p1z6', 'p1dc15', 'p2', 'p2z6', 'p2mortar'],
    'Special Forces': ['arc', 'wookiees'],
    'Support': ['barc', 'atrt', 'commandos', 'isp'],
    'Heavy': ['tx130'],
}

SEPARATIST_UNITS = {
    'Commanders': ['gg', 'dooku', 'tseries'],
    'Operatives': ['ventress', 'cadbane', 'maul'],
    'Corps': ['b1', 'b1e5', 'b1e6', 'b2', 'b2ha', 'b2acm', 'geonosians'],
    'Special Forces': ['bx', 'magnaguards'],
    'Support': ['dekas', 'spider', 'stap'],
    'Heavy': ['aat'],
}

EMPIRE_UNITS = {
    'Commanders': ['vader'],
    'Operatives': ['boba', 'ig88'],
    'Corps': ['storms', 'snows'],
    'Special Forces': ['deathtroopers', 'scouts'],
    'Support': [],
    'Heavy': ['atst'],
}

REBEL_UNITS = {
    'Commanders': ['luke', 'han', 'leia'],
    'Operatives': ['chewie'],
    'Corps': ['rebels'],
    'Special Forces': ['rebelcommandos'],
    'Support': [],
    'Heavy': [],
}

def get_units_by_faction():
    """
    Returns a hierarchical structure of all units organized by faction and type.

    Returns:
        dict: {faction_name: {unit_type: [(unit_id, unit_name), ...]}}
    """
    from config import unit_config

    units_by_faction = {}

    # Republic
    units_by_faction['Republic'] = {}
    for unit_type in UNIT_TYPES:
        units = []
        for unit_id in REPUBLIC_UNITS.get(unit_type, []):
            if unit_id in republic_config:
                unit_name = republic_config[unit_id]['name']
                units.append((unit_id, unit_name))
        units_by_faction['Republic'][unit_type] = units

    # Separatist
    units_by_faction['Separatist'] = {}
    for unit_type in UNIT_TYPES:
        units = []
        for unit_id in SEPARATIST_UNITS.get(unit_type, []):
            if unit_id in separatist_config:
                unit_name = separatist_config[unit_id]['name']
                units.append((unit_id, unit_name))
        units_by_faction['Separatist'][unit_type] = units

    # Empire
    units_by_faction['Empire'] = {}
    for unit_type in UNIT_TYPES:
        units = []
        for unit_id in EMPIRE_UNITS.get(unit_type, []):
            if unit_id in empire_config:
                unit_name = empire_config[unit_id]['name']
                units.append((unit_id, unit_name))
        units_by_faction['Empire'][unit_type] = units

    # Rebel
    units_by_faction['Rebel'] = {}
    for unit_type in UNIT_TYPES:
        units = []
        for unit_id in REBEL_UNITS.get(unit_type, []):
            if unit_id in rebel_config:
                unit_name = rebel_config[unit_id]['name']
                units.append((unit_id, unit_name))
        units_by_faction['Rebel'][unit_type] = units

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
        # Get dice counts [white, black, red]
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

        # Build description
        if keywords:
            desc = f"Weapon {i}: [{dice_str}] {', '.join(keywords)}"
        else:
            desc = f"Weapon {i}: [{dice_str}]"

        weapon_descriptions.append(desc)

    return weapon_descriptions
