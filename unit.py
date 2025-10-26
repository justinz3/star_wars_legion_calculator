from math import comb

from config import unit_config
from constants import COVER_NONE, COVER_LIGHT, COVER_HEAVY
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
        self.cover_improvement = config[Props.COVER_IMPROVEMENT] if Props.COVER_IMPROVEMENT in config.keys() else 0
        self.defense_surges = config[Props.BLOCK_SURGES] if Props.BLOCK_SURGES in config.keys() else 0
        self.shields = config[Props.SHIELDS] if Props.SHIELDS in config.keys() else 0
        self.armor = config[Props.ARMOR] if Props.ARMOR in config.keys() else 0
        self.immune_pierce = config[Props.IMMUNE_PIERCE] if Props.IMMUNE_PIERCE in config.keys() else False
        self.impervious = config[Props.IMPERVIOUS] if Props.IMPERVIOUS in config.keys() else False

    @staticmethod
    def get_cover_cancellation_distribution(hits, cover_level):
        """
        Calculate the probability distribution of hits cancelled by cover.
        Returns a list where index i = probability of cancelling i hits.

        Cover works by rolling 1 white defense die per hit:
        - Light cover: cancel on blocks only (1/6 probability)
        - Heavy cover: cancel on blocks + surges (2/6 probability)
        """
        if cover_level == COVER_NONE or hits == 0:
            return [1.0]  # No cancellations

        # White defense die: [4 blanks, 1 block, 1 surge] out of 6 faces
        if cover_level == COVER_LIGHT:
            cancel_probability = 1.0 / NUM_DEFENSE_DICE_FACES  # Blocks only
        elif cover_level == COVER_HEAVY:
            cancel_probability = 2.0 / NUM_DEFENSE_DICE_FACES  # Blocks + surges
        else:
            return [1.0]  # Invalid cover level

        no_cancel_probability = 1.0 - cancel_probability

        # Calculate binomial distribution for hits cancelled
        distribution = [0.0] * (hits + 1)
        for cancels in range(hits + 1):
            # P(k successes in n trials) = C(n,k) * p^k * (1-p)^(n-k)
            distribution[cancels] = comb(hits, cancels) * \
                (cancel_probability ** cancels) * \
                (no_cancel_probability ** (hits - cancels))

        return distribution

    def get_defense_distribution(self, hits, crits, dodges=0, shields=0, defense_surges=0, pierce=0,
                                 cover_level=COVER_NONE, ignore_dodges=False, bypass_immune_pierce=False):
        """
        Calculate the probability distribution of wounds after defense.

        Defense sequence:
        1. Apply cover (roll white dice to cancel hits)
        2. Apply shields (cancel crits first)
        3. Apply dodges and armor (cancel remaining hits) - skipped if ignore_dodges=True
        4. Roll defense dice for remaining wounds

        Args:
            ignore_dodges: If True, skip applying dodge tokens (e.g., High Velocity)
            bypass_immune_pierce: If True, ignore defender's Immune: Pierce (e.g., Makashi Mastery)
        """
        # Get cover cancellation distribution
        cover_distribution = Unit.get_cover_cancellation_distribution(hits, cover_level)

        # Calculate the maximum possible wounds (for sizing the output distribution)
        max_possible_wounds = hits + crits
        final_distribution = [0.0] * (max_possible_wounds + 1)

        # For each possible cover outcome, calculate defense and weight by probability
        for hits_cancelled, cover_prob in enumerate(cover_distribution):
            if cover_prob == 0:
                continue

            remaining_hits = hits - hits_cancelled

            # Apply shields (block crits first, then hits)
            remaining_shields = max(shields - crits, 0)
            incoming_wounds = max(crits - shields, 0)

            # Apply dodges and armor (can be skipped by High Velocity)
            effective_dodges = 0 if ignore_dodges else dodges
            incoming_wounds += max(remaining_hits - effective_dodges - self.armor - remaining_shields, 0)

            # Roll defense dice
            total_dice = incoming_wounds + pierce if self.impervious else incoming_wounds
            probability_blank = self.saves[0] / NUM_DEFENSE_DICE_FACES
            probability_block = self.saves[1] / NUM_DEFENSE_DICE_FACES
            probability_surge = self.saves[2] / NUM_DEFENSE_DICE_FACES

            for i in range(total_dice + 1): # blanks
                for j in range(total_dice + 1 - i): # blocks
                    k = total_dice - i - j # surges
                    total_blocks = j + min(defense_surges, k)

                    # Apply pierce to blocks (can bypass Immune: Pierce with Makashi Mastery)
                    is_immune_to_pierce = self.immune_pierce and not bypass_immune_pierce
                    total_blocks = total_blocks if is_immune_to_pierce else max(0, total_blocks - pierce)
                    total_blocks = min(total_blocks, incoming_wounds)

                    save_probability = comb(total_dice, i + j) * comb(i + j, i) * \
                        (probability_blank ** i) * (probability_block ** j) * (probability_surge ** k)

                    wounds = incoming_wounds - total_blocks
                    final_distribution[wounds] += cover_prob * save_probability

        return final_distribution
    
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
    
    def defend(self, attack_distribution, dodges=0, shields=0, defense_surges=0, pierce=0, cover=COVER_NONE,
              ignore_dodges=False, bypass_immune_pierce=False):
        """
        Calculate the wound distribution after all defense steps.

        Args:
            cover: Base cover level from terrain (0=none, 1=light, 2=heavy)
                   Will be improved by unit's cover_improvement ability
            ignore_dodges: If True, skip applying dodge tokens (e.g., High Velocity)
            bypass_immune_pierce: If True, ignore defender's Immune: Pierce (e.g., Makashi Mastery)
        """
        dodges += self.dodges
        shields += self.shields
        defense_surges += self.defense_surges

        # Apply unit's cover improvement ability
        cover_level = min(cover + self.cover_improvement, COVER_HEAVY)

        wound_distribution = [0] * len(attack_distribution)
        for i in range(len(attack_distribution)): # counting hits
            for j in range(len(attack_distribution[i]) - i): # counting crits
                defense_distribution = self.get_defense_distribution(i, j, dodges=dodges, shields=shields,
                                                                     defense_surges=defense_surges, pierce=pierce,
                                                                     cover_level=cover_level, ignore_dodges=ignore_dodges,
                                                                     bypass_immune_pierce=bypass_immune_pierce)
                for k, defense_prob in enumerate(defense_distribution):
                    temp = defense_prob * attack_distribution[i][j]
                    wound_distribution[k] += temp
        return wound_distribution
    
