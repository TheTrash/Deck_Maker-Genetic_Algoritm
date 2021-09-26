import numpy.random as rnd

class algoritmo_genetico:
    def __init__(self,prob,seed,weight=[0.5,0,5],nelem=20, p_cross=0.9, p_mut=0.05,elit=True,verbose=False):
        self.problem=prob
        rnd.seed(seed)
        self.num_elem=nelem
        self.prob_cross=p_cross
        self.weight=weight
        self.prob_mut=p_mut
        self.elit=elit
        self.verbose = verbose
        self.history = [[],[]]

    def run(self,num_gen,verbose=False):
        self.best_elem=(None, 0)
        self.gen=0
        self.init_population()
        for g in range(num_gen):
            self.gen=g+1
            coppie=self.selection_tournament()
            figli=self.apply_crossover(coppie)
            self.apply_mutation(figli)
            self.update_population(figli)
        return self.best_elem

    
        # here i've to call GAME object and play the match
        # make an internal tournament seems a good way to 
        # select best element 
        # in fact here we want to make the couples for 
        # crossover operation
        # so the tournament is good

    def selection(self):
        coppie=[]
        fit=[1.0/(self.fo[i]+1) for i in range(self.num_elem)]
        sum_fit=sum(fit)
        prob=[f/sum_fit for f in fit]
        for i in range(self.num_elem):
            coppie.append(self.roulette_wheel(prob))
        return coppie
    
    def selection_tournament(self):
        coppie=[]
        result= [0]*20
        win = 0
        for i in range(self.num_elem):
            result[i]=0
            win = 0
            for j in range(self.num_elem):
                if i != j :
                    for t in range(3):
                        p1,p2,_ = self.problem.game.match(self.pop[i],self.pop[j])
                        if p1 > p2:
                            win +=1
                    if win > 1:
                        result[i]+=1     
        sum_win=sum(result)
        prob=[win/self.num_elem for win in result]
        for i in range(self.num_elem):
            coppie.append(self.roulette_wheel(prob))
        return coppie


    def roulette_wheel(self,prob):
        r=rnd.random()
        j=0
        while prob[j]<r:
            r=r-prob[j]
            j+=1
        return self.pop[j]

    def init_population(self):
        # initialize to empty
        self.pop = [None]*self.num_elem
        self.fo = [0]*self.num_elem
        for i in range(self.num_elem):
            self.pop[i]=self.problem.generate_solution()
            self.fo[i]=self.evaluate(self.pop[i])
        self.update_best()

    def update_best(self):
        i_best = 0
        for i in range(1,self.num_elem):
            if self.fo[i]>self.fo[i_best]:
                i_best=i
        if self.fo[i_best]>self.best_elem[1]:
            self.best_elem=(self.pop[i_best],self.fo[i_best])
            if self.verbose:
                print(f"nuovo best deck {self.fo[i_best]} trovato alla {self.gen}")
                self.history[0].append(self.gen)
                self.history[1].append(self.fo[i_best])
        self.i_best=i_best
    
    def apply_crossover(self, coppie):
        figli = []
        for i in range(0,self.num_elem,2):
            if rnd.random() < self.prob_cross:
                c1,c2 = self.problem.do_crossover(coppie[i],coppie[i+1])
            else:
                c1=list(coppie[i])
                c2=list(coppie[i+1])
            figli.append(c1)
            figli.append(c2)
        return figli
    
    def apply_mutation(self,figli):
        for i in range(self.num_elem):
            self.problem.do_mutation(figli[i],self.prob_mut)
    
    def update_population(self,figli):
        best = self.pop[self.i_best]
        bestf = self.fo[self.i_best]
        self.pop=figli
        # valuta la nuova popolazione
        self.fo=[self.evaluate(p) for p in self.pop]
        if self.elit:
            j_worst=0
            for i in range(1,self.num_elem):
                if self.fo[i]>self.fo[j_worst]:
                    j_worst=i
            self.pop[j_worst]=best
            self.fo[j_worst]=bestf
        self.update_best()

    def evaluate(self,deck):
        value = self.problem.evaluate_body(deck)
        return value