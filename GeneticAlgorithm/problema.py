import numpy.random as rnd
# make deck
from CardGame.card import Card
import copy as cp

class Problema:
    def __init__(self,coll_manager,game,seed):
        rnd.seed(seed)
        self.game = game
        self.coll_manager = coll_manager

    def evaluate_body(self, d):
        total_body = 0
        for c in range(len(d)):
            total_body += (d[c].attack + d[c].defense)/2 + (d[c].skill != "none")
        return total_body/self.coll_manager.deck_len


    def do_crossover(self,d1,d2):
        cut1 = rnd.randint(1,int(len(d1)/2))
        cut2 = rnd.randint(cut1,len(d1)-2)
        c1 =  d1[:cut1] + d2[cut1:cut2] + d1[cut2:]
        c2 =  d2[:cut1] + d1[cut1:cut2] + d1[cut2:]

        return c1,c2
    
    def do_mutation(self, deck, prob_mut=0.05):
        for i in range(len(deck)):
            if rnd.random()<prob_mut:
                old = deck.pop(i)
                tmpCard = self.coll_manager.getCard()
                if rnd.random() < 0.5 and tmpCard not in deck:
                    card = Card(tmpCard.attack,tmpCard.defense,tmpCard.skill)
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
    

    def generate_solution(self):
        deck = self.coll_manager.makeDeck()
        return deck



