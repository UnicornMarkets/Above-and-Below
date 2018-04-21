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
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, game):
        pass

class Point(pygame.sprite.Sprite):
    """
    these add points for the player
    """
    def __init__(self, x, y, ab, level, *groups):
        super(Point, self).__init__(*groups)
        self.image = pygame.image.load(data.filepath("points",
                                    ab + str(level) + ".png"))

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.rect.Rect((x, y), self.image.get_size())

        def update(self, game):
            pass
