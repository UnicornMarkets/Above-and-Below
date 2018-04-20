import pygame
import character
import groups
import random
import data
from constants import *

class Help:
    """
    Help Screen from the menu
    """

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(data.filepath("top", "show_help.png"))
        self.image_pos = (SCREEN_W / 2 - self.image.get_rect().width / 2,
                         SCREEN_H / 2 - self.image.get_rect().height / 2)
        pygame.mixer.music.load(data.filepath('sounds', 'help.wav'))
        pygame.mixer.music.set_volume(.4)
        pygame.mixer.music.play(-1)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if event.key == pygame.K_SPACE:
                        return
            # display help screen, exit on spacebar event
            self.screen.fill((212, 253, 204))
            self.screen.blit(self.image, self.image_pos)
            pygame.display.flip()


class Ending:
    """
    This is an ending at the end of the game.

    Returns to the main menu after a pressing a key
    """
    def __init__(self, screen, win_lose):
        pygame.mixer.music.stop()
        self.screen = screen
        self.image = pygame.image.load(data.filepath("top", win_lose + ".png"))
        self.image_pos = (SCREEN_W / 2 - self.image.get_rect().width / 2,
                         SCREEN_H / 2 - self.image.get_rect().height / 2)
        pygame.mixer.music.load(data.filepath('sounds', win_lose + '.mp3'))
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)
        self.top_image = pygame.image.load(data.filepath("top",
                                    win_lose + "1.png"))
        self.bottom_image = pygame.image.load(data.filepath("top",
                                    win_lose + "2.png"))
        self.top_image_pos = (SCREEN_W / 2 - self.top_image.get_rect().width / 2,
                              SCREEN_H * 1 / 16 - self.top_image.get_rect().height / 2)
        self.bottom_image_pos = (SCREEN_W / 2 - self.bottom_image.get_rect().width / 2,
                                SCREEN_H * 15 / 16 - self.bottom_image.get_rect().height / 2)



    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if event.key == pygame.K_SPACE:
                        return
            # display ending screen - ending music, exit after spacebar
            self.screen.fill((212, 253, 204))
            self.screen.blit(self.image, self.image_pos)
            self.screen.blit(self.top_image, self.top_image_pos)
            self.screen.blit(self.bottom_image, self.bottom_image_pos)
            pygame.display.flip()


