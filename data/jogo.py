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
		#self.screen.blit(barco_teste, (60, 390))
		clickable[barco_teste] = (60,390) #poe a posicao do elemento no dict de elementos clicaveis
		#pygame.mixer.music.stop()

#Mapa da tela
#============================		
		matriz_tela_com = cria_mapa(330, 72)
		matriz_jogo_com = cria_matriz_de_barcos()
		matriz_tela_player = cria_mapa(10,72)
		matriz_jogo_player = cria_matriz_de_barcos()
		#print matriz_jogo_com
#============================
		start_rect = barco_teste.get_rect()
		image_rect = start_rect
		pygame.display.flip()
		time = pygame.time.Clock()
		time.tick(60)

                imagem_acertou = pygame.image.load(filepath("hitten.png"));
		imagem_nada = pygame.image.load(filepath("nada.png"));

                imagem_ganhador_cpu = pygame.image.load(filepath("perdeu.png"))
                imagem_ganhador_jogador = pygame.image.load(filepath("ganhou.png"))

                contador_tiros_cpu = 0
                contador_tiros_player = 0
		while True:
			for evento in pygame.event.get():
                                print evento
				if evento.type == pygame.QUIT:
					exit()
				#print evento
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
						quadrado_clicado = verifica_quadrado_clicado(matriz_tela_com,evento)
						if quadrado_clicado!=None:
							if matriz_jogo_com[quadrado_clicado[0]][quadrado_clicado[1]] == 11:
								continue
							if matriz_jogo_com[quadrado_clicado[0]][quadrado_clicado[1]] > 0:
								self.screen.blit(imagem_acertou, (matriz_tela_com[quadrado_clicado[0]][quadrado_clicado[1]][0]-1,matriz_tela_com[quadrado_clicado[0]][quadrado_clicado[1]][1]-1))
								#pygame.mixer.music.load(musicapath("explosao.ogg"))  # Carrega som da bomba
								#pygame.mixer.music.play()
								#pygame.mixer.music.queue(musicapath("menu.ogg"))
								pygame.display.update()
								matriz_jogo_com[quadrado_clicado[0]][quadrado_clicado[1]] = 11
                                                                contador_tiros_player +=1
								tiro = tiro_aleatorio(matriz_jogo_player)
							
								if matriz_jogo_player[tiro[0]][tiro[1]] > 0 and matriz_jogo_player[tiro[0]][tiro[1]] < 11:
									teempo = cria_tempo_cpu()
                                                                        pygame.time.delay(teempo)
                                                                        self.screen.blit(imagem_acertou, (matriz_tela_player[tiro[0]][tiro[1]][0]-1,matriz_tela_player[tiro[0]][tiro[1]][1]-1))
									matriz_jogo_player[tiro[0]][tiro[1]] = 11
                                                                        contador_tiros_cpu += 1
								else:
                                                                        teempo = cria_tempo_cpu()
                                                                        pygame.time.delay(teempo)
									self.screen.blit(imagem_nada, (matriz_tela_player[tiro[0]][tiro[1]][0]-1,matriz_tela_player[tiro[0]][tiro[1]][1]-1))
									matriz_jogo_player[tiro[0]][tiro[1]] = 11									
								pygame.display.update()
							
							if matriz_jogo_com[quadrado_clicado[0]][quadrado_clicado[1]] <= 0:
								self.screen.blit(imagem_nada, (matriz_tela_com[quadrado_clicado[0]][quadrado_clicado[1]][0]-1,matriz_tela_com[quadrado_clicado[0]][quadrado_clicado[1]][1]-1))
								pygame.mixer.music.load(musicapath("agua.ogg"))  # Carrega som da agua
								pygame.mixer.music.queue(musicapath("menu.ogg"))
								pygame.mixer.music.play()
								pygame.display.update()
								matriz_jogo_com[quadrado_clicado[0]][quadrado_clicado[1]] = 11
								tiro = tiro_aleatorio(matriz_jogo_player)
							
								if matriz_jogo_player[tiro[0]][tiro[1]] <= 0:
                                                                        teempo = cria_tempo_cpu()
                                                                        pygame.time.delay(teempo)
									self.screen.blit(imagem_nada, (matriz_tela_player[tiro[0]][tiro[1]][0]-1,matriz_tela_player[tiro[0]][tiro[1]][1]-1))
									matriz_jogo_player[tiro[0]][tiro[1]] = 11
								
								elif matriz_jogo_player[tiro[0]][tiro[1]] > 0 and matriz_jogo_player[tiro[0]][tiro[1]] < 11:
                                                                        teempo = cria_tempo_cpu()
                                                                        pygame.time.delay(teempo)
									self.screen.blit(imagem_acertou, (matriz_tela_player[tiro[0]][tiro[1]][0]-1,matriz_tela_player[tiro[0]][tiro[1]][1]-1))
									matriz_jogo_player[tiro[0]][tiro[1]] = 11
                                                                        contador_tiros_cpu += 1
                                                                        print contador_tiros_cpu
								pygame.display.update()


                                                        if verifica_ganhador(contador_tiros_cpu,contador_tiros_player) == 'cpu':
                                                            self.screen.blit(imagem_ganhador_cpu,(0, 140))
                                                        if verifica_ganhador(contador_tiros_cpu,contador_tiros_player) == 'player':
                                                            self.screen.blit(imagem_ganhador_jogador,(0, 140))

					#=======================================	
