import time
from dice import Dice
from score import Score
from user import User
from computer_players import Static
from utility import create_username


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


def get_username():
    player_name = create_username()
    return player_name


def create_dice():
    player_dice = []
    computer_dice = []
    for die in range(3):
        player_dice.append(Dice())
        computer_dice.append(Dice())
    return player_dice, computer_dice


def create_players(player_name, player_dice, computer_dice):
    player = User(player_name, player_dice)
    cpu_player = Static("Static Spinner", computer_dice)
    return player, cpu_player


def setup():
    player_name = get_username()
    player_dice, computer_dice = create_dice()
    player, cpu = create_players(player_name, player_dice, computer_dice)
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


def display_winner(player_total, cpu_total, player_name, cpu_name):
    if player_total > cpu_total:
        print(f"{player_name} defeats {cpu_name} and takes Risky Rollers")
    elif cpu_total > player_total:
        print(f"{cpu_name} defeats {player_name} and takes Risky Rollers")
    else:
        print("Its a draw")
    time.sleep(2)


def closing_statement():
    print("Thanks for playing Risky Rollers!")


def main():
    opening_statement()
    player, cpu = setup()
    display_names(player.name, cpu.name)
    player.initial_roll()
    cpu.initial_roll()
    player.dice_values()
    player_total, player_raw, player_bonus, player_bonuses = Score(player.dice).calculate_score()
    display_score(player_total, player_raw, player_bonus, player_bonuses)
    player.roll_again_option()
    player.dice_values()
    player_total, player_raw, player_bonus, player_bonuses = Score(player.dice).calculate_score()
    display_score(player_total, player_raw, player_bonus, player_bonuses)
    cpu.dice_values()
    cpu_total, cpu_raw, cpu_bonus, cpu_bonuses = Score(cpu.dice).calculate_score()
    display_score(cpu_total, cpu_raw, cpu_bonus, cpu_bonuses)
    display_winner(player_total, cpu_total, player.name, cpu.name)
    closing_statement()


if __name__ == "__main__":
    main()
