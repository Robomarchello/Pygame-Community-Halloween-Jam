import pygame
from pygame.locals import *
from random import choice
from .ui import ImgButton


class Radio:
    def __init__(self, cursor):
        self.volumeTime = 0
        self.maxTime = 500

        self.cursor = cursor

        self.font = pygame.font.Font('src/assets/radioFont.ttf', 64)

        self.music = [
            pygame.mixer.Sound('src/sounds/MusicBadDynomite.ogg')
        ]
        self.CurrentMusic = choice(self.music)
        self.MusicChannel = self.CurrentMusic.play()

        self.radioImg = pygame.image.load('src/assets/radio.png').convert()

        self.VolUpImg = pygame.image.load('src/assets/VolUp.png').convert_alpha()
        self.VolDownImg = pygame.image.load('src/assets/VolDown.png').convert_alpha()

        self.VolDownBtn  = ImgButton(self.cursor, (775, 230), self.VolDownImg,
        self.VolDownImg, self.addVol)
        
        self.VolUpBtn  = ImgButton(self.cursor, (675, 230), self.VolUpImg,
        self.VolUpImg, self.subVol)

        self.opened = True

    def addVol(self):
        self.volumeTime += self.maxTime * 0.1
        if self.volumeTime > self.maxTime:
            self.volumeTime = self.maxTime
        
    def subVol(self):
        self.volumeTime -= self.maxTime * 0.1

        if self.volumeTime < 0:
            self.volumeTime = 0

    def draw(self, screen):
        if self.opened:
            screen.blit(self.radioImg, (0, 0))

            VolPercent = round(self.volumeTime / self.maxTime, 2) * 100
            render = self.font.render(f'Volume: {VolPercent}', False, (255, 255, 255))

            screen.blit(render, (205, 260))

            self.VolUpBtn.draw(screen)
            self.VolDownBtn.draw(screen)
    
    def update(self, dt):
        if self.volumeTime < self.maxTime:
            self.volumeTime += dt
        else:
            self.volumeTime = self.maxTime

        self.MusicChannel.set_volume(self.volumeTime / self.maxTime)

        self.VolUpBtn.check()
        self.VolDownBtn.check()

    def handle_event(self, event):
        self.VolUpBtn.handle_event(event)
        self.VolDownBtn.handle_event(event)
