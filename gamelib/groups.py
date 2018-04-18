import pygame
from constants import *
import data

class Wall(pygame.sprite.Sprite):
    """
    Walls and platforms for the game
    """

    def __init__(self, x, y, *groups):
        super(Wall, self).__init__(*groups)
        self.image = pygame.transform.scale(pygame.image.load(
                                    data.filepath("world", "block.png")),
                                    (BLOCK_S, BLOCK_S))
        self.rect = pygame.rect.Rect((x, y), self.image.get_size())

    def update(self, game):
        pass

class Ground(pygame.sprite.Sprite):

    def __init__(self, x, y, length, *groups):
        super(Ground, self).__init__(*groups)
        self.image = pygame.transform.scale(pygame.image.load(
                                    data.filepath("world", "ground.png")),
                                    (BLOCK_S  * length, BLOCK_S))
        if y == 0:
            self.image = pygame.transform.flip(self.image, False, True)

        self.rect = pygame.rect.Rect((x, y), self.image.get_size())

    def update(self, game):
        pass

class Platforms(pygame.sprite.Sprite):
    pass

class Points(pygame.sprite.Sprite):
    """
    to make the game more interesting these objects give points
    """
    pass
