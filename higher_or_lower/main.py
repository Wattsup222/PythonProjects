from number import Number
from handle_user_input import HandleUserInput
from feedback import Feedback
from outcome import Outcome


def setup():
    number_of_turns = 6
    number = Number()
    random_number = number.generate_random_number()
    return number_of_turns, random_number


def get_user_number():
    player_number = HandleUserInput()
    input_number = player_number.get_user_number()
    return input_number


def response(input_number, random_number):
    feedback = Feedback(random_number, input_number)
    state = feedback.compare()
    return state


def result(state, number_of_turns, random_number):
    outcome = Outcome(state, number_of_turns, random_number)
    outcome.handle_outcome()


def main():
    number_of_turns, random_number = setup()
    state = 0
    while number_of_turns != 0 and state != 1:
        input_number = get_user_number()
        state = response(input_number, random_number)
        number_of_turns -= 1
    result(state, number_of_turns, random_number)


if __name__ == '__main__':
    main()
