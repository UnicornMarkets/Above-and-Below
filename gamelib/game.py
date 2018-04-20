import pygame
import character
import groups
import random
import data
from constants import *

class Ending:
    """
    This is an ending at the end of the game.

    Returns to the main menu after a pressing a key
    """
    def __init__(self, screen):
        self.screen = screen

    def play(self):
        pass

class Menu:
    """
    This is a menu at the start of the game.

    Displays how to play, start and exit
    """
    def __init__(self, screen):
        self.screen = screen
        self.above = pygame.image.load(data.filepath("top", "above_below.png"))
        self.below = pygame.transform.flip(pygame.image.load(
                        data.filepath("top", "above_below.png")), False, True)
        self.name_image = pygame.image.load(data.filepath("top", "abv_blw.png"))
        self.name_pos = (SCREEN_W / 2 - self.name_image.get_rect().width / 2,
                         SCREEN_H / 2 - self.name_image.get_rect().height / 2)
        self.above_d = {1: pygame.transform.scale(self.above,
                                    (int(1.4 * self.above.get_rect().width),
                                    int(1.4 * self.above.get_rect().height))),
                        2: pygame.transform.scale(self.above,
                                     (int(1.8 * self.above.get_rect().width),
                                      int(1.8 * self.above.get_rect().height)))}
        self.below_d = {1: pygame.transform.scale(self.below,
                                    (int(1.4 * self.below.get_rect().width),
                                    int(1.4 * self.below.get_rect().height))),
                        2: pygame.transform.scale(self.below,
                                    (int(1.8 * self.below.get_rect().width),
                                    int(1.8 * self.below.get_rect().height)))}
        self.above_pos = {1: (SCREEN_W / 2 - self.above_d[1].get_rect().width / 2,
                            SCREEN_H / 4 - self.above_d[1].get_rect().height / 2),
                          2: (SCREEN_W / 2 - self.above_d[2].get_rect().width / 2,
                            SCREEN_H / 4 - self.above_d[2].get_rect().height / 2)}
        self.below_pos = {1: (SCREEN_W / 2 - self.below_d[1].get_rect().width / 2,
                         SCREEN_H * 3 / 4 - self.below_d[1].get_rect().height / 2),
                          2: (SCREEN_W / 2 - self.below_d[2].get_rect().width / 2,
                         SCREEN_H * 3 / 4 - self.below_d[2].get_rect().height / 2)}
        self.world = None
        self.above_p = self.above_pos[1]
        self.above_i = self.above_d[1]
        self.below_p = self.below_pos[1]
        self.below_i = self.below_d[1]
        self.ding = pygame.mixer.Sound(data.filepath('sounds', 'ding.wav'))
        self.ding.set_volume(.6)
        self.start_sound = pygame.mixer.Sound(data.filepath('sounds', 'start.wav'))

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if event.key == pygame.K_UP:
                        self.ding.play()
                        self.above_i = self.above_d[2]
                        self.above_p = self.above_pos[2]
                        self.below_i = self.below_d[1]
                        self.below_p = self.below_pos[1]
                        self.world = 1
                    if event.key == pygame.K_DOWN:
                        self.ding.play()
                        self.above_i = self.above_d[1]
                        self.above_p = self.above_pos[1]
                        self.below_i = self.below_d[2]
                        self.below_p = self.below_pos[2]
                        self.world = 0
                    if event.key == pygame.K_SPACE:
                        self.start_sound.play()
                        return self.world

            self.screen.fill((212, 253, 204))
            self.screen.blit(self.name_image, self.name_pos)
            self.screen.blit(self.above_i, self.above_p)
            self.screen.blit(self.below_i, self.below_p)
            pygame.display.flip()


class Game:
    """
    This class runs the game
    """

    def __init__(self, screen, level=0, world=0):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(30)
        self.sprites = pygame.sprite.Group()
        self.player = character.Player(100, 100, self.dt, self.sprites)
        self.distance = 100
        self.levels = {}
        self.level = level
        self.world = world
        self.flipped = False

    def run(self):
        [self.read_levels(i) for i in range(5)]
        return self.loop()

    def read_levels(self, level_num):
        self.levels[level_num] = pygame.sprite.Group()
        level = data.load('levels', 'level' + str(level_num) + '.txt', 'r')
        y = 0
        for row in level.readlines():
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
                if self.level == 4 and self.flipped == False:
                    self.flipped = True
                    self.world = 1
                    self.player.rect.centery = 0
                    self.player.dy = - self.player.dy
                elif self.level == 4:
                    return 'win'
                else:
                    self.level += 1
                    self.player.rect.centery = SCREEN_H
            if self.player.rect.centery > SCREEN_H and self.world == 0:
                return 'lose'

            if self.player.rect.centery > SCREEN_H and self.world == 1:
                if self.level == 0 and self.flipped == False:
                    self.flipped = True
                    self.world = 0
                    self.player.rect.centery = 0
                    self.player.dy = - self.player.dy
                elif self.level == 0:
                    return 'win'
                else:
                    self.level -= 1
                    self.player.rect.centery = 0
            if self.player.rect.centery < 0 and self.world == 1:
                return 'lose'


            self.view()

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
