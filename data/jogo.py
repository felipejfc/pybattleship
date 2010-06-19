import pygame, sys, os
from pygame.locals import *
import menu
import menu2
from functions import *  #importa as funcoes do functions.py

clickable = {} #cria um dicionario de elementos clicaveis na tela.

matriz_tela = {}

class Jogo(object):

	def __init__(self,screen):
		barco_selecionado = 0
		self.screen = screen  #recebe screen do main.py
		campo = pygame.image.load(filepath("campo.png"))
		self.screen.blit(campo, (0, 0))

		barco_teste = pygame.image.load(filepath("barco.png"));
		self.screen.blit(barco_teste, (60, 390))
		clickable[barco_teste] = (60,390) #poe a posicao do elemento no dict de elementos clicaveis

#Mapa da tela
#============================		
		matriz_tela = cria_mapa(330, 72)
		matriz_jogo = cria_matriz_de_barcos()
		print matriz_jogo
#============================
		start_rect = barco_teste.get_rect()
		image_rect = start_rect
		pygame.display.flip()
		time = pygame.time.Clock()
		time.tick(60)
		imagem_acertou = pygame.image.load(filepath("hitten.png"));
		imagem_nada = pygame.image.load(filepath("nada.png"));
		while True:
			for evento in pygame.event.get():	
				if evento.type == pygame.QUIT:
					exit()
				if barco_selecionado:
					while not evento.type == MOUSEBUTTONUP:
						for evento in pygame.event.get():
							mouse_pos = list(evento.pos)
							image_rect = start_rect.move(mouse_pos)
						self.screen.blit(campo, (0, 0))
						self.screen.blit(barco_teste, (image_rect[0]-45,image_rect[1]-25))
						pygame.display.update()
					
					barco_selecionado = 0
					
				if evento.type == MOUSEBUTTONDOWN: #Verifica onde o usuario clicou.
					if evento.button == 1:
						for key,value in clickable.items():
							if checkclick(value,key.get_size(),evento.pos) and key==barco_teste:
								barco_selecionado = 1
								
					#verificar qual quadrado o usuario clicou
					#=======================================	
						quadrado_clicado = verifica_quadrado_clicado(matriz_tela,evento)
						if quadrado_clicado!=None:
							if matriz_jogo[quadrado_clicado[0]][quadrado_clicado[1]] > 0:
								self.screen.blit(imagem_acertou, (matriz_tela[quadrado_clicado[0]][quadrado_clicado[1]][0]-1,matriz_tela[quadrado_clicado[0]][quadrado_clicado[1]][1]-1))
								pygame.display.update()
							if matriz_jogo[quadrado_clicado[0]][quadrado_clicado[1]] <= 0:
								self.screen.blit(imagem_nada, (matriz_tela[quadrado_clicado[0]][quadrado_clicado[1]][0]-1,matriz_tela[quadrado_clicado[0]][quadrado_clicado[1]][1]-1))
								pygame.display.update()
					#=======================================	
