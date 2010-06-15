import pygame, sys, os
from pygame.locals import *
import menu
import menu2
from functions import *  #importa as funcoes do functions.py

clickable = {} #cria um dicionario de elementos clicaveis na tela.
		
class Jogo(object):
	def __init__(self,screen):
		barco_selecionado = 0
		self.screen = screen  #recebe screen do main.py
		campo = pygame.image.load(filepath("campo.png"))
		self.screen.blit(campo, (0, 0))

		barco_teste = pygame.image.load(filepath("barco.png"));
		self.screen.blit(barco_teste, (60, 390))
		
		clickable[barco_teste] = (60,390) #poe a posicao do elemento no dict de elementos clicaveis
		
		start_rect = barco_teste.get_rect()
		image_rect = start_rect
		pygame.display.flip()
		
		while True:
			for evento in pygame.event.get():				
				if evento.type == pygame.QUIT:
					exit()

				if barco_selecionado:
					if evento.type == pygame.MOUSEBUTTONDOWN:
						print evento.pos, list(evento.pos)  # test
						mouse_pos = list(evento.pos)
						image_rect = start_rect.move(mouse_pos)
						self.screen.blit(campo, (0, 0))
						self.screen.blit(barco_teste, (60, 390))
						self.screen.blit(barco_teste, (image_rect[0]-45,image_rect[1]-25))
						barco_selecionado = 0
					pygame.display.flip()
					
				if evento.type == MOUSEBUTTONDOWN: #Verifica onde o usurio clicou.
					if evento.button == 1:
						for key,value in clickable.items():
							if checkclick(value,key.get_size(),evento.pos) and key==barco_teste:
								barco_selecionado = 1
