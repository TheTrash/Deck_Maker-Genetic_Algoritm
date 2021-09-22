

f = open('my_collection.json',)

data = json.load(f)
collection = []

for i in range(len(data)):
    c = data[i]
    card = Card(c["attack"],c["defense"],c["ability"])
    collection.append(card)

collection_len = len(collection)

def makeDeck(len_deck = 10):
    deck = rnd.sample(collection,10)
    return deck

