#I know this is an awesome name for python script
from tkinter.messagebox import NO
import pygame
from pygame.locals import *
from random import choice
from .utils import SpriteSheet


class Scarer:
    def __init__(self):
        self.sheets = [
            SpriteSheet(
                pygame.image.load('src/assets/JumpScare1.png').convert_alpha(),
                (960, 540))
        ]
        self.sound = [
            pygame.mixer.Sound('src/sounds/scream.ogg')
        ]

        self.start = False
        self.ChoosenSheet = choice(self.sheets)
        self.frame = 0
        self.animFrames = len(self.ChoosenSheet) - 3
        self.speed = 1.25#0.15

        self.font = pygame.font.Font('src/assets/pixel.ttf', 30)

        self.ItWasOn = None
        self.heAteYou = self.font.render('Pygame Snake Ate You', False, (0, 0, 0))
        self.AllOver = self.font.render("The remains of your body are scattered",
        False, (0, 0 ,0))
        self.OverFloor = self.font.render("all over the floor",
        False, (0, 0 ,0))
        self.rRestart = self.font.render("Press R to restart",
        False, (0, 0 ,0))

        self.heAteRect = self.heAteYou.get_rect(center=(480, 50))
        self.AllOverRect = self.AllOver.get_rect(center=(480, 100))
        self.OverFloorRect = self.OverFloor.get_rect(center=(480, 150))
        self.rRestartRect = self.rRestart.get_rect(center=(480, 500))
    
    def restart(self):
        self.start = False
        self.frame = 0
        
    def draw(self, screen, GameOver, monster, radio, dt):
        if GameOver:
            if not self.start:
                self.sound[0].play()
                if monster['onLeft']:
                    self.ItWasOn = self.font.render('It Came From The Left Door.',
                    False, (0, 0, 0))

                if monster['onCenter']:
                    self.ItWasOn = self.font.render('It Came From The Center Door.',
                    False, (0, 0, 0))

                if monster['onRight']:
                    self.ItWasOn = self.font.render('It Came From The Right Door.',
                    False, (0, 0, 0))

                self.ItWasOnRect = self.ItWasOn.get_rect(center=(480, 270))

            self.start = True

            if self.frame < self.animFrames:
                self.frame += dt * self.speed
                screen.blit(self.ChoosenSheet[int(self.frame)], (0, 0))
            else:
                screen.blit(self.ChoosenSheet[15], (0, 0))

                screen.blit(self.heAteYou, self.heAteRect.topleft)
                screen.blit(self.AllOver, self.AllOverRect.topleft)
                screen.blit(self.OverFloor, self.OverFloorRect.topleft)
                screen.blit(self.ItWasOn, self.ItWasOnRect.topleft)
                screen.blit(self.rRestart, self.rRestartRect.topleft)

        else:
            if self.start:
                #restart the thing
                self.start = False
