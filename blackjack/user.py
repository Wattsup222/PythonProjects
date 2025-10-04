from player import Player


class User(Player):
    def __init__(self, card_one, card_two):
        super().__init__(card_one, card_two)

    @staticmethod
    def stand_or_hit():
        while True:
            choice = input("Stand (S) or Hit (H): ")
            if choice in ["S", "H"]:
                return choice
            else:
                print(f"Please enter a valid option not {choice}!")
