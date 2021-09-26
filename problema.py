import numpy.random as rnd
# make deck
from CardGame.card import Card
import copy as cp

class Problema:
    def __init__(self,coll_manager,game,seed, len_eval_set=5,):
        rnd.seed(seed)
        self.game = game
        self.coll_manager = coll_manager
        self.len_eval_set = len_eval_set 
        self.test_deck_set = [ coll_manager.makeDeck() for i in range(len_eval_set) ]

    def evaluate_body(self, d):
        # for now we evaluate the body medium of the deck
        total_body = 0
        for c in range(len(d)):
            skill_point = 0
            for skill in d[c].skill:
                skill_point += skill != "none"
            total_body += (d[c].attack + d[c].defense)/2 + skill_point
        return total_body/self.coll_manager.deck_len

        # the main doubt here is how to evaluate the deck?
        # fight against his-self n times
        # make some calculus : body((attack+def)/2) medio 
        #       and add some extra point for the abilities that arent already considered
        # HOW I CAN SAY THAT ONE DECK IS BETTER THAN ANOTHER? ( ratio of win )
    def evaluate_winrate(self,d):
        win = 0
        for i in range(self.len_eval_set):
            tmp = 0
            for t in range(3):
                p1,p2,_ = self.game.match(d,self.test_deck_set[i])
                if p1 > p2:
                    tmp +=1
            if tmp > 1:
                win+=1
        win_rate= win/self.len_eval_set

        return win_rate

    def do_crossover(self,d1,d2):
        ## the deck has to be sorted?
        # crossover a due tagli 
        cut1 = rnd.randint(1,int(len(d1)/2))
        cut2 = rnd.randint(cut1,len(d1)-2)
        c1 =  d1[:cut1] + d2[cut1:cut2] + d1[cut2:]
        c2 =  d2[:cut1] + d1[cut1:cut2] + d1[cut2:]

        return c1,c2
    
    def do_mutation(self, deck, prob_mut=0.05):
        # here occurs the problem that the ability has to be activated after the mutation
        # in fact we can reinitialize the card but is a quite annoying
        for i in range(len(deck)):
            if rnd.random()<prob_mut:
                old = deck.pop(i)
                if rnd.random()<0.5:
                    tmpCard = self.coll_manager.getCard()
                    if tmpCard not in deck:
                        card = Card(tmpCard.attack,tmpCard.defense,tmpCard.skill)
                    else:
                        card = Card(old.attack,old.defense, old.skill)
                else:
                    skill = self.coll_manager.getNewSkill(old.skill)
                    if old.skill == "attaccante":
                       card = Card(old.attack-1,old.defense, skill)
                    elif old.skill == "difensore":
                        card = Card(old.attack,old.defense-1,skill)
                    else:
                        card = Card(old.attack,old.defense,skill)
                deck.insert(i,card)
        return deck
    
    #this solution generate one deck
    def generate_solution(self):
        deck = self.coll_manager.makeDeck()
        return deck



