import pygame
from pygame.locals import *
from src.scripts.musicHandler import MusicHandler
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

        self.GameOver = False

        self.musicHandler = MusicHandler()

        self.noiseSound = pygame.mixer.Sound('src/sounds/noisesnd.ogg')
        self.noiseSound.play(-1)

        doorImg = pygame.image.load('src/assets/doorSheet.png').convert_alpha()
        self.doorSheet = SpriteSheet(doorImg, (521, 540))
        
        btnImg = pygame.image.load('src/assets/button.png').convert_alpha()
        HoverBtnImg = pygame.image.load('src/assets/bottomBtn.png').convert_alpha()
        RadioBtnImg = pygame.image.load('src/assets/radioButton.png').convert_alpha()

        self.jumpScareDummy = pygame.image.load('src/assets/scare.png').convert()

        self.monster = {'onLeft': False, 'onCenter': False, 'onRight': False}
        self.monsterTimer = 1#randint(3, 7) * 60
        self.timerFreeze = False
        self.jumpTimer = 7.5 * 60

        self.stepSound = pygame.mixer.Sound('src/sounds/steps.ogg')
        self.stepChannel = None
        self.stepVolume = (0, 0)

        self.ClosedDoor = {'left': False, 'center': False, 'right': False}

        self.camera = Camera(screen, map, self.doorSheet)
        self.Radio = Radio(self.cursor, self.musicHandler)
        
        self.doorMenu = DoorToolKit(btnImg, btnImg, screen,
        self.cursor, self.ClosedDoor, self.musicHandler)
        
        self.HoverBtn = HoverButton(self.cursor, (148, 470), HoverBtnImg, 
        HoverBtnImg, self.DoorMenuOpen, (583, 80))
        
        self.RadioBtn = HoverButton(self.cursor, (755, 470), RadioBtnImg, 
        RadioBtnImg, self.RadioOpen, (95, 80))

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

    def restartMonster(self):
        self.monster = {'onLeft': False, 'onCenter': False, 'onRight': False}
        self.monster[choice(list(self.monster.keys()))] = True

        self.monsterTimer = randint(3, 7) * 60
        self.timerFreeze = False
        self.jumpTimer = 7.5 * 60

        print('success')

    def update(self):
        self.musicHandler.inMenu = self.doorMenu.opened
        self.monsterTimer -= 0.5#-= dt
        
        if self.monsterTimer < 0 and not self.timerFreeze:
            self.monster[choice(list(self.monster.keys()))] = True
            print(self.monster)
            #self.monster['onRight'] = True
            
            self.timerFreeze = True
            self.monsterTimer = randint(3, 7) * 60

        if self.timerFreeze:
            self.jumpTimer -= 0.5

        if self.jumpTimer < 0:
            if self.monster['onLeft']:
                print('left')
                if not self.ClosedDoor['left']:
                    self.GameOver = True
                    self.screen.blit(self.jumpScareDummy, (0, 0))

            if self.monster['onCenter']:
                print('center')
                if not self.ClosedDoor['center']:
                    self.GameOver = True
                    self.screen.blit(self.jumpScareDummy, (0, 0))
                    
            if self.monster['onRight']:
                if not self.ClosedDoor['right']:
                    self.screen.blit(self.jumpScareDummy, (0, 0))
                    self.GameOver = True

        if self.timerFreeze:
            if self.stepChannel == None:
                if self.monster['onLeft']:
                    self.stepChannel = self.stepSound.play()
                    self.stepVolume = (1, 0)

                if self.monster['onCenter']:
                    self.stepChannel = self.stepSound.play()
                    self.stepVolume = (1, 1)

                if self.monster['onRight']:
                    self.stepChannel = self.stepSound.play()
                    self.stepVolume = (0, 1)

            else:
                self.stepChannel.set_volume(self.stepVolume[0], self.stepVolume[1])
                
                
                if self.doorMenu.opened:
                    self.stepChannel.set_volume(0)
                
                if self.Radio.volume > 0.9:
                    self.stepChannel.set_volume(0)
                
                    #self.stepChannel.set_volume(1 - self.Radio.volume)

        self.Radio.update(0.20)

        self.HoverBtn.check()
        self.RadioBtn.check()
        self.musicHandler.check()
    
    def handle_event(self, event):
        self.doorMenu.handle_event(event)
        self.Radio.handle_event(event)