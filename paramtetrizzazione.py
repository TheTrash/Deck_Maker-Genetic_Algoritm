from CardGame.game import Game
from CardGame.collection_manager import CollectionManager
from GeneticAlgorithm.problema import Problema
from GeneticAlgorithm.genetic_algorithm import algoritmo_genetico

import copy as cp
import numpy.random as rnd
from numpy import var, average, std
import time
import matplotlib.pyplot as plt

params = [
        # ==== risalto elitismo con pochi elementi
        [10,0.2,0.05,False],
        [10,0.2,0.05,True], 
        # ====  risalto valori minimi e medi
        [20,0.2,0.05,False],    # min
        [20,0.5,0.25,False],    # medi
        # ==== risalto valori minimi medi massimi
        [30,0.2,0.05, False],   # min 
        [30,0.5,0.25,False], 
        [30,0.9,0.5, False],    # max
        ]

seed=35 #rnd.randint(500) #385
game = Game(max_point=50)
coll_manager = CollectionManager(collection_len=200,deck_len=10,seed=seed)
prob = Problema(coll_manager,game,seed=seed)


for i, p in enumerate(params):
    ag = algoritmo_genetico(prob,seed=seed,select="normal", nelem=p[0], p_cross=p[1], p_mut=p[2], elit=p[3], verbose=True)

    t = time.process_time()
    ag.run(num_gen=1000)
    elapsed_time = time.process_time() - t
    print("time to complete: ",elapsed_time)
    print(ag.gen, "generations")

    st = "["
    for c in ag.best_elem[0]:
        st += str(c.to_json()) + ",\n"
    st += "]"

    
    plt.plot(ag.history[0],ag.history[1])
    print(ag.history)
    plt.ylabel('Best Deck Body')
    plt.xlabel('Generations')
    plt.savefig(f'Experiments/params/gen1000_{round(elapsed_time,2)}-nelem={p[0]}-p_cross={p[1]}-p_mut={p[2]}-elit={p[3]}.png')
    plt.cla()
