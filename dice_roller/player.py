import time


class Player:
    def __init__(self, name, dice, is_cpu):
        self.name = name
        self.dice = dice
        self.is_cpu = is_cpu

    def initial_roll(self):
        for die in self.dice:
            die.roll()

    def dice_values(self):
        dice_num = 0
        print("\nRolling...")
        time.sleep(1)
        for die in self.dice:
            dice_num += 1
            print(f"Dice {dice_num}: {die.value}")
            time.sleep(1)

    def reroll(self, die):
        match die:
            case 1:
                self.dice[0].roll()
            case 2:
                self.dice[1].roll()
            case 3:
                self.dice[2].roll()

    def roll_again(self):
        while True:
            reroll_dice = input("Which dice do you want to reroll? (1/2/3): ")
            if reroll_dice.isdigit():
                reroll_dice = int(reroll_dice)
                if reroll_dice in (1, 2, 3):
                    self.reroll(reroll_dice)
                    break
                else:
                    print("Invalid Selection")
            else:
                print("Invalid Selection")

    def roll_again_option(self):
        while True:
            selection = input("\nDo you want to reroll a dice? (Y/N): ")
            selection = selection.capitalize()
            if selection in "Y":
                self.roll_again()
                break
            elif selection in "N":
                break
            else:
                print("Invalid Selection")
