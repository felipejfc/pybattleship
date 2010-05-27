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
		sobre_button = pygame.image.load(filepath("sobre.png")) #Carrega o botao sobre
		sobre_button_vermelho = pygame.image.load(filepath("sobre_s.png")) #Carrega o botao sobre vermelho
		saida_button = pygame.image.load(filepath("sair.png")) #Carrega o botao sair 
		saida_button_vermelho = pygame.image.load(filepath("sair_s.png")) #Carrega  o botao sair vermehlo
		clickable[ng_button] = (21,420) #poe a posicao do elemento no dict
		clickable[sobre_button] = (336,420) #poe a posicao do botao sobre no dict
		clickable[saida_button] = (540,420)  #poe a posicao do botao saida no dict
		pygame.mixer.music.load(musicapath("menu.ogg"))  # Carrega a musica do menu
		pygame.mixer.music.play(-1) # TOCA A MUSICA DO MENU SEM PARAR
		while True:              #Loop do menu, que pega os eventos.
			for evento in pygame.event.get():
				print evento
				menu = 1
				no_botaong = False
				no_botaosobre = False
				no_botaosaida = False
				if evento.type == pygame.QUIT:
					exit()
				if evento.type == MOUSEMOTION: #Verifica onde o ponteiro do mouse anda...
					for key,value in clickable.items():
						if checkclick(value,key.get_size(),evento.pos) and key==ng_button:
							no_botaong = True  
				if evento.type == MOUSEMOTION: #Verifica onde o ponteiro do mouse anda...
					for key,value in clickable.items():
						if checkclick(value,key.get_size(),evento.pos) and key==sobre_button:
							no_botaosobre = True 
				if evento.type == MOUSEMOTION: #Verifica onde o ponteiro do mouse anda...
					for key,value in clickable.items():
						if checkclick(value,key.get_size(),evento.pos) and key==saida_button:
							no_botaosaida = True   
				if evento.type == MOUSEBUTTONDOWN: #Verifica onde o usurio clicou.
					if evento.button == 1:
						for key,value in clickable.items():
							if checkclick(value,key.get_size(),evento.pos) and key==ng_button:
								Menu.menu2(self,screen)
								menu = 2
				if evento.type == MOUSEBUTTONDOWN: #Verifica onde o usurio clicou.
					if evento.button == 1:
						for key,value in clickable.items():
							if checkclick(value,key.get_size(),evento.pos) and key==saida_button:
								exit() # SAIR DO JOGO SE CLICAR NO BOTAO SAIDA
			if menu == 2: # Sair do loop se clicar no botao novo jogo
				break
			if no_botaong == True:
				self.screen.blit(ng_button_vermelho, (21, 420))
				pygame.display.flip()
			elif no_botaosobre == True:
				self.screen.blit(sobre_button_vermelho, (295, 420))
				pygame.display.flip()
			elif no_botaosaida == True:
				self.screen.blit(saida_button_vermelho, (540,420))
				pygame.display.flip()
			else:
				self.screen.blit(background, (0, 0)) #Desenha o BG
				self.screen.blit(ng_button, (21, 420)) #Desenha o botao newgame na tela
				self.screen.blit(sobre_button, (295, 420)) # Desenha o botao sobre na tela
				self.screen.blit(saida_button, (540,420)) # Desenha o botao sobre na tela
			pygame.display.flip() #Atualiza a Tela
                                
                                                                

