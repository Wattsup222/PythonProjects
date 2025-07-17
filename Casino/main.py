import random


class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def test(self):
        print(f"{self.value}{self.suite}")


values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
suites = ("♣️", "♠️", "♦️", "♥️")

cards = []
for suite in suites:
    for value in values:
        cards.append(Card(suite, value))

random.shuffle(cards)

for card in cards:
    card.test()
