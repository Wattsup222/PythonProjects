class HandleUserInput:
    def __init__(self):
        self.number = 0
        self.isValid = False
        self.lowest_number = 0
        self.highest_number = 100

    def get_user_number(self):
        while not self.isValid:
            self.number = input(f"Enter a number between {self.lowest_number} & {self.highest_number}: ")
            if self.number.isnumeric():
                self.number = int(self.number)
                if 0 <= self.number <= 100:
                    self.isValid = True
                else:
                    print(f"Please enter a number between {self.lowest_number} and {self.highest_number}")
            else:
                print("Please input a number")
        return self.number
