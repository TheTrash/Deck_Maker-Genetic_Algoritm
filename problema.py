import random as rnd
# make deck
from CardGame.card import Card

class Problema:
    def __init__(self,coll_manager,seed=35):
        rnd.seed(seed)
        self.coll_manager = coll_manager

    def evaluate(self, d):
        # for now we evaluate the body medium of the deck
        total_body = 0
        for c in range(len(d)):
            skill_point = 0
            for skill in d[c].skill:
                skill_point += skill != "none"
            total_body += (d[c].attack + d[c].defense)/2 + skill_point
        return total_body

        # the main doubt here is how to evaluate the deck?
        # fight against his-self n times
        # make some calculus : body((attack+def)/2) medio 
        #       and add some extra point for the abilities that arent already considered
        # HOW I CAN SAY THAT ONE DECK IS BETTER THAN ANOTHER? ( ratio of win )
    
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
                card = self.coll_manager.getCard(deck)
                if card == None:
                    if old.skill == "attaccante":
                       card = Card(old.attack-1,old.defense, skill)
                    elif old.skill == "difensore":
                        card = Card(old.attack,old.defense-1,skill)
                    else:
                        skill = rnd.sample(self.coll_manager.skill_list,1)
                    card = Card(old.attack,old.defense,skill)
                deck.insert(i,card)
        return deck
    
    #this solution generate one deck
    def generate_solution(self):
        deck = self.coll_manager.makeDeck()
        return deck
        
