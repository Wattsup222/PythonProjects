import time
from random import uniform


def welcome_statement():
    message = "Welcome to Starlight City Casino"
    message_length = len(message)
    symbol_row = "*" * message_length
    print(f"{symbol_row}\n{message}\n{symbol_row}")


def setup():
    starting_capitol = round(uniform(100, 10000), 2)
    return starting_capitol


def main_menu():
    time.sleep(1)
    print("\n1: View balance\n2: View Games\n3: Quit")
    choice = int(input("\nSelection: "))
    return choice


def check_value(x):
    match x:
        case 1:
            balance_menu()
        case 2:
            game_menu()
        case 3:
            app_quit()


def balance_menu():
    pass


def game_menu():
    pass


def app_quit():
    message = "Thanks for Visiting Starlight City Casino"
    message_length = len(message)
    symbol_row = "*" * message_length
    print(f"\n{symbol_row}\n{message}\n{symbol_row}")
    quit()


if __name__ == "__main__":
    capitol = setup()
    welcome_statement()
    option = main_menu()
    check_value(option)
