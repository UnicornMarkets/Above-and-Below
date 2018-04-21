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

class Star(pygame.sprite.Sprite):
    """
    these add points for the player
    """
    def __init__(self, x, y, ab, *groups):
        super(Star, self).__init__(*groups)
        self.image_dict = {1: pygame.transform.scale(pygame.image.load(
                                data.filepath("star", "star_" + ab + "1.png")),
                                        (BLOCK_S, BLOCK_S)),
                            2: pygame.transform.scale(pygame.image.load(
                                data.filepath("star", "star_" + ab + "2.png")),
                                        (BLOCK_S, BLOCK_S)),
                            3: pygame.transform.scale(pygame.image.load(
                                data.filepath("star", "star_" + ab + "3.png")),
                                        (BLOCK_S, BLOCK_S)),}

        self.mask_dict = {1: pygame.mask.from_surface(self.image_dict[1]),
                          2: pygame.mask.from_surface(self.image_dict[2]),
                          3: pygame.mask.from_surface(self.image_dict[3])}

        self.last_time = pygame.time.get_ticks()
        self.image_num = 1
        self.image = self.image_dict[self.image_num]
        self.mask = self.mask_dict[self.image_num]
        self.rect = pygame.rect.Rect((x, y), self.image.get_size())

        def update(self, game):
            self.image = self.image_dict[self.image_num]
            self.mask = self.mask_dict[self.image_num]
            if pygame.time.get_ticks() > self.last_time + 200:
                if self.image_num >= 3:
                    self.image_num = 1
                else:
                    self.image_num += 1

                self.last_time = pygame.time.get_ticks()
