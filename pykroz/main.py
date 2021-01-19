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
    
    kit = sounds.FootStep()
    sound = crt._audio.compose(kit, crt._audio.square_wave)
    # crt.audio.sound_out('sound/scrap/tone.wav', sound)
    sound.play()
    sleep(0.5)
    kit = sounds.GrabSound()
    sound = crt._audio.compose(kit, crt._audio.square_wave)
    sound.play()
    sleep(0.5)
    kit = sounds.BlockSound()
    sound = crt._audio.compose(kit, crt._audio.square_wave)
    sound.play()
    sleep(0.5)
    kit = sounds.NoneSound()
    sound = crt._audio.compose(kit, crt._audio.square_wave)
    sound.play()
    sleep(0.5)
    kit = sounds.Static()
    sound = crt._audio.compose(kit, crt._audio.square_wave)
    sound.play()
    sleep(0.5)
    # clock = pygame.time.Clock()
    # while True:
    #     if not pygame.mixer.get_busy():
    #         clock.tick(30)
    #         crt.tick()

if __name__ == "__main__":
    main()
