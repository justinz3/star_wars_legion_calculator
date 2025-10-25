from unit_config_properties import UnitProperties as Props
from dice import DefenseDice, MAX_DICE_ROLLED
from weapon import Weapon
from constants import UNLIMITED_TOKENS

republic_config = {
    'ob': {
        Props.NAME: 'Obi-Wan Kenobi',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 2, 2], impacts=2, criticals=2, pierce=2) # Obi-Wan's Lightsaber
        ],
        Props.SAVES: DefenseDice.RED, 
        Props.IMMUNE_PIERCE: True,
    },
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
        Props.DODGES: 1, # Improves Cover by 1 (NOTE TO USER: Unless I take the time to separate out cover from dodges, REMEMBER THIS in case the speeder is in high-cover)
    },
}
