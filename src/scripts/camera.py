import pygame
from pygame.locals import *


class Camera:
    def __init__(self, screen, surface, doorSheet):
        self.screen = screen
        self.ScreenSize = screen.get_size()
        
        self.surface = surface
        self.centerX = (self.surface.get_width() - self.ScreenSize[0]) // 2

        self.xOffset = 302
        self.maxOffset = 300

        self.CamLeftRect = pygame.Rect(0, 0, 300, self.ScreenSize[1])
        self.CamRightRect = pygame.Rect(660, 0, 300, self.ScreenSize[1])

        self.moveDir = {'left': False, 'right': False}

        self.doorSheet = doorSheet

    def draw(self, screen, mp, ClosedDoor):
        self.update(mp)
        screen.blit(self.surface, (-(self.centerX + self.xOffset), 0))

        if ClosedDoor['left']:
            screen.blit(self.doorSheet[0], (-self.xOffset - 300, 0))
        if ClosedDoor['center']:
            screen.blit(self.doorSheet[1], (220 - self.xOffset, 0))
        if ClosedDoor['right']:
            screen.blit(self.doorSheet[2], (740 - self.xOffset, 0))

    def update(self, mp):
        if mp.x < 300 and self.xOffset > -self.maxOffset:
            self.xOffset -= ((300 - mp.x) / 300) * 3#* dt
        
        if mp.x > 660 and self.xOffset < self.maxOffset:
            self.xOffset -= ((660 - mp.x) / 300) * 3 #* dt
        
    