from unit_config_properties import UnitProperties as Props
from dice import DefenseDice
from weapon import Weapon
from constants import UNLIMITED_TOKENS

empire_config = {
    # ===== COMMANDERS =====
    'vader': {
        Props.NAME: 'Darth Vader',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 6], impacts=3, pierce=3)  # Vader's Lightsaber
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
        # NOTE: Deflect, Relentless, Master of the Force 1 not simulated
    },

    # ===== OPERATIVES =====
    'boba': {
        Props.NAME: 'Boba Fett',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 3]),                      # Boot Spikes (melee)
            Weapon([1, 3, 0], impacts=1),           # Integrated Rockets (range 1-2, Versatile not simulated)
            Weapon([0, 2, 0], pierce=1),            # Fett's EE-3 Carbine (range 1-3, Sharpshooter 2 not simulated)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        Props.IMPERVIOUS: True,
        # NOTE: Arsenal 2, Bounty, Independent, Sharpshooter 2 not simulated
    },
    'ig88': {
        Props.NAME: 'IG-88',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 1], pierce=1),            # IG-88's Vibro-Cleaver (melee)
            Weapon([2, 1, 0], pierce=1),            # Modified E-11 Blaster (range 1-3, Versatile not simulated)
            Weapon([1, 2, 0]),                      # Modified DLT-20A Rifle (range 1-4, Sharpshooter 1 not simulated)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.CRIT_SURGES: UNLIMITED_TOKENS, # Surge: Crit
        Props.ARMOR: 1,
        Props.IMPERVIOUS: True,
        # NOTE: Arsenal 2, Bounty, Sharpshooter 1 not simulated
    },

    # ===== CORPS =====
    'storms': {
        Props.NAME: 'Stormtroopers',
        Props.SIZE: 4,
        Props.WEAPONS: [
            Weapon([0, 1, 0]),  # Unarmed (melee), E-11 Blaster Rifle (range 1-3)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.HIT_SURGES: UNLIMITED_TOKENS, # Surge: Hit
        # NOTE: Precise 1 not simulated
    },
    'snows': {
        Props.NAME: 'Snowtroopers',
        Props.SIZE: 4,
        Props.WEAPONS: [
            Weapon([0, 1, 0]),  # Unarmed (melee), E-11 Blaster Rifle (range 1-3)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.HIT_SURGES: UNLIMITED_TOKENS, # Surge: Hit
        # NOTE: Steady not simulated
    },

    # ===== SPECIAL FORCES =====
    'deathtroopers': {
        Props.NAME: 'Imperial Death Troopers',
        Props.SIZE: 4,
        Props.WEAPONS: [
            Weapon([0, 0, 1]),  # Close Quarters Combat (melee)
            Weapon([2, 0, 0]),  # SE-14r Light Blaster (range 1-2)
            Weapon([0, 1, 0]),  # E-11D Blaster Rifle (range 1-3, Precise 2 not simulated)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.HIT_SURGES: UNLIMITED_TOKENS,   # Surge: Hit
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        # NOTE: Disciplined 1, Precise 2, Ready 1 not simulated
    },
    'scouts': {
        Props.NAME: 'Scout Troopers',
        Props.SIZE: 4,
        Props.WEAPONS: [
            Weapon([0, 1, 0]),  # Unarmed (melee)
            Weapon([0, 2, 0]),  # EC-17 Hold-out Blaster (Sharpshooter 1 not simulated)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        # NOTE: Low Profile, Scout 3, Sharpshooter 1 not simulated
    },

    # ===== HEAVY =====
    'atst': {
        Props.NAME: 'AT-ST',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 4]),                      # Fence-Cutting Blades (melee)
            Weapon([2, 2, 2], impacts=3),           # MS-4 Twin Blaster Cannon (range 1-4, Fixed: Front not simulated)
            # NOTE: Arsenal 2 allows attacking with multiple weapons - user can simulate by using unit multiple times
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        Props.ARMOR: 2,
        # NOTE: Weak Point 1: Rear not simulated
    },
}
