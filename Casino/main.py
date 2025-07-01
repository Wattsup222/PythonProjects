from random import uniform


def generate_card_balance():
    # floating point between a and b to two decimal places
    balance = round(uniform(100, 10000), 2)
    return balance


def deposit(available):
    amount_viable = False
    while not amount_viable:
        amount = int(input("How much do you want to deposit: "))
        if amount <= available:
            print(f"You have successfully deposited ${amount}")
            amount_viable = True
        else:
            print(f"Not enough funds to deposit ${amount}")
    return amount


if __name__ == '__main__':
    capital_available = generate_card_balance()
    tab = deposit(capital_available)
