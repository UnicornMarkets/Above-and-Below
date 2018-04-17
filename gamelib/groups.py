import pygame
from constants import *
import data

class ScrolledGroup(pygame.sprite.Group):
    """
    all groups that are scolled through.

    This should be the ground and ceiling at each different height,
    platforms to jump on/off in the game,
    objects that give powerups/destroy you.
    """
    def draw(self, surface, distance):
        for sprite in self.sprites():
            surface.blit(sprite.image, (sprite.rect.x - distance,
                sprite.rect.y))

class Platforms(ScrolledGroup):
    """
    These are for jumping,
    you have to jump your way to the top or the bottom, but not fall through
    """
    last_add = None

    def update(self, distance):
        for block in self.sprites():
            if block.rect.right < 0:
                block.kill()
        if self.last_add is None:
            self.last_add = self.sprites()[-1].rect.right
        if distance > self.last_add - 300:
            self.last_add = x = distance + SCREEN_W
            self.add(Wall(SCREEN_W, SCREEN_H / 2))

class Wall(pygame.sprite.Sprite):
    """
    boundries for the game
    """

    def __init__(self, x, y, *groups):
        super(Wall, self).__init__(*groups)
        self.image = pygame.transform.scale(pygame.image.load(
                                    data.filepath("world", "block.png")),
                                    (WALL_S, WALL_S))
        self.rect = pygame.rect.Rect((x, y), self.image.get_size())

    def update(self, game):
        pass
