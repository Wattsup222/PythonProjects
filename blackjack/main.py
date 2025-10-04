from card import Card
from deck_of_cards import DeckOfCards
from user import User
from computer import Computer


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
    player = create_player(card_one, card_two)
    return player


def create_player(card_one, card_two):
    player = User(card_one, card_two)
    return player


def cpu_starting_hand(shuffled_deck_of_cards):
    card_one = shuffled_deck_of_cards.draw()
    card_two = shuffled_deck_of_cards.draw()
    cpu = create_cpu(card_one, card_two)
    return cpu


def create_cpu(card_one, card_two):
    cpu = Computer(card_one, card_two)
    return cpu


def display_player_card_total(player):
    total = player.card_total()
    print(f"Card total is {total}")
    return total


def display_player_cards(player):
    print("Player Cards:")
    for card in player.cards:
        print(f"{card}")


def display_cpu_cards(cpu):
    print(f"CPU Cards:\n{cpu.cards[0]}\nX❔\n")


def user_choice(player, deck_of_cards):
    choice = player.stand_or_hit()
    if choice == "H":
        card = hit(deck_of_cards)
        player.add_card(card)
        display_player_cards(player)
        total = display_player_card_total(player)
        if total > 21:
            game_loss()
            exit()
        else:
            return True, total
    else:
        return False, 0


def hit(shuffled_deck_of_cards):
    temporary_card = shuffled_deck_of_cards.draw()
    return temporary_card


def game_loop(player, shuffled_deck_of_cards, cpu):
    game_active = True
    while game_active:
        game_active, player_total = user_choice(player, shuffled_deck_of_cards)
    cpu_total = cpu_actions(cpu, shuffled_deck_of_cards)
    print(cpu_total)
    if cpu_total > 21:
        game_win()
    else:
        compare_totals(cpu_total, player_total)


def cpu_actions(cpu, shuffled_deck_of_cards):
    while True:
        total = cpu.card_total()
        if total <= 16:
            card = hit(shuffled_deck_of_cards)
            cpu.add_card(card)
        else:
            break
    return total


def compare_totals(player_total, cpu_total):
    if player_total > cpu_total:
        print("Fire Up Ya CAT you Win!")
    else:
        print("You Lose")


def game_loss():
    print("You went above 21 you Muffin!")


def game_win():
    print("Fire Up Ya CAT you Win!")


def main():
    cards = create_cards()
    deck_of_cards = create_deck(cards)
    shuffled_deck_of_cards = shuffle_deck(deck_of_cards)
    player = player_starting_hand(shuffled_deck_of_cards)
    cpu = cpu_starting_hand(shuffled_deck_of_cards)
    display_cpu_cards(cpu)
    display_player_cards(player)
    display_player_card_total(player)
    game_loop(player, shuffled_deck_of_cards, cpu)


if __name__ == '__main__':
    main()
