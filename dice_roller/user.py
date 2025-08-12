from player import Player


class User(Player):

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
                return True
            elif selection in "N":
                return False
            else:
                print("Invalid Selection")
