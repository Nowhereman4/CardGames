# a player has a hand and a score. a hand is a just a deck and a score
# a discard deck is for cards that are collected in various games like in spades when you
# win a round you keep the cards

from Deck import Deck
class Player():

    hand: Deck

    def __init__(self, name, playerNumber):
        self.name = name
        self.hand = Deck()
        self.score = 0
        self.number = playerNumber

        self.discard = Deck()

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def setScore(self, points):
        self.score = points
    def getScore(self):
        return self.score

    def setHand(self, deck):
        self.hand = deck
    def getHand(self):
        return self.hand

    def setNumber(self, no):
        self.number = no
    def getNumber(self):
        return self.number

    def printHand(self):
        temp = self.hand
        temp.printAll()