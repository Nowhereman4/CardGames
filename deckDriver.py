# driver for deck methods so that way it is easier to test each part of the program
from Deck import Deck
from Card import Card

# tests for all methods methods: buildDeck insertAtBeginning removeFromBeginning, getNumberedCard insertAtEnd
# getHighestValue, getHighestValueBySuit, getHighestRank, getHighestRankBySuit, getByRankAndSuit, printAll

# testing insert at beginning using 2 cards
# works
print("testing insert at beginning")
deck = Deck()
aofs = Card("ace", 14, 1, "spades", True)
qofs = Card("queen", 12, 1, "spades", True)
# print head to make sure it's empty
print(deck.head)
deck.insertAtBeginning(aofs)
deck.printAll()
# insert card at beginning to make sure it's at beginning and print it

deck.insertAtBeginning(qofs)
#print(deck.head.__str__())

# testing remove from beginning
# works
print("\n\ntesting remove from beginning")
deck.head = None
deck.insertAtBeginning(qofs) # add queen of spades
deck.insertAtBeginning(aofs) # add ace, which should be the top card now
RFB = deck.removeFromBeginning()
 # print("removed card is", RFB.__str__())

# GET NUMBERED CARD
# using a full deck to get from beginning, middle, and end using a test card
# works
print("\n\nTEST FOR GET NUMBERED CARD\n")
testCard =  Card("TEST", 14, 1, "QUINOA", True)
deck.head = None
deck.buildDeck()

print("\nPRINTING DECK")
deck.printAll()
removedCard = deck.getNumberedCard(52)
print("\nREMOVED last CARD, WHICH SHOULD BE ace of clubs")
print(removedCard.__str__())
print("\nCHECK TO SEE IF REMOVED CARD WAS REMOVED FROM DECK ")
deck.printAll()
print("checking if first card is removed")
removedCard = deck.getNumberedCard(1)

print("\nremoved card:", removedCard.__str__())
print("\n")
deck.printAll()
#deck.printAll()

# test insertAtEnd...
# success
'''
deck.head = None
testCard.next = None
deck.buildDeck()
deck.insertAtEnd(testCard)
print("\nINSERTING TEST CARD AT END\n")
deck.printAll()

# test getHighestValue
# success
deck.head = None
testCard.setRank(20)
testCard.setValue(20)
deck.buildDeck()
#make sure cards pointers are set to null
testCard.next = None
qofs.next = None
aofs.next = None
deck.insertAtBeginning(testCard)
deck.insertAtBeginning(qofs)
deck.insertAtBeginning(aofs)
highestVal = deck.getHighestValue()
print("\nTEST FOR HIGHEST VALUE")
print("\nhighest value should be 20:\n",highestVal.__str__(), "with value of", highestVal.getValue())

# test get highest value by suit
print("\nHIGHEST VALUE BY SUIT\n")
deck.head = None
deck.buildDeck()
testCard.next = None
testCard.setSuit("spades")
qofs.next = None
aofs.next = None
deck.insertAtBeginning(qofs)
deck.insertAtBeginning(testCard)
deck.insertAtBeginning(aofs)
highVal = deck.getHighestValuebySuit("spades")
print("highest value for", highVal.getSuit(), "is", highVal.__str__(), "with value", highVal.getValue())
highVal = deck.getHighestValuebySuit("hearts")
print("highest value for", highVal.getSuit(), "is", highVal.__str__(), "with value", highVal.getValue())

# get by rank has the same exact logic so it wasn't tested. might be a regret 
sfdg '''