class Menu:
    """
    This is a menu at the start of the game.

    Displays how to play, start and exit
    """
    def __init__(self, screen):
        pygame.mixer.music.stop()
        self.screen = screen
        self.above = pygame.image.load(data.filepath("top", "above_below.png"))
        self.below = pygame.transform.flip(pygame.image.load(
                        data.filepath("top", "above_below.png")), False, True)
        self.help = pygame.image.load(data.filepath("top", "help.png"))
        self.exit = pygame.image.load(data.filepath("top", "exit.png"))
        self.name_image = pygame.image.load(data.filepath("top", "abv_blw.png"))
        self.name_pos = (SCREEN_W / 2 - self.name_image.get_rect().width / 2,
                         SCREEN_H / 2 - self.name_image.get_rect().height / 2)
        self.help_d = {1: pygame.transform.scale(self.help,
                                    (int(.9 * self.help.get_rect().width),
                                    int(.9 * self.help.get_rect().height))),
                       2: pygame.transform.scale(self.help,
                                     (int(1.3 * self.help.get_rect().width),
                                      int(1.3 * self.help.get_rect().height)))}
        self.exit_d = {1: pygame.transform.scale(self.exit,
                                    (int(.9 * self.exit.get_rect().width),
                                    int(.9 * self.exit.get_rect().height))),
                       2: pygame.transform.scale(self.exit,
                                     (int(1.3 * self.exit.get_rect().width),
                                      int(1.3 * self.exit.get_rect().height)))}
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
        self.help_pos = {1: (SCREEN_W / 16 - self.help_d[1].get_rect().width / 2,
                             SCREEN_H / 2 - self.help_d[1].get_rect().height / 2),
                         2: (SCREEN_W / 16 - self.help_d[2].get_rect().width / 2,
                             SCREEN_H / 2 - self.help_d[2].get_rect().height / 2)}
        self.exit_pos = {1: (SCREEN_W * 15 / 16 - self.exit_d[1].get_rect().width / 2,
                             SCREEN_H / 2 - self.exit_d[1].get_rect().height / 2),
                         2: (SCREEN_W * 15 / 16 - self.exit_d[2].get_rect().width / 2,
                             SCREEN_H / 2 - self.exit_d[2].get_rect().height / 2)}
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
        self.help_p = self.help_pos[1]
        self.help_i = self.help_d[1]
        self.exit_p = self.exit_pos[1]
        self.exit_i = self.exit_d[1]

        self.ding = pygame.mixer.Sound(data.filepath('sounds', 'ding.wav'))
        self.ding.set_volume(.6)
        self.start_sound = pygame.mixer.Sound(data.filepath('sounds', 'start.wav'))
        pygame.mixer.music.load(data.filepath('sounds', 'menu.wav'))
        pygame.mixer.music.set_volume(.6)
        pygame.mixer.music.play(-1)

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
                        self.help_p = self.help_pos[1]
                        self.help_i = self.help_d[1]
                        self.exit_p = self.exit_pos[1]
                        self.exit_i = self.exit_d[1]
                        self.world = 'above'

                    if event.key == pygame.K_DOWN:
                        self.ding.play()
                        self.above_i = self.above_d[1]
                        self.above_p = self.above_pos[1]
                        self.below_i = self.below_d[2]
                        self.below_p = self.below_pos[2]
                        self.help_p = self.help_pos[1]
                        self.help_i = self.help_d[1]
                        self.exit_p = self.exit_pos[1]
                        self.exit_i = self.exit_d[1]
                        self.world = 'below'

                    if event.key == pygame.K_LEFT:
                        self.ding.play()
                        self.above_i = self.above_d[1]
                        self.above_p = self.above_pos[1]
                        self.below_i = self.below_d[1]
                        self.below_p = self.below_pos[1]
                        self.help_p = self.help_pos[2]
                        self.help_i = self.help_d[2]
                        self.exit_p = self.exit_pos[1]
                        self.exit_i = self.exit_d[1]
                        self.world = 'help'


                    if event.key == pygame.K_RIGHT:
                        self.ding.play()
                        self.above_i = self.above_d[1]
                        self.above_p = self.above_pos[1]
                        self.below_i = self.below_d[1]
                        self.below_p = self.below_pos[1]
                        self.help_p = self.help_pos[1]
                        self.help_i = self.help_d[1]
                        self.exit_p = self.exit_pos[2]
                        self.exit_i = self.exit_d[2]
                        self.world = 'exit'

                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.start_sound.play()
                        pygame.mixer.music.stop()
                        return self.world


            self.screen.fill((212, 253, 204))
            self.screen.blit(self.name_image, self.name_pos)
            self.screen.blit(self.above_i, self.above_p)
            self.screen.blit(self.below_i, self.below_p)
            self.screen.blit(self.help_i, self.help_p)
            self.screen.blit(self.exit_i, self.exit_p)
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
        self.sound_list = []

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

            if self.world == 0:
                g = self.below_world()

            if self.world == 1:
                g = self.above_world()

            if g:
                return g

            self.view()

    def below_world(self):
        if self.player.rect.centery < 0:
            if self.level == 4 and self.flipped == False:
                for sound in self.sound_list:
                    sound.stop()
                pygame.mixer.music.stop()
                pygame.mixer.music.load(data.filepath('sounds', 'above4.wav'))
                pygame.mixer.music.set_volume(.3)
                pygame.mixer.music.play(-1)
                self.flipped = True
                self.world = 1
                self.player.rect.centery = 0
                self.player.dy = - self.player.dy
            elif self.level == 4:
                for sound in self.sound_list:
                    sound.stop()
                return 'win'
            else:
                self.level += 1
                self.player.rect.centery = SCREEN_H
                s = pygame.mixer.Sound(data.filepath('sounds', 'below' +
                                        str(self.level) + '.wav'))
                s.set_volume(.3)
                s.play(-1)
                self.sound_list.append(s)
        if self.player.rect.centery > SCREEN_H:
            for sound in self.sound_list:
                sound.stop()
            return 'lose'


    def above_world(self):
        if self.player.rect.centery > SCREEN_H:
            if self.level == 0 and self.flipped == False:
                for sound in self.sound_list:
                    sound.stop()
                pygame.mixer.music.stop()
                pygame.mixer.music.load(data.filepath('sounds', 'below0.wav'))
                pygame.mixer.music.set_volume(.3)
                pygame.mixer.music.play(-1)
                self.flipped = True
                self.world = 0
                self.player.rect.centery = 0
                self.player.dy = - self.player.dy
            elif self.level == 0:
                for sound in self.sound_list:
                    sound.stop()
                return 'win'
            else:
                self.level -= 1
                self.player.rect.centery = 0
                s = pygame.mixer.Sound(data.filepath('sounds', 'above' +
                                        str(self.level) + '.wav'))
                s.set_volume(.3)
                s.play(-1)
                self.sound_list.append(s)
        if self.player.rect.centery < 0 and self.world == 1:
            for sound in self.sound_list:
                sound.stop()
            return 'lose'

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
