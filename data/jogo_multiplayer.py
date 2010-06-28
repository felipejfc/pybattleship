import pygame, sys, os
import socket
import thread
from pygame.locals import *
import menu
import menu2
from functions import *


class Jogomultiplayer(object):
    	def __init__(self,screen):
            self.screen = screen  #recebe screen do main.py
            campo = pygame.image.load(filepath("campo.png"))
            self.screen.blit(campo, (0, 0))
            #pygame.mixer.music.stop()

#============================Criação Socket=====================================
            HOST = ''              # Endereco IP do Servidor
            PORT = 5000            # Porta que o Servidor esta
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
            orig = (HOST, PORT)
            tcp.bind(orig) #abre o socket no ip e porta
            tcp.listen(1) #quantos ouvintes o socket vai ter

#============================Mapa da tela=======================================
            #matriz_tela_com = cria_mapa(330, 72)
            #matriz_jogo_com = cria_matriz_de_barcos()
            matriz_tela_player = cria_mapa(10,72)
            matriz_jogo_player = cria_matriz_de_barcos()
            #print matriz_jogo_com
#============================Carrega imagens====================================
            imagem_acertou = pygame.image.load(filepath("hitten.png"));
            imagem_nada = pygame.image.load(filepath("nada.png"));
            imagem_ganhador_cpu = pygame.image.load(filepath("perdeu.png"))
            imagem_ganhador_jogador = pygame.image.load(filepath("ganhou.png"))

            botao_sim = pygame.image.load(filepath("botao_sim.png"))
            botao_nao = pygame.image.load(filepath("botao_nao.png"))
#============================Cria dicionarios de elementos clicaveis============
            dicionario_elementos_clicaveis = {}
            dicionario_elementos_clicaveis[botao_sim] = (390,237)
            dicionario_elementos_clicaveis[botao_nao] = (420,237)
#===========================Contadores de tiros=================================
            #contador_tiros_cpu = 0
            contador_tiros_player = 0
#===========================Loop do jogo========================================
            while True:
                for evento in pygame.event.get():
                    print evento
                    if evento.type == pygame.QUIT:
                        exit()
#===========================Verifica quem ganhou o jogo=========================
                    if verifica_ganhador(contador_tiros_cpu,contador_tiros_player) == 'player':
                        self.screen.blit(imagem_ganhador_jogador,(0,140))
                        self.screen.blit(botao_sim, (390,223))
                        self.screen.blit(botao_nao, (440,222))
                        pygame.display.update()
                        if evento.type == MOUSEBUTTONDOWN: #Verifica onde o usurio clicou.
                            if evento.button == 1:
                                for key,value in dicionario_elementos_clicaveis.items():
                                    if checkclick(value,key.get_size(),evento.pos) and key==botao_sim:
                                        print 'FUNCIONA'
                                    if checkclick(value,key.get_size(),evento.pos) and key==botao_nao:
                                        menu.Menu(screen)


                    if verifica_ganhador(contador_tiros_cpu,contador_tiros_player) == 'cpu':
                        self.screen.blit(imagem_ganhador_cpu,(0, 140))
                        self.screen.blit(botao_sim, (390,223))
                        self.screen.blit(botao_nao, (440,222))
                        if evento.type == MOUSEBUTTONDOWN: #Verifica onde o usurio clicou.
                            if evento.button == 1:
                                for key,value in dicionario_elementos_clicaveis.items():
                                    if checkclick(value,key.get_size(),evento.pos) and key==botao_sim:
                                        print 'FUNCIONA'

                                    if checkclick(value,key.get_size(),evento.pos) and key==botao_nao:
                                        menu.Menu(screen)
                        pygame.display.update()
#=====================================             =============================
                    if evento.type == MOUSEBUTTONDOWN: #Verifica onde o usuario clicou.
                        if evento.button == 1:
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
                                    tiro = 'MENSAGEM RECEBIDA DO OUTRO PLAYER'
                                        if matriz_jogo_player[tiro[0]][tiro[1]] > 0 and matriz_jogo_player[tiro[0]][tiro[1]] < 11:
                                            self.screen.blit(imagem_acertou, (matriz_tela_player[tiro[0]][tiro[1]][0]-1,matriz_tela_player[tiro[0]][tiro[1]][1]-1))
                                            matriz_jogo_player[tiro[0]][tiro[1]] = 11
                                            contador_tiros_cpu += 1

                                        else:
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
                                    tiro = 'MENSAGEM RECEBIDA DO OUTRO PLAYER'

                                        if matriz_jogo_player[tiro[0]][tiro[1]] <= 0:
                                            self.screen.blit(imagem_nada, (matriz_tela_player[tiro[0]][tiro[1]][0]-1,matriz_tela_player[tiro[0]][tiro[1]][1]-1))
                                            matriz_jogo_player[tiro[0]][tiro[1]] = 11

                                        elif matriz_jogo_player[tiro[0]][tiro[1]] > 0 and matriz_jogo_player[tiro[0]][tiro[1]] < 11:
                                            self.screen.blit(imagem_acertou, (matriz_tela_player[tiro[0]][tiro[1]][0]-1,matriz_tela_player[tiro[0]][tiro[1]][1]-1))
                                            matriz_jogo_player[tiro[0]][tiro[1]] = 11
                                            contador_tiros_cpu += 1
                                        pygame.display.update()

