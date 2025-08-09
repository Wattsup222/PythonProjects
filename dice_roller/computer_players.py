from player import Player
import random


class Static(Player):
    pass


class Random(Player):

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
