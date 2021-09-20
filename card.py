import json

class Card():

    def __init__(self,at, de, ab):
        self.attack = at
        self.defense = de
        self.ability = ab
        for a in self.ability:
            if a == "attaccante":
                self.attack +=1
            if a == "difensore":
                self.defense +=1



    def to_json(self):
        return {"attack":self.attack, "defense":self.defense,"ability":self.ability } 