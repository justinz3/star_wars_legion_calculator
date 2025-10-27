from unit_config_properties import UnitProperties as Props
from dice import DefenseDice
from weapon import Weapon
from constants import UNLIMITED_TOKENS
from constants import UNLIMITED_TOKENS

empire_config = {

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
    'darthvader': {
        Props.NAME: 'Darth Vader',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 6], impacts=3, pierce=3, name="Vader's Lightsaber"),  # Vader's Lightsaber
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
    },
    'directororsonkrennic': {
        Props.NAME: 'Director Orson Krennic',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([1, 1, 1], pierce=1, name="Krennic's DT-29 Blaster Pistol"),  # Krennic's DT-29 Blaster Pistol
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
    },
    'emperorpalpatine': {
        Props.NAME: 'Emperor Palpatine',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 2, 2], pierce=2, name="Force Lightning"),  # Force Lightning
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.IMMUNE_PIERCE: True,
    },
    'generalveers': {
        Props.NAME: 'General Veers',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Combat Expertise"),  # Combat Expertise
            Weapon([3, 0, 0], pierce=1, name="Veers' E-11 Blaster Rifle"),  # Veers' E-11 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'idenversio': {
        Props.NAME: 'Iden Versio',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 2], name="Advanced Combat Training"),  # Advanced Combat Training
            Weapon([3, 0, 0], pierce=1, name="Iden's E-11 Blaster Rifle"),  # Iden's E-11 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'imperialofficer': {
        Props.NAME: 'Imperial Officer',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([1, 1, 0], name="Officer's RK-3 Blaster Pistol"),  # Officer's RK-3 Blaster Pistol
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
    },
    'moffgideon': {
        Props.NAME: 'Moff Gideon',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 2], name="Advanced Combat Training"),  # Advanced Combat Training
            Weapon([2, 1, 0], pierce=1, name="Gideon's Custom Blaster Pistol"),  # Gideon's Custom Blaster Pistol
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
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

    # ===== OPERATIVE =====
    'agentkallus': {
        Props.NAME: 'Agent Kallus',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 2], name="Advanced Combat Training"),  # Advanced Combat Training
            Weapon([1, 2, 0], pierce=1, name="Kallus's RK-3 Blaster Pistol"),  # Kallus's RK-3 Blaster Pistol
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'bobafett': {
        Props.NAME: 'Boba Fett',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 3], name="Boot Spikes"),  # Boot Spikes
            Weapon([0, 3, 0], name="Integrated Rockets"),  # Integrated Rockets
            Weapon([0, 0, 0], name="Keywords"),  # Keywords
            Weapon([0, 2, 0], pierce=1, name="Fett's EE-3 Carbine"),  # Fett's EE-3 Carbine
            Weapon([0, 0, 1], name="Boba's Flame Projector"),  # Boba's Flame Projector
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.DODGES: 1,
        Props.IMPERVIOUS: True,
        # Warnings: No range found, No dice pool found
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
    'darthvaderoperative': {
        Props.NAME: 'Darth Vader (Operative)',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 5], impacts=3, pierce=3, name="Vader's Lightsaber"),  # Vader's Lightsaber
            Weapon([0, 2, 0], name="Force Throw"),  # Force Throw
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
        # Warnings: No range found
    },
    'dindjarin': {
        Props.NAME: 'Din Djarin',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Vibro-Knife"),  # Vibro-Knife
            Weapon([0, 1, 2], name="Din's Modified IB-94 Pistol"),  # Din's Modified IB-94 Pistol
        ],
        Props.SAVES: DefenseDice.RED,
        Props.DODGES: 1,
        Props.IMPERVIOUS: True,
        # Warnings: No range found
    },
    'fifthbrother': {
        Props.NAME: 'Fifth Brother',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 5, 0], impacts=2, pierce=1, name="Spinning Lightsaber"),  # Spinning Lightsaber
            Weapon([0, 3, 0], impacts=2, pierce=1, name="Thrown Spinning Lightsaber"),  # Thrown Spinning Lightsaber
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
        # Warnings: No range found
    },
    'ig11': {
        Props.NAME: 'IG-11',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 4], name="Overpower"),  # Overpower
            Weapon([2, 1, 0], pierce=1, name="Modified E-11 Blaster"),  # Modified E-11 Blaster
            Weapon([1, 2, 0], name="Modified DLT-20A Rifle"),  # Modified DLT-20A Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        Props.ARMOR: 1,
        Props.IMPERVIOUS: True,
        # Warnings: No range found, No range found
    },
    'ig88': {
        Props.NAME: 'IG-88',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 1], pierce=1, name="IG-88's Vibro-Cleaver"),  # IG-88's Vibro-Cleaver
            Weapon([2, 1, 0], pierce=1, name="Modified E-11 Blaster"),  # Modified E-11 Blaster
            Weapon([1, 2, 0], name="Modified DLT-20A Rifle"),  # Modified DLT-20A Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        Props.ARMOR: 1,
        Props.IMPERVIOUS: True,
        # Warnings: No range found, No range found
    },
    'seventhsister': {
        Props.NAME: 'Seventh Sister',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 5, 0], impacts=2, pierce=1, name="Spinning Lightsaber"),  # Spinning Lightsaber
            Weapon([0, 3, 0], impacts=2, pierce=1, name="Thrown Spinning Lightsaber"),  # Thrown Spinning Lightsaber
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
        # Warnings: No range found
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
    'shoretroopers': {
        Props.NAME: 'Shoretroopers',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 1, 0], name="E-22 Blaster Rifle"),  # E-22 Blaster Rifle
            Weapon([2, 2, 0], criticals=1, name="T-21B Trooper"),  # T-21B Trooper
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'df90mortartrooper': {
        Props.NAME: 'DF-90 Mortar Trooper',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 1, 0], name="E-22 Blaster Rifle"),  # E-22 Blaster Rifle
            Weapon([3, 0, 0], criticals=1, name="DF-90 Mortar"),  # DF-90 Mortar
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found, No range found
    },
    'snowtroopers': {
        Props.NAME: 'Snowtroopers',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([1, 0, 0], name="E-11 Blaster Rifle"),  # E-11 Blaster Rifle
            Weapon([0, 1, 0], name="Flametrooper"),  # Flametrooper
            Weapon([2, 1, 0], impacts=1, name="T-7 Ion Snowtrooper"),  # T-7 Ion Snowtrooper
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'stormtroopers': {
        Props.NAME: 'Stormtroopers',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([1, 0, 0], name="E-11 Blaster Rifle"),  # E-11 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'stormtroopersheavyresponseunit': {
        Props.NAME: 'Stormtroopers (Heavy Response Unit)',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([1, 0, 0], name="E-11 Blaster Rifle"),  # E-11 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },

    # ===== SPECIAL FORCES =====
    'imperialdeathtroopers': {
        Props.NAME: 'Imperial Death Troopers',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 1], name="Close Quarters Combat"),  # Close Quarters Combat
            Weapon([2, 0, 0], name="SE-14r Light Blaster"),  # SE-14r Light Blaster
            Weapon([0, 1, 0], name="E-11D Blaster Rifle"),  # E-11D Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found, No range found
    },
    'imperialroyalguards': {
        Props.NAME: 'Imperial Royal Guards',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 1], name="Force Pike"),  # Force Pike
            Weapon([0, 2, 0], name="EC-17 Hold-out Blaster"),  # EC-17 Hold-out Blaster
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'imperialspecialforces': {
        Props.NAME: 'Imperial Special Forces',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 1, 0], name="Special Forces E-11D Blaster Rifle"),  # Special Forces E-11D Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'imperialspecialforcesinfernosquad': {
        Props.NAME: 'Imperial Special Forces (Inferno Squad)',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 1], name="Close Quarters Combat"),  # Close Quarters Combat
            Weapon([0, 2, 0], name="Inferno Squad E-11 Blaster Rifle"),  # Inferno Squad E-11 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'scouttroopers': {
        Props.NAME: 'Scout Troopers',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 2, 0], name="EC-17 Hold-out Blaster"),  # EC-17 Hold-out Blaster
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
    },
    'scouttroopersstriketeam': {
        Props.NAME: 'Scout Troopers (Strike Team)',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 2, 0], name="EC-17 Hold-out Blaster"),  # EC-17 Hold-out Blaster
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
    },

    # ===== SUPPORT =====
    '74zspeederbikes': {
        Props.NAME: '74-Z Speeder Bikes',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="EC-17 Hold-out Blaster"),  # EC-17 Hold-out Blaster
            Weapon([1, 1, 1], impacts=1, name="Ax-20 Blaster Cannon"),  # Ax-20 Blaster Cannon
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.COVER_IMPROVEMENT: 1,
        # Warnings: No range found
    },
    'dewbackrider': {
        Props.NAME: 'Dewback Rider',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([3, 0, 3], criticals=2, name="Razor Claws & Shock Prod"),  # Razor Claws & Shock Prod
            Weapon([1, 1, 0], name="CR-24 Flame Rifle"),  # CR-24 Flame Rifle
            Weapon([3, 0, 1], name="RT-97C Blaster Rifle"),  # RT-97C Blaster Rifle
            Weapon([4, 0, 0], criticals=2, name="T-21 Blaster Rifle"),  # T-21 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        Props.ARMOR: 1,
    },
    'ewebheavyblasterteam': {
        Props.NAME: 'E-Web Heavy Blaster Team',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Unarmed"),  # Unarmed
            Weapon([2, 0, 0], name="E-11 Blaster Rifle"),  # E-11 Blaster Rifle
            Weapon([2, 2, 1], name="E-Web Heavy Blaster"),  # E-Web Heavy Blaster
            Weapon([0, 0, 0], name="Cumbersome, Fixed: Front"),  # Cumbersome, Fixed: Front
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found, No range found
    },

    # ===== HEAVY =====
    'rangetroopers': {
        Props.NAME: 'Range Troopers',
        Props.RANK: 'heavy',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Gripton Boot Kick"),  # Gripton Boot Kick
            Weapon([0, 0, 0], name="Keywords"),  # Keywords
            Weapon([0, 0, 1], name="E-10R Blaster Rifle"),  # E-10R Blaster Rifle
            Weapon([0, 0, 0], name="Keywords"),  # Keywords
            Weapon([0, 0, 2], impacts=2, name="DLT-20A Range Trooper"),  # DLT-20A Range Trooper
            Weapon([2, 2, 0], name="T-21A Range Trooper"),  # T-21A Range Trooper
        ],
        Props.SAVES: DefenseDice.RED,
        Props.ARMOR: 1,
        # Warnings: No dice pool found, No range found
    },
    'atst': {
        Props.NAME: 'AT-ST',
        Props.RANK: 'heavy',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 4], name="Fence-Cutting Blades"),  # Fence-Cutting Blades
            Weapon([2, 2, 2], impacts=3, name="MS-4 Twin Blaster Cannon"),  # MS-4 Twin Blaster Cannon
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.ARMOR: 1,
        # Warnings: No range found
    },
    'imperialdarktroopers': {
        Props.NAME: 'Imperial Dark Troopers',
        Props.RANK: 'heavy',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 0, 1], name="Crushing Punch"),  # Crushing Punch
            Weapon([0, 1, 0], name="E-11D Blaster"),  # E-11D Blaster
        ],
        Props.SAVES: DefenseDice.RED,
        Props.ARMOR: 1,
        # Warnings: No range found
    },
    'laatlepatroltransport': {
        Props.NAME: 'LAAT/le Patrol Transport',
        Props.RANK: 'heavy',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 3, 1], name="Twin Laser Cannons"),  # Twin Laser Cannons
            Weapon([0, 0, 0], name="Fixed: Front"),  # Fixed: Front
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.ARMOR: 1,
        Props.COVER_IMPROVEMENT: 1,
        # Warnings: No dice pool found, No range found
    },
    'majormarquand': {
        Props.NAME: 'Major Marquand',
        Props.RANK: 'heavy',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Grenade Launcher"),  # Grenade Launcher
            Weapon([1, 1, 1], impacts=1, name="88 Twin Light Blaster"),  # 88 Twin Light Blaster
            Weapon([2, 2, 2], impacts=3, name="MS-4 Twin Blaster Cannon"),  # MS-4 Twin Blaster Cannon
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.ARMOR: 1,
        # Warnings: No range found, No range found
    },
}
