import pygame
from typing import cast
from random import seed
from tcod.tileset import load_tilesheet, CHARMAP_CP437
from tcod import Console
from tcod.event import Event, wait
from tcod.context import new
from crt import Crt
from levels import Border, Update_Info

WIDTH = 80
HEIGHT = 60

def main() -> None:
    seed(None)
    pygame.init()
    crt = Crt(80, 60, 'Lord_Nightmare-Fixedsys-03.png')
    crt.open()

if __name__ == "__main__":
    main()
