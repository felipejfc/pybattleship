import pygame, sys, os
from pygame.locals import *

from functions import *  #importa as funcoes do functions.py

class Menu(object):
	
	def menu2(self,screen):
		clickable = {} #cria um dicionario de elementos clicaveis na tela.
		self.screen = screen  #recebe screen do main.py
		menu2img = pygame.image.load(filepath("menu2.png")) #Carrega o Menu2
		background = pygame.image.load(filepath("menu.jpg")) #Carrega BG
		#self.screen.blit(background, (0, 0)) #Desenha o BG
		#pygame.display.flip() #Atualiza a Tela
		while True:              #Loop do menu, que pega os eventos.
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					exit()
				self.screen.blit(menu2img, (222, 140))
				pygame.display.flip()
					
	def __init__(self, screen):
		clickable = {} #cria um dicionario de elementos clicaveis na tela.
		self.screen = screen  #recebe screen do main.py
		background = pygame.image.load(filepath("menu.jpg")) #Carrega BG
		ng_button = pygame.image.load(filepath("newgamebutton.png")) #Carrega NB
		ng_button_vermelho = pygame.image.load(filepath("newgamebutton_s.png")) #Carrega NB_VERMELHO
		clickable[ng_button] = (21,420) #poe a posicao do elemento no dict
		while True:              #Loop do menu, que pega os eventos.
			for evento in pygame.event.get():
				menu = 1
				no_botao = False
				if evento.type == pygame.QUIT:
					exit()
				if evento.type == MOUSEMOTION: #Verifica onde o ponteiro do mouse anda...
					for key,value in clickable.items():
						if checkclick(value,key.get_size(),evento.pos):
							no_botao = True     
				if evento.type == MOUSEBUTTONDOWN: #Verifica onde o usurio clicou.
					if evento.button == 1:
						for key,value in clickable.items():
							if checkclick(value,key.get_size(),evento.pos) and key==ng_button:
								Menu.menu2(self,screen)
								menu = 2
			if menu == 2:
				break
			if no_botao == True:
				self.screen.blit(ng_button_vermelho, (21, 420))
				pygame.display.flip()
			else:
				self.screen.blit(background, (0, 0)) #Desenha o BG
				self.screen.blit(ng_button, (21, 420)) #Desenha o botao newgame na tela
			pygame.display.flip() #Atualiza a Tela
                                
                                                                

