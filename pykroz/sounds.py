from random import randint
from typing import Union

SINGLE_FRAME_DURATION = 1

def FootStep(sample_rate: Union[int, None] = None):
    parts = []
    for _ in range(50):
        freq = randint(0, 500) + 350
        parts.append((freq, 120 / 50))
    parts.append((None, 120))
    for _ in range(60):
        freq = randint(0, 50) + 150
        parts.append((freq, 120 / 60))
    return parts

def GrabSound():
    return [(randint(1, 1000) + 1000, SINGLE_FRAME_DURATION) for _ in range(160)]

def BlockSound():
    return [(x, 3) for x in range(60, 30, -1)]

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
                parts.append((randint(0, 4000) + 3000, SINGLE_FRAME_DURATION))
        else:
            parts.append((0, randint(3, 30)))
    return parts