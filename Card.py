# card object has name (string), value (int), rank (int), suit, color (black/red suit) - bool true for black, false for red
# (value could be 10 for face cards, where as rank would be ace > king > queen > jack)
# player number describes which player the card belongs to. player one is 1, the deck is 0
class Card:
    value: int
    color: bool

    def __init__(self, name, rank, value, suit, color, next = None):
        self.name = name
        self.rank = rank
        self.value = value
        self.suit = suit
        self.color = color
        self.next = next
        self.playerNumber = 0

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
        return self.value
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

    def setNext(self, nextCard):
        self.next = nextCard
    def getNext(self):
        return self.next

    def __str__(self):
        return "The {} of {}".format(self.name,self.suit)






