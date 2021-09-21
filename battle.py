from card_generator import makeCard
from deck import Deck
import copy as cp

deck1 = Deck([makeCard() for i in range(10)])
deck2 = Deck([makeCard() for i in range(10)])

# evaluation parameters
life1, life2 = (0,0)
total_battle = 0
total_round = 0

#first of all valut the ability
# in fact now the ability are evaluate on card creation

def fight(c1,c2):
    c1.defense -= c2.attack
    c2.defense -= c1.attack
    if c1.defense > 0 and c2.defense > 0:
        return 1
    else:
        return 0
    
def evaluate_board(b1,b2):
    r1,r2 = (0,0)
    for p1,p2 in zip(b1,b2):
        if p1.defense > 0:
            r1+=1
        if p2.defense > 0:
            r2+=1
    return r1,r2
 
while(life1 < 20 and life2 < 20):
    board1 = cp.deepcopy(deck1.draw())
    board2 = cp.deepcopy(deck2.draw())

    position = [1,1,1]
    rund = 1
    ''' evaluate the guaritore effect
        if pos1.ability == "guaritore":
            print("player1 +1 hp")
        if pos2.ability == "guaritore":
            print("player2 +1 hp")
    '''
    print(position)
    print( f'battle {total_battle} ')
    while(sum(position) > 0):
        print(f"round : {rund}")
        for i,e in enumerate(position):
            print( f'row {i} ')
            if e == 1:
                res = fight(board1[i],board2[i])
                position[i] = res
        rund +=1
        print(position)
    total_battle+=1
    # evaluate 
    # if p1 or p2 has "roccaforte" +1 hp
    # p1.attack -> p2.defense
    # p2.attack -> p1.defense
    # if they die remove from the game

# evaluated the board discard dead card and put new card in that position

    r1,r2 = evaluate_board(board1,board2)
    print(f"player 1 board has {r1} card alive")
    for cd in board1:
        print(cd.to_json())
    print(f"player 2 board has {r2} card alive")
    for cd in board2:
        print(cd.to_json())

    life1+=r1
    life2+=r2
    total_round += rund
    print(life1,life2, total_round, total_battle)

# for demo propouse print the deck
for ca in deck1.list:
    print(ca.to_json())