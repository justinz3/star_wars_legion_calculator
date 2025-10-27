from unit_config_properties import UnitProperties as Props
from dice import DefenseDice
from weapon import Weapon
from constants import UNLIMITED_TOKENS

# NOTE: Most mercenary units (Bossk, Cad Bane, IG-88, Boba Fett, etc.)
# are already defined in other faction configs and can be used as mercs.
# The Shadow Collective faction itself is very limited.

mercenary_config = {

    # ===== COMMANDER =====
    'blacksunvigo': {
        Props.NAME: 'Black Sun Vigo',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 3, 0], name="Martial Arts"),  # Martial Arts
            Weapon([2, 2, 0], name="Vigo's BH-4 Double Blaster"),  # Vigo's BH-4 Double Blaster
            Weapon([0, 0, 0], name=""),  # 
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found, No dice pool found
    },
    'garsaxon': {
        Props.NAME: 'Gar Saxon',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 2], name="Advanced Combat Training"),  # Advanced Combat Training
            Weapon([0, 0, 0], name=""),  # 
            Weapon([1, 2, 1], pierce=1, name="Saxon's Westar-35 Blaster Pistol"),  # Saxon's Westar-35 Blaster Pistol
            Weapon([1, 1, 1], name="Saxon's Galar-90 Rifle"),  # Saxon's Galar-90 Rifle
            Weapon([0, 0, 3], impacts=2, name="Saxon's Z-3X Jetpack Rockets"),  # Saxon's Z-3X Jetpack Rockets
            Weapon([1, 1, 0], name="Saxon's ZX Flame Projector"),  # Saxon's ZX Flame Projector
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.IMPERVIOUS: True,
        # Warnings: No dice pool found, No range found
    },
    'pykesyndicatecapo': {
        Props.NAME: 'Pyke Syndicate Capo',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 3, 0], name="Capo's P13 Long Blaster"),  # Capo's P13 Long Blaster
            Weapon([0, 0, 0], name=""),  # 
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.DODGES: 1,
        # Warnings: No range found, No dice pool found
    },

    # ===== OPERATIVE =====
    'bossk': {
        Props.NAME: 'Bossk',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 2, 1], pierce=1, name="Frenzy"),  # Frenzy
            Weapon([4, 0, 1], pierce=1, name="Relby-v10 Mortar Rifle"),  # Relby-v10 Mortar Rifle
        ],
        Props.SAVES: DefenseDice.WHITE,
        # Warnings: No range found
    },
    'cadbane': {
        Props.NAME: 'Cad Bane',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 3, 0], name="Martial Arts"),  # Martial Arts
            Weapon([0, 4, 0], pierce=1, name="Dual LL-30 Blaster Pistols"),  # Dual LL-30 Blaster Pistols
            Weapon([0, 0, 4], name="Electro Gauntlets"),  # Electro Gauntlets
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.DODGES: 2,
        # Warnings: No range found
    },
    'maulshadowcollective': {
        Props.NAME: 'Maul (Shadow Collective)',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([4, 0, 4], impacts=2, pierce=2, name="Maul's Double-bladed Lightsaber"),  # Maul's Double-bladed Lightsaber
            Weapon([0, 6, 0], impacts=2, pierce=2, name="The Darksaber (Maul)"),  # The Darksaber (Maul)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
    },

    # ===== CORPS =====
    'blacksunenforcers': {
        Props.NAME: 'Black Sun Enforcers',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 1], name="Close Quarters Combat"),  # Close Quarters Combat
            Weapon([1, 1, 0], name="BH-4 Double Blaster"),  # BH-4 Double Blaster
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'pykesyndicatefootsoldiers': {
        Props.NAME: 'Pyke Syndicate Foot Soldiers',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 0, 0], name="Stun Baton"),  # Stun Baton
            Weapon([0, 1, 0], name="P13 Long Blaster"),  # P13 Long Blaster
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.DODGES: 1,
        # Warnings: No range found
    },

    # ===== SPECIAL FORCES =====
    'mandaloriansupercommandos': {
        Props.NAME: 'Mandalorian Super Commandos',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Combat Expertise"),  # Combat Expertise
            Weapon([0, 2, 0], name="Westar-35 Blaster Pistols"),  # Westar-35 Blaster Pistols
            Weapon([1, 1, 0], name="Galar-15 Blaster Carbine"),  # Galar-15 Blaster Carbine
            Weapon([2, 0, 2], name="Rook Kast"),  # Rook Kast
            Weapon([2, 2, 0], name="Super Commando Gunslinger"),  # Super Commando Gunslinger
            Weapon([1, 1, 1], name="Super Commando Marksman"),  # Super Commando Marksman
            Weapon([0, 0, 1], impacts=1, criticals=1, name="Super Commando Jetpack Rockets"),  # Super Commando Jetpack Rockets
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.IMPERVIOUS: True,
        # Warnings: No range found, No range found
    },

    # ===== SUPPORT =====
    'swoopbikeriders': {
        Props.NAME: 'Swoop Bike Riders',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 0], name="Heavy Blaster Pistol"),  # Heavy Blaster Pistol
            Weapon([0, 1, 2], name="Vibroaxe"),  # Vibroaxe
            Weapon([0, 0, 0], name="Keywords"),  # Keywords
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.DODGES: 1,
        Props.COVER_IMPROVEMENT: 1,
        # Warnings: No range found, No dice pool found
    },

    # ===== HEAVY =====
    'aa5speedertruck': {
        Props.NAME: 'A-A5 Speeder Truck',
        Props.RANK: 'heavy',
        Props.SIZE: 1,
        Props.WEAPONS: [],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.ARMOR: 1,
        # Warnings: No weapons found
    },
}
