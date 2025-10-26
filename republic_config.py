from unit_config_properties import UnitProperties as Props
from dice import DefenseDice, MAX_DICE_ROLLED
from weapon import Weapon
from constants import UNLIMITED_TOKENS

republic_config = {
    # ===== COMMANDERS =====
    'ob': {
        Props.NAME: 'Obi-Wan Kenobi',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 2, 2], impacts=2, criticals=2, pierce=2) # Obi-Wan's Lightsaber
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
    },
    'anakin': {
        Props.NAME: 'Anakin Skywalker',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 5], impacts=3, pierce=3) # Anakin's Lightsaber
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
    },
    'yoda': {
        Props.NAME: 'Yoda',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 4], impacts=2, pierce=2),  # Yoda's Lightsaber (melee)
            Weapon([0, 4, 0]),                        # Force Wave (range 1-2, Blast, Suppressive - not simulated)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.HIT_SURGES: UNLIMITED_TOKENS,   # Surge: Hit
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        Props.IMMUNE_PIERCE: True,
    },
    'rex': {
        Props.NAME: 'Clone Captain Rex',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 2]),  # Advanced Combat Training (melee)
            Weapon([0, 0, 3]),  # Dual DC-17 Hand Blasters (range 1-2, Gunslinger not simulated)
        ],
        Props.SAVES: DefenseDice.RED,
    },
    'cody': {
        Props.NAME: 'Clone Commander Cody',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 2]),              # Advanced Combat Training (melee)
            Weapon([1, 1, 2], impacts=1),   # Cody's DC-15a Blaster (range 1-4, Lethal 1 not simulated)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.CRIT_SURGES: UNLIMITED_TOKENS, # Surge: Crit
    },
    'ahsoka': {
        Props.NAME: 'Ahsoka Tano',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 2, 2], impacts=2, pierce=2)  # Ahsoka's Lightsabers (Jar'Kai Mastery, Deflect not simulated)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.CRIT_SURGES: UNLIMITED_TOKENS, # Surge: Crit
        Props.IMMUNE_PIERCE: True,
        # NOTE: Deflect only works vs ranged attacks - not simulated
    },

    # ===== OPERATIVES =====
    'padme': {
        Props.NAME: 'Padmé Amidala',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 3, 0]),              # Martial Arts (melee)
            Weapon([0, 3, 0], pierce=1),    # Padmé's ELG-3A Blaster Pistol (range 1-2, Sharpshooter 2 not simulated)
        ],
        Props.SAVES: DefenseDice.WHITE,
    },
    'r2d2': {
        Props.NAME: 'R2-D2',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([3, 0, 0])  # Electro-Shock (melee/range 1, Suppressive not simulated)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.HIT_SURGES: UNLIMITED_TOKENS,   # Surge: Hit
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
    },

    # ===== CORPS =====
    'p1': {
        Props.NAME: 'Phase-I Clone Troopers',
        Props.SIZE: 4,
        Props.WEAPONS: [
            Weapon([0, 1, 0])   # Unarmed, DC-15A Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
    },
    'p1z6': {
        Props.NAME: 'Z-6 Phase I Trooper',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([6, 0, 0]),
            Weapon([0, 1, 0])   # Unarmed, DC-15A Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
    },
    'p1dc15': {
        Props.NAME: 'DC-15 Phase I Trooper',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 2], criticals=1),
            Weapon([0, 1, 0])   # Unarmed, DC-15A Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
    },
    'p2': {
        Props.NAME: 'Phase-II Clone Troopers',
        Props.SIZE: 4,
        Props.WEAPONS: [
            Weapon([0, 1, 0])   # Unarmed, DC-15A Blaster Rifle (melee/range 1-3)
        ],
        Props.SAVES: DefenseDice.RED,
    },
    'p2z6': {
        Props.NAME: 'Z-6 Phase II Trooper',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([6, 0, 0]),  # Z-6 Rotary Blaster (range 1-3)
            Weapon([0, 1, 0])   # Unarmed, DC-15A Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
    },
    'p2mortar': {
        Props.NAME: 'Phase II Mortar Trooper',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], criticals=1),  # Mortar (range 2-4, Suppressive, Cumbersome not simulated)
            Weapon([0, 1, 0])                 # Unarmed, DC-15A Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
    },

    # ===== SPECIAL FORCES =====
    'arc': {
        Props.NAME: 'ARC Troopers',
        Props.SIZE: 4,
        Props.WEAPONS: [
            Weapon([1, 1, 0]),  # Combat Training (melee)
            Weapon([1, 1, 0]),  # DC-17 Hand Blasters (range 1-2)
            Weapon([1, 1, 0]),  # DC-15A Blaster Rifle (range 1-3, Sharpshooter 1 not simulated)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        Props.IMPERVIOUS: True,
    },
    'wookiees': {
        Props.NAME: 'Wookiee Warriors',
        Props.SIZE: 3,
        Props.WEAPONS: [
            Weapon([0, 2, 0]),  # Ryyk Blade (melee, Charge not simulated)
            Weapon([1, 1, 0]),  # Kashyyyk Pistol (range 1-2)
        ],
        Props.SAVES: DefenseDice.WHITE,
        # NOTE: Indomitable (roll red dice instead of white during Rally) not simulated
    },

    # ===== SUPPORT =====
    'barc': {
        Props.NAME: 'BARC Speeder',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 1]),              # Twin Light Blaster Cannons
            Weapon([0, 1, 0]),              # DC-15A Blaster Rifle
            Weapon([1, 3, 0], impacts=1),   # BARC Ion Gunner
            Weapon([1, 1, 1], impacts=2),   # BARC RPS-6 Gunner
            Weapon([2, 2, 0]),              # BARC Twin Laser Gunner
        ],
        Props.SAVES: DefenseDice.RED,
        Props.HIT_SURGES: UNLIMITED_TOKENS,   # Attack Surge: Hit (converts all attack surges to hits)
        Props.COVER_IMPROVEMENT: 1,           # Cover 1 keyword
    },
    'atrt': {
        Props.NAME: 'AT-RT',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 3], impacts=1),           # Grappling Claws (melee)
            Weapon([2, 1, 0], criticals=1, impacts=1), # RPC-2 Rocket Launcher (range 1-3)
            # TODO: Add hardpoint weapons (Flamethrower, Laser Cannon, Rotary Blaster)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.HIT_SURGES: UNLIMITED_TOKENS,   # Surge: Hit
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        Props.ARMOR: 1, # Armor keyword
    },
    'commandos': {
        Props.NAME: 'Clone Commandos',
        Props.SIZE: 4,
        Props.WEAPONS: [
            Weapon([0, 2, 0]),  # Gauntlet Vibroblade (melee)
            Weapon([1, 1, 0]),  # DC-17m ICWS Blaster Carbine (range 1-2, Suppressive not simulated)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.SHIELDS: 1, # Shielded 1 (treating as 1 shield token)
    },
    'isp': {
        Props.NAME: 'Infantry Support Platform',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0])  # DC-15 Blaster Rifles (range 1-3)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.HIT_SURGES: UNLIMITED_TOKENS,   # Surge: Hit
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        Props.ARMOR: 3,
        Props.COVER_IMPROVEMENT: 1, # Cover 1
    },

    # ===== HEAVY =====
    'tx130': {
        Props.NAME: 'TX-130 Saber-class Fighter Tank',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 2, 2], criticals=1, impacts=2)  # Twin Lateral GA-6n Laser Cannons (range 1-4, Fixed: Front not simulated)
            # NOTE: Arsenal 2 allows attacking with multiple weapons - user can simulate by adding same unit multiple times
            # TODO: Add turret weapons (Twin Laser Turret, Beam Cannon Turret)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.ARMOR: 1, # Armor keyword (exact value not specified, using 1)
        # NOTE: Weak Point 1: Rear, Sides not simulated (directional defense)
    },
}
