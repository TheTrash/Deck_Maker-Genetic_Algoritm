from CardGame.game import Game
from CardGame.collection_manager import CollectionManager
from GeneticAlgorithm.problema import Problema
from GeneticAlgorithm.genetic_algorithm import algoritmo_genetico

import copy as cp
import numpy.random as rnd
from numpy import var, average, std
import time


seed=35 #rnd.randint(500) #385
game = Game()

coll_manager = CollectionManager(collection_len=200,deck_len=10,seed=seed)
prob = Problema(coll_manager,game,seed=seed)
ag = algoritmo_genetico(prob,nelem=10, p_mut=0.5, select="normal", seed=seed, verbose=True)


t = time.process_time()
ag.run(num_gen=50000,verbose=True)
elapsed_time = time.process_time() - t
print("time to complete: ",elapsed_time)
print(ag.gen, "generations")
print("best deck list")
for c in ag.best_elem[0]:
    print(c.to_json())


import matplotlib.pyplot as plt
plt.plot(ag.history[0],ag.history[1])
print(ag.history)
plt.ylabel('Best Deck Body')
plt.xlabel('Generations')
plt.show()