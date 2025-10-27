from unit_config_properties import UnitProperties as Props
from dice import DefenseDice
from weapon import Weapon
from constants import UNLIMITED_TOKENS
from constants import UNLIMITED_TOKENS

rebel_config = {

    # ===== COMMANDER =====
    'c3pogoldengod': {
        Props.NAME: 'C-3PO (Golden God)',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No weapons found
    },
    'hansolo': {
        Props.NAME: 'Han Solo',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([3, 0, 0], name="Brawl"),  # Brawl
            Weapon([0, 0, 2], pierce=2, name="Han's DL-44 Blaster Pistol"),  # Han's DL-44 Blaster Pistol
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
    },
    'landocalrissian': {
        Props.NAME: 'Lando Calrissian',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 0], name="Combat Training"),  # Combat Training
            Weapon([0, 1, 1], pierce=1, name="Lando's X-8 Night Sniper Pistol"),  # Lando's X-8 Night Sniper Pistol
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
    },
    'leiaorgana': {
        Props.NAME: 'Leia Organa',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 3, 0], name="Martial Arts"),  # Martial Arts
            Weapon([0, 3, 0], pierce=1, name="Leia's Defender Sporting Blaster"),  # Leia's Defender Sporting Blaster
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.COVER_IMPROVEMENT: 2,
        # Warnings: No range found
    },
    'logray': {
        Props.NAME: 'Logray',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Staff"),  # Staff
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.DODGES: 1,
    },
    'lukeskywalker': {
        Props.NAME: 'Luke Skywalker',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 6, 0], impacts=2, pierce=2, name="Anakin's Lightsaber"),  # Anakin's Lightsaber
            Weapon([0, 0, 2], pierce=2, name="Luke's DL-44 Blaster Pistol"),  # Luke's DL-44 Blaster Pistol
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
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
    'rebelofficer': {
        Props.NAME: 'Rebel Officer',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([1, 1, 0], name="Officer's A-180 Blaster Pistol"),  # Officer's A-180 Blaster Pistol
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.COVER_IMPROVEMENT: 1,
        # Warnings: No range found
    },
    'wicket': {
        Props.NAME: 'Wicket',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 2], pierce=1, name="Spear"),  # Spear
            Weapon([0, 1, 0], pierce=1, name="Sling"),  # Sling
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.DODGES: 1,
        # Warnings: No range found
    },

    # ===== OPERATIVE =====
    'ahsokatano': {
        Props.NAME: 'Ahsoka Tano',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 2, 2], name="Ahsoka's Lightsabers"),  # Ahsoka's Lightsabers
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
    },
    'thebadbatch': {
        Props.NAME: 'The Bad Batch',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 1], name="Advanced Combat Training"),  # Advanced Combat Training
            Weapon([1, 1, 0], name="DC-17 Hand Blaster"),  # DC-17 Hand Blaster
            Weapon([1, 1, 1], name="Wrecker (Bad Batch)"),  # Wrecker (Bad Batch)
            Weapon([0, 0, 1], criticals=1, pierce=1, name="Crosshair (Bad Batch)"),  # Crosshair (Bad Batch)
            Weapon([2, 0, 0], name="Omega"),  # Omega
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMPERVIOUS: True,
        # Warnings: No range found
    },
    'bobafettdaimyo': {
        Props.NAME: 'Boba Fett (Daimyo)',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 3], name="Fett's Gaderffii Stick"),  # Fett's Gaderffii Stick
            Weapon([0, 3, 0], pierce=1, name="Fett's EE-3 Carbine"),  # Fett's EE-3 Carbine
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.IMPERVIOUS: True,
        # Warnings: No range found
    },
    'cassianandor': {
        Props.NAME: 'Cassian Andor',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 2], name="Advanced Combat Training"),  # Advanced Combat Training
            Weapon([2, 0, 1], pierce=1, name="Cassian's Covert Blaster"),  # Cassian's Covert Blaster
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
    },
    'chewbacca': {
        Props.NAME: 'Chewbacca',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 4], name="Overwhelm"),  # Overwhelm
            Weapon([2, 0, 2], impacts=1, pierce=1, name="Chewbacca's Bowcaster"),  # Chewbacca's Bowcaster
        ],
        Props.SAVES: DefenseDice.WHITE,
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
    'jynerso': {
        Props.NAME: 'Jyn Erso',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 4, 0], name="Collapsible Tonfa"),  # Collapsible Tonfa
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
    },
    'k2so': {
        Props.NAME: 'K-2SO',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 4], name="Overpower"),  # Overpower
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.ARMOR: 1,
    },
    'lukeskywalkeroperative': {
        Props.NAME: 'Luke Skywalker (Operative)',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 7, 0], impacts=2, pierce=2, name="Luke's Lightsaber"),  # Luke's Lightsaber
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
    },
    'r2d2': {
        Props.NAME: 'R2-D2',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([3, 0, 0], name="Electro-Shock"),  # Electro-Shock
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
    },
    'sabinewren': {
        Props.NAME: 'Sabine Wren',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Combat Expertise"),  # Combat Expertise
            Weapon([1, 1, 1], pierce=1, name="Dual Westar-35 Blaster Pistols"),  # Dual Westar-35 Blaster Pistols
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.IMPERVIOUS: True,
        # Warnings: No range found
    },

    # ===== CORPS =====
    'ewokskirmishers': {
        Props.NAME: 'Ewok Skirmishers',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Spear"),  # Spear
            Weapon([0, 0, 1], impacts=1, pierce=1, name="Axe Ewok"),  # Axe Ewok
        ],
        Props.SAVES: DefenseDice.WHITE,
    },
    'fleettroopers': {
        Props.NAME: 'Fleet Troopers',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([2, 0, 0], name="DH-17 Blaster Pistol"),  # DH-17 Blaster Pistol
            Weapon([2, 1, 0], impacts=2, name="MPL-57 Barrage Trooper"),  # MPL-57 Barrage Trooper
            Weapon([0, 0, 2], pierce=1, name="Scatter Gun Trooper"),  # Scatter Gun Trooper
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
    'rebeltroopers': {
        Props.NAME: 'Rebel Troopers',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 1, 0], name="A-280 Blaster Rifle"),  # A-280 Blaster Rifle
            Weapon([0, 0, 2], impacts=1, name="MPL-57 Ion Trooper"),  # MPL-57 Ion Trooper
            Weapon([6, 0, 0], name="Z-6 Trooper"),  # Z-6 Trooper
            Weapon([2, 0, 2], impacts=1, name="SX-21 Trooper"),  # SX-21 Trooper
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
    },
    'rebelveterans': {
        Props.NAME: 'Rebel Veterans',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 1, 0], name="A-280 Blaster Rifle"),  # A-280 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
    },
    'markiimediumblastertrooper': {
        Props.NAME: 'Mark II Medium Blaster Trooper',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 1, 0], name="A-280 Blaster Rifle"),  # A-280 Blaster Rifle
            Weapon([0, 4, 0], name="Mark II Medium Blaster"),  # Mark II Medium Blaster
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found, No range found
    },

    # ===== SPECIAL FORCES =====
    'ewokslingers': {
        Props.NAME: 'Ewok Slingers',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 0, 0], name="Stones"),  # Stones
            Weapon([0, 1, 0], name="Slings"),  # Slings
            Weapon([0, 0, 0], name="Primitive"),  # Primitive
            Weapon([0, 0, 1], impacts=1, pierce=1, name="Axe Ewok"),  # Axe Ewok
        ],
        Props.SAVES: DefenseDice.WHITE,
        # Warnings: No range found, No dice pool found
    },
    'mandalorianresistance': {
        Props.NAME: 'Mandalorian Resistance',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 0], name="Combat Training"),  # Combat Training
            Weapon([0, 2, 0], name="Westar 35 Blaster Pistols"),  # Westar 35 Blaster Pistols
            Weapon([0, 0, 2], pierce=1, name="Beskad Duelist"),  # Beskad Duelist
            Weapon([0, 2, 0], pierce=1, name="Tristan Wren"),  # Tristan Wren
            Weapon([1, 1, 1], name="Ursa Wren"),  # Ursa Wren
            Weapon([0, 0, 1], impacts=1, name="Jetpack Rockets"),  # Jetpack Rockets
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.IMPERVIOUS: True,
        # Warnings: No range found
    },
    'mandalorianresistanceclanwren': {
        Props.NAME: 'Mandalorian Resistance (Clan Wren)',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Combat Expertise"),  # Combat Expertise
            Weapon([0, 0, 0], name="Keywords"),  # Keywords
            Weapon([0, 2, 0], name="Westar 35 Blaster Pistols"),  # Westar 35 Blaster Pistols
        ],
        Props.SAVES: DefenseDice.RED,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.IMPERVIOUS: True,
        # Warnings: No dice pool found, No range found
    },
    'rebelcommandos': {
        Props.NAME: 'Rebel Commandos',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 1, 0], name="A-280 Blaster Rifle"),  # A-280 Blaster Rifle
            Weapon([2, 0, 1], impacts=1, name="Proton Charge Saboteur"),  # Proton Charge Saboteur
            Weapon([1, 1, 0], pierce=1, name="DH-447 Sniper"),  # DH-447 Sniper
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
    },
    'rebelcommandosstriketeam': {
        Props.NAME: 'Rebel Commandos Strike Team',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 1, 0], name="A-280 Blaster Rifle"),  # A-280 Blaster Rifle
            Weapon([2, 0, 1], impacts=1, name="Proton Charge Saboteur"),  # Proton Charge Saboteur
            Weapon([1, 1, 0], pierce=1, name="DH-447 Sniper"),  # DH-447 Sniper
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
    },
    'rebelpathfinders': {
        Props.NAME: 'Rebel Pathfinders',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([2, 0, 0], name="A-300 Blaster Rifle"),  # A-300 Blaster Rifle
            Weapon([1, 0, 1], name="A-300 Short Range/Long Range Config"),  # A-300 Short Range/Long Range Config
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
    },
    'wookieewarriorsfreedomfighters': {
        Props.NAME: 'Wookiee Warriors (Freedom Fighters)',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 0, 0], name="Ryyk Blade"),  # Ryyk Blade
            Weapon([1, 1, 0], name="Kashyyyk Pistol"),  # Kashyyyk Pistol
            Weapon([0, 2, 2], name="Battle Shield Wookiee"),  # Battle Shield Wookiee
            Weapon([1, 0, 1], impacts=1, pierce=1, name="Bowcaster Wookiee"),  # Bowcaster Wookiee
            Weapon([0, 2, 0], name="Long Gun Wookiee"),  # Long Gun Wookiee
        ],
        Props.SAVES: DefenseDice.WHITE,
        # Warnings: No range found
    },
    'wookieewarriorskashyyykresistance': {
        Props.NAME: 'Wookiee Warriors (Kashyyyk Resistance)',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 0], name="Combat Training"),  # Combat Training
            Weapon([2, 0, 0], name="X1 Carbine"),  # X1 Carbine
            Weapon([0, 2, 2], name="Battle Shield Wookiee"),  # Battle Shield Wookiee
            Weapon([1, 0, 1], impacts=1, pierce=1, name="Bowcaster Wookiee"),  # Bowcaster Wookiee
            Weapon([0, 2, 0], name="Long Gun Wookiee"),  # Long Gun Wookiee
        ],
        Props.SAVES: DefenseDice.WHITE,
        # Warnings: No range found
    },

    # ===== SUPPORT =====
    '14fdlasercannonteam': {
        Props.NAME: '1.4 FD Laser Cannon Team',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Unarmed"),  # Unarmed
            Weapon([4, 0, 0], name="DH-17 Blaster Pistols"),  # DH-17 Blaster Pistols
            Weapon([0, 5, 0], impacts=2, name="1.4 FD Laser Cannon"),  # 1.4 FD Laser Cannon
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found, No range found
    },
    'atrt': {
        Props.NAME: 'AT-RT',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 3], impacts=1, name="Grappling Claws"),  # Grappling Claws
            Weapon([2, 0, 0], name="A-300 Blaster Rifle"),  # A-300 Blaster Rifle
            Weapon([0, 2, 0], name="AT-RT Flamethrower"),  # AT-RT Flamethrower
            Weapon([0, 2, 1], impacts=3, name="AT-RT Laser Cannon"),  # AT-RT Laser Cannon
            Weapon([0, 5, 0], name="AT-RT Rotary Blaster"),  # AT-RT Rotary Blaster
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.ARMOR: 1,
        # Warnings: No range found
    },
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
    'tauntaunriders': {
        Props.NAME: 'Tauntaun Riders',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 2, 0], name="Horns & Hind Claws"),  # Horns & Hind Claws
            Weapon([0, 0, 2], name="DL-44 Blaster Pistol"),  # DL-44 Blaster Pistol
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
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
    'chewbaccaletthewookieewin': {
        Props.NAME: 'Chewbacca (Let the Wookiee Win)',
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
    't47airspeeder': {
        Props.NAME: 'T-47 Airspeeder',
        Props.RANK: 'heavy',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 3, 3], impacts=3, name="AP/11 Double Laser Cannon"),  # AP/11 Double Laser Cannon
            Weapon([0, 4, 0], name="Ax-108 “Ground Buzzer”"),  # Ax-108 “Ground Buzzer”
            Weapon([0, 0, 1], impacts=1, name="Mo/DK Power Harpoon"),  # Mo/DK Power Harpoon
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.ARMOR: 1,
        Props.COVER_IMPROVEMENT: 1,
    },
    'x34landspeeder': {
        Props.NAME: 'X-34 Landspeeder',
        Props.RANK: 'heavy',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 0, 0], name="Driver's DH-17 Blaster Pistol"),  # Driver's DH-17 Blaster Pistol
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.ARMOR: 2,
        Props.COVER_IMPROVEMENT: 1,
    },
}
