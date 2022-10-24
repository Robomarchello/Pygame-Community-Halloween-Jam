from turtle import left
import pygame
from pygame.locals import *
from src.scripts.camera import Camera
from src.scripts.doortool import DoorToolKit
from src.scripts.utils import SpriteSheet
from src.scripts.ui import HoverButton
from random import choice, randint

pygame.mixer.init()


class Game():
    def __init__(self, screen, map, cursor):
        self.screen = screen

        self.noiseSound = pygame.mixer.Sound('src/assets/noisesnd.ogg')
        self.noiseSound.play(-1)

        self.monster = {'onLeft': False, 'inFront': False, 'onRight': False}
        self.monsterTimer = 1#randint(3, 7) * 60
        self.timerFreeze = False
        self.jumpTimer = 0#4 * 60

        doorImg = pygame.image.load('src/assets/doorSheet.png')
        self.doorSheet = SpriteSheet(doorImg, (521, 540))

        self.ClosedDoor = {'left': False, 'center': False, 'right': False}

        self.camera = Camera(screen, map, self.doorSheet)

        self.cursor = cursor

        self.stepSound = pygame.mixer.Sound('src/assets/steps.ogg')
        self.stepChannel = None

        btnImg = pygame.image.load('src/assets/button.png')
        self.doorMenu = DoorToolKit(btnImg, btnImg, screen,
        self.cursor, self.ClosedDoor)

        HoverBtnImg = pygame.image.load('src/assets/bottomBtn.png')
        self.HoverBtn = HoverButton(self.cursor, (188, 470), HoverBtnImg, 
        HoverBtnImg, self.DoorMenuOpen, (583, 80))

    def DoorMenuOpen(self):
        if self.doorMenu.opened:
            self.doorMenu.opened = False
        else:
            self.doorMenu.opened = True

    def draw(self, screen, mp):
        self.camera.draw(screen, mp, self.ClosedDoor)

        self.doorMenu.draw(screen)

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
                    self.stepChannel = self.stepSound.play(-1)
                    self.stepChannel.set_volume(1, 0)

                if self.monster['inFront']:
                    self.stepSound.play()
                    self.stepChannel = 1

                if self.monster['onRight']:
                    self.stepChannel = self.stepSound.play(-1)
                    self.stepChannel.set_volume(0, 1)

   
        self.HoverBtn.check()
        self.HoverBtn.draw(self.screen)
    
    def handle_event(self, event):
        self.doorMenu.handle_event(event)