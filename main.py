from CardGame.game import Game
from CardGame.collection_manager import CollectionManager
from problema import Problema
from ag import algoritmo_genetico
import copy as cp
import numpy.random as rnd
from numpy import var, average, std

seed=rnd.randint(500)
coll_manager = CollectionManager()
game = Game()
prob = Problema(coll_manager,seed=seed)

'''
d1 = coll_manager.makeDeck()
c1 = coll_manager.getCard(d1)
print(c1)
'''

ag = algoritmo_genetico(prob, game,p_mut=0.5)
ag.run(num_gen=500,verbose=True)
print([i.to_json() for i in ag.best_elem[0]])








'''
#tournament
pop = [prob.generate_solution() for i in range(20)]
fo = [prob.evaluate(pop[i]) for i in range(20)]
print(fo)
result= [0]*20
win = 0
for i in range(len(pop)):
    result[i]=0
    win = 0
    for j in range(len(pop)):
        if i != j :
            for t in range(3):
                p1,p2,_ = game.match(pop[i],pop[j])
                if p1 > p2:
                    win +=1
            if win > 1:
                result[i]+=1

print(result)
'''
