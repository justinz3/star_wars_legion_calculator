from unit_config_properties import UnitProperties as Props
from dice import DefenseDice, MAX_DICE_ROLLED
from weapon import Weapon
from constants import UNLIMITED_TOKENS
from constants import UNLIMITED_TOKENS

separatist_config = {

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
    'countdooku': {
        Props.NAME: 'Count Dooku',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 5], impacts=2, pierce=2, name="Dooku's Lightsabers"),  # Dooku's Lightsabers
            Weapon([0, 5, 0], pierce=1, name="Dooku's Lightning"),  # Dooku's Lightning
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
        # Warnings: No range found
    },
    'generalgrievous': {
        Props.NAME: 'General Grievous',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 2, 1], impacts=1, pierce=1, name="Trophy Lightsabers"),  # Trophy Lightsabers
            Weapon([1, 2, 1], impacts=1, pierce=1, name="Trophy Lightsabers"),  # Trophy Lightsabers
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMPERVIOUS: True,
        # Warnings: No range found
    },
    'pogglethelesser': {
        Props.NAME: 'Poggle the Lesser',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Staff of Commannd"),  # Staff of Commannd
            Weapon([0, 2, 0], name="Concealed Blaster"),  # Concealed Blaster
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
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
    'tseriestacticaldroid': {
        Props.NAME: 'T-Series Tactical Droid',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 0, 0], name="Bludgeon"),  # Bludgeon
            Weapon([1, 0, 1], name="Commander's E-5 Blaster Rifle"),  # Commander's E-5 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.WHITE,
        # Warnings: No range found
    },

    # ===== OPERATIVE =====
    'asajjventress': {
        Props.NAME: 'Asajj Ventress',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 8, 0], impacts=2, pierce=2, name="Asajj Ventress' Lightsabers"),  # Asajj Ventress' Lightsabers
        ],
        Props.SAVES: DefenseDice.RED,
        Props.DODGES: 1,
        Props.IMMUNE_PIERCE: True,
    },
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
    'maul': {
        Props.NAME: 'Maul',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([4, 0, 4], impacts=2, pierce=2, name="Maul's Double-bladed Lightsaber"),  # Maul's Double-bladed Lightsaber
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
    },
    'sunfac': {
        Props.NAME: 'Sun Fac',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 0, 1], name="Force Pike"),  # Force Pike
            Weapon([0, 0, 0], name="Keywords"),  # Keywords
            Weapon([1, 1, 1], name="Sun Fac's Sonic Carbine"),  # Sun Fac's Sonic Carbine
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.COVER_IMPROVEMENT: 1,
        # Warnings: No dice pool found, No range found
    },

    # ===== CORPS =====
    'b1battledroids': {
        Props.NAME: 'B1 Battle Droids',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 0, 0], name="Bludgeon"),  # Bludgeon
            Weapon([1, 0, 0], name="E-5 Blaster Rifle"),  # E-5 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.WHITE,
        # Warnings: No range found
    },
    'b2superbattledroids': {
        Props.NAME: 'B2 Super Battle Droids',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 0, 0], name="Unarmed"),  # Unarmed
            Weapon([1, 1, 0], name="Arm Cannons"),  # Arm Cannons
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.ARMOR: 1,
        # Warnings: No range found
    },
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
    'geonosianwarriors': {
        Props.NAME: 'Geonosian Warriors',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Spears"),  # Spears
            Weapon([1, 1, 0], name="Sonic Blasters"),  # Sonic Blasters
            Weapon([2, 1, 1], name="Force Pike Warrior"),  # Force Pike Warrior
            Weapon([1, 1, 1], impacts=1, name="Sonic Cannon Warrior"),  # Sonic Cannon Warrior
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
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
    'bxseriesdroidcommandos': {
        Props.NAME: 'BX-series Droid Commandos',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([2, 0, 0], name="Commando E-5 Blaster Rifle"),  # Commando E-5 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMPERVIOUS: True,
        # Warnings: No range found
    },
    'bxseriesdroidcommandosstriketeam': {
        Props.NAME: 'BX-series Droid Commandos Strike Team',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([2, 0, 0], name="Commando E-5 Blaster Rifle"),  # Commando E-5 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMPERVIOUS: True,
        # Warnings: No range found
    },
    'drk1sithprobedroids': {
        Props.NAME: 'DRK-1 Sith Probe Droids',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 0, 0], name="Electro-stun Micro Blaster"),  # Electro-stun Micro Blaster
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
    },
    'ig100magnaguards': {
        Props.NAME: 'IG-100 MagnaGuards',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Electrostaff"),  # Electrostaff
            Weapon([1, 1, 0], name="Precision Laser Dart"),  # Precision Laser Dart
            Weapon([0, 0, 2], name="Electro-whip MagnaGuard"),  # Electro-whip MagnaGuard
            Weapon([1, 1, 1], impacts=2, criticals=1, name="RPS-6 MagnaGuard"),  # RPS-6 MagnaGuard
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
        # Warnings: No range found
    },
    'ig100magnaguardsprototypeassassindroids': {
        Props.NAME: 'IG-100 MagnaGuards (Prototype Assassin Droids)',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 0], name="Electrostaff"),  # Electrostaff
            Weapon([1, 1, 0], name="Precision Laser Dart"),  # Precision Laser Dart
            Weapon([0, 0, 2], name="Electro-whip MagnaGuard"),  # Electro-whip MagnaGuard
            Weapon([1, 1, 1], impacts=2, criticals=1, name="RPS-6 MagnaGuard"),  # RPS-6 MagnaGuard
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
        # Warnings: No range found
    },

    # ===== SUPPORT =====
    'droidekas': {
        Props.NAME: 'Droidekas',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 1], name="Dual Twin Blaster Cannons"),  # Dual Twin Blaster Cannons
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.SHIELDS: 4,
    },
    'dsd1dwarfspiderdroid': {
        Props.NAME: 'DSD1 Dwarf Spider Droid',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 1], name="Wicked Kick"),  # Wicked Kick
            Weapon([0, 0, 3], impacts=1, name="DSD1 Dwarf Spider Droid"),  # DSD1 Dwarf Spider Droid
            Weapon([1, 0, 1], name="Nose-Mounted Flamethrower"),  # Nose-Mounted Flamethrower
            Weapon([3, 3, 0], impacts=2, name="Nose-Mounted Ion Cannon"),  # Nose-Mounted Ion Cannon
            Weapon([1, 3, 1], criticals=1, name="Nose-Mounted Laser Cannon"),  # Nose-Mounted Laser Cannon
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.ARMOR: 3,
        # Warnings: No range found
    },
    'stapriders': {
        Props.NAME: 'STAP Riders',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 3, 0], name="Repeating Dual Blaster Cannons"),  # Repeating Dual Blaster Cannons
        ],
        Props.SAVES: DefenseDice.WHITE,
    },

    # ===== HEAVY =====
    'nrn99persuaderclasstankdroid': {
        Props.NAME: 'NR-N99 Persuader-Class Tank Droid',
        Props.RANK: 'heavy',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 1], impacts=1, name="Ion Cannons"),  # Ion Cannons
            Weapon([2, 2, 1], criticals=1, name="Heavy Repeating Blasters"),  # Heavy Repeating Blasters
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.ARMOR: 1,
        # Warnings: No range found
    },
    'nrn99persuaderclasstankdroidprototypetankdroid': {
        Props.NAME: 'NR-N99 Persuader-Class Tank Droid (Prototype Tank Droid)',
        Props.RANK: 'heavy',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 1], name="Experimental Ion Cannons"),  # Experimental Ion Cannons
            Weapon([0, 0, 0], name="Ion 1, Fixed: Front"),  # Ion 1, Fixed: Front
            Weapon([2, 2, 1], name="Heavy Repeating Blasters"),  # Heavy Repeating Blasters
            Weapon([0, 0, 0], name="Fixed: Front"),  # Fixed: Front
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.ARMOR: 1,
        # Warnings: No dice pool found, No range found
    },
}
