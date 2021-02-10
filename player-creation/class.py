
import math

class PlayerClass:
    def __init__(self):
        self.level = 1
        self.proficiency_bonus = 2

    def proficency_bonus(self):
        return math.floor(0.25 * self.level + 1.75)

    def level_up(self):
        self.level += 1

