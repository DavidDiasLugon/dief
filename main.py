import pygame, sys
from config import *
from level import Level
from dief import *
from PPlay import *
import pygame
from pygame.locals import *
from pygame import mixer
from random import randint
from menu import menu_inic

class Game:
    def __init__(self):
        # Setup geral
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dief")
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.menu = False

    def run(self):
        return_to_menu = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            color = (0, 0, 0)
            self.screen.fill(color)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

            if self.level.player.has_opened_chest():
                return_to_menu = True
                break
            
        if return_to_menu:
            menu_result = menu_inic()
            if not menu_result:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    menu_result = menu_inic()
    if menu_result:
        game = Game()
        game.run()