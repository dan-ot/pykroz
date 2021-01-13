import pygame
from random import seed
from crt import Crt

WIDTH = 80
HEIGHT = 60

def main() -> None:
    seed(None)
    pygame.init()
    crt = Crt(80, 60, 'PTMono-Regular.ttf', 12, 2.0)
    crt.open()

if __name__ == "__main__":
    main()
