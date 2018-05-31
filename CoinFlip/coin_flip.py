import random


def coin_flip(number):

    flip_wins, heads, tails = [], 0, 0

    for i in range(number):
        
        flip = random.randint(0, 1)

        if flip == 0:
            print("Heads")
            flip_wins.append("Heads")
        else:
            print("Tails")
            flip_wins.append("Tails")

    print(flip_wins)


coin_flip(10)
