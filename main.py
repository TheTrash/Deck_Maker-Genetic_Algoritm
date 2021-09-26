from CardGame.game import Game
from CardGame.collection_manager import CollectionManager
from problema import Problema
from ag import algoritmo_genetico
import copy as cp
import numpy.random as rnd
from numpy import var, average, std

seed=35#rnd.randint(500) #385
game = Game()

coll_manager = CollectionManager(collection_len=200,seed=seed)
prob = Problema(coll_manager,game,seed=seed)

ag = algoritmo_genetico(prob,nelem=10,p_mut=0.5,weight=[1,0], seed=seed, verbose=True)

ag.run(num_gen=500,verbose=True)
print([i.to_json() for i in ag.best_elem[0]])







'''
#tournament
pop = [prob.generate_solution() for i in range(20)]
fo = [prob.evaluate_body(pop[i]) for i in range(20)]
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
tmp1, tmp2 = zip(*sorted(zip(result, fo)))
print(tmp1,"\n",tmp2)

'''