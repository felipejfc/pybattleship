import pygame, sys, os
from pygame.locals import *

from functions import *  #importa as funcoes do functions.py

class Menu(object):
	def __init__(self, screen):
		clickable = {} #cria um dicionario de elementos clicaveis na tela.
		self.screen = screen  #recebe screen do main.py
		background = pygame.image.load(filepath("menu.jpg")) #Carrega BG
		ng_button = pygame.image.load(filepath("newgamebutton.png")) #Carrega NB
		clickable[ng_button] = (21,420) #poe a posicao do elemento no dict
		print clickable.values()
		
		while True:             #Loop do menu, que pega os eventos.
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					exit()
				if evento.type == MOUSEBUTTONDOWN: #Verifica onde o usurio clicou.
					if evento.button == 1:
						for key,value in clickable.items():
							if checkclick(value,key.get_size(),evento.pos) and key==ng_button:
								print "Novo Jogo!"								
			
			self.screen.blit(background, (0, 0)) #Desenha o botao newgame na tela
			self.screen.blit(ng_button, (21, 420)) #Desenha o BG
			pygame.display.flip() #Atualiza a Tela
