import json

class Card():

    def __init__(self,at, di, ab):
        self.attack = at
        self.defense = di
        self.skill = ab
        for a in self.skill:
            if a == "fighter":
                self.attack +=1
            if a == "defender":
                self.defense +=1

    def to_json(self):
        return {"attack":self.attack, "defense":self.defense,"skill":self.skill } 
