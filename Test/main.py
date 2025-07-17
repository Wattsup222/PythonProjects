import random
from card import Card

values = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
suits = ("♣️", "♠️", "♦️", "♥️")


def main():
    deck_of_cards = [Card(suit, value) for suit in suits for value in values]
    ply_cards = []
    cpu_cards = []
    shuffled_deck_of_cards = shuffle_deck(deck_of_cards)
    ply_cards = player_hand(shuffled_deck_of_cards)
    cpu_cards = computer_hand(shuffled_deck_of_cards)


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def player_hand(deck):
    card_one = deck[0]
    card_two = deck[1]
    return card_one, card_two


def computer_hand(deck):
    card_one = deck[2]
    card_two = deck[3]
    return card_one, card_two


if __name__ == "__main__":
    main()
