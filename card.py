VALID_SUITS = {'Clubs', 'Diamonds', 'Hearts', 'Spades'}

class Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    def __str__(self):  # obj.tostring()
        return f"{self.rank}-{self.suit}"

    @property
    def rank(self): # getter property
        return self._rank
    
    @property
    def suit(self):  # getter property
        return self._suit
    
    @suit.setter
    def suit(self, value):  # setter property
        if value in VALID_SUITS:
            self._suit = value
        else:
            raise ValueError("Invalid suit name")

if __name__ == "__main__":
    c1 = Card("A", "Clubs")
    c2 = Card("8", "Diamonds")
    print(c1)  # str()
    print(c2)
    print(f"{c1 = }")  # repr()
    print(c1.rank)
    print(c1.suit)
    c1.suit = "Spades"
