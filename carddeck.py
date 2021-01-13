import random

class CardDeck:  # inherits from object
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'clubs diamonds hearts spades'.split()

    def __init__(self, dealer):
        self._dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    # getter method (AKA accessor)
    def get_dealer(self):
        return self._dealer

    # getter property (AKA accessor)
    @property
    def dealer(self):
        return self._dealer

    # setter property (AKA mutator)
    @dealer.setter
    def dealer(self, dealer):
        self._dealer = dealer

    def deal(self):
        return self._cards.pop()