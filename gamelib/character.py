
import pygame
import data
import math
from threading import Timer
from constants import *

def clamp(value, min_value, max_value):
    """Clamp value to a range between min_value and max_value."""
    return max(min_value, min(value, max_value))

class Player(pygame.sprite.Sprite):
    """
    the main actor in the game
    """

    def __init__(self, x, y, dt, *groups):
        """
        setup player
        """
        super(Player, self).__init__(*groups)
        self.points = 0
        self.image = pygame.transform.scale(pygame.image.load(
                                 data.filepath("coloredspheres", "sphere-" +
                                                    str(self.points) + ".png")),
                                         (2 * RADIUS, 2 * RADIUS))
        self.rect = pygame.rect.Rect((x, y), self.image.get_size())
        self.resting = False
        self.dy = 0
        self.dt = dt / 1000.
        self.bounce = pygame.mixer.Sound(data.filepath('sounds', 'bounce.mp3'))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, game):
        """
        method that handles all player updates during gameplay
        """
        last = self.rect.copy()
        key = pygame.key.get_pressed()
        self.horizontal(key)
        self.vertical(key, game)
        self.collisions(last, game)
        self.groups()[0].camera_y = self.rect.y - (SCREEN_H - 0.5 * RADIUS)

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

    def vertical(self, key, game):
        """
        deals with vertical movement of player
        """
        if game.world == 0:
            if self.resting and key[pygame.K_SPACE]:
                self.dy = -850
                self.resting = False
            self.dy = self.dy + 25
            self.rect.y += self.dy * self.dt
        if game.world == 1:
            if self.resting and key[pygame.K_SPACE]:
                self.dy = 850
                self.resting = False

            self.dy = self.dy - 25
            self.rect.y += self.dy * self.dt

    def _rgravity_bounce(self, wall):
        if abs(self.dy) > 150:
            self.bounce.play()
            self.dy = - self.dy - 150
        else:
            self.resting = True
            self.dy = 0

    def _gravity_bounce(self, wall):
        if abs(self.dy) > 150:
            self.bounce.play()
            self.dy = - self.dy + 150
        else:
            self.resting = True
            self.dy = 0

    def _normal_bounce(self, wall):
        if abs(self.dy) > 150:
            self.bounce.play()
            self.dy = - self.dy
        else:
            self.resting = True
            self.dy = 0

    def collisions(self, last, game):
        """
        handles any player collisions with walls and/or objects
        """
        walls = game.levels[game.level]
        for wall in pygame.sprite.spritecollide(self, walls, False):

            if last.right <= wall.rect.left:
                self.rect.right = wall.rect.left
            if last.left >= wall.rect.right:
                self.rect.left = wall.rect.right
            if game.world == 0:
                if last.bottom <= wall.rect.top:
                    self.rect.bottom = wall.rect.top
                    if self.dy > 0:
                        self._gravity_bounce(wall)
                if last.top >= wall.rect.bottom:
                    self.rect.top = wall.rect.bottom
                    if self.dy < 0:
                        self._normal_bounce(wall)
            if game.world == 1:
                if last.bottom <= wall.rect.top:
                    self.rect.bottom = wall.rect.top
                    if self.dy > 0:
                        self._normal_bounce(wall)
                if last.top >= wall.rect.bottom:
                    self.rect.top = wall.rect.bottom
                    if self.dy < 0:
                        self._rgravity_bounce(wall)
