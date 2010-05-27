import pygame, sys, os
from pygame.locals import *
import menu
from functions import *  #importa as funcoes do functions.py

class Menu2(object):
	
	def __init__(self,screen):
		
		self.screen = screen  #recebe screen do main.py
		clickable_m2 = {}
		
		#background = pygame.image.load(filepath("menu.jpg")) #Carrega BG
		#self.screen.blit(background, (0, 0)) #Desenha o BG
		
		menu2img = pygame.image.load(filepath("menu2.png")) #Carrega o Menu2
		
		menu2bt1   = pygame.image.load(filepath("menu2_button1.png")) #Carrega o botao 1
		menu2bt1_r = pygame.image.load(filepath("menu2_button1_r.png")) #Carrega o botao 1
		menu2bt2   = pygame.image.load(filepath("menu2_button2.png")) #Carrega o botao 1
		menu2bt2_r = pygame.image.load(filepath("menu2_button2_r.png")) #Carrega o botao 1
		menu2bt3   = pygame.image.load(filepath("menu2_button3.png")) #Carrega o botao 1
		menu2bt3_r = pygame.image.load(filepath("menu2_button3_r.png")) #Carrega o botao 1
		
		
		clickable_m2[menu2bt1] = (270,230)
		clickable_m2[menu2bt2] = (275,270)
		clickable_m2[menu2bt3] = (293,310)
		
		bt1 = False
		bt2 = False
		bt3 = False
		
		while True:              #Loop do menu, que pega os eventos.
			menu__ = 2
			for evento in pygame.event.get():
				bt1 = False
				bt2 = False
				bt3 = False
				if evento.type == pygame.QUIT:
					exit()
					
				if evento.type == MOUSEMOTION: #Verifica onde o ponteiro do mouse anda...
					for key,value in clickable_m2.items():
						if checkclick(value,key.get_size(),evento.pos) and key==menu2bt1:
							bt1 = True
						if checkclick(value,key.get_size(),evento.pos) and key==menu2bt2:
							bt2 = True
						if checkclick(value,key.get_size(),evento.pos) and key==menu2bt3:
							bt3 = True
				if evento.type == MOUSEBUTTONDOWN:
					for key,value in clickable_m2.items():
						if checkclick(value,key.get_size(),evento.pos) and key==menu2bt3:
							menu.Menu(screen)
							menu__ = 1
			if menu__<>2:
				break
			self.screen.blit(menu2img, (222, 140))
			if bt1:
				self.screen.blit(menu2bt1_r, (270, 230))
			else:
				self.screen.blit(menu2bt1, (270, 230))
			if bt2:
				self.screen.blit(menu2bt2_r, (275, 270))
			else:
				self.screen.blit(menu2bt2, (275, 270))
			if bt3:
				self.screen.blit(menu2bt3_r, (293, 310))
			else:
				self.screen.blit(menu2bt3, (293, 310))
			pygame.display.flip()
