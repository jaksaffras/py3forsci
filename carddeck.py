import random

class CardDeck:  # inherits from object
    CLUB = '\u2663'
    DIAMOND = '\u2662'
    HEART = '\u2661'
    SPADE = '\u2660'

    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self._dealer = dealer
        self.color = "blue"
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.CLUB, self.DIAMOND, self.HEART, self.SPADE:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards

    @property  # decorator
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    def get_dealer(self):
        return self._dealer

    def set_dealer(self, dealer):
        self._dealer = dealer

    def __len__(self):
        return len(self._cards)

    def __add__(self, other):
        my_type = type(self)
        tmp = my_type(self.dealer)
        tmp._cards = self._cards + other._cards
        return tmp

