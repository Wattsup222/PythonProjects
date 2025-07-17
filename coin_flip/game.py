from random import choice


class Game:
    def __init__(self):
        self.outcome = ""

    def flip(self):
        self.outcome = choice(("H", "T"))
        return self.outcome

    def result(self, player_choice):
        if player_choice == self.outcome:
            print("You Win")
        else:
            print("You Lose")
