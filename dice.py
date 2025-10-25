from math import comb

NUM_ATTACK_DICE_TYPES = 3
NUM_ATTACK_DICE_FACES = 8
class AttackDice:
    WHITE = [5,1,1,1] # blank, hit, crit, surge
    BLACK = [3,3,1,1]
    RED = [1,5,1,1]

NUM_DEFENSE_DICE_FACES = 6
class DefenseDice:
    WHITE = [4,1,1] # blank, block, surge
    RED = [2,3,1]

MAX_DICE_ROLLED = 100 # arbitrary maximum 

def get_attack_dice_distribution(attack_dice_type, dice_count):
    distribution = [[[0] * (dice_count + 1) for a in range(dice_count + 1)] for b in range(dice_count + 1)]
    
    probability_blank = attack_dice_type[0] / NUM_ATTACK_DICE_FACES
    probability_hit = attack_dice_type[1] / NUM_ATTACK_DICE_FACES
    probability_crit = attack_dice_type[2] / NUM_ATTACK_DICE_FACES
    probability_surge = attack_dice_type[3] / NUM_ATTACK_DICE_FACES
    
    total_probability = 0
    for i in range(dice_count + 1): # blanks
        for j in range(dice_count + 1 - i): # hits
            for k in range(dice_count + 1 - i - j): # crits
                l = dice_count - i - j - k # surges
                
                probability = comb(dice_count, i + j + k) * comb(i + j + k, i + j) * comb(i + j, i) * \
                    (probability_blank ** i) * (probability_hit ** j) * (probability_crit ** k) * (probability_surge ** l)
                distribution[j][k][l] = probability
                total_probability += probability
    return distribution

