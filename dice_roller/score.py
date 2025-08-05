class Score:
    def __init__(self, dice):
        self.value_one = dice[0].value
        self.value_two = dice[1].value
        self.value_three = dice[2].value
        self.raw_score = 0
        self.bonus_score = 0
        self.total_score = 0
        self.bonuses = []

    def value_score(self):
        self.raw_score = self.value_one + self.value_two + self.value_three

    def same_value(self):
        if self.value_one == self.value_two and self.value_two == self.value_three:
            self.bonus_score += 10
            self.bonuses.append("Same Value")

    def all_odd(self):
        if self.value_one % 2 == 1 and self.value_two % 2 == 1 and self.value_three % 2 == 1:
            self.bonus_score += 2
            self.bonuses.append("All Odd")

    def all_even(self):
        if self.value_one % 2 == 0 and self.value_two % 2 == 0 and self.value_three % 2 == 0:
            self.bonus_score += 2
            self.bonuses.append("All Even")

    def consecutive_values_increasing(self):
        if self.value_one < self.value_two < self.value_three:
            if self.value_two - self.value_one == 1 and self.value_three - self.value_two == 1:
                self.bonus_score += 7
                self.bonuses.append("Consecutive Straight")
            else:
                self.bonus_score += 1
                self.bonuses.append("Consecutive Not Straight")

    def consecutive_values_decreasing(self):
        if self.value_one > self.value_two > self.value_three:
            if self.value_one - self.value_two == 1 and self.value_two - self.value_three == 1:
                self.bonus_score += 7
                self.bonuses.append("Consecutive Straight")
            else:
                self.bonus_score += 1
                self.bonuses.append("Consecutive Not Straight")

    def consecutive_values(self):
        self.consecutive_values_increasing()
        self.consecutive_values_decreasing()

    def calculate_score(self):
        self.value_score()
        self.same_value()
        self.all_odd()
        self.all_even()
        self.consecutive_values()
        self.total_score = self.raw_score + self.bonus_score
        return self.total_score, self.raw_score, self.bonus_score, self.bonuses
