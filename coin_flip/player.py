class Player:
    def __init__(self):
        self.wins = 0
        self.losses = 0

    @staticmethod
    def select_choice():
        while True:
            choice = input("Heads or Tails (H/T): ")
            if choice in ("H","T"):
                return choice
            else:
                print("Invalid option")