'''Game main module.

Runs the game from run_game.py

Responsible for transitioning from the menu to the game and the final screens
'''

import pygame
import data
from game import Game, Menu, Ending, Help
from constants import SCREEN_H, SCREEN_W

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H),
                            pygame.HWSURFACE|pygame.FULLSCREEN)
    while True:
        m = Menu(screen).play()
        if m == 'above':
            pygame.mixer.music.load(data.filepath('sounds', 'above4.wav'))
            pygame.mixer.music.set_volume(.3)
            pygame.mixer.music.play(-1)
            g = Game(screen, 4, 1)
            win_lose = g.run()
            pygame.mixer.music.stop()
            if win_lose != None:
                Ending(screen, win_lose).play()
        elif m  == 'below':
            pygame.mixer.music.load(data.filepath('sounds', 'below0.wav'))
            pygame.mixer.music.set_volume(.3)
            pygame.mixer.music.play(-1)
            g = Game(screen)
            win_lose = g.run()
            pygame.mixer.music.stop()
            if win_lose != None:
                Ending(screen, win_lose).play()
        elif m == 'help':
            Help(screen).play()
        elif m == 'exit':
            return
