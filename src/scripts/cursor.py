import pygame
from pygame.locals import MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP


class Cursor:
    def __init__(self):
        self.mp = pygame.Vector2(0, 0)


    def update(self):
        ...

    def handle_event(self, event):
        if event.type == MOUSEMOTION:
            self.mp = pygame.Vector2(event.pos)