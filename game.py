import copy as cp

class Game():
    total_battle = 0
    total_round = 0
    def __init__(self,d1,d2,max_point=20):
        self.deck1 = cp.deepcopy(d1)
        self.deck2 = cd.deepcopy(d2)
        self.point1 = 0
        self.point2 = 0
        self.max_point = max_point

        ## make the player with deck
        ## use deep copy for prevent to modify the deck
    def match(self):
        while (self.point1 < self.max_point and point2 < self.max_point):
            board1 = cp.deepcopy(self.deck1.draw())
            board2 = cp.deepcopy(self.deck2.draw())
            position = [1,1,1]
            step = 1
            while(sum(position) > 0):
                for i, e in enumerate(position):
                    if e == 1:
                        res = fight(board1[i],board2[i])
                        position[i] = res
                step+=1
            

            r1,r2 = evaluate_board(board1,board2)
            self.point1+=r1
            self.point2+=r2
            total_round += step
            self.total_battle+=1
        return point1,point2, total_round, total_battle


    def evaluate_board(b1,b2):
        r1,r2 = (0,0)
        for p1,p2 in zip(b1,b2):
            r1+=evaluate_card(p1)
            r2+=evaluate_card(p2)
        return r1,r2
    
    def evaluate_card(c):
        r = 0
        if c.defense > 0:
            r+=1
            if c.skill == "expert":
                print("expertizer")
                r+=1
        return r  
  
    def fight(c1,c2):
        c1.defense -= c2.attack
        c2.defense -= c1.attack
        if c1.defense > 0 and c2.defense > 0:
            return 1
        else:
            return 0