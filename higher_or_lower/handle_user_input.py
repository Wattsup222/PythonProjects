class HandleUserInput:
    def __init__(self):
        self.number = 0
        self.lowest_number = 0
        self.highest_number = 100

    def get_user_number(self):
        is_valid = False
        while not is_valid:
            self.input_number_guide()
            if self.number.isnumeric():
                self.number = int(self.number)
                if self.lowest_number <= self.number <= self.highest_number:
                    is_valid = True
                else:
                    self.outside_bounds()
            else:
                print("Please input a number")
        return self.number

    def input_number_guide(self):
        if self.lowest_number != self.highest_number:
            self.number = input(f"Enter a number between {self.lowest_number} & {self.highest_number}: ")
        else:
            self.number = input(f"The number is {self.lowest_number}: ")

    def outside_bounds(self):
        if self.lowest_number != self.highest_number:
            print(f"Please enter a number between {self.lowest_number} and {self.highest_number}")
        else:
            print(f"Please enter {self.lowest_number}")
