from random import seed
import pygame
import pygame.time
import pygame.mixer
from engine.crt import Crt

def main() -> None:
    seed(None)
    pygame.mixer.pre_init(frequency=110100, size = -16, channels = 1)
    pygame.init()
    crt = Crt(80, 25, 'assets/terminal8x12_gs_ro.png')

    clock = pygame.time.Clock()
    while True:
        if not pygame.mixer.get_busy():
            clock.tick(30)
            crt.tick()

if __name__ == "__main__":
    main()
