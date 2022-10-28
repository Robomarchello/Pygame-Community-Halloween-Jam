import pygame
from pygame.locals import *
from random import randint


class RandomSnek:
    def __init__(self, DoorMenu, Radio, Scarer):
        self.appear = False
        self.Played = False
        self.opened = False

        self.ScareTimer = 0
        self.Time = 90
        
        self.DoorMenu = DoorMenu
        self.Radio = Radio
        self.Scarer = Scarer
        self.sound = pygame.mixer.Sound('src/sounds/randomSnek.ogg')
        self.image = pygame.image.load('src/assets/RandomSnek.png').convert_alpha()

    def restart(self):
        self.appear = False
        self.ScareTimer = 0
        self.Played = False
        self.opened = False

    def draw(self, screen, educated, dt):
        if self.appear:
            if not self.ScareTimer > self.Time:
                screen.blit(self.image, (0, 0))
        else:
            self.ScareTimer = 0

        if educated:
            if self.DoorMenu.opened:
                if not self.opened:
                    if randint(0, 7) == 7:
                        if not self.Played:
                            self.appear = True
                
                if self.Played:
                    self.appear = False
                    self.Played = False

                self.opened = True
            else:
                if self.appear:
                    if not self.Played:
                        self.sound.play()
                        self.Played = True
                        
                self.opened = False

        if self.appear:
            self.ScareTimer += dt
            if self.ScareTimer > self.Time:
                self.Scarer.isSecond = True

                return True
        
        return False