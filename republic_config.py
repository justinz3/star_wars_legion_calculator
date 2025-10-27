from unit_config_properties import UnitProperties as Props
from dice import DefenseDice, MAX_DICE_ROLLED
from weapon import Weapon
from constants import UNLIMITED_TOKENS
from constants import UNLIMITED_TOKENS

republic_config = {

    # ===== COMMANDER =====
    'anakinskywalker': {
        Props.NAME: 'Anakin Skywalker',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 5], impacts=3, pierce=3, name="Anakin's Lightsaber"),  # Anakin's Lightsaber
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
    },
    'chewbaccarepublic': {
        Props.NAME: 'Chewbacca (Republic)',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 4], name="Overwhelm"),  # Overwhelm
            Weapon([2, 0, 2], impacts=1, criticals=1, pierce=1, name="Chewbacca's Bowcaster"),  # Chewbacca's Bowcaster
        ],
        Props.SAVES: DefenseDice.WHITE,
        # Warnings: No range found
    },
    'clonecaptainrex': {
        Props.NAME: 'Clone Captain Rex',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 2], name="Advanced Combat Training"),  # Advanced Combat Training
            Weapon([0, 0, 3], name="Dual DC-17 Hand Blasters"),  # Dual DC-17 Hand Blasters
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'clonecommander': {
        Props.NAME: 'Clone Commander',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 2], name="Advanced Combat Training"),  # Advanced Combat Training
            Weapon([0, 3, 0], name="Commander's DC-15 Blaster Rifle"),  # Commander's DC-15 Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'clonecommandercody': {
        Props.NAME: 'Clone Commander Cody',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 2], name="Advanced Combat Training"),  # Advanced Combat Training
            Weapon([1, 1, 2], name="Cody's DC-15a Blaster"),  # Cody's DC-15a Blaster
        ],
        Props.SAVES: DefenseDice.RED,
        Props.COVER_IMPROVEMENT: 1,
        # Warnings: No range found
    },
    'obiwankenobi': {
        Props.NAME: 'Obi-Wan Kenobi',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 2, 2], impacts=2, criticals=2, pierce=2, name="Obi-Wan's Lightsaber"),  # Obi-Wan's Lightsaber
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMMUNE_PIERCE: True,
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
    'wookieechieftain': {
        Props.NAME: 'Wookiee Chieftain',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 2, 2], name="Ancestral Weapon"),  # Ancestral Weapon
            Weapon([0, 4, 0], impacts=1, pierce=1, name="Chieftain's Bowcaster"),  # Chieftain's Bowcaster
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
    },
    'yoda': {
        Props.NAME: 'Yoda',
        Props.RANK: 'commander',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 4], impacts=2, pierce=2, name="Yoda's Lightsaber"),  # Yoda's Lightsaber
            Weapon([0, 4, 0], name="Force Wave"),  # Force Wave
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.IMMUNE_PIERCE: True,
        # Warnings: No range found
    },

    # ===== OPERATIVE =====
    'padmamidala': {
        Props.NAME: 'Padmé Amidala',
        Props.RANK: 'operative',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 3, 0], name="Martial Arts"),  # Martial Arts
            Weapon([0, 3, 0], pierce=1, name="Padmé's ELG-3A Blaster Pistol"),  # Padmé's ELG-3A Blaster Pistol
            Weapon([1, 0, 1], pierce=1, name="Looted E-5 Blaster"),  # Looted E-5 Blaster
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        # Warnings: No range found
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

    # ===== CORPS =====
    'phaseiclonetroopers': {
        Props.NAME: 'Phase I Clone Troopers',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 1, 0], name="DC-15A Blaster Rifle"),  # DC-15A Blaster Rifle
            Weapon([6, 0, 0], name="Z-6 Phase I Trooper"),  # Z-6 Phase I Trooper
            Weapon([0, 0, 2], criticals=1, name="DC-15 Phase I Trooper"),  # DC-15 Phase I Trooper
            Weapon([1, 2, 0], pierce=1, name="DP-23 Phase I Trooper"),  # DP-23 Phase I Trooper
            Weapon([1, 1, 1], impacts=2, name="RPS-6 Phase I Trooper"),  # RPS-6 Phase I Trooper
        ],
        Props.SAVES: DefenseDice.RED,
        # Warnings: No range found
    },
    'phaseiiclonetroopers': {
        Props.NAME: 'Phase II Clone Troopers',
        Props.RANK: 'corps',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="Unarmed"),  # Unarmed
            Weapon([0, 1, 0], name="DC-15A Blaster Rifle"),  # DC-15A Blaster Rifle
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
    'arctroopers': {
        Props.NAME: 'ARC Troopers',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 0], name="Combat Training"),  # Combat Training
            Weapon([1, 1, 0], name="DC-17 Hand Blasters"),  # DC-17 Hand Blasters
            Weapon([1, 1, 0], name="DC-15A Blaster Rifle"),  # DC-15A Blaster Rifle
            Weapon([0, 1, 1], criticals=1, name="DC-15x ARC Trooper"),  # DC-15x ARC Trooper
            Weapon([0, 3, 0], name="Fives"),  # Fives
            Weapon([0, 0, 2], criticals=1, name="Echo"),  # Echo
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMPERVIOUS: True,
        # Warnings: No range found, No range found
    },
    'arctroopersstriketeam': {
        Props.NAME: 'ARC Troopers (Strike Team)',
        Props.RANK: 'special forces',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 0], name="Combat Training"),  # Combat Training
            Weapon([1, 1, 0], name="DC-17 Hand Blasters"),  # DC-17 Hand Blasters
            Weapon([1, 1, 0], name="DC-15A Blaster Rifle"),  # DC-15A Blaster Rifle
        ],
        Props.SAVES: DefenseDice.RED,
        Props.IMPERVIOUS: True,
        # Warnings: No range found, No range found
    },
    'wookieewarriorskashyyykdefenders': {
        Props.NAME: 'Wookiee Warriors (Kashyyyk Defenders)',
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
    'wookieewarriorsnoblefighters': {
        Props.NAME: 'Wookiee Warriors (Noble Fighters)',
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

    # ===== SUPPORT =====
    'atrtgalacticrepublic': {
        Props.NAME: 'AT-RT (Galactic Republic)',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 0, 3], impacts=1, name="Grappling Claws"),  # Grappling Claws
            Weapon([2, 1, 0], impacts=1, criticals=1, name="Merr-Sonn RPC-2 Rocket Launcher"),  # Merr-Sonn RPC-2 Rocket Launcher
            Weapon([0, 2, 0], name="AT-RT Flamethrower"),  # AT-RT Flamethrower
            Weapon([0, 2, 1], impacts=3, name="AT-RT Laser Cannon"),  # AT-RT Laser Cannon
            Weapon([0, 5, 0], name="AT-RT Rotary Blaster"),  # AT-RT Rotary Blaster
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.ARMOR: 1,
        # Warnings: No range found
    },
    'barcspeeder': {
        Props.NAME: 'BARC Speeder',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 1, 0], name="DC-15A Blaster Rifle"),  # DC-15A Blaster Rifle
            Weapon([1, 1, 1], name="Twin Light Blaster Cannons"),  # Twin Light Blaster Cannons
            Weapon([0, 0, 0], name="Fixed: Front"),  # Fixed: Front
            Weapon([1, 1, 1], impacts=2, name="BARC RPS-6 Gunner"),  # BARC RPS-6 Gunner
            Weapon([1, 3, 0], impacts=1, name="BARC Ion Gunner"),  # BARC Ion Gunner
            Weapon([2, 2, 0], name="BARC Twin Laser Gunner"),  # BARC Twin Laser Gunner
        ],
        Props.SAVES: DefenseDice.RED,
        Props.COVER_IMPROVEMENT: 1,
        # Warnings: No range found, No dice pool found
    },
    'clonecommandos': {
        Props.NAME: 'Clone Commandos',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Gauntlet Vibroblade"),  # Gauntlet Vibroblade
            Weapon([1, 1, 0], name="DC17m ICWS Blaster Carbine"),  # DC17m ICWS Blaster Carbine
            Weapon([0, 2, 1], impacts=1, name="DC-17m ICWS Sniper/Anti-Armor Config"),  # DC-17m ICWS Sniper/Anti-Armor Config
        ],
        Props.SAVES: DefenseDice.RED,
        Props.ARMOR: 1,
        Props.SHIELDS: 1,
        # Warnings: No range found
    },
    'clonecommandosdeltasquad': {
        Props.NAME: 'Clone Commandos (Delta Squad)',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="Gauntlet Vibroblade"),  # Gauntlet Vibroblade
            Weapon([0, 2, 0], name="DC17m ICWS Blaster Carbine"),  # DC17m ICWS Blaster Carbine
            Weapon([0, 2, 1], impacts=1, name="DC-17m ICWS Sniper/Anti-Armor Config"),  # DC-17m ICWS Sniper/Anti-Armor Config
        ],
        Props.SAVES: DefenseDice.RED,
        Props.ARMOR: 1,
        Props.SHIELDS: 1,
        # Warnings: No range found
    },
    'raddaughgnaspfluttercraft': {
        Props.NAME: 'Raddaugh Gnasp Fluttercraft',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 0], name="Pilot's Kashyyyk Pistol"),  # Pilot's Kashyyyk Pistol
            Weapon([2, 0, 2], name="Gnasp Bombardier"),  # Gnasp Bombardier
            Weapon([0, 2, 2], impacts=1, pierce=1, name="Gnasp Gunner"),  # Gnasp Gunner
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
    },
    'raddaughgnaspfluttercraftattackcraft': {
        Props.NAME: 'Raddaugh Gnasp Fluttercraft (Attack Craft)',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([1, 1, 0], name="Pilot's Kashyyyk Pistol"),  # Pilot's Kashyyyk Pistol
            Weapon([2, 0, 2], name="Gnasp Bombardier"),  # Gnasp Bombardier
            Weapon([0, 2, 2], impacts=1, pierce=1, name="Gnasp Gunner"),  # Gnasp Gunner
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
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
    'laatlepatroltransport': {
        Props.NAME: 'LAAT/le Patrol Transport',
        Props.RANK: 'support',
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
    'tx130saberclassfightertank': {
        Props.NAME: 'TX-130 Saber-class Fighter Tank',
        Props.RANK: 'support',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([2, 2, 2], impacts=2, criticals=1, name="Twin Lateral GA-6n Laser Cannons"),  # Twin Lateral GA-6n Laser Cannons
            Weapon([0, 3, 0], criticals=1, name="TX-130 Twin Laser Turret"),  # TX-130 Twin Laser Turret
            Weapon([0, 0, 2], name="TX-130 Beam Cannon Turret"),  # TX-130 Beam Cannon Turret
        ],
        Props.SAVES: DefenseDice.RED,
        Props.ARMOR: 1,
    },

    # ===== HEAVY =====
    'infantrysupportplatform': {
        Props.NAME: 'Infantry Support Platform',
        Props.RANK: 'heavy',
        Props.SIZE: 1,
        Props.WEAPONS: [
            Weapon([0, 2, 0], name="DC-15 Blaster Rifles"),  # DC-15 Blaster Rifles
            Weapon([2, 0, 2], name="Twin Beam Cannons"),  # Twin Beam Cannons
            Weapon([0, 6, 0], criticals=2, name="Twin Blaster Cannons"),  # Twin Blaster Cannons
            Weapon([0, 0, 4], impacts=2, name="Twin Missile Pods"),  # Twin Missile Pods
        ],
        Props.SAVES: DefenseDice.WHITE,
        Props.BLOCK_SURGES: UNLIMITED_TOKENS,
        Props.ARMOR: 3,
        Props.COVER_IMPROVEMENT: 1,
    },
}
