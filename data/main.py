import pygame, os
from pygame.locals import *

import menu

def main():
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mouse.set_visible(1) #Faz o mouse ser visivel na tela.
    pygame.display.set_caption("PyBattleShip(DEMO)")
    screen = pygame.display.set_mode((640, 480)) #Cria a Janela do Jogo!
    menu.Menu(screen) #Chama o Menu.
