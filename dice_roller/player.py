import time


class Player:
    def __init__(self, name, dice):
        self.name = name
        self.dice = dice

    def initial_roll(self):
        for die in self.dice:
            die.roll()

    def dice_values(self):
        dice_num = 0
        print(f"\n{self.name}")
        time.sleep(1)
        print("\nRolling...")
        time.sleep(1)
        for die in self.dice:
            dice_num += 1
            print(f"Dice {dice_num}: {die.value}")
            time.sleep(1)
