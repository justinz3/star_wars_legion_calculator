from unit import Unit
from distribution import DamageDistribution
from constants import COVER_NONE, COVER_LIGHT, COVER_HEAVY

class SWLegion:
    @staticmethod
    def attack(attacker_ids, defender_id, weapons=None, attacker_minis=None,
            attack_only=False, reroll_hits=False, reroll_surges=True,
            aims=0, precise=0, attack_hit_surges=0, criticals=0, impacts=0, pierce=0, improvements=0,
            dodges=0, cover=COVER_NONE, shields=0, defense_surges=0, defender_minis=0,
            ignore_dodges=False, bypass_immune_pierce=False):
        attackers = [Unit(attacker_id) for attacker_id in attacker_ids]
        defender = Unit(defender_id)
        defender_minis = defender.size if defender_minis == 0 else defender_minis
        
        weapons = [0] * len(attackers) if weapons is None else weapons + [0] * max(len(attackers) - len(weapons), 0)
        attacker_minis = [0] * len(attackers) if attacker_minis is None else attacker_minis + [0] * max(len(attackers) - len(attacker_minis), 0)
        weapon_pool = SWLegion.join_attacker_weapons(attackers, weapons, attacker_minis, defender_minis)
        
        # Modify Weapon pool with inputs
        weapon_pool.aims += aims
        weapon_pool.hit_surges += attack_hit_surges
        weapon_pool.criticals += criticals
        weapon_pool.impacts += impacts
        weapon_pool.precise += precise
        weapon_pool.pierce += pierce
        weapon_pool.improvements += improvements
        
        # Join Attack Distributions 
        pooled_attack_distribution = Unit.get_attack_distribution(weapon_pool, reroll_hits=reroll_hits, reroll_surges=reroll_surges) # TODO port into this file
        
        if(attack_only):
            wound_distribution = Unit.convert_attack_distribution_to_damage_distribution(pooled_attack_distribution) # TODO port into this file
        else:
            # Apply Damage
            wound_distribution = defender.defend(pooled_attack_distribution, dodges=dodges, cover=cover,
                                                shields=shields, defense_surges=defense_surges, pierce=weapon_pool.pierce,
                                                ignore_dodges=ignore_dodges, bypass_immune_pierce=bypass_immune_pierce)
        
        # Print modifier text (for when manually modified results)
        modifiers = ""
        if(attack_only):
            modifiers += "-- SKIPPING DEFENSE STEPS (Only showing attack damage) "
        if(sum(weapons)):
            modifiers += "-- Using weapons {} ".format(weapons)
        if(sum(attacker_minis)):
            modifiers += "-- Unit sizes {} ".format(attacker_minis)
        if(aims):
            modifiers += "-- {} Aims ".format(aims)
        if(precise):
            modifiers += "-- {} Precises ".format(precise)
        if(attack_hit_surges):
            modifiers += "-- {} Surge-to-Hits ".format(attack_hit_surges)
        if(criticals):
            modifiers += "-- {} Criticals ".format(criticals)
        if(impacts):
            modifiers += "-- Impact {} ".format(impacts)
        if(pierce):
            modifiers += "-- Pierce {} ".format(pierce)
        if(improvements):
            modifiers += "-- {} Attack Dice Improvements ".format(improvements)
        if(cover == COVER_LIGHT):
            modifiers += "-- Light Cover "
        elif(cover == COVER_HEAVY):
            modifiers += "-- Heavy Cover "
        if(dodges):
            modifiers += "-- {} Dodges ".format(dodges)
        if(ignore_dodges):
            modifiers += "-- High Velocity (Ignores Dodges) "
        if(shields):
            modifiers += "-- {} Shields ".format(shields)
        if(defense_surges):
            modifiers += "-- {} Surge-to-Blocks ".format(defense_surges)
        if(bypass_immune_pierce):
            modifiers += "-- Makashi Mastery (Bypasses Immune: Pierce) "
            
        DamageDistribution(wound_distribution, ' + '.join([attacker.name for attacker in attackers]), defender.name, modifiers=modifiers)
    
    @staticmethod
    def join_attacker_weapons(attackers, weapons, attacker_mini_counts, defender_minis=1):
        weapon_pool = attackers[0].get_attack_dice(weapons[0], attacker_mini_counts[0])
        if(attackers[0].weapons[weapons[0]].spray):
            for i in range(defender_minis - 1):
                weapon_pool.add_to_pool(attackers[0].get_attack_dice(weapons[0], attackers[0].size))
        
        attackers = attackers[1:]
        weapons = weapons[1:]
        attacker_mini_counts = attacker_mini_counts[1:]
        for attacker, weapon, attacker_minis in zip(attackers, weapons, attacker_mini_counts):
            weapon_pool.add_to_pool(attacker.get_attack_dice(weapon, attacker_minis))
            if(attacker.weapons[weapon].spray):
                for i in range(defender_minis - 1):
                    weapon_pool.add_to_pool(attacker.get_attack_dice(weapon, attacker_minis))
        return weapon_pool
                            

