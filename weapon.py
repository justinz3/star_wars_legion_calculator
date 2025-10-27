
class Weapon:
    def __init__(self, dice_counts, aims=0, hit_surges=0, criticals=0, impacts=0, precise=0, spray=False, pierce=0, improvements=0, name=None):
        self.dice_counts = dice_counts
        self.aims = aims
        self.hit_surges = hit_surges
        self.criticals = criticals
        self.impacts = impacts
        self.improvements = improvements
        self.precise = precise # TODO
        self.spray = spray
        self.pierce = pierce
        self.name = name  # Weapon name for GUI display 
    
    def __mul__(self, unit_size):
        return WeaponPool(
            [dice_count * unit_size for dice_count in self.dice_counts], 
            hit_surges=self.hit_surges * unit_size,
            criticals=self.criticals * unit_size,
            impacts=self.impacts * unit_size,
            precise=self.precise * unit_size,
            spray=self.spray,
            pierce=self.pierce * unit_size)
    
    def __rmul__(self, unit_size):
        return self.__mul__(unit_size)

class WeaponPool(Weapon):
    def add_to_pool(self, other):
        for i in range(len(self.dice_counts)):
            self.dice_counts[i] += other.dice_counts[i]
        
        self.aims += other.aims
        self.hit_surges += other.hit_surges
        self.criticals += other.criticals
        self.impacts += other.impacts
        self.precise += other.precise
        self.spray = self.spray and other.spray
        self.pierce += other.pierce
