from random import randint
from typing import Union

def FootStep():
    parts = []
    for _ in range(5):
        freq = randint(0, 500) + 350
        parts.append((freq, 1))
    parts.append((None, 120))
    for _ in range(6):
        freq = randint(0, 50) + 150
        parts.append((freq, 4))
    return parts

def GrabSound():
    return [(randint(1, 1000) + 1000, 0.5) for _ in range(50)]

def BlockSound():
    return [(x, 30) for x in range(60, 30, -3)]

def NoneSound():
    parts = []
    for _ in range(5):
        parts.append((400, 10))
        parts.append((None, 10))
        parts.append((700, 10))
        parts.append((None, 10))
    return parts

def Static():
    parts = []
    for _ in range(33):
        if randint(0, 1) == 0:
            for _ in range(randint(0, 60) + 10):
                parts.append((randint(0, 4000) + 3000, 1))
        else:
            parts.append((None, randint(3, 30)))
    return parts