# Wesnoth Style Damage Distribution
# DamageDistribution([0.3, 0.7], "Mage", "Ghost")

# Aim testing
#SWLegion.attack(['b1'], 'p1', attacker_minis=[6], dodges=0, aims=0, attack_only=True)
#SWLegion.attack(['b1'], 'p1', attacker_minis=[6], dodges=0, aims=1, attack_only=True)
#SWLegion.attack(['b1'], 'p1', attacker_minis=[6], dodges=0, aims=2, attack_only=True)
#SWLegion.attack(['b1'], 'p1', attacker_minis=[8], dodges=0, attack_only=True)
#SWLegion.attack(['b1'], 'p1', attacker_minis=[10], dodges=0, attack_only=True)
#SWLegion.attack(['p1'], 'dekas', dodges=2, shields=-4, attack_only=True) # Wheel mode
#SWLegion.attack(['p1'], 'dekas', dodges=2, shields=-4, attack_only=True, aims=1) # Wheel mode
#SWLegion.attack(['p1'], 'dekas', dodges=2, shields=-4, attack_only=True, aims=2) # Wheel mode
#SWLegion.attack(['p1'], 'dekas', dodges=2, shields=-4, attack_only=True, aims=3) # Wheel mode

# Note to User:
# Implement Arsenal (and Fire Support) by including more attackers in the attack pool
# Implement Cover by incrementing dodges (Likewise, Implement Blast by not adding dodges for Cover)

# Sanity tests for Debugging
#SWLegion.attack(['p1'], 'dekas', dodges=2, shields=-4, attack_only=True) # Wheel mode
#SWLegion.attack(['p1'], 'dekas', dodges=2, shields=-4, improvements=1, attack_only=True) # Wheel mode
#SWLegion.attack(['p1'], 'dekas', dodges=2, shields=-4, improvements=2, attack_only=True) # Wheel mode
#SWLegion.attack(['p1'], 'dekas', dodges=2, shields=-4, improvements=3, attack_only=True) # Wheel mode
#SWLegion.attack(['p1'], 'dekas', dodges=2, shields=-4, improvements=4, attack_only=True) # Wheel mode
#SWLegion.attack(['p1'], 'dekas', dodges=2, shields=-4, improvements=8, attack_only=True) # Wheel mode
#SWLegion.attack(['p1'], 'dekas', dodges=2, shields=-4, improvements=8, reroll_hits=True, attack_only=True) # Wheel mode

#SWLegion.attack(['p1'], 'dekas', dodges=2, shields=-4, attack_only=False) # Wheel mode
#SWLegion.attack(['p1'], 'dekas', shields=-4, attack_only=False) # No shield
#SWLegion.attack(['p1'], 'dekas') # Full shield
#SWLegion.attack(['p1'], 'dekas', attack_only=True) # Full shield
#SWLegion.attack(['p1', 'p1'], 'dekas') # Full shield
#SWLegion.attack(['p1', 'p1'], 'dekas', attack_only=True) # Full shield


