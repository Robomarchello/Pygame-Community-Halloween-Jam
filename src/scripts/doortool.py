import pygame
from pygame.locals import *
from .ui import ImgButton, HoverButton


class DoorToolKit:
    def __init__(self, screen, buttonImg1, buttonImg2, cursor, ClosedDoor):
        self.screen = screen
        self.surface = pygame.Surface((960, 540))

        self.background = pygame.image.load('src/assets/DoorCloserBg.png').convert()

        self.ClosedDoor = ClosedDoor

        self.buttonImg1 = buttonImg1
        self.buttonImg2 = buttonImg2

        self.cursor = cursor

        self.leftBtn = ImgButton(self.cursor, (75, 250), self.buttonImg1,
        self.buttonImg2, self.left) 
        self.centerBtn = ImgButton(self.cursor, (375, 250), self.buttonImg1,
        self.buttonImg2, self.center) 
        self.rightBtn = ImgButton(self.cursor, (675, 250), self.buttonImg1,
        self.buttonImg2, self.right) 

        self.screen = screen

        self.opened = False
    
    #
    def left(self):
        if self.ClosedDoor['left']:
            self.ClosedDoor['left'] = False
        else:
            self.ClosedDoor['left'] = True

        self.ClosedDoor['center'] = False
        self.ClosedDoor['right'] = False

    def center(self):
        if self.ClosedDoor['center']:
            self.ClosedDoor['center'] = False
        else:
            self.ClosedDoor['center'] = True

        self.ClosedDoor['left'] = False
        self.ClosedDoor['right'] = False

    def right(self):
        if self.ClosedDoor['right']:
            self.ClosedDoor['right'] = False
        else:
            self.ClosedDoor['right'] = True

        self.ClosedDoor['left'] = False
        self.ClosedDoor['center'] = False

    def draw(self, screen):
        if self.opened:
            self.surface.blit(self.background, (0, 0))
            
            self.leftBtn.check()
            self.centerBtn.check()
            self.rightBtn.check()

            self.leftBtn.draw(self.surface)
            self.centerBtn.draw(self.surface)
            self.rightBtn.draw(self.surface)

            screen.blit(self.surface, (0, 0))

    def handle_event(self, event):
        self.leftBtn.handle_event(event)
        self.centerBtn.handle_event(event)
        self.rightBtn.handle_event(event)