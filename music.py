import pygame
from constants import MUSIC_LOOP_SECONDS, MUSIC_REWIND_SECONDS

class Music(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.mixer.music.load("Battle Squadron In Game - Maf Remix.mp3")
        pygame.mixer.music.play(loops=-1)
    
    def update(self, deltaTime):
        music_pos = pygame.mixer.music.get_pos() / 1000
        if music_pos > MUSIC_LOOP_SECONDS:
            music_startpos = music_pos - MUSIC_REWIND_SECONDS
            print(f"Music rewinded to: {music_startpos}")
            #pygame.mixer.music.rewind()
            pygame.mixer.music.play(loops=-1, start=music_startpos)
            #self.loopend = MUSIC_REWIND_SECONDS
