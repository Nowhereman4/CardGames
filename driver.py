# this driver is used  to test various functionalities of both card and deck to make sure they work as intended

from Deck import Deck
from Card import Card
from Player import Player
from Game import Game
# creating a new deck with the head being a random card



mygame = Game(4)
mygame.deck.printAll()
mygame.dealDeck()
print("dealt deck")

mygame.printAllHands()


