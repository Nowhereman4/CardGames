# deck class has instances of cards and can shuffle, might also use a "deck" as a hand for each player
# a deck is a linked list of cards. head is the top card
# any "remove" or "delete" will return the card it is deleting, so the card can be given to a player
# when counting cards you have to start 1 since getNumberedCard starts at 1
from Card import Card


class Deck(Card):
    valueSize = 10
    cardSuits = tuple(("clubs", "diamonds", "hearts", "spades"))
    cardValues = tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10))
    cardRanks = tuple((14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    cardNames = tuple(
        ("ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"))

    # initial constructor
    def __init__(self):
        self.head = None

    # create 52 card deck with no jokers
    def buildDeck(self):
        # for each suit
        for suit in self.cardSuits:
            # for each name, value and rank, since there are 13 of each
            for value in range(len(self.cardValues)):
                # if it's suppposed to be a red card, set color to false
                if suit == "diamonds" or suit == "hearts":
                    # check to make sure the value and ranks are right and they describe the right type of card
                    temp = Card(self.cardNames[value], self.cardRanks[value], self.cardValues[value], suit, False)
                else:
                    temp = Card(self.cardNames[value], self.cardRanks[value], self.cardValues[value], suit, True)
                self.insertAtBeginning(temp)

    # add card to top of deck
    def insertAtBeginning(self, card):
        # if it's only head, just set the new card equal to head
        # otherwise set card.next to head.next, then set head to card
        if (self.head == None):
            self.head = card
        else:
            card.next = self.head
            self.head = card

    # remove head aka the top of the deck, take the card out of the deck, set its pointer to null, and return it
    def removeFromBeginning(self):
        # if there is one card, return it
        if (self.head.next == None):
            card = self.head
            self.head = None
        # set the top card to card to return it. then set the top card to the next card
        else:
            card = self.head
            self.head = self.head.next

        return card

    # used to simulate shuffling when giving out cards in a game. instead of rearranging the order of the cards,
    # a random number will be generated, and that number will be sent to this function to return that numbered card
    # we will assume that the game keeps track of the size of the deck, so when a random number is generated it will
    # be within the limits of the deck
    def getNumberedCard(self, count):
        temp = self.head
        previous = self.head
        tempCounter = 1;
        # if
        foundCard = False
        while (temp.next != None):

            if (tempCounter == count):
                myCard = temp
                temp = temp.next
                break
            tempCounter += 1
            previous = temp
            temp = temp.next

        # if you're at the last card or second to last card where a pointer could potentially be equal to None,
        # set previous. next
        if (temp.next == None or temp == None):
            previous.next = None
        else:
            previous.next = temp

        return myCard

    # add card to bottom of deck
    def insertAtEnd(self, card):
        tempCard = self.head
        while tempCard.next != None:
            tempCard = tempCard.next

        tempCard.next = card

    # highest value is 10, and an ace is considered 1
    # not related to suit or color
    # when you get the highest value, the index in the linked list is set
    # this is used to remove the card using getNumberedCard(int).
    # find highestValue will return the card found
    def findHighestValue(self):
        tempCard = self.head
        myValue = 0
        myCount = 1 # index of card that has the highest value
        counter = 1 # overall counter
        while(tempCard.next != None):
            if(tempCard.getValue() > myValue):
                myValue = tempCard.getValue()
                myCount = counter
            counter+=1
            tempCard = tempCard.next

        return self.getNumberedCard(myCount)

    # same logic as findHighestValue but you check if the suit matches the parameter
    def findHighestValuebySuit(self,suit):
        tempCard = self.head
        myValue = 0
        myCount = 1  # index of card that has the highest value
        counter = 1  # overall counter
        while (tempCard.next != None):
            if (tempCard.getValue() > myValue and tempCard.getSuit() == suit):
                myValue = tempCard.getValue()
                myCount = counter
            counter += 1
            tempCard = tempCard.next

        return self.getNumberedCard(myCount)

    # highest rank is 14 (ace)
    # not based on suit or color
    # same logic for finding highest value
    def findHighestRank(self):
        tempCard = self.head
        myValue = 0
        myCount = 1  # index of card that has the highest value
        counter = 1  # overall counter
        while (tempCard.next != None):
            if (tempCard.getRank() > myValue):
                myValue = tempCard.getRank()
                myCount = counter
            counter += 1
            tempCard = tempCard.next

        return self.getNumberedCard(myCount)

    # same logic as findHighestRank but you check if the suit matches the parameter
    def findHighestRankBySuit(self, suit):
        tempCard = self.head
        myValue = 0
        myCount = 1  # index of card that has the highest value
        counter = 1  # overall counter
        while (tempCard.next != None):
            if (tempCard.getRank() > myValue and tempCard.getSuit() == suit):
                myValue = tempCard.getRank()
                myCount = counter
            counter += 1
            tempCard = tempCard.next

        return self.getNumberedCard(myCount)
    # print all the cards in the deck
    def printAll(self):
        tempCard = self.head
        while (tempCard.next != None):
            print(tempCard.__str__(), "with value of {} and rank of {}".format(tempCard.getValue(), tempCard.getRank()))
            tempCard = tempCard.getNext()
