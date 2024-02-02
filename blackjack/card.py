class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.suit + " "+ str(self.value)
    
deck = [
    Card("Hearts", 2),
    Card("Hearts", 3),
    Card("Hearts", 4),
    Card("Hearts", 5),
    Card("Hearts", 6),
    Card("Hearts", 7),
    Card("Hearts", 8),
    Card("Hearts", 9),
    Card("Hearts", 10),
    Card("Hearts", 10),
    Card("Hearts", 10),
    Card("Hearts", 10),
    Card("Hearts", 11),
    
    Card("Spades", 2),
    Card("Spades", 3),
    Card("Spades", 4),
    Card("Spades", 5),
    Card("Spades", 6),
    Card("Spades", 7),
    Card("Spades", 8),
    Card("Spades", 9),
    Card("Spades", 10),
    Card("Spades", 10),
    Card("Spades", 10),
    Card("Spades", 10),
    Card("Spades", 11),

    Card("Clubs", 2),
    Card("Clubs", 3),
    Card("Clubs", 4),
    Card("Clubs", 5),
    Card("Clubs", 6),
    Card("Clubs", 7),
    Card("Clubs", 8),
    Card("Clubs", 9),
    Card("Clubs", 10),
    Card("Clubs", 10),
    Card("Clubs", 10),
    Card("Clubs", 10),
    Card("Clubs", 11),

    Card("Diamonds", 2),
    Card("Diamonds", 3),
    Card("Diamonds", 4),
    Card("Diamonds", 5),
    Card("Diamonds", 6),
    Card("Diamonds", 7),
    Card("Diamonds", 8),
    Card("Diamonds", 9),
    Card("Diamonds", 10),
    Card("Diamonds", 10),
    Card("Diamonds", 10),
    Card("Diamonds", 10),
    Card("Diamonds", 11),
]
