from math import floor

from constants import PROBABILITY_UNIT

class DamageDistribution:
    def __init__(self, probability_list, attacker_name, defender_name, modifiers=""):
        print("-------------------------------------------")
        print("Damage Probability Chart - {} attacking {}".format(attacker_name, defender_name))
        if(modifiers):
            print(modifiers)
        expected_wounds = 0
        for i, prob in enumerate(probability_list):
            print("{} - {:5.2f}% | {}".format(i, prob * 100, floor(prob / PROBABILITY_UNIT) * '#'))
            expected_wounds += i * prob
        print("Expected Damage: {:.2f}".format(expected_wounds))
        print("-------------------------------------------")
