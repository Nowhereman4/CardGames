from Game import Game

# spades inherits from the Game class. "play" function that includes the actual game logic of the game players bet
# how many tricks they will win in a round. (player.score)  A round is in this case when the deck is empty (13 rounds)
# the discard deck for each player will include all hands and be checked for spades
class Spades(Game):

    # assume spades has four players
    def __init__(self):
        super().__init__(4)
        self.winningScore = 500
        self.dealDeck()
        # contract points is the multiplier for how many games you won and the points awarded
        self.contractPoints = 10
        self.pointsOver = 1
        # if you don't win enough some versions punish you based on how many you were under but in this version we won't
        self.underPenalty = 0
        self.trumpSuit = "spades"
        self.leadSuit = ""
        self.teamOneScore = 0
        self.teamTwoScore = 0

    def roundScore(self):
        print("calculating score")
        # for each player
            # if player score == player bet
                # team score += player score * self.contractPoints
            # elif player score > player bet
                #  extraPoints = player score - player bet
                # team score += ((player score * self.contractPoints) + (self.pointsOver * extraPoints))
            # else: # player score < player bet
                # team score += player score * self.underPenalty

    # using self.listOfCards[], determine who won the round
    def trickWinner(self):
        teamOnePoints = 0
        teamTwoPoints = 0
        # get a card from each player and put it in "listOfCards"
        self.getCardFromPlayersByNameAndSuit()
        self.leadSuit = self.listOfCards[0].getSuit()
        # current leading card
        currentWinner = self.listOfCards[0]

        # determine winner from all cards
        # the possible scenarios
            # if LEADING SUIT IS SPADE:
                # 1a. if card is not a spade:   continue
                # 1a. else:     compare ranks
            # if LEADING SUIT IS NOT SPADE:
                # 1b. if current winner is a spade:     continue
                    # 2b. if card is a spade:   compare ranks
                # 3b. if card is in lead suit:      compare ranks
                # 3b. else:     continue

            # 1. your card is in the lead suit and the current card is not a spade
            # 2. your card is a spade
            # 4. your card is in neither spades or lead suit
        for cards in self.listOfCards:
            # if the leading suit is spades
            if(self.leadSuit == self.trumpSuit):
                # if your card is a spade then compare, if it isn't a spade then it can't be ranked higher
                if(cards.getSuit() == self.trumpSuit):
                    if (cards.getRank() > currentWinner.getRank()):
                        currentWinner = cards
            # the lead suit isn't spades
            else:
                # if the current winning card is a spade and your card is a spade
                if(cards.getSuit() == self.trumpSuit):
                    if(currentWinner.getSuit() == self.trumpSuit):
                        if(cards.getRank() > currentWinner.getRank()):
                            currentWinner = cards
                    else:
                        currentWinner = cards
                #if your card is in the lead suit
                elif(cards.getSuit() == self.leadSuit):
                    if(cards.getRank() > currentWinner.getRank()):
                        currentWinner = cards
                # if your card isn't a spade or a lead suit, then it loses to the highest ranked card
        winnerIndex = 0
        for index, cards in enumerate(self.listOfCards):
            if(currentWinner.getName() == cards.getName()):
                if(currentWinner.getSuit() == cards.getSuit()):
                    winnerIndex = index
                    print("winner index is ", winnerIndex)
                    break

        if(winnerIndex == 0 or 2):
            self.teamOne


spadesGame = Spades()
spadesGame.trickWinner()
spadesGame.trickWinner()
spadesGame.trickWinner()
spadesGame.trickWinner()

        # determine tbghhe winner and give the point to the correct team



