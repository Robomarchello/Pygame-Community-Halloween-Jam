import pygame
from pygame.locals import *


class Camera:
    def __init__(self, screen, surface, doorSheet):
        self.screen = screen
        self.ScreenSize = screen.get_size()
        
        self.surface = surface
        self.centerX = (self.surface.get_width() - self.ScreenSize[0]) // 2

        self.xOffset = 0
        self.maxOffset = 300

        self.CamLeftRect = pygame.Rect(0, 0, 300, self.ScreenSize[1])
        self.CamRightRect = pygame.Rect(660, 0, 300, self.ScreenSize[1])

        self.moveDir = {'left': False, 'right': False}

        self.doorSheet = doorSheet

        #means left - 0.0, center - 0.5, right = 1
        self.normalOffset = self.xOffset / self.maxOffset + 0.5

    def draw(self, screen, mp, ClosedDoor, dt):
        self.update(mp, dt)
        screen.blit(self.surface, (-(self.centerX + self.xOffset), 0))

        if ClosedDoor['left']:
            screen.blit(self.doorSheet[0], (-self.xOffset - 300, 0))
        if ClosedDoor['center']:
            screen.blit(self.doorSheet[1], (220 - self.xOffset, 0))
        if ClosedDoor['right']:
            screen.blit(self.doorSheet[2], (740 - self.xOffset, 0))

    def update(self, mp, dt):
        if mp.x < 300 and self.xOffset > -self.maxOffset:
            self.xOffset -= ((300 - mp.x) / 300) * dt * 5
        
        if mp.x > 660 and self.xOffset < self.maxOffset:
            self.xOffset -= ((660 - mp.x) / 300) * dt * 5

        #for sound
        #self.normalOffset = round(self.xOffset / (self.maxOffset * 2), 2)
        #print(self.normalOffset)

    