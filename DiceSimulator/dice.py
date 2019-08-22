import random

# simple dice class, all it does is return a random number from 1~6

class Dice:
    def __init__(self):
        pass

    def roll(self):
        return (random.randrange(1,7))