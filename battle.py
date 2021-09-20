from card_generator import makeCard
player1 = [makeCard() for i in range(3)]
player2 = [makeCard() for i in range(3)]

#first of all valut the ability
# in fact now the ability are evaluate on card creation

def fight(c1,c2):
    c1.defense -= c2.attack
    c2.defense -= c1.attack
    if c1.defense <= 0:
        r1 = None
    else:
        r1 = c1
    if c2.defense <=0:
        r2 = None
    else:
        r2 = c2
    return c1,c2

c=0


for p1, p2 in zip(player1,player2):
    print( f'battle {c} ')
    c1,c2 = fight(p1,p2)
    p1,p2 = (c1,c2)
    print(c1.to_json())
    print(c2.to_json())
    c+=1
    # evaluate 
    # if p1 or p2 has "roccaforte" +1 hp
    # p1.attack -> p2.defense
    # p2.attack -> p1.defense
    # if they die remove from the game

# evaluated the board discard dead card and put new card in that position
print("player 1 board remains:")
for cd in player1:
    print(cd.to_json())
print("player 2 board remains:")
for cd in player2:
    print(cd.to_json())


