from card import Card
from deck_of_cards import DeckOfCards
from player import Player


def create_cards():
    values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    suits = ["♥️", "♦️", "♠️", "♣️"]
    cards = []
    for suit in suits:
        for value in values:
            cards.append(Card(suit, value))
    return cards


def create_deck(cards):
    deck_of_cards = DeckOfCards(cards)
    return deck_of_cards


def shuffle_deck(deck_of_cards):
    deck_of_cards.shuffle()
    return deck_of_cards


def player_starting_hand(shuffled_deck_of_cards):
    card_one = shuffled_deck_of_cards.draw()
    card_two = shuffled_deck_of_cards.draw()
    print(card_one, card_two)
    return card_one, card_two


def create_player(card_one, card_two):
    player = Player(card_one, card_two)
    return player


def main():
    cards = create_cards()
    deck_of_cards = create_deck(cards)
    shuffled_deck_of_cards = shuffle_deck(deck_of_cards)
    card_one, card_two = player_starting_hand(shuffled_deck_of_cards)
    player = create_player(card_one, card_two)



if __name__ == '__main__':
    main()