class DicePool:
    def __init__(self, blanks, hits, crits, surges, aims=0, precise=0, 
            criticals=0, hit_surges=0, impacts=0, improvements=0, reroll_hits=False, reroll_surges=True):
        self.blanks = blanks
        self.hits = hits
        self.crits = crits
        self.surges = surges
        self.aims = aims
        self.precise = precise
        self.criticals = criticals
        self.hit_surges = hit_surges
        self.impacts = impacts
        self.improvements = improvements
        self.reroll_hits = reroll_hits
        self.reroll_surges = reroll_surges
    
    def modify_dice(self):
        if(self.criticals > 0 and sum(self.surges) > 0):
            for i in range(NUM_ATTACK_DICE_TYPES): # Greedily improve white dice first
                surge_to_crit_count = min(self.surges[i], self.criticals)
                self.crits[i] += surge_to_crit_count
                self.surges[i] -= surge_to_crit_count
                self.criticals -= surge_to_crit_count
        
        if(not self.reroll_hits and self.hit_surges > 0 and sum(self.surges) > 0):
            for i in range(NUM_ATTACK_DICE_TYPES): # Greedily improve white dice first
                surge_to_hit_count = min(self.surges[i], self.hit_surges)
                self.hits[i] += surge_to_hit_count
                self.surges[i] -= surge_to_hit_count
                self.hit_surges -= surge_to_hit_count
        
        if(self.impacts > 0 and sum(self.hits) > 0):
            for i in range(NUM_ATTACK_DICE_TYPES): # Greedily improve white dice first
                impact_count = min(self.hits[i], self.impacts)
                self.crits[i] += impact_count
                self.hits[i] -= impact_count
                self.impacts -= impact_count
    
    def improve_dice(self):
        improvable_dice_count = sum(self.blanks) + (sum(self.hits) if self.reroll_hits else 0) 
            #  + (sum(self.surges) if self.reroll_surges else 0) # Rules say you can't reroll surges
        while(self.improvements > 0 and improvable_dice_count > 0):
            #print("blanks: " + str(self.blanks) + " hits: " + str(self.hits) + " crits: " + str(self.crits) + " surges: " + str(self.surges) + "improvements: " + str(self.improvements))
            if(self.reroll_hits and sum(self.hits) > 0):
                for i in range(NUM_ATTACK_DICE_TYPES): # Hit -> Crit improvement doesn't care about color
                    improvement_count = min(self.hits[i], self.improvements)
                    self.hits[i] -= improvement_count
                    self.crits[i] += improvement_count
                    self.improvements -= improvement_count
            
            if(sum(self.blanks) > 0):
                for i in range(NUM_ATTACK_DICE_TYPES): # Greedily improve white dice first
                    improvement_count = min(self.blanks[i], self.improvements)
                    self.blanks[i] -= improvement_count
                    self.hits[i] += improvement_count
                    self.improvements -= improvement_count
            
            improvable_dice_count = sum(self.blanks) + (sum(self.hits) if self.reroll_hits else 0) 
        #print("DONE blanks: " + str(self.blanks) + " hits: " + str(self.hits) + " crits: " + str(self.crits) + " surges: " + str(self.surges) + "improvements: " + str(self.improvements))

    # TODO Make more generic (with a count instead of aim and a base precision value) so can use for observations
    def apply_aims(self, distribution, base_probability=1.0):
        if(self.aims == 0):
            distribution[sum(self.hits)][sum(self.crits)] += base_probability
            return
        
        #print("AIMING")
        #print(self.blanks, self.hits, self.crits, self.surges, base_probability)
        
        self.aims -= 1
        rerolls = 2 + self.precise
        
        dice_counts = [0] * NUM_ATTACK_DICE_TYPES
        # Greedily reroll suboptimal best dice first
        for i in range(NUM_ATTACK_DICE_TYPES - 1, -1, -1):
            if(rerolls == 0):
                break
                
            #print("i: ", i, rerolls)
        
            blanks_to_reroll = min(rerolls, self.blanks[i])
            rerolls -= blanks_to_reroll
            self.blanks[i] -= blanks_to_reroll
            dice_counts[i] += blanks_to_reroll
            
            if(self.reroll_surges):
                surges_to_reroll = min(rerolls, self.surges[i])
                rerolls -= surges_to_reroll
                self.surges[i] -= surges_to_reroll
                dice_counts[i] += surges_to_reroll
            
            if(self.reroll_hits):
                hits_to_reroll = min(rerolls, self.hits[i])
                rerolls -= hits_to_reroll
                self.hits[i] -= hits_to_reroll
                dice_counts[i] += hits_to_reroll
        
        #print("Rerolling: ", dice_counts, rerolls)
        
        white_distribution = get_attack_dice_distribution(AttackDice.WHITE, dice_counts[0])
        black_distribution = get_attack_dice_distribution(AttackDice.BLACK, dice_counts[1])
        red_distribution = get_attack_dice_distribution(AttackDice.RED, dice_counts[2])
        
        total_probability = 0
        for a in range(dice_counts[0] + 1): # white hits
            for b in range(dice_counts[0] + 1 - a): # white crits
                for c in range(dice_counts[0] + 1 - a - b): # white surges
                    for d in range(dice_counts[1] + 1): # black hits
                        for e in range(dice_counts[1] + 1 - d): # black crits
                            for f in range(dice_counts[1] + 1 - d - e): # black surges
                                for g in range(dice_counts[2] + 1): # red hits
                                    for h in range(dice_counts[2] + 1 - g): # red crits
                                        for i in range(dice_counts[2] + 1 - g - h): # red surges
                                            probability = white_distribution[a][b][c] * \
                                                black_distribution[d][e][f] * \
                                                red_distribution[g][h][i]
                                            
                                            dice_pool = DicePool(
                                                [dice_counts[0] - a - b - c + self.blanks[0], 
                                                    dice_counts[1] - d - e - f + self.blanks[1], 
                                                    dice_counts[2] - g - h - i + self.blanks[2]], \
                                                [a + self.hits[0], d + self.hits[1], g + self.hits[2]], 
                                                [b + self.crits[0], e + self.crits[1], h + self.crits[2]], 
                                                [c + self.surges[0], f + self.surges[1], i + self.surges[2]], \
                                                aims=self.aims, precise=self.precise, \
                                                criticals=self.criticals, hit_surges=self.hit_surges, impacts=self.impacts, \
                                                improvements=self.improvements, reroll_hits=self.reroll_hits, reroll_surges=self.reroll_surges)
                                            
                                            dice_pool.modify_dice()
                                            dice_pool.improve_dice()
                                            
                                            dice_pool.apply_aims(distribution, base_probability=base_probability * probability)
                                            total_probability += probability
        #print("total_probability: ", total_probability)
        
