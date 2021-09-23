from CardGame import Game
import collection_reader


deck1 = collection_reader.makeDeck()
deck2 = collection_reader.makeDeck()

game = Game(deck1,deck2)

#print(game.match())
