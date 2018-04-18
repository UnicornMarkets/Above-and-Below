import pygame
import character
import groups
import random
import data
from constants import *

class Game:

    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(30)
        self.sprites = pygame.sprite.Group()
        self.player = character.Player(100, 100, self.dt, self.sprites)
        self.distance = 100
        self.levels = {}
        self.level = 0
        self.world = 0

    def run(self):
        [self.read_levels(i) for i in range(5)]
        self.loop()

    def read_levels(self, level_num):
        self.levels[level_num] = pygame.sprite.Group()
        level = data.load('levels', 'level' + str(level_num) + '.txt', 'r')
        y = 0
        for row in level.readlines():
            if row[0] == 'C' or row[0] == 'G':
                groups.Ground(x, y * BLOCK_S, row[0],
                              self.levels[level_num])
            else:
                for x in range(HOR_BL):
                    if row[x] == 'W':
                        groups.Wall(x * BLOCK_S, y * BLOCK_S,
                                    self.levels[level_num])
            y += 1

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if (event.type == pygame.KEYDOWN and
                        event.key == pygame.K_ESCAPE):
                    return

            if self.player.rect.centery < 0 and self.world == 0:
                self.level += 1
                self.player.rect.centery = SCREEN_H
            if self.player.rect.centery > SCREEN_H and self.world == 0:
                print("you lost!")
                return

            if self.player.rect.centery > SCREEN_H and self.world == 1:
                self.level -= 1
                self.player.rect.centery = 0
            if self.player.rect.centery < 0 and self.world == 1:
                print("you lost!")
                return


            self.view()

    def flip_world(self):

        self.world = 1

    def view(self):

        if self.world == 0:
            world_color = (108 + self.level * 24, 186 + self.level * 7, 255)
        elif self.world == 1:
            world_color = (255,  186 + self.level * 7, 108 + self.level * 24)

        self.sprites.update(self)
        self.screen.fill(world_color)
        self.sprites.draw(self.screen)
        self.levels[self.level].draw(self.screen)
        pygame.display.flip()
