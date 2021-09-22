#card card management
import random as rnd
from card import Card
import json

collection_len = 20

attack = [i for i in range(2,7)]
body = [i for i in range(3,8)]
ability = ["attaccante","difensore","esperto", "guaritore"]

def makeCard():
    de = body[rnd.randrange(len(body))]
    at = attack[rnd.randrange(len(attack))]
    ab = ["none"]
    if rnd.random() < 0.15:
        ab = [ability[rnd.randrange(len(ability))]]
    cd = Card(at,de,ab)
    return cd

def makeCollection(l):
    collection = [makeCard().to_json() for i in range(l)]
    out_file = open("my_collection.json", "w")
    json.dump(collection,out_file, indent=1, separators=(',', ':'))