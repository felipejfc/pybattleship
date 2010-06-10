import pygame, sys, os
from pygame.locals import *
import menu
import menu2
from functions import *  #importa as funcoes do functions.py

class Jogo(object):
	def __init__(self,screen):
		self.screen = screen  #recebe screen do main.py
		campo = pygame.image.load(filepath("campo.png"))
		while True:
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					exit()
			self.screen.blit(campo, (0, 0))
			pygame.display.flip()
