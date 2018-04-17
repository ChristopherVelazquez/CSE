import random
money = 15
answer = 7
rounds = 0
highest_money = 0
top_round= 0


while money > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = (dice2 + dice1)
    print("You rolled a %s and a %s which in total is %s" % (dice1,dice2,dice3))

    if(dice1 + dice2) == answer:
        money += 4
    else:
        money -= 1
    print("You have $%s left" % money)
    rounds += 1
    print ("You have played %s rounds" % rounds)
    print ("High Score: $%s at round %s" % (highest_money,top_round))
    if money > highest_money:
        highest_money = money
        top_round = rounds