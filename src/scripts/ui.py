import pygame
from pygame.locals import *

pygame.init()


class ImgButton:
    def __init__(self, cursor, position, image1, image2, func):
        self.cursor = cursor
        self.position = position

        self.mp = self.cursor.mp

        self.image1 = image1
        self.image2 = image2

        self.rect = self.image1.get_rect(topleft=self.position)

        self.hovered = False
        self.pressed = False
        self.runFunc = False

        self.func = func
        
    def draw(self, screen):
        screen.blit(self.image1, self.position)
    
    def check(self):
        self.hovered = False
        self.mp = self.cursor.mp

        if self.rect.collidepoint(self.mp):
            self.hovered = True
            self.cursor.handCursor = True

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.hovered:
                    self.pressed = True
                    
                    self.func()

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self.pressed = False


#button that presses only just by hovering on it
class HoverButton:
    def __init__(self, cursor, position, image1, image2, func, rectSize=None):
        self.cursor = cursor
        self.position = position

        self.mp = self.cursor.mp

        self.image1 = image1
        self.image2 = image2

        self.rect = self.image1.get_rect(topleft=self.position)
        if rectSize != None:
            self.rect.width = rectSize[0]
            self.rect.height = rectSize[1]

        self.hovered = False
        self.pressed = False
        self.runned = False
        self.runFunc = False

        self.func = func
        
    def draw(self, screen):
        if not self.runned:
            screen.blit(self.image1, self.position)
    
    def check(self):
        self.hovered = False
        self.mp = self.cursor.mp

        if self.rect.collidepoint(self.mp):
            self.hovered = True

        if self.hovered and not self.runned:
            self.func()

            self.runFunc = True
            self.runned = True
            

        if not self.hovered:
            self.runFunc = False
            self.runned = False

