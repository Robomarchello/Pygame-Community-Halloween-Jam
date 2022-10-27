import pygame
from pygame.locals import *
from src.scripts.game import Game
from src.scripts.cursor import Cursor

pygame.init()


class App():
    def __init__(self, ScreenSize, caption, fps):
        self.ScreenSize = ScreenSize
        
        self.screen = pygame.display.set_mode(ScreenSize, SCALED)
        pygame.display.set_caption(caption)

        self.clock = pygame.time.Clock()
        self.fps = fps

        self.cursor = Cursor()

        wide = pygame.image.load('src/assets/wide1.png').convert()
        self.game = Game(self.screen, wide, self.cursor, self.clock)

        self.event_handlers = [self.cursor, self.game]

    def loop(self):
        screen = self.screen
        while True:
            self.clock.tick(self.fps)
            screen.fill((255, 255, 255))
            
            self.cursor.update()
            
            mp = self.cursor.mp

            self.game.draw(screen, mp)
            self.game.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    raise SystemExit
                
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        raise SystemExit

                    if event.key == K_F11:
                        pygame.display.toggle_fullscreen()

                for event_handler in self.event_handlers:
                    event_handler.handle_event(event)
            
            
            pygame.display.update()