# Deka Killing Power tests
#SWLegion.attack(['dekas'], 'p1', dodges=0)
#SWLegion.attack(['dekas'], 'p1', dodges=2)
#SWLegion.attack(['dekas', 'dekas'], 'p1', dodges=0)
#SWLegion.attack(['dekas', 'dekas'], 'p1', dodges=2)

# Order 66 Experiments
#SWLegion.attack(['p1'], 'ob')
#SWLegion.attack(['p1', 'p1'], 'ob')
#SWLegion.attack(['p1', 'p1', 'p1z6', 'p1dc15'], 'ob')
#SWLegion.attack(['p1', 'p1', 'p1z6', 'p1dc15'], 'ob', attacker_minis=[5,5])
#SWLegion.attack(['p1', 'p1'], 'ob', attacker_minis=[6,6])
#SWLegion.attack(['ob'], 'p1', pierce=0)
#SWLegion.attack(['ob'], 'p1', pierce=-2)

# Phase I Heavy Weapon Experiments 
#SWLegion.attack(['p1'], 'b1', attack_only=False)
#SWLegion.attack(['p1', 'p1z6'], 'b1', attack_only=False)
#SWLegion.attack(['p1', 'p1dc15'], 'b1', attack_only=False)
#SWLegion.attack(['p1'], 'b1', attack_only=False, aims=1)
#SWLegion.attack(['p1', 'p1z6'], 'b1', attack_only=False, aims=1)
#SWLegion.attack(['p1', 'p1dc15'], 'b1', attack_only=False, aims=1)
#SWLegion.attack(['p1'], 'b1', attack_only=False, aims=2)
#SWLegion.attack(['p1', 'p1z6'], 'b1', attack_only=False, aims=2)
#SWLegion.attack(['p1', 'p1dc15'], 'b1', attack_only=False, aims=2)
#SWLegion.attack(['p1', 'p1z6'], 'b1', attack_only=False, criticals=100)
#SWLegion.attack(['p1', 'p1dc15'], 'b1', attack_only=False, criticals=100)
#SWLegion.attack(['p1', 'p1', 'p1z6', 'p1z6'], 'b1')
#SWLegion.attack(['p1', 'p1', 'p1dc15', 'p1dc15'], 'b1')
#SWLegion.attack(['p1', 'p1', 'p1z6', 'p1dc15'], 'b1')

