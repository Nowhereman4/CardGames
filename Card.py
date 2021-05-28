# card object has name (string), value (int), rank , suit, color (black/red suit) - bool true for black, false for red(value could be 10 for face cards, where as rank would be king > queen > jack)
class Card:
    value: int
    color: bool

    def __init__(self, name, rank, value, suit, color):  # basic constructor for a card
        self.name = name    #string
        self.rank = rank
        self.value = value
        self.suit = suit
        self.color = color
        self

    #setters and getters
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def getRank(self):
        return self.rank
    def setRank(self, rank):
        self.rank = rank

    def getValue(self):
        return self.rank
    def setValue(self, value):
        self.value = value

    def getSuit(self):
        return self.suit
    def setSuit(self, suit):
        self.suit = suit

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color



