from time import sleep
import sounds
from random import randint, seed
import pygame
import pygame.time
import pygame.mixer
from crt import Crt

WIDTH = 80
HEIGHT = 60

def main() -> None:
    seed(None)
    pygame.mixer.pre_init(frequency=110100, size = -16, channels = 1)
    pygame.init()
    crt = Crt(80, 25, 'terminal8x12_gs_ro.png')
    for _ in range(3):
        kit = sounds.FootStep(crt.audio.sample_rate)
        sound = crt.audio.compose(kit, crt.audio.square_wave) #crt.audio.compose(kit, crt.audio.sine_wave)
        crt.audio.sound_out('sound/scrap/tone.wav', sound)
        sound.play()
        sleep(0.5)
    # clock = pygame.time.Clock()
    # while True:
    #     if not pygame.mixer.get_busy():
    #         clock.tick(30)
    #         crt.tick()

if __name__ == "__main__":
    main()
