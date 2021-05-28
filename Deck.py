# deck class has instances of cards and can shuffle, might also use a "deck" as a hand for each player
import Card
class Deck:
    valueSize = 10
    cardSuits = tuple(("clubs", "diaomonds", "hearts", "spades"))
    cardValuesAsString = tuple(("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"))
    #def __init__(self, Card)