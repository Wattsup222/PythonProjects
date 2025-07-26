from dice import Dice
from score import Score


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


def create_dice():
    player_dice = []
    computer_dice = []
    for die in range(3):
        player_dice.append(Dice())
        computer_dice.append(Dice())
    return player_dice, computer_dice


def roll_dice(dice):
    dice_num = 0
    for die in dice:
        dice_num += 1
        die.roll()
        print(f"Dice {dice_num}: {die.value}")


def calculate_score(dice):
    score = Score(dice)
    score_functions = [score.value_score, score.is_prime, score.same_value, score.all_odd, score.all_even,
                       score.consecutive_values]
    for functions in score_functions:
        functions()
    player_score = score.get_score()
    return player_score


def roll_again_option():
    while True:
        selection = input("Do you want to reroll a dice? (Y/N): ")
        selection = selection.capitalize()
        if selection in ("Y", "N"):
            return selection
        else:
            print("Invalid Selection")


def roll_again():
    while True:
        reroll_dice = input("Which dice do you want to reroll? (1/2/3): ")
        if reroll_dice.isdigit():
            reroll_dice = int(reroll_dice)
            if reroll_dice in (1, 2, 3):
                return reroll_dice
            else:
                print("Invalid Selection")
        else:
            print("Invalid Selection")


def reroll(die, dice):
    match die:
        case 1:
            dice[0].roll()
        case 2:
            dice[1].roll()
        case 3:
            dice[2].roll()


def closing_statement():
    print("Thanks for playing Dice Roller!")


def main():
    opening_statement()
    while True:
        selection = user_selection()
        if selection in "Y":
            player_dice, computer_dice = create_dice()
            roll_dice(player_dice)
            player_score = calculate_score(player_dice)
            placeholder = roll_again_option()
            if placeholder in "Y":
                die = roll_again()
                reroll(die, player_dice)
                print(player_dice[0].value, player_dice[1].value, player_dice[2].value)
                player_score = calculate_score(player_dice)
            else:
                break
        else:
            break
    closing_statement()


if __name__ == "__main__":
    main()
