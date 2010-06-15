import pygame, sys, os
from pygame.locals import *
import menu
import jogo
from functions import *  #importa as funcoes do functions.py

class Menu2(object):
	
	def __init__(self,screen):
		
		self.screen = screen  #recebe screen do main.py
		dicionario_elementos_clicaveis_2 = {}
		
		#background = pygame.image.load(filepath("menu.jpg")) #Carrega BG
		#self.screen.blit(background, (0, 0)) #Desenha o BG
		
		background_menu_2 = pygame.image.load(filepath("menu2.png")) #Carrega o Menu2
		
		botao_singleplayer   = pygame.image.load(filepath("menu2_button1.png")) #Carrega o botao 1
		botao_singleplayer_vermelho = pygame.image.load(filepath("menu2_button1_r.png")) #Carrega o botao 1
		botao_multiplayer   = pygame.image.load(filepath("menu2_button2.png")) #Carrega o botao 1
		botao_multiplayer_vermelho = pygame.image.load(filepath("menu2_button2_r.png")) #Carrega o botao 1
		botao_cancel   = pygame.image.load(filepath("menu2_button3.png")) #Carrega o botao 1
		botao_cancel_vermelho = pygame.image.load(filepath("menu2_button3_r.png")) #Carrega o botao 1
		
		
		dicionario_elementos_clicaveis_2[botao_singleplayer] = (270,230)
		dicionario_elementos_clicaveis_2[botao_multiplayer] = (275,270)
		dicionario_elementos_clicaveis_2[botao_cancel] = (293,310)
		
		botao_singleplayer_pressionado = False
		botao_multiplayer_pressionado = False
		botao_cancel_pressionado = False
		
		while True:              #Loop do menu, que pega os eventos.
			menu__ = 2
			for evento in pygame.event.get():
				botao_singleplayer_pressionado = False
				botao_multiplayer_pressionado = False
				botao_cancel_pressionado = False
				if evento.type == pygame.QUIT:
					exit()
					
				if evento.type == MOUSEMOTION: #Verifica onde o ponteiro do mouse anda...
					for key,value in dicionario_elementos_clicaveis_2.items():
						if checkclick(value,key.get_size(),evento.pos) and key==botao_singleplayer:
							botao_singleplayer_pressionado = True
						if checkclick(value,key.get_size(),evento.pos) and key==botao_multiplayer:
							botao_multiplayer_pressionado = True
						if checkclick(value,key.get_size(),evento.pos) and key==botao_cancel:
							botao_cancel_pressionado = True
				if evento.type == MOUSEBUTTONDOWN:
					for key,value in dicionario_elementos_clicaveis_2.items():
						if checkclick(value,key.get_size(),evento.pos) and key==botao_cancel:
							menu.Menu(screen)
							menu__ = 1
						if checkclick(value,key.get_size(),evento.pos) and key==botao_singleplayer:
							jogo.Jogo(screen)
							menu__ = 3
			if menu__<>2:
				break
			
			self.screen.blit(background_menu_2, (222, 140))
			if botao_singleplayer_pressionado:
				self.screen.blit(botao_singleplayer_vermelho, (270, 230))
			else:
				self.screen.blit(botao_singleplayer, (270, 230))
			if botao_multiplayer_pressionado:
				self.screen.blit(botao_multiplayer_vermelho, (275, 270))
			else:
				self.screen.blit(botao_multiplayer, (275, 270))
			if botao_cancel_pressionado:
				self.screen.blit(botao_cancel_vermelho, (293, 310))
			else:
				self.screen.blit(botao_cancel, (293, 310))
			pygame.display.flip()
