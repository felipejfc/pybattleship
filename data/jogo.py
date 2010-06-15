import pygame, sys, os
from pygame.locals import *
import menu
import menu2
from functions import *  #importa as funcoes do functions.py

class Jogo(object):
	def __init__(self,screen):
		self.screen = screen  #recebe screen do main.py
		campo = pygame.image.load(filepath("campo.png"))
		self.screen.blit(campo, (0, 0))

		barco_teste = pygame.image.load(filepath("barco.png"));
		self.screen.blit(barco_teste, (60, 390))



		start_rect = barco_teste.get_rect()
		image_rect = start_rect





		while True:
			event = pygame.event.poll()
			keyinput = pygame.key.get_pressed()
    # exit on corner 'x' click or escape key press
			if keyinput[pygame.K_ESCAPE]:
				raise SystemExit
			elif event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				print event.pos, list(event.pos)  # test
				mouse_loc = "mouse click at (%d, %d)" % event.pos
				pygame.display.set_caption(mouse_loc)
				mouse_pos = list(event.pos)
				image_rect = start_rect.move(mouse_pos)
				"""
				print image_rect  # test
				print "corner coordinates --> (%d, %d, %d, %d)" % \
					(image_rect.left, image_rect.top, image_rect.right,
					image_rect.bottom)
				"""
    # this erases the old sreen with black
			self.screen.blit(campo, (0, 0))
    # put the image on the screen
			self.screen.blit(barco_teste, image_rect)
    # update screen
			pygame.display.flip()
