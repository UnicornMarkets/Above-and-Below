
import pygame
import data
import math
from constants import *

class Player(pygame.sprite.Sprite):
    """
    the main actor in the game
    """

    def __init__(self, x, y, dt, *groups):
        """
        setup player
        """
        super(Player, self).__init__(*groups)
        self.image = pygame.transform.scale(pygame.image.load(
                            data.filepath("coloredspheres", "sphere-00.png")),
                                         (2 * RADIUS, 2 * RADIUS))
        self.rect = pygame.rect.Rect((x, y), self.image.get_size())
        self.resting = False
        self.dy = 0
        self.dt = dt / 1000.
        self.bounce = pygame.mixer.Sound(data.filepath('sounds', 'bounce.mp3'))

    def update(self, game):
        """
        method that handles all player updates during gameplay
        """
        last = self.rect.copy()
        key = pygame.key.get_pressed()
        self.horizontal(key)
        self.vertical(key)
        self.collisions(last, game)

    def horizontal(self, key):
        """
        deals with horizontal movements of player
        """
        if key[pygame.K_LEFT]:
            self.rect.x -= 300 * self.dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300 * self.dt
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_W:
            self.rect.right = SCREEN_W

    def vertical(self, key):
        """
        deals with vertical movement of player
        """
        if self.resting and key[pygame.K_SPACE]:
            self.dy = -650
        self.dy = self.dy + 25
        self.rect.y += self.dy * self.dt
        self.resting = False

    def collisions(self, last, game):
        """
        handles any player collisions with walls and/or objects
        """
        for wall in pygame.sprite.spritecollide(self, game.walls, False):
            if last.bottom <= wall.rect.top:
                self.resting = True
                self.rect.bottom = wall.rect.top
                if abs(self.dy) > 150:
                    self.bounce.play()
                self.dy = - self.dy + 150
            if last.top >= wall.rect.bottom:
                self.rect.top = wall.rect.bottom
                if abs(self.dy) > 150:
                    self.bounce.play()
                self.dy = - self.dy
