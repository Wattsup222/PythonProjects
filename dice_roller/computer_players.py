from player import Player
import random


class Static(Player):
    def __init__(self, dice):
        super().__init__("Static Steve", dice)


class Random(Player):
    def __init__(self, dice):
        super().__init__("Random Ronny", dice)

    def select_dice(self):
        die = random.randint(1, 3)
        self.reroll(die)

    def reroll(self, die):
        match die:
            case 1:
                self.dice[0].roll()
            case 2:
                self.dice[1].roll()
            case 3:
                self.dice[2].roll()
