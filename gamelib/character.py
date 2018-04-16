
import pygame
import data
from constants import *

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.transform.scale(pygame.image.load(
                            data.filepath("coloredspheres", "sphere-00.png")),
                                         (2 * RADIUS, 2 * RADIUS))
        self.rect = pygame.rect.Rect((x, y), self.image.get_size())
        self.resting = False
        self.dy = 0

    def update(self, game):
        dt = game.dt / 1000.
        last = self.rect.copy()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300 * dt
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_W:
            self.rect.right = SCREEN_W

        if self.resting and key[pygame.K_SPACE]:
            self.dy = -800
        self.dy = self.dy + 25

        self.rect.y += self.dy * dt

        new = self.rect
        self.resting = False
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell = cell.rect
            if last.bottom <= cell.top and new.bottom > cell.top:
                self.resting = True
                new.bottom = cell.top
                self.dy = 0
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.dy = 0


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, *groups):
        super(Wall, self).__init__(*groups)
        self.image = pygame.transform.scale(pygame.image.load(
                                    data.filepath("world", "block.png")),
                                    (WALL_S, WALL_S))
        self.rect = pygame.rect.Rect((x, y), self.image.get_size())

    def update(self, game):
        pass
