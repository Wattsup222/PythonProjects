class Outcome:
    def __init__(self, state, max_turns, random_number, current_turn):
        self.state = state
        self.max_turns = max_turns
        self.random_number = random_number
        self.current_turn = current_turn
        self.win_string = ""

    def win(self):
        print(self.win_string)

    def win_message(self):
        match self.current_turn:
            case 1:
                self.win_string = "FIRE UP YA CAT! You got it first attempt!"
            case self.max_turns:
                self.win_string = "Phew! You got it on the final attempt!"
            case _:
                self.win_string = f"You Win! You got it after {self.current_turn} attempts!"

    def lose(self):
        print(f"You Muffin! The random number was {self.random_number}!")

    def handle_outcome(self):
        if self.state == 1:
            self.win_message()
            self.win()
        else:
            self.lose()
