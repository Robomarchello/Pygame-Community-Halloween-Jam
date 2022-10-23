import pygame
from pygame.locals import *


def SpriteSheet(surface, CellSize):
    SurfSize = surface.get_size()

    xCells = SurfSize[0] // CellSize[0]
    yCells = SurfSize[1] // CellSize[1]

    Sheet = []

    CellSurf = pygame.Surface(CellSize, SRCALPHA)
    for yCell in range(yCells):
        for xCell in range(xCells):
            SurfOffset = (-xCell * CellSize[0], -yCell // CellSize[1])
            CellSurf.blit(surface, SurfOffset)

            Sheet.append(CellSurf.copy())

            CellSurf.fill((0, 0, 0, 0))
    
    return Sheet


def CutSurface(surface, position, size):
    '''Cuts the surface by a given position and size'''
    CuttedSurf = pygame.Surface(size, SRCALPHA)
    CuttedSurf.blit(surface, (-position[0], -position[1]))

    return CuttedSurf