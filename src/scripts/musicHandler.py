import pygame
from pygame.locals import *
from random import choice


class MusicHandler:
    def __init__(self):
        self.music = [
            pygame.mixer.Sound('src/sounds/MusicBadDynomite1.ogg')
        ]
        self.CurrentMusic = choice(self.music)
        self.MusicChannel = self.CurrentMusic.play()

        self.inMenu = False

    def check(self):
        if self.CurrentMusic.get_num_channels() == 0:
            self.CurrentMusic = choice(self.music)

    def set_volume(self, volume):
        if not self.inMenu:
            self.CurrentMusic.set_volume(volume)
        else:
            self.CurrentMusic.set_volume(1)