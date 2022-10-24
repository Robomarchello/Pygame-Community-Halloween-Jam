from turtle import left
import pygame
from pygame.locals import *
from src.scripts.camera import Camera
from src.scripts.doortool import DoorToolKit
from src.scripts.utils import SpriteSheet
from src.scripts.ui import HoverButton
from src.scripts.radio import Radio
from random import choice, randint

pygame.mixer.init()


class Game():
    def __init__(self, screen, map, cursor):
        self.screen = screen

        self.cursor = cursor

        self.noiseSound = pygame.mixer.Sound('src/sounds/noisesnd.ogg')
        self.noiseSound.play(-1)

        self.monster = {'onLeft': False, 'inFront': False, 'onRight': False}
        self.monsterTimer = 1#randint(3, 7) * 60
        self.timerFreeze = False
        self.jumpTimer = 0#4 * 60

        doorImg = pygame.image.load('src/assets/doorSheet.png').convert_alpha()
        self.doorSheet = SpriteSheet(doorImg, (521, 540))

        self.stepSound = pygame.mixer.Sound('src/sounds/steps.ogg')
        self.stepChannel = None
        self.stepVolume = (0, 0)

        self.ClosedDoor = {'left': False, 'center': False, 'right': False}

        self.camera = Camera(screen, map, self.doorSheet)

        btnImg = pygame.image.load('src/assets/button.png').convert_alpha()
        self.doorMenu = DoorToolKit(btnImg, btnImg, screen,
        self.cursor, self.ClosedDoor)

        self.Radio = Radio(self.cursor)

        HoverBtnImg = pygame.image.load('src/assets/bottomBtn.png').convert_alpha()
        self.HoverBtn = HoverButton(self.cursor, (148, 470), HoverBtnImg, 
        HoverBtnImg, self.DoorMenuOpen, (583, 80))
        
        RadioBtnImg = pygame.image.load('src/assets/radioButton.png').convert_alpha()
        self.RadioBtn = HoverButton(self.cursor, (755, 470), RadioBtnImg, 
        RadioBtnImg, self.RadioOpen, (82, 80))

    def DoorMenuOpen(self):
        if self.doorMenu.opened:
            self.Radio.opened = False
            self.doorMenu.opened = False
        else:
            self.Radio.opened = False
            self.doorMenu.opened = True

    def RadioOpen(self):
        if self.Radio.opened:
            self.Radio.opened = False
            self.doorMenu.opened = False
        else:
            self.Radio.opened = True
            self.doorMenu.opened = False
    
    def draw(self, screen, mp):
        self.camera.draw(screen, mp, self.ClosedDoor)

        self.doorMenu.draw(screen)
        self.Radio.draw(screen)
        self.HoverBtn.draw(screen)
        self.RadioBtn.draw(screen)

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

        self.Radio.update(0)

        self.HoverBtn.check()
        self.RadioBtn.check()
    
    def handle_event(self, event):
        self.doorMenu.handle_event(event)
        self.Radio.handle_event(event)