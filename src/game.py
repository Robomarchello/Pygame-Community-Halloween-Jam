#https://fontstruct.com/fontstructions/download/1059881
import pygame
from pygame.locals import *
from src.scripts import *
from random import choice, randint

pygame.mixer.init()


class Game():
    def __init__(self, screen, map, cursor, clock):
        self.screen = screen

        self.cursor = cursor

        self.clock = clock

        self.GameOver = False
        self.restarted = False

        self.dt = get_dt(60)

        self.timer = Timer()

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
        self.monsterTimer = randint(3, 7) * 60
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

        self.Scarer = Scarer()

        self.restartMonster()
        self.restarted = True

        self.winScreen = pygame.image.load('src/assets/winningScreen.png').convert()

        self.tutorial = pygame.mixer.Sound('src/sounds/tutorial.ogg')
        self.tutorial.set_volume(0.5)
        #self.tutorial.play()
        self.TutorialTimer = 60 * 60
        self.Educated = True

        self.RandomSnek = RandomSnek(self.doorMenu, self.Radio, self.Scarer)

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
        self.dt = get_dt(self.clock.get_fps()) 
        self.camera.draw(screen, mp, self.ClosedDoor, self.dt)

        GameOver = self.RandomSnek.draw(self.screen, self.Educated, self.dt)
        if GameOver:
            self.GameOver = True

        self.doorMenu.draw(screen)
        self.Radio.draw(screen)
        self.HoverBtn.draw(screen)
        self.RadioBtn.draw(screen)
        
        #print(self.dt)
        if self.Educated:
            self.timer.draw(screen, self.dt)

        
        self.Scarer.draw(screen, self.GameOver, self.monster, self.Radio, self.dt)

        if self.timer.won:
            screen.blit(self.winScreen, (0, 0))

    def restart(self):
        self.Radio.volume = 0.0
        self.camera.xOffset = 0

        self.doorMenu.opened = False
        self.Radio.opened = False

        #self.ClosedDoor = {'left': False, 'center': False, 'right': False}
        self.ClosedDoor['left'] = False
        self.ClosedDoor['center'] = False
        self.ClosedDoor['right'] = False
        
        self.RandomSnek.restart()
        self.Scarer.restart()
        self.restartMonster()
        self.timer.restart()

        self.GameOver = False

    def restartMonster(self):
        self.monster = {'onLeft': False, 'onCenter': False, 'onRight': False}
        self.restarted = True

        self.jumpTimer = 7.5 * 60
        self.monsterTimer = randint(3, 7) * 60
        self.monster[choice(list(self.monster.keys()))] = True

        self.stepChannel = None

    def update(self):
        self.dt = get_dt(self.clock.get_fps())
        self.musicHandler.inMenu = self.doorMenu.opened
        
        if self.TutorialTimer > 0:
            self.TutorialTimer -= self.dt
        else:
            self.Educated = True

        
        if self.Educated:
            if self.monsterTimer > 0:
                self.monsterTimer -= self.dt
            else:
                if self.stepChannel == None:
                    self.stepChannel = self.stepSound.play()

                restart = False
                self.jumpTimer -= self.dt
                if self.jumpTimer <= 0:
                    if self.monster['onLeft']:
                        if self.ClosedDoor['left']:
                            restart = True
                        else:
                            self.GameOver = True
                
                    if self.monster['onCenter']:
                        if self.ClosedDoor['center']:
                            restart = True
                        else:
                            self.GameOver = True
                
                    if self.monster['onRight']:
                        if self.ClosedDoor['right']:
                            self.restartMonster()
                            restart = True
                        else:
                            self.GameOver = True     

                    if restart:
                        self.restartMonster()

        else:
            self.doorMenu.musicHandler.set_volume(0)
        
        vol = 1 - self.Radio.volume
        if self.monster['onLeft']:
            self.stepVolume = (vol, 0)

        elif self.monster['onCenter']:
            self.stepVolume = (vol, vol)

        elif self.monster['onRight']:
            self.stepVolume = (0, vol)

        if self.stepChannel != None:
            self.stepChannel.set_volume(self.stepVolume[0], self.stepVolume[1])
        
        if self.doorMenu.opened:
            self.stepChannel.set_volume(0)

        if not self.Educated:
            self.Radio.volumeTime = 0

        self.Radio.update(self.dt)

        self.HoverBtn.check()
        self.RadioBtn.check()
        self.musicHandler.check()
    
    def handle_event(self, event):
        self.doorMenu.handle_event(event)
        self.Radio.handle_event(event)

        if event.type == KEYDOWN:
            if event.key == K_r:
                if self.GameOver:
                    self.restart()