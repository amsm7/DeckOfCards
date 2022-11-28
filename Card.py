class Card:

    def __init__(self,  value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


card_suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_value =['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K']


c1 = Card(card_value[0], card_suit[0])
c2 = Card(card_value[7], card_suit[2])
c3 = Card(card_value[5], card_suit[3])


