import pygame
from pygame.locals import *
from random import randint

pygame.init()


class ScareHandler:
    def __init__(self):
        self.stepSound = pygame.mixer.Sound('src/sounds/steps.ogg')
        self.stepChannel = None
        self.stepVolume = (0, 0)

    def update(self):
        self.monsterTimer -= 0.5#-= dt
        
        if self.monsterTimer < 0 and not self.timerFreeze:
            #self.monster[choice(list(self.monster.keys()))] = True
            self.monster['onRight'] = True
            
            self.timerFreeze = True
            self.monsterTimer = randint(3, 7) * 60

        if self.timerFreeze:
            self.jumpTimer -= 0.5

        if self.jumpTimer < 0:
            ...
            #print('jumpscare')

        if self.timerFreeze:
            normalOffset = self.camera.normalOffset
            if self.stepChannel == None:
                if self.monster['onLeft']:
                    self.stepChannel = self.stepSound.play()
                    self.stepVolume = (1, 0)

                if self.monster['inFront']:
                    self.stepSound.play()
                    self.stepVolume = (1, 1)

                if self.monster['onRight']:
                    self.stepChannel = self.stepSound.play()
                    self.stepVolume = (0, 1)

            else:
                self.stepChannel.set_volume(self.stepVolume[0], self.stepVolume[1])
                
                if self.doorMenu.opened:
                    self.stepChannel.set_volume(0)