if __name__ == '__main__':
    # New Imperial and Rebel Units Tests
    print("\n=== NEW IMPERIAL & REBEL UNITS TESTS ===\n")

    # Imperial tests
    print("Darth Vader vs Luke Skywalker:")
    SWLegion.attack(['vader'], 'luke')

    print("\nBoba Fett vs Han Solo (EE-3 Carbine):")
    SWLegion.attack(['boba'], 'han', weapons=[2])
    
    print("\nStormtroopers vs Rebel Troopers:")
    SWLegion.attack(['storms'], 'rebels')
    
    print("\nAT-ST vs Phase I Clones (Twin Blaster Cannon):")
    SWLegion.attack(['atst'], 'p1', weapons=[1])
    
    # Rebel tests
    print("\nLuke Skywalker vs Darth Vader (lightsaber):")
    SWLegion.attack(['luke'], 'vader', weapons=[0])
    
    print("\nHan Solo vs Stormtroopers (DL-44):")
    SWLegion.attack(['han'], 'storms', weapons=[1])
    
    print("\nChewbacca vs B2 Super Battle Droids (Bowcaster):")
    SWLegion.attack(['chewie'], 'b2', weapons=[1])
    
    print("\nRebel Commandos vs Scout Troopers:")
    SWLegion.attack(['rebelcommandos'], 'scouts')
    
    # Special Mechanics Tests
    print("\n=== SPECIAL MECHANICS TESTS ===\n")
    
    # Test Makashi Mastery (Bypass Immune: Pierce)
    print("Count Dooku vs Obi-Wan (normal - both have Immune: Pierce):")
    SWLegion.attack(['dooku'], 'ob', weapons=[0])
    
    print("\nCount Dooku vs Obi-Wan (WITH Makashi Mastery - bypasses Immune: Pierce BUT Pierce 2->1):")
    SWLegion.attack(['dooku'], 'ob', weapons=[0], bypass_immune_pierce=True, pierce=-1)
    
    print("\nCount Dooku vs Obi-Wan (Makashi without pierce reduction - for comparison):")
    SWLegion.attack(['dooku'], 'ob', weapons=[0], bypass_immune_pierce=True)
    
    # Test High Velocity (Ignore Dodges) - better example with Phase I Clones
    print("\nPhase II Clones vs Cad Bane (normal - 2 dodges):")
    SWLegion.attack(['p2'], 'cadbane')
    
    print("\nPhase II Clones vs Cad Bane (WITH High Velocity - ignores dodges):")
    SWLegion.attack(['p2'], 'cadbane', ignore_dodges=True)
    
    # Test both together
    print("\nCount Dooku vs Asajj Ventress (normal - she has 1 dodge and Immune: Pierce):")
    SWLegion.attack(['dooku'], 'ventress', weapons=[0])
    
    print("\nCount Dooku vs Asajj Ventress (Makashi + High Velocity - bypasses both):")
    SWLegion.attack(['dooku'], 'ventress', weapons=[0], bypass_immune_pierce=True, ignore_dodges=True)
    
    # New Separatist Units Tests
    print("\n=== NEW SEPARATIST UNITS TESTS ===\n")
    
    # Test new commanders
    #print("Count Dooku vs Obi-Wan (melee):")
    #SWLegion.attack(['dooku'], 'ob', weapons=[0])
    
    #print("\nCount Dooku vs Obi-Wan (lightning):")
    #SWLegion.attack(['dooku'], 'ob', weapons=[1])
    
    # Test new operatives
    print("\nAsajj Ventress vs Ahsoka:")
    SWLegion.attack(['ventress'], 'ahsoka')
    
    print("\nMaul vs Anakin:")
    SWLegion.attack(['maul'], 'anakin')
    
    print("\nCad Bane vs Phase I Clones (blasters):")
    SWLegion.attack(['cadbane'], 'p1', weapons=[1])
    
    # Test new corps
    print("\nB2 Super Battle Droids vs Phase I Clones (arm cannons):")
    SWLegion.attack(['b2'], 'p1', weapons=[1])
    
    print("\nGeonosian Warriors vs B1s (blasters):")
    SWLegion.attack(['geonosians'], 'b1', weapons=[1])
    
    # Test special forces
    print("\nBX Commandos vs Phase I Clones (rifles):")
    SWLegion.attack(['bx'], 'p1', weapons=[1])
    
    print("\nIG-100 MagnaGuards vs Obi-Wan (melee):")
    SWLegion.attack(['magnaguards'], 'ob', weapons=[0])
    
    # Test vehicles
    print("\nAAT Battle Tank vs TX-130 (artillery cannon):")
    SWLegion.attack(['aat'], 'tx130', weapons=[1])
    
    print("\nSTAP Riders vs Phase II Clones:")
    SWLegion.attack(['stap'], 'p2')
    
    # New Republic Units Tests
    print("\n=== NEW REPUBLIC UNITS TESTS ===\n")
    
    # Test new commanders
    #print("Anakin vs B1 Battle Droids:")
    #SWLegion.attack(['anakin'], 'b1')
    
    #print("\nAhsoka vs General Grievous:")
    #SWLegion.attack(['ahsoka'], 'gg')
    
    #print("\nYoda vs General Grievous (melee):")
    #SWLegion.attack(['yoda'], 'gg', weapons=[0])
    
    # Test new corps
    #print("\nPhase II Clones vs B1s:")
    #SWLegion.attack(['p2'], 'b1')
    
    #print("\nARC Troopers vs B1s (using blaster rifles):")
    #SWLegion.attack(['arc'], 'b1', weapons=[2])
    
    # Test vehicles
    #print("\nTX-130 vs Obi-Wan:")
    #SWLegion.attack(['tx130'], 'ob')
    
    #print("\nAT-RT vs B1s (melee):")
    #SWLegion.attack(['atrt'], 'b1', weapons=[0])
    
    print("\n=== COVER SYSTEM TESTS ===\n")
    
    # Basic cover test: Phase I vs B1s
    #print("Phase I Clones vs B1 Battle Droids - No Cover:")
    #SWLegion.attack(['p1'], 'b1')
    
    #print("\nPhase I Clones vs B1 Battle Droids - Light Cover:")
    #SWLegion.attack(['p1'], 'b1', cover=COVER_LIGHT)
    
    #print("\nPhase I Clones vs B1 Battle Droids - Heavy Cover:")
    #SWLegion.attack(['p1'], 'b1', cover=COVER_HEAVY)
    
    # BARC speeder cover improvement test
    #print("\nPhase I Clones vs BARC Speeder - No Cover (BARC has Cover 1, so becomes Light):")
    #SWLegion.attack(['p1'], 'barc')
    
    #print("\nPhase I Clones vs BARC Speeder - Light Cover (BARC improves to Heavy):")
    #SWLegion.attack(['p1'], 'barc', cover=COVER_LIGHT)
    
    # Cover + Dodges stacking test
    #print("\nPhase I Clones vs B1s - Light Cover + 1 Dodge:")
    #SWLegion.attack(['p1'], 'b1', cover=COVER_LIGHT, dodges=1)
    
    print("\n=== ORIGINAL TESTS ===\n")
    
    # Obi-Wan Experiments
    #SWLegion.attack(['ob'], 'gg')
    #SWLegion.attack(['ob'], 'b1')
    #SWLegion.attack(['ob'], 'dekas', shields=-4) # Melee
    #SWLegion.attack(['ob'], 'ob')
    #SWLegion.attack(['ob'], 'ob', dodges=1, defense_surges=100)
    #SWLegion.attack(['ob'], 'p1')
    #SWLegion.attack(['ob'], 'barc')
    
    # Grevious Experiments
    #SWLegion.attack(['gg', 'gg'], 'ob')
    #SWLegion.attack(['gg', 'gg'], 'ob', criticals=100)
    #SWLegion.attack(['gg', 'gg'], 'ob', criticals=100, aims=1) 
    #SWLegion.attack(['gg', 'gg'], 'ob', dodges=1, defense_surges=100) 
    #SWLegion.attack(['gg', 'gg'], 'p1') 
    #SWLegion.attack(['gg', 'gg'], 'barc') 
    #SWLegion.attack(['gg', 'gg'], 'gg') 
    #SWLegion.attack(['gg', 'gg'], 'b1') 
    #SWLegion.attack(['gg', 'gg'], 'dekas', shields=-4) # Melee 
    
    # B1 Battle Droid Experiments
    #SWLegion.attack(['b1'], 'b1')
    #SWLegion.attack(['b1'], 'b1', dodges=2)
    #SWLegion.attack(['b1'], 'p1')
    #SWLegion.attack(['b1'], 'p1', dodges=2)
    #SWLegion.attack(['b1', 'b1e5'], 'b1')
    #SWLegion.attack(['b1', 'b1e5'], 'b1', dodges=2)
    #SWLegion.attack(['b1', 'b1e5'], 'p1')
    #SWLegion.attack(['b1', 'b1e5'], 'p1', dodges=2)
    #SWLegion.attack(['b1', 'b1e6'], 'b1')
    #SWLegion.attack(['b1', 'b1e6'], 'b1', dodges=2)
    #SWLegion.attack(['b1', 'b1e6'], 'p1')
    #SWLegion.attack(['b1', 'b1e6'], 'p1', dodges=2)

