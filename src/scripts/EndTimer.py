import pygame
from pygame.locals import *


class Timer:
    def __init__(self):
        self.font = pygame.font.Font('src/assets/pixel.ttf', 24)

        self.timerUpdate = 0
        self.UpdateTime = 30 * 60

        self.time = 0
        self.timeStr = '12 AM'

        self.won = False
    
    def draw(self, screen, dt):
        self.timerUpdate += dt
        
        if self.timerUpdate > self.UpdateTime:
            self.timerUpdate = 0
            self.time += 1

        if self.time > 0:
            self.timeStr = f'{self.time} AM'
            
        if self.time >= 6:
            self.won = True

        self.timeRender = self.font.render(self.timeStr, False, (200, 200, 200))
        screen.blit(self.timeRender, (15, 15))

    def restart(self):
        self.time = 0 
        self.timeStr = '12 AM'