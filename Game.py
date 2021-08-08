from Deck import Deck
import random
from Player import Player

# the way players are named can be changed in the future

# changed getcardbynameandsuit to getCardFromPlayersByNameAndSuit and made it so within the method it append()'s the
# player's card to listofcards[] that the player chooses

class Game():
    playerTuple = tuple((Player("one", 1), Player("two", 2), Player("Three", 3), Player("Four", 4), Player("Five", 5), Player("Six", 6), Player("Seven", 7), Player("Eight", 8)))
    # the round of game is used to hold a deck of the cards players play in around. The key is putting the cards in order
    roundOfGame = Deck()
    # list of cards is an array that holds card objects.
    # these are cards players put in during a round or trick of a game
    # so that they can be compared to see who won the round
    listOfCards =[]
    # create a game by starting with how many players there are and add them to the list of players
    # create a deck of 52 cards
    def __init__(self, numberOfPlayers):
        # start with 52 cards
        self.deck = Deck()
        self.deck.buildDeck()
        self.size = 52
        self.players = list()
        for count in range(0, numberOfPlayers):
            self.players.append(self.playerTuple[count])

    # all cards in the deck are divided evenly among players

    def dealDeck(self):
        # while there are still cards in the game deck
        endOfDeck = False
        while(self.deck.head != None):
            if(endOfDeck):
                break
            for player in self.players:
                # cards cannot always be given equally to all players, so we must create a break
                if(self.size == 0):
                    endOfDeck = True
                    break
                cardNumber = random.randint(1,self.size)
                self.size-= 1
                # a player will be given a card from the deck. you remove a card from the deck, and the player inserts that card into their hand
                playerCard = self.deck.getNumberedCard(cardNumber)
                #print(playerCard.__str__())
                player.hand.insertAtBeginning(playerCard);


    # ask each player for a card in a certain suit and add it to self.listOfCards[]
    def getCardFromPlayersByNameAndSuit(self):
        self.listOfCards = []
        for player in self.players:
            # for each player get the card name, for example "ace", "four" etc
            player.printHand()
            print("player",player.getName(),":")
            name = input("input your card name (i.e ace, two, jack). If you want to see your hand type'help'")
            print("player",player.getName(),":")
            suit = input("input the suit of this card")
            self.listOfCards.append(player.hand.getByNameAndSuit(name, suit))


    # returns the number of cards in the deck that are of the suit
    def getCountBySuit(self, suit):
        temp = self.head
        count = 0
        while(temp):
            if(temp.getSuit() == suit):
                count+= 1

        return count

    # returns the number of cards with that name in the deck
    def getCountByName(self, name):
        temp = self.head
        count = 0
        while(temp):
            if(temp.getName() == name):
                count+= 1

            return count
    def printAllHands(self):
        for x in range(self.players.__len__()):
            print("\nplayer {}'s hand:".format(x))
            self.players[x].printHand()


