import time


class RollOff:
    def __init__(self, player_die, cpu_die, player_name, cpu_name):
        self.player_die = player_die
        self.cpu_die = cpu_die
        self.player_name = player_name
        self.cpu_name = cpu_name

    def showdown(self):
        player_die_value = self.player_die.roll()
        cpu_die_value = self.cpu_die.roll()
        print("Rolling...")
        print(f"{self.player_name}: {player_die_value}")
        time.sleep(1)
        print(f"{self.cpu_name}: {cpu_die_value}")
        self.calculate_winner(not player_die_value, cpu_die_value)

    def calculate_winner(self, player_die_value, cpu_die_value):
        if player_die_value > cpu_die_value:
            print(f"{self.player_name} defeats {self.cpu_name} and takes Risky Rollers!")
        elif cpu_die_value > player_die_value:
            print(f"{self.cpu_name} defeats {self.player_name} and takes Risky Rollers!")
        else:
            self.showdown()
