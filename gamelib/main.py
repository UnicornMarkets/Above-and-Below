'''Game main module.

Runs the game from run_game.py

Responsible for transitioning from the menu to the game and the final screens
'''

import pygame
from game import Game, Menu, Ending
from constants import SCREEN_H, SCREEN_W

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H),
                            pygame.HWSURFACE|pygame.FULLSCREEN)
    m = Menu(screen).play()

    if m == 1:
        g = Game(screen, 4, 1)
    elif m  == 0:
        g = Game(screen)
    else:
        return

    win_lose = g.run()

    if win_lose == 'lose':
        print("you lose!")
    elif win_lose == 'win':
        print("you win!")
