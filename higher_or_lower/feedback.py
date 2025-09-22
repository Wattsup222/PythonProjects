class Feedback:
    def __init__(self, random_number, player_number, max_turns, current_turn):
        self.random_number = random_number
        self.player_number = player_number
        self.max_turns = max_turns
        self.current_turn = current_turn

    def compare(self):
        if self.player_number == self.random_number:
            return 1
        elif self.player_number >= self.random_number:
            self.handle_lower_feedback()
            return 0
        else:
            self.handle_higher_feedback()
            return -1

    def handle_lower_feedback(self):
        if self.current_turn != self.max_turns:
            print("Lower!")
            self.remaining_turns()

    def handle_higher_feedback(self):
        if self.current_turn != self.max_turns:
            print("Higher!")
            self.remaining_turns()

    def remaining_turns(self):
        remaining_attempts = self.max_turns - self.current_turn
        if remaining_attempts != 0:
            print(f"You have {remaining_attempts} attempts remaining")
