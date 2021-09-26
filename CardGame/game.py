from .deck import Deck
import copy as cp

## Game take two lists and initialize it as a deck for the battle


class Game:
    def __init__(self, max_point=50, verbose=False):
        self.max_point = max_point
        self.verbose = verbose

        ## make the  deck
        ## use deep copy for prevent to modify the deck
    def match(self, d1, d2):
        point1 = 0
        point2 = 0
        total_battle = 0
        total_round = 0
        deck1 = Deck(d1)
        deck2 = Deck(d2)
        while (point1 < self.max_point and point2 < self.max_point):

            board1 = deck1.draw()
            board2 = deck2.draw()
            for i in range(len(board1)):
                self.fight(board1[i],board2[i])

            r1,r2 = self.evaluate_board(board1,board2)

            point1+=r1
            point2+=r2
            total_battle+=1
            if self.verbose:
                print(point1,point2, total_battle)
        return point1, point2, total_battle


    def evaluate_board(self,b1,b2):
        r1,r2 = (0,0)
        for p1,p2 in zip(b1,b2):
            r1+=self.evaluate_card(p1)
            r2+=self.evaluate_card(p2)
        return r1,r2
    
    def evaluate_card(self,c):
        r = 0
        if c.defense > 0:
            r+=1
            if c.skill == "esperto":
                r+=1
        return r  
  
    def fight(self,c1,c2):
        c1.defense -= c2.attack
        c2.defense -= c1.attack