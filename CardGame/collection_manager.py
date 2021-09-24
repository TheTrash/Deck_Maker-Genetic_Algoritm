import json
import numpy.random as rnd
from CardGame.card import Card
import copy

class CollectionManager:
    def __init__(self,collection_len, seed ,deck_len=10, prob_mut=0.05, filename="my_collection.json", ):
        self.collection_len = collection_len
        self.deck_len=deck_len
        self.filename = filename
        self.seed = seed
        rnd.seed(self.seed)
        self.skill_list = ["attaccante","difensore","esperto"]
        self.attack_list = [i for i in range(0,9)]
        self.body_list = [i  for i in range(2,12)]
        self.prob_mut = prob_mut
        #initialize collection
        self.collection_list = []

        try:
            # try to read
            f = open(self.filename,"r")
            data = json.load(f)
        except FileNotFoundError:
            # if not exist make it
            data = self.makeCollection()
        for i in range(len(data)):
            c = data[i]
            card = Card(c["attack"],c["defense"],c["skill"])
            self.collection_list.append(card)

    def makeCard(self):
        de = self.body_list[rnd.randint(len(self.body_list))]
        at = self.attack_list[rnd.randint(len(self.attack_list))]
        ab = ["none"]
        if rnd.random() < self.prob_mut:
            ab = [self.skill_list[rnd.randint(len(self.skill_list))]]
        cd = Card(at,de,ab)
        return cd

    def makeDeck(self):
        deck = rnd.choice(self.collection_list,self.deck_len,replace=False)
        return list(deck)


    def makeCollection(self):
        data = [self.makeCard().to_json() for i in range(self.collection_len)]
        out_file = open(self.filename, "w")
        json.dump(data,out_file, indent=1, separators=(',', ':'))
        return data

    def getCard(self,deck):
        card = self.collection_list[rnd.randint(self.collection_len)]
        if card not in deck:
            return card
        else:
            return None
