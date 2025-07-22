import random


class Dice:
    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randrange(1, 7)
        return self.value
