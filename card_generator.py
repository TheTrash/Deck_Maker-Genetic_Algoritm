#card generator
import random as rnd
from card import Card

def makeCard():
    de = body[rnd.randrange(len(body))]
    at = attack[rnd.randrange(len(attack))]
    ab = ["none"]
    if rnd.random() < 0.2:
        ab = [ability[rnd.randrange(len(ability))]]
    cd = Card(at,de,ab)
    return cd

attack = [i for i in range(2,7)]
body = [i for i in range(3,8)]
ability = ["attaccante","difensore","roccaforte"]


deck = [makeCard() for i in range(20)]

for cd in deck:
    print(cd.to_json())

