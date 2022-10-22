import pygame
from pygame.locals import *
from src.scripts.camera import Camera
from random import choice, randint

pygame.mixer.init()

class Game():
    def __init__(self, screen, map):
        self.monster = {'onLeft': False, 'inFront': False, 'onRight': False}
        self.monsterTimer = randint(3, 7) * 60
        self.timerFreeze = False
        self.jumpTimer = 4 * 60

        self.camera = Camera(screen, map)

        self.stepSound = pygame.mixer.Sound('src/assets/steps.ogg')
        self.stepChannel = None

    def draw(self, screen, mp):
        self.camera.draw(screen, mp)

    def update(self):
        self.monsterTimer -= 0.5#-= dt
        if self.monsterTimer < 0 and not self.timerFreeze:
            self.monster[choice(list(self.monster.keys()))] = True
            self.timerFreeze = True
            self.monsterTimer = randint(3, 7) * 60

        if self.timerFreeze:
            if self.stepChannel == None:
                if self.monster['onLeft']:
                    self.stepChannel = self.stepSound.play()
                    self.stepChannel.set_volume(1, 0)

                if self.monster['inFront']:
                    self.stepChannel = self.stepSound.play()
                    self.stepChannel.set_volume(1, 1)

                elif self.monster['onRight']:
                    self.stepChannel = self.stepSound.play()
                    self.stepChannel.set_volume(0, 1)
