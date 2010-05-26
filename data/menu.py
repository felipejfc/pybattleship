import pygame, sys, os
from pygame.locals import *

from functions import *  #importa as funções do functions.py

class Menu(object):
	def __init__(self, screen):
		self.screen = screen  #recebe screen do main.py
		background = pygame.image.load(filepath("menu.jpg")) #Carrega BG
		new_game_button = pygame.image.load(filepath("newgamebutton.png")) #Carrega NB
		
		while True:             #Loop do menu, que pega os eventos.
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					exit()
				if evento.type == MOUSEBUTTONDOWN: #Verifica onde o usurio clicou.
					if evento.button == 1:
						print "Left click at:",evento.pos
						new_game_button.clickCheck()
			
			self.screen.blit(background, (0, 0)) #Desenha o botao newgame na tela
			self.screen.blit(new_game_button, (21, 420)) #Desenha o BG
			pygame.display.flip() #Atualiza a Tela
