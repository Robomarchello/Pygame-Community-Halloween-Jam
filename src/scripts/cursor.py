import pygame
from pygame.locals import MOUSEMOTION, SYSTEM_CURSOR_HAND, SYSTEM_CURSOR_ARROW


class Cursor:
    def __init__(self):
        self.handCursor = False
        self.mp = pygame.Vector2(0, 0)


    def update(self):
        if self.handCursor:
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)

        self.handCursor = False

    def handle_event(self, event):
        if event.type == MOUSEMOTION:
            self.mp = pygame.Vector2(event.pos)