from unit_config_properties import UnitProperties as Props
from dice import DefenseDice
from weapon import Weapon
from constants import UNLIMITED_TOKENS

rebel_config = {
    # ===== COMMANDERS =====
    'luke': {
        Props.NAME: 'Luke Skywalker',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 6, 0], impacts=2, pierce=2),  # Anakin's Lightsaber (melee, Charge, Deflect not simulated)
            Weapon([0, 0, 2], pierce=2),             # Luke's DL-44 Blaster Pistol (range 1-2)
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        Props.IMMUNE_PIERCE: True,
        # NOTE: Charge, Deflect not simulated
    },
    'han': {
        Props.NAME: 'Han Solo',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([3, 0, 0]),              # Brawl (melee)
            Weapon([0, 0, 2], pierce=2),    # Han's DL-44 Blaster Pistol (range 1-2, Gunslinger, Sharpshooter 1 not simulated)
        ],
        Props.SAVES: DefenseDice.WHITE,
        # NOTE: Gunslinger, Sharpshooter 1, Low Profile, Uncanny Luck 3, Steady not simulated
    },
    'leia': {
        Props.NAME: 'Leia Organa',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 3, 0]),              # Martial Arts (melee)
            Weapon([0, 3, 0], pierce=1),    # Leia's Defender Sporting Blaster (range 1-2, Sharpshooter 2 not simulated)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        # NOTE: Sharpshooter 2, Take Cover 2, Inspire 2, Nimble not simulated
    },

    # ===== OPERATIVES =====
    'chewie': {
        Props.NAME: 'Chewbacca',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 4]),                      # Overwhelm (melee, Lethal 1 not simulated)
            Weapon([2, 0, 2], impacts=1, pierce=1), # Chewbacca's Bowcaster (range 1-3)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.CRIT_SURGES: UNLIMITED_TOKENS, # Surge: Crit (defense)
        # NOTE: Enrage 4, Guardian 3, Scale, Teamwork not simulated
    },

    # ===== CORPS =====
    'rebels': {
        Props.NAME: 'Rebel Troopers',
        Props.SIZE: 4,
        Props.WEAPONS: [
            Weapon([0, 1, 0]),  # Unarmed (melee), A-280 Blaster Rifle (range 1-3)
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        # NOTE: Nimble not simulated
    },

    # ===== SPECIAL FORCES =====
    'rebelcommandos': {
        Props.NAME: 'Rebel Commandos',
        Props.SIZE: 4,
        Props.WEAPONS: [
            Weapon([0, 1, 0]),  # Unarmed (melee), A-280 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.HIT_SURGES: UNLIMITED_TOKENS,   # Surge: Hit
        Props.BLOCK_SURGES: UNLIMITED_TOKENS, # Surge: Block
        # NOTE: Low Profile, Scout 2, Sharpshooter 1 not simulated
    },
}
