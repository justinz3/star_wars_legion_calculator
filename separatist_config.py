from unit_config_properties import UnitProperties as Props
from dice import DefenseDice, MAX_DICE_ROLLED
from weapon import Weapon

separatist_config = {
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
}
