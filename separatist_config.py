from unit_config_properties import UnitProperties as Props
from dice import DefenseDice, MAX_DICE_ROLLED
from weapon import Weapon
from constants import UNLIMITED_TOKENS

separatist_config = {
    # ===== COMMANDERS =====
    'gg': {
        Props.NAME: 'General Grievous',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 2, 1], impacts=1, pierce=1),   # Trophy Lightsabers
            Weapon([2, 2, 0], criticals=1, pierce=1), # DT-57 "Annihilator"
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMPERVIOUS: True,
    },
    'dooku': {
        Props.NAME: 'Count Dooku',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 5], impacts=2, pierce=2),  # Dooku's Lightsabers (melee)
            Weapon([0, 5, 0], pierce=1),              # Dooku's Lightning (range 1-2, Scatter not simulated)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.CRIT_SURGES: UNLIMITED_TOKENS, # Surge: Crit
        Props.IMMUNE_PIERCE: True,
        # NOTE: Deflect (ranged attacks), Makashi Mastery not simulated
    },
    'tseries': {
        Props.NAME: 'T-Series Tactical Droid',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 0, 0]),  # Bludgeon (melee)
            Weapon([1, 0, 1]),  # Commander's E-5 Blaster Rifle (range 1-2, Sharpshooter 1 not simulated)
        ],
        Props.SAVES: DefenseDice.WHITE,
    },

    # ===== OPERATIVES =====
    'ventress': {
        Props.NAME: 'Asajj Ventress',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 8, 0], impacts=2, pierce=2)  # Asajj Ventress' Lightsabers (Jar'Kai Mastery, Deflect not simulated)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.DODGES: 1, # Independent: Dodge 1
        Props.IMMUNE_PIERCE: True,
        # NOTE: Deflect (ranged attacks), Indomitable, Relentless not simulated
    },
    'cadbane': {
        Props.NAME: 'Cad Bane',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 3, 0]),              # Martial Arts (melee)
            Weapon([0, 4, 0], pierce=1),    # Dual LL-30 Blaster Pistols (range 1-2, Sharpshooter 1 not simulated)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.DODGES: 2, # Independent: Dodge 2
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        # NOTE: Danger Sense 2 not simulated
    },
    'maul': {
        Props.NAME: 'Maul',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([4, 0, 4], impacts=2, pierce=2)  # Maul's Double-bladed Lightsaber (Juyo Mastery, Deflect not simulated)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
        # NOTE: Deflect (ranged attacks) not simulated
    },

    # ===== CORPS =====
    'b1': {
        Props.NAME: 'B1 Battle Droids',
        Props.SIZE: 6,
        Props.WEAPONS: [
            Weapon([1, 0, 0])   # Bludgeon, E-5 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.WHITE,
    },
    'b1e5': {
        Props.NAME: 'E-5C B1 Trooper',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 3, 0]),
            Weapon([1, 0, 0])   # Bludgeon, E-5 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.WHITE,
    },
    'b1e6': {
        Props.NAME: 'E-60R B1 Trooper',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 1], impacts=2),
            Weapon([1, 0, 0])   # Bludgeon, E-5 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.WHITE,
    },
    'b2': {
        Props.NAME: 'B2 Super Battle Droids',
        Props.SIZE: 3,
        Props.WEAPONS: [
            Weapon([1, 0, 0]),  # Unarmed (melee)
            Weapon([1, 1, 0]),  # Arm Cannons (range 1-2)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.ARMOR: 1, # Armor 1
        # NOTE: AI: Attack not simulated
    },
    'b2ha': {
        Props.NAME: 'B2-HA Trooper',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 0, 3], impacts=2),  # B2-HA Blaster (range 2-3, Blast, Cycle not simulated)
            Weapon([1, 1, 0]),              # Arm Cannons (range 1-2)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.ARMOR: 1,
    },
    'b2acm': {
        Props.NAME: 'B2-ACM Trooper',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 3]),  # B2-ACM Blaster (range 1-2)
            Weapon([1, 1, 0]),  # Arm Cannons (range 1-2)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.ARMOR: 1,
    },
    'geonosians': {
        Props.NAME: 'Geonosian Warriors',
        Props.SIZE: 4,
        Props.WEAPONS: [
            Weapon([0, 1, 0]),  # Spears (melee, Death From Above not simulated)
            Weapon([1, 1, 0]),  # Sonic Blasters (range 1-2)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        # NOTE: Jump 3, Scale, Death From Above, Weighed Down not simulated
    },

    # ===== SPECIAL FORCES =====
    'bx': {
        Props.NAME: 'BX-series Droid Commandos',
        Props.SIZE: 4,
        Props.WEAPONS: [
            Weapon([0, 1, 0]),  # Unarmed (melee)
            Weapon([2, 0, 0]),  # Commando E-5 Blaster Rifle (range 1-3, Sharpshooter 1 not simulated)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.HIT_SURGES: UNLIMITED_TOKENS, # Surge: Hit
        Props.IMPERVIOUS: True,
        # NOTE: AI: Dodge, Move; Scout 3 not simulated
    },
    'magnaguards': {
        Props.NAME: 'IG-100 MagnaGuards',
        Props.SIZE: 3,
        Props.WEAPONS: [
            Weapon([0, 2, 0]),  # Electrostaff (melee)
            Weapon([1, 1, 0]),  # Precision Laser Dart (range 1-2)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.HIT_SURGES: UNLIMITED_TOKENS, # Surge: Hit
        Props.IMMUNE_PIERCE: True, # Immune: Melee Pierce (treating as full pierce immunity)
        # NOTE: Guardian 2: Commander not simulated
    },

    # ===== SUPPORT =====
    'dekas': {
        Props.NAME: 'Droidekas',
        Props.SIZE: 2,
        Props.WEAPONS: [
            Weapon([0, 2, 1]),  # Dual Twin Blaster Cannons
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.DODGES: 0, # For wheel mode, use 2
        Props.SHIELDS: 4,
    },
    'spider': {
        Props.NAME: 'DSD1 Dwarf Spider Droid',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 1]),              # Wicked Kick (melee)
            Weapon([0, 0, 3], impacts=1),   # DSD1 Self-Destruct Mechanism (melee, Blast not simulated)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        Props.ARMOR: 3,
        # NOTE: Self-Destruct mechanics (dies after using weapon 1) not simulated
    },
    'stap': {
        Props.NAME: 'STAP Riders',
        Props.SIZE: 2,
        Props.WEAPONS: [
            Weapon([0, 3, 0], criticals=1)  # Repeating Dual Blaster Cannons (range 1-3, Fixed: Front not simulated)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.COVER_IMPROVEMENT: 1, # Cover 1
        # NOTE: Agile 1, Speeder 1 not simulated
    },

    # ===== HEAVY =====
    'aat': {
        Props.NAME: 'AAT Battle Tank',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 3, 0]),                      # Lateral Anti-Personnel Lasers (Fixed: Front not simulated)
            Weapon([0, 0, 4], criticals=2, impacts=1), # MX-8 Artillery Laser Cannon (High Velocity not simulated)
            # NOTE: Arsenal 2, Barrage allow multiple attacks - user can simulate by using unit multiple times
        ],
        Props.SAVES: DefenseDice.RED,
        Props.CRIT_SURGES: UNLIMITED_TOKENS, # Surge: Crit
        Props.ARMOR: 1, # Armor keyword (exact value not specified, using 1)
        # NOTE: Weak Point 2: Rear; AI: Attack not simulated
    },
}
