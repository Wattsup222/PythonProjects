import random


class Number:
    def __init__(self):
        self.number = 0

    def generate_random_number(self):
        self.number = random.randint(0, 100)
        return self.number
