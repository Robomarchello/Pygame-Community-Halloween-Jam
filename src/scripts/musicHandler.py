import pygame
from pygame.locals import *
from random import choice


class MusicHandler:
    def __init__(self):
        self.music = [
            pygame.mixer.Sound('src/sounds/MusicBadDynomite.ogg'),
            pygame.mixer.Sound('src/sounds/ForgottenLies.ogg'),
            pygame.mixer.Sound('src/sounds/StoriesViaEmail.ogg')
        ]
        self.CurrentMusic = choice(self.music)
        self.MusicChannel = self.CurrentMusic.play(-1)

        self.inMenu = False

    def check(self):
        if self.MusicChannel == None:
            self.CurrentMusic = choice(self.music)
            self.MusicChannel = self.CurrentMusic.play()
            
        elif not self.MusicChannel.get_busy():
            self.CurrentMusic = choice(self.music)
            self.MusicChannel = self.CurrentMusic.play()

    def set_volume(self, volume):
        if not self.inMenu:
            self.CurrentMusic.set_volume(volume)
        else:
            self.CurrentMusic.set_volume(1)