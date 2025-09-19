from traceback import print_tb


class Outcome:
    def __init__(self, state, number_of_turns, random_number):
        self.state = state
        self.number_of_turns = number_of_turns
        self.random_number = random_number

    def win(self):
        print(f"You Win! You got it with {self.number_of_turns} turns remaining")

    def lose(self):
        print(f"You Lose! The random number was {self.random_number}")

    def handle_outcome(self):
        if self.state == 1:
            self.win()
        else:
            self.lose()
