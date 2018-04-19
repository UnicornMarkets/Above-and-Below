'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''

import pygame
from game import Game
from constants import SCREEN_H, SCREEN_W

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H),
                            pygame.HWSURFACE|pygame.FULLSCREEN)
    g = Game(screen)
    win_lose = g.run()
    if win_lose == 'lose':
        print("you lose!")
    elif win_lose == 'win':
        print("you win!")
