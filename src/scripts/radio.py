import pygame
from pygame.locals import *
from random import choice
from .ui import ImgButton


class Radio:
    def __init__(self, cursor, musicHandler):
        self.volumeTime = 0
        self.maxTime = 500

        self.volume = self.volumeTime / self.maxTime

        self.cursor = cursor

        self.musicHandler = musicHandler

        self.font = pygame.font.Font('src/assets/radioFont.ttf', 64)

        self.radioImg = pygame.image.load('src/assets/radio.png').convert()

        self.VolUpImg = pygame.image.load('src/assets/VolUp.png').convert_alpha()
        self.VolDownImg = pygame.image.load('src/assets/VolDown.png').convert_alpha()

        self.VolDownBtn  = ImgButton(self.cursor, (775, 230), self.VolDownImg,
        self.VolDownImg, self.addVol)
        
        self.VolUpBtn  = ImgButton(self.cursor, (675, 230), self.VolUpImg,
        self.VolUpImg, self.subVol)

        self.opened = False

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

            VolPercent = int(self.volume * 100)
            render = self.font.render(f'Volume: {VolPercent}', False, (255, 255, 255))

            screen.blit(render, (205, 260))

            self.VolUpBtn.draw(screen)
            self.VolDownBtn.draw(screen)
    
    def update(self, dt):
        self.volume = self.volumeTime / self.maxTime

        if self.volumeTime < self.maxTime:
            self.volumeTime += dt * 0.4
        else:
            self.volumeTime = self.maxTime

        self.musicHandler.set_volume(self.volume)

        if self.opened:
            self.VolUpBtn.check()
            self.VolDownBtn.check()

    def handle_event(self, event):
        self.VolUpBtn.handle_event(event)
        self.VolDownBtn.handle_event(event)
