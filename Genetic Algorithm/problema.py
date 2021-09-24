# classe del problema Number Partitioning
# 

import random as rnd

class Problema:
    
    def __init__(self,lista):
        self.numeri=lista
        self.num_numeri=len(lista)
        
    def evaluate(self,soluz):
        sum0=0
        sum1=0
        for i in range(self.num_numeri):
            if soluz[i]==0:
                sum0 += self.numeri[i]
            else:
                sum1 += self.numeri[i]
        return abs(sum0-sum1)
    
    def do_crossover(self, s1, s2):
        # crossover ad un punto
        t=random.randint(1,self.num_numeri-2)
        c1=s1[:t] + s2[t:]
        c2=s2[:t] + s1[t:]
        return c1,c2
        
    def do_mutation(self, soluz, prob_mut=0.05):
        # inversione di ogni singolo bit con prob. prob_mut
        for j in range(self.num_numeri):
            if rnd.random()<prob_mut:
                soluz[j]=1-soluz[j]
                
    def generate_solution(self):            
        l=[random.randint(0,1) for j in range(self.num_numeri)]
        return l
          

            
