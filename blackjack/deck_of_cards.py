from random import shuffle


class DeckOfCards:
    def __init__(self, cards):
        self.cards = cards
        self.index = 0

    def __iter__(self):
        return iter(self.cards)

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        card = self.cards[self.index]
        self.remove_card()
        return card

    def remove_card(self):
        self.cards.pop(self.index)
