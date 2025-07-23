from dice import Dice
from score import Score


def opening_statement():
    print("Welcome to Dice Roller!")


def user_selection():
    while True:
        selection = input("Roll the dice? (Y/N): ")
        selection = selection.capitalize()
        if selection in ("Y", "N"):
            return selection
        else:
            print("Invalid Selection!")


def create_dice():
    die_one = Dice()
    die_two = Dice()
    die_three = Dice()
    return die_one, die_two, die_three


def roll_dice(die_one, die_two, die_three):
    value_one = die_one.roll()
    value_two = die_two.roll()
    value_three = die_three.roll()
    print(f"({value_one}, {value_two}, {value_three})")
    return value_one, value_two, value_three


def closing_statement():
    print("Thanks for playing Dice Roller!")


def calculate_score(value_one, value_two, value_three):
    score = Score(value_one, value_two, value_three)
    score_functions = [score.value_score, score.is_prime, score.same_value, score.all_odd, score.all_even, score.consecutive_values]
    for functions in score_functions:
        functions()
    player_score = score.get_score()
    print(f"Score: {player_score}")


def main():
    opening_statement()
    while True:
        selection = user_selection()
        if selection in "Y":
            die_one, die_two, die_three = create_dice()
            value_one, value_two, value_three = roll_dice(die_one, die_two, die_three)
            calculate_score(value_one, value_two, value_three)
        else:
            break
    closing_statement()


if __name__ == "__main__":
    main()
