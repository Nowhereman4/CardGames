# deck class has instances of cards and can shuffle, might also use a "deck" as a hand for each player
# a deck is a linked list of cards. head is the top card
# any "remove" or "delete" will return the card it is deleting, so the card can be given to a player or put into a pile to compare cards from all players
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
    # works
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
    # works
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
        card.next = None
        return card

    # get NumberedCard can be used in a variety of ways to simulate shuffling, and getting cards based on certain attributes
    def getNumberedCard(self, count):
        temp = self.head
        previous = self.head
        myCard = None
        tempCounter = 1;
        # if
        foundCard = False
        if(count == 1 or count == 0):
            myCard = self.removeFromBeginning()
        else:
            while (temp != None):

                if (tempCounter == count):
                    myCard = temp
                    temp = temp.next
                    break
                tempCounter += 1
                previous = temp
                temp = temp.next

            # if you call a number that is greater than the size of the deck, just take the last card instead
            if (temp == None):
                myCard = self.removeFromEnd()
            else:
                previous.next = temp
            myCard.next = None
        return myCard

    # add card to bottom of deck
    def insertAtEnd(self, card):
        card.next = None
        tempCard = self.head
        if(self.head == None):
            self.head = card
        while tempCard.next != None:
            tempCard = tempCard.next

        tempCard.next = card

    def removeFromEnd(self):
        tempCard = self.head
        previous = tempCard
        while(tempCard.next != None):
            previous = tempCard
            tempCard = tempCard.next
        previous.next = None
        return tempCard
    # highest value is 10, and an ace is considered 1
    # not related to suit or color
    # when you get the highest value, the index in the linked list is set
    # this is used to remove the card using getNumberedCard(int).
    # find highestValue will return the card found
    def getHighestValue(self):
        tempCard = self.head
        myValue = 0
        myCount = 1 # index of card that has the highest value
        counter = 1 # overall counter
        while(tempCard != None):
            if(tempCard.getValue() > myValue):
                myValue = tempCard.getValue()
                myCount = counter
            counter+=1
            tempCard = tempCard.next

        return self.getNumberedCard(myCount)

    # same logic as findHighestValue but you check if the suit matches the parameter
    def getHighestValuebySuit(self,suit):
        tempCard = self.head
        myValue = 0
        myCount = 1  # index of card that has the highest value
        counter = 1  # overall counter
        while (tempCard != None):
            if (tempCard.getValue() > myValue and tempCard.getSuit() == suit):
                myValue = tempCard.getValue()
                myCount = counter
            counter += 1
            tempCard = tempCard.next

        return self.getNumberedCard(myCount)

    # highest rank is 14 (ace)
    # not based on suit or color
    # same logic for finding highest value
    def getHighestRank(self):
        tempCard = self.head
        myValue = 0
        myCount = 1  # index of card that has the highest value
        counter = 1  # overall counter
        while (tempCard != None):
            if (tempCard.getRank() > myValue):
                myValue = tempCard.getRank()
                myCount = counter
            counter += 1
            tempCard = tempCard.next

        return self.getNumberedCard(myCount)

    # same logic as findHighestRank but you check if the suit matches the parameter
    def getHighestRankBySuit(self, suit):
        tempCard = self.head
        myValue = 0
        myCount = 1  # index of card that has the highest value
        counter = 1  # overall counter
        while (tempCard != None):
            if (tempCard.getRank() > myValue and tempCard.getSuit() == suit):
                myValue = tempCard.getRank()
                myCount = counter

            counter += 1
            tempCard = tempCard.next

        return self.getNumberedCard(myCount)

    # find card based on its name and suit since rank is unique to each card, return the card
    def getByRankAndSuit(self, rank, suit):
        tempCard = self.head
        counter = 1  # overall counter
        foundCard = False
        while(tempCard != None):
            if(tempCard.getRank() == rank and tempCard.getSuit() == suit): #if you find your card set your counter
                foundCard = True
                break
            counter += 1
            tempCard = tempCard.next

        # if you don't find the card return none
        if(foundCard == True):
            return self.getNumberedCard(counter)
        else:
            return None

    def getByNameAndSuit(self, name, suit):
        tempCard = self.head
        counter = 1  # overall counter
        foundCard = False
        while(tempCard != None):
            if(tempCard.getName() == name and tempCard.getSuit() == suit): #if you find your card set your counter
                foundCard = True
                break
            counter += 1
            tempCard = tempCard.next

        # if you don't find the card return none
        if(foundCard == True):
            return self.getNumberedCard(counter)
        else:
            return None
    # print all the cards in the deck
    def printAll(self):
        tempCard = self.head
        while (tempCard != None):
            print(tempCard.__str__(), "with value of {} and rank of {}".format(tempCard.getValue(), tempCard.getRank()))
            tempCard = tempCard.getNext()
