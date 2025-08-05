import time
from dice import Dice
from player import Player
from score import Score
from utility import generate_name, create_username


def opening_statement():
    print("Welcome to Risky Rollers!")


def user_selection():
    while True:
        selection = input("Roll the dice? (Y/N): ")
        selection = selection.capitalize()
        if selection in ("Y", "N"):
            return selection
        else:
            print("Invalid Selection!")


def create_name():
    player_name = create_username()
    cpu_name = generate_name()
    return player_name, cpu_name


def create_dice():
    player_dice = []
    computer_dice = []
    for die in range(3):
        player_dice.append(Dice())
        computer_dice.append(Dice())
    return player_dice, computer_dice


def create_players(player_name, cpu_name, player_dice, computer_dice):
    player = Player(player_name, player_dice, False)
    cpu = Player(cpu_name, computer_dice, True)
    return player, cpu


def setup():
    player_name, cpu_name = create_name()
    player_dice, computer_dice = create_dice()
    player, cpu = create_players(player_name, cpu_name, player_dice, computer_dice)
    return player, cpu


def display_names(player_name, cpu_name):
    print(f"\n{player_name} VS {cpu_name}")
    time.sleep(1.5)


def display_score(total_score, raw_score, bonus_score, bonuses):
    print(f"\nRaw Score: {raw_score}")
    time.sleep(1)
    print(f"Bonus Score: {bonus_score}")
    if bonuses:
        print(f"Bonuses: ", end='')
        for bonus in bonuses:
            print(f"{bonus}, ", end='')
        print("")
    time.sleep(1)
    print(f"Total Score: {total_score}")
    time.sleep(1)



def closing_statement():
    print("Thanks for playing Dice Roller!")


def main():
    opening_statement()
    player, cpu = setup()
    display_names(player.name, cpu.name)
    player.initial_roll()
    player.dice_values()
    player_total, player_raw, player_bonus, player_bonuses = Score(player.dice).calculate_score()
    display_score(player_total, player_raw, player_bonus, player_bonuses)
    player.roll_again_option()
    player.dice_values()
    player_total, player_raw, player_bonus, player_bonuses = Score(player.dice).calculate_score()
    display_score(player_total, player_raw, player_bonus, player_bonuses)


if __name__ == "__main__":
    main()
