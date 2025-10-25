from math import comb

from config import unit_config
from dice import AttackDice, DefenseDice, NUM_ATTACK_DICE_FACES, NUM_DEFENSE_DICE_FACES, DicePool, get_attack_dice_distribution
from unit_config_properties import UnitProperties as Props
from weapon import Weapon

class Unit:
    def __init__(self, unit_id):
        config = unit_config[unit_id]
        self.name = config[Props.NAME]
        self.size = config[Props.SIZE]
        self.weapons = config[Props.WEAPONS]
        self.saves = config[Props.SAVES]
        self.attack_hit_surges = config[Props.HIT_SURGES] if Props.HIT_SURGES in config.keys() else 0
        self.attack_crit_surges = config[Props.CRIT_SURGES] if Props.CRIT_SURGES in config.keys() else 0
        self.impacts = config[Props.IMPACTS] if Props.IMPACTS in config.keys() else 0
        self.dodges = config[Props.DODGES] if Props.DODGES in config.keys() else 0
        self.defense_surges = config[Props.BLOCK_SURGES] if Props.BLOCK_SURGES in config.keys() else 0
        self.shields = config[Props.SHIELDS] if Props.SHIELDS in config.keys() else 0
        self.armor = config[Props.ARMOR] if Props.ARMOR in config.keys() else 0 
        self.immune_pierce = config[Props.IMMUNE_PIERCE] if Props.IMMUNE_PIERCE in config.keys() else False
        self.impervious = config[Props.IMPERVIOUS] if Props.IMPERVIOUS in config.keys() else False
    
    def get_defense_distribution(self, hits, crits, dodges=0, shields=0, defense_surges=0, pierce=0):
        remaining_shields = max(shields - crits, 0)
        incoming_wounds = max(crits - shields, 0)
        incoming_wounds += max(hits - dodges - self.armor - remaining_shields, 0)
        total_dice = incoming_wounds + pierce if self.impervious else incoming_wounds
        probability_blank = self.saves[0] / NUM_DEFENSE_DICE_FACES
        probability_block = self.saves[1] / NUM_DEFENSE_DICE_FACES
        probability_surge = self.saves[2] / NUM_DEFENSE_DICE_FACES
                
        distribution = [0] * (incoming_wounds + 1)
        for i in range(total_dice + 1): # blanks
            for j in range(total_dice + 1 - i): # blocks
                k = total_dice - i - j # surges
                total_blocks = j + min(defense_surges, k)
                total_blocks = total_blocks if self.immune_pierce else max(0, total_blocks - pierce)
                total_blocks = min(total_blocks, incoming_wounds)
                probability = comb(total_dice, i + j) * comb(i + j, i) * \
                    (probability_blank ** i) * (probability_block ** j) * (probability_surge ** k)
                distribution[incoming_wounds - total_blocks] += probability
        return distribution
    
    @staticmethod
    def get_attack_distribution(weapon_pool, reroll_hits=False, reroll_surges=True):
        white_dice_count = weapon_pool.dice_counts[0]
        black_dice_count = weapon_pool.dice_counts[1]
        red_dice_count = weapon_pool.dice_counts[2]
        
        white_distribution = get_attack_dice_distribution(AttackDice.WHITE, white_dice_count)
        black_distribution = get_attack_dice_distribution(AttackDice.BLACK, black_dice_count)
        red_distribution = get_attack_dice_distribution(AttackDice.RED, red_dice_count)
        
        total_dice_rolled = white_dice_count + black_dice_count + red_dice_count
        distribution = [[0] * (total_dice_rolled + 1) for a in range(total_dice_rolled + 1)]
        
        total_probability = 0
        for a in range(white_dice_count + 1): # white hits
            for b in range(white_dice_count + 1 - a): # white crits
                for c in range(white_dice_count + 1 - a - b): # white surges
                    for d in range(black_dice_count + 1): # black hits
                        for e in range(black_dice_count + 1 - d): # black crits
                            for f in range(black_dice_count + 1 - d - e): # black surges
                                for g in range(red_dice_count + 1): # red hits
                                    for h in range(red_dice_count + 1 - g): # red crits
                                        for i in range(red_dice_count + 1 - g - h): # red surges
                                            probability = white_distribution[a][b][c] * \
                                                black_distribution[d][e][f] * \
                                                red_distribution[g][h][i]
                                            #hits = a + d + g
                                            #crits = b + e + h
                                            #surges = c + f + i
                                            
                                            dice_pool = DicePool([white_dice_count - a - b - c, black_dice_count - d - e - f, red_dice_count - g - h - i], \
                                                [a, d, g], [b, e, h], [c, f, i], \
                                                aims=weapon_pool.aims, precise=weapon_pool.precise, \
                                                criticals=weapon_pool.criticals, hit_surges=weapon_pool.hit_surges, impacts=weapon_pool.impacts, \
                                                improvements=weapon_pool.improvements, reroll_hits=reroll_hits, reroll_surges=reroll_surges)
                                            
                                            dice_pool.modify_dice()
                                            dice_pool.improve_dice()
                                            
                                            hits = sum(dice_pool.hits)
                                            crits = sum(dice_pool.crits)
                                            surges = sum(dice_pool.surges)
                                            criticals = dice_pool.criticals
                                            hit_surges = dice_pool.hit_surges
                                            impacts = dice_pool.impacts
                                            improvements = dice_pool.improvements
                                            
                                            # Apply Aim/Precise rerolls
                                            # TODO Pick up to (2 + Precise) dice to reroll, and begin recursive rerolls until Aims are exhausted
                                            dice_pool.apply_aims(distribution, probability)
                                            
                                            # Greedy: Convert White Surges first, then Black, Red
                                            # Convert White Impacts first, then Black, then Red
                                            # Finally, take a boolean for reroll strategy (go for crits, or go for hits+crits), and reroll best dice that aren't optimal first
                                            # Each call of the recursive function takes a base probability (and dice state) and a reference to the existing distribution to modify
                                            # It will recurse (and deal with smaller and smaller probabilities) until aims reach 0 or no dice can be improved.
                                            # In the base-case, it will modify the distribution with the final dice-pool
                                            
                                            #distribution[hits][crits] += probability
                                            total_probability += probability
        return distribution
    
    def get_attack_dice(self, weapon=0, attacker_minis=0):
        attacker_minis = self.size if attacker_minis == 0 else attacker_minis
        return self.weapons[weapon] * attacker_minis
    
    @staticmethod
    def convert_attack_distribution_to_damage_distribution(attack_distribution):
        damage_distribution = [0] * len(attack_distribution)
        for i in range(len(attack_distribution)): # counting hits
            for j in range(len(attack_distribution) - i): # counting crits
                damage_distribution[i + j] += attack_distribution[i][j]
        return damage_distribution
    
    # For our purposes, we can equate cover with dodges
    def defend(self, attack_distribution, dodges=0, shields=0, defense_surges=0, pierce=0):
        dodges += self.dodges
        shields += self.shields
        defense_surges += self.defense_surges
        
        wound_distribution = [0] * len(attack_distribution)
        for i in range(len(attack_distribution)): # counting hits
            for j in range(len(attack_distribution[i]) - i): # counting crits
                defense_distribution = self.get_defense_distribution(i, j, dodges=dodges, shields=shields, defense_surges=defense_surges, pierce=pierce)
                for k, defense_prob in enumerate(defense_distribution):
                    temp = defense_prob * attack_distribution[i][j]
                    wound_distribution[k] += temp
        return wound_distribution
    
