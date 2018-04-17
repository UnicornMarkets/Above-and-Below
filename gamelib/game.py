import pygame
import character
import groups
import random
from constants import *

class Game:

    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(30)
        self.sprites = pygame.sprite.Group()
        self.player = character.Player(100, 100, self.dt, self.sprites)
        self.distance = 100

    def run(self):
        self.walls = pygame.sprite.Group()
        self.platforms = groups.Platforms()
        for x in range(0, SCREEN_W, WALL_S):
            for y in [-2 * SCREEN_H, -SCREEN_H-WALL_S, -SCREEN_H, -WALL_S,
                        0, SCREEN_H-WALL_S, SCREEN_H, -2 * SCREEN_H-WALL_S]:
                if x not in [WALL_S * n for n in range(8, 12, 1)] \
                        or y not in [0, -WALL_S]:
                    groups.Wall(x, y, self.walls)
        self.sprites.add(self.walls)
        self.loop()

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if (event.type == pygame.KEYDOWN and
                        event.key == pygame.K_ESCAPE):
                    return

            self.view()

    def view(self):
        self.sprites.update(self)
        self.screen.fill((200, 200, 200))
        self.sprites.draw(self.screen)
        self.platforms.draw(self.screen, self.distance)
        pygame.display.flip()
