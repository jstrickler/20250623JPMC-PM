import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):  # constructor
        self._make_deck()

    def _make_deck(self):  # helper (private) method
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):  # getter property
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    def __repr__(self):
        return "CardDeck()"
    
    def __str__(self):
        return f"CardDeck:{len(self)}"

    def __len__(self):
        return len(self._cards)

    @staticmethod
    def double(x):
        return x * 2

if __name__ == '__main__':
    d1 = CardDeck()
    d2 = CardDeck()
    d1.shuffle()
    print(f"{d1.cards = }")
    for _ in range(5):
        card = d1.draw()
        print(card)
    print(len(d1))
    print(d1)
    print(d2)
    print(d1.get_suits())
    print(CardDeck.get_suits())
    print(CardDeck.double(22))