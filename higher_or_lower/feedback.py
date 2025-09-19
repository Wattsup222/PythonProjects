class Feedback:
    def __init__(self, random_number, player_number):
        self.random_number = random_number
        self.player_number = player_number

    def compare(self):
        if self.player_number == self.random_number:
            print("You Guessed It Right!")
            return 1
        elif self.player_number >= self.random_number:
            print("Lower!")
            return 0
        else:
            print("Higher!")
            return 0
