class Player:
    def __init__(self, card_one, card_two):
        self.cards = [card_one, card_two]

    def add_card(self, card):
        self.cards.append(card)

    def card_total(self):
        total = 0
        for card in self.cards:
            value = card.get_string_value()
            if value == "A" and total >= 11:
                total += 1
            else:
                total += card.get_numeric_value()
        return total
