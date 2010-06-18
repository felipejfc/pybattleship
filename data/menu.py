import pygame, sys, os
from pygame.locals import *
import menu2
import menu_sobre
from functions import *  #importa as funcoes do functions.py

class Menu(object):
								
	def __init__(self, screen):
		dicionario_elementos_clicaveis = {} #cria um dicionario de elementos clicaveis na tela.
		self.screen = screen  #recebe screen do main.py
		background = pygame.image.load(filepath("menu.jpg")) #Carrega BG
		
		botao_novojogo = pygame.image.load(filepath("newgamebutton.png")) #Carrega NB
		botao_novojogo_vermelho = pygame.image.load(filepath("newgamebutton_s.png")) #Carrega NB_VERMELHO
		botao_sobre = pygame.image.load(filepath("sobre.png")) #Carrega o botao sobre
		botao_sobre_vermelho = pygame.image.load(filepath("sobre_s.png")) #Carrega o botao sobre vermelho
		botao_sair = pygame.image.load(filepath("sair.png")) #Carrega o botao sair 
		botao_sair_vermelho = pygame.image.load(filepath("sair_s.png")) #Carrega  o botao sair vermehlo
		
		dicionario_elementos_clicaveis[botao_novojogo] = (21,420) #poe a posicao do elemento no dict
		dicionario_elementos_clicaveis[botao_sobre] = (295,420) #poe a posicao do botao sobre no dict
		dicionario_elementos_clicaveis[botao_sair] = (540,420)  #poe a posicao do botao saida no dict
		#pygame.mixer.music.load(musicapath("menu.ogg"))  # Carrega a musica do menu
		#pygame.mixer.music.play(-1) # TOCA A MUSICA DO MENU SEM PARAR
		menu = 1
		botao_novojogo_pressionado = False
		botao_sobre_pressionado = False
		botao_sair_pressionado = False
		while True:              #Loop do menu, que pega os eventos.
			for evento in pygame.event.get():
				botao_novojogo_pressionado = False
				botao_sobre_pressionado = False
				botao_sair_pressionado = False
				if evento.type == pygame.QUIT:
					exit()
			
				if evento.type == MOUSEMOTION: #Verifica onde o ponteiro do mouse anda... para destacar os botoes.
					for key,value in dicionario_elementos_clicaveis.items():
						if checkclick(value,key.get_size(),evento.pos) and key==botao_novojogo:
							botao_novojogo_pressionado = True  
						if checkclick(value,key.get_size(),evento.pos) and key==botao_sobre:
							botao_sobre_pressionado = True 
						if checkclick(value,key.get_size(),evento.pos) and key==botao_sair:
							botao_sair_pressionado = True   
							
				if evento.type == MOUSEBUTTONDOWN: #Verifica onde o usurio clicou.
					if evento.button == 1:
						for key,value in dicionario_elementos_clicaveis.items():
							if checkclick(value,key.get_size(),evento.pos) and key==botao_novojogo:
								menu2.Menu2(screen)
								menu = 2
							if checkclick(value,key.get_size(),evento.pos) and key==botao_sobre:
								menu_sobre.Menu_sobre(screen)
								menu = 3
							if checkclick(value,key.get_size(),evento.pos) and key==botao_sair:
								exit() # SAIR DO JOGO SE CLICAR NO BOTAO SAIR
								
			if menu == 2: # Sair do loop se clicar no botao novo jogo
				break
			if menu == 3: # Sair do loop se clicar no botao sobre
				break
			if botao_novojogo_pressionado == True:
				self.screen.blit(botao_novojogo_vermelho, (21, 420))
				pygame.display.flip()
			elif botao_sobre_pressionado == True:
				self.screen.blit(botao_sobre_vermelho, (295, 420))
				pygame.display.flip()
			elif botao_sair_pressionado == True:
				self.screen.blit(botao_sair_vermelho, (540,420))
				pygame.display.flip()
			else:
				self.screen.blit(background, (0, 0)) #Desenha o BG
				self.screen.blit(botao_novojogo, (21, 420)) #Desenha o botao newgame na tela
				self.screen.blit(botao_sobre, (295, 420)) # Desenha o botao sobre na tela
				self.screen.blit(botao_sair, (540,420)) # Desenha o botao sobre na tela
			pygame.display.flip() #Atualiza a Tela
                                
                                                                

