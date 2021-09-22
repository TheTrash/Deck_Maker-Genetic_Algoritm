import json
from card import Card

f = open('my_collection.json',)

data = json.load(f)
collection = []
for i in range(len(data)):
    c = data[i]
    card = Card(c["attack"],c["defense"],c["ability"])
    collection.append(card)
    print(card.to_json())
print(len(collection))