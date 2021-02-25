from random import seed
import pygame
import pygame.time
import pygame.mixer

from states.core_states import CoreState

def main() -> None:
    seed(None)
    pygame.mixer.pre_init(frequency=110100, size = -16, channels = 1)
    pygame.init()
    gamestate = CoreState()
    gamestate.run()

if __name__ == "__main__":
    main()
