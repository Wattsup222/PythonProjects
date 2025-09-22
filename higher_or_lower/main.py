from number import Number
from handle_user_input import HandleUserInput
from feedback import Feedback
from outcome import Outcome


def setup():
    current_turn = 0
    max_turns = 6
    initial_turns(max_turns)
    player_number = HandleUserInput()
    number = Number()
    random_number = number.generate_random_number()
    return current_turn, max_turns, player_number, random_number


def initial_turns(max_turns):
    print(f"You have {max_turns} attempts to guess the number")


def get_user_number(player_number):
    input_number = player_number.get_user_number()
    return input_number, player_number


def response(input_number, random_number, number_of_turns, current_turn):
    feedback = Feedback(random_number, input_number, number_of_turns, current_turn)
    state = feedback.compare()
    return state


def modify_lowest_highest(state, player_number, input_number):
    if state == -1:
        lowest_possible = input_number + 1
        player_number.lowest_number = lowest_possible
    else:
        highest_possible = input_number - 1
        player_number.highest_number = highest_possible


def result(state, max_turns, random_number, current_turn):
    outcome = Outcome(state, max_turns, random_number, current_turn)
    outcome.handle_outcome()


def game_loop(player_number, current_turn, random_number, max_turns):
    input_number, player_number = get_user_number(player_number)
    current_turn += 1
    state = response(input_number, random_number, max_turns, current_turn)
    modify_lowest_highest(state, player_number, input_number)
    return state, current_turn


def main():
    current_turn, max_turns, player_number, random_number = setup()
    state = 0
    while current_turn != max_turns and state != 1:
        state, current_turn = game_loop(player_number, current_turn, random_number, max_turns)
    result(state, max_turns, random_number, current_turn)


if __name__ == '__main__':
    main()
