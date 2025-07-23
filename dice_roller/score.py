from mpmath.libmp import isprime


class Score:
    def __init__(self, value_one, value_two, value_three):
        self.value_one = value_one
        self.value_two = value_two
        self.value_three = value_three
        self.score = 0

    def value_score(self):
        self.score = self.value_one + self.value_two + self.value_three

    def is_prime(self):
        roll = self.value_one + self.value_two + self.value_three
        if isprime(roll):
            self.score += 2
            print("prime")

    def same_value(self):
        if self.value_one == self.value_two and self.value_two == self.value_three:
            self.score += 10
            print("Same Value")

    def all_odd(self):
        if self.value_one % 2 == 1 and self.value_two % 2 == 1 and self.value_three % 2 == 1:
            self.score += 2
            print("All Odd")

    def all_even(self):
        if self.value_one % 2 == 0 and self.value_two % 2 == 0 and self.value_three % 2 == 0:
            self.score += 2
            print("All Even")

    def consecutive_values_increasing(self):
        if self.value_one < self.value_two < self.value_three:
            if self.value_two - self.value_one == 1 and self.value_three - self.value_two == 1:
                self.score += 7
                print("Consecutive Straight Increasing")
            else:
                self.score += 1
                print("Consecutive not Straight Increasing")

    def consecutive_values_decreasing(self):
        if self.value_one > self.value_two > self.value_three:
            if self.value_one - self.value_two == 1 and self.value_two - self.value_three == 1:
                self.score += 7
                print("Consecutive Straight Decreasing")
            else:
                self.score += 1
                print("Consecutive not Straight Decreasing")

    def consecutive_values(self):
        self.consecutive_values_increasing()
        self.consecutive_values_decreasing()

    def get_score(self):
        return self.score
