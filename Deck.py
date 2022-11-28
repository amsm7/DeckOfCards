from random import shuffle

from Card import Card

class Deck:
    cards_count =52

    def __init__(self):
        card_suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        card_value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        self.cards = [Card(card,suit) for card in card_value for suit in card_suit]
        print(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        remove_num = min([count, num])
        if count > 0:
            cards = self.cards[-remove_num:]
            self.cards = self.cards[:-remove_num]
            return cards

        else:
            raise ValueError("All cards have been dealt.")

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, number):
        return self._deal(number)

    def shuffle(self, full_deck):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled.")
        shuffle(self.cards)



deck = Deck()
print(deck._deal(42))
deck_count = deck.__repr__()
print(deck_count)



