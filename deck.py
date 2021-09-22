import random as rnd
import copy as cp

class Deck():
    
    def __init__(self, cards):
        self.list = cp.deepcopy(cards)
        self.active = cp.deepcopy(cards)
        self.scramble()
        self.discard = []
    
    def draw(self):
        board = []
        if len(self.active) < 3:
            self.refill()
        for i in range(3):
            c = self.active.pop()
            board.append(c)
        self.discard += board

        return cp.deepcopy(board)

    def scramble(self):
        rnd.shuffle(self.active)
    
    def refill(self):
        self.active += self.discard
        self.discard = []


