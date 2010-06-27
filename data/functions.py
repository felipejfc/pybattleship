import pygame, sys, os
from pygame.locals import *
import random

import os

data_py = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.normpath(os.path.join(data_py, 'images'))
som_py = os.path.abspath(os.path.dirname(__file__))
som_dir = os.path.normpath(os.path.join(som_py, 'som'))

def filepath(nome_arquivo):
    return os.path.join(data_dir, nome_arquivo)

def musicapath(nome_arquivo):
    return os.path.join(som_dir, nome_arquivo)
    
def checkclick(posicao_objeto,tamanho_objeto,posicao_click):
	if posicao_click[0]>=posicao_objeto[0] and posicao_click[0]<=posicao_objeto[0]+tamanho_objeto[0]:
		if posicao_click[1]>=posicao_objeto[1] and posicao_click[1] <= posicao_objeto[1]+tamanho_objeto[1]:
			return True
	return False


def cria_mapa(xtela, ytela):
	#matriz_tela = {}
	matriz_tela = []
	for i in range(10):
		matriz_tela.append([0,0,0,0,0,0,0,0,0,0])
	x_tela = xtela
	for x in range(10):
		y_tela = ytela
		for y in range(10):
			matriz_tela[x][y] = (x_tela,y_tela)
			y_tela+=30
		x_tela += 30
			
	return matriz_tela
	
def verifica_quadrado_clicado(matriz_tela,evento):
	for i in range(10):
		for j in range(10):
			if evento.pos[0] >= matriz_tela[i][j][0] and evento.pos[0]<=matriz_tela[i][j][0]+30:
				if evento.pos[1] >= matriz_tela[i][j][1] and evento.pos[1]<=matriz_tela[i][j][1]+30:
					return (i,j)	
def cria_tempo_cpu():
    tempo = random.randint(2000,4000) #cria um numero para ser usado no tempo entre 2s e 4s
    return tempo

def verifica_ganhador(tiro_cpu,tiro_player):
    if tiro_cpu == 20:
        return 'cpu'
    if tiro_player == 20:
        return 'player'

def tiro_aleatorio(matriz):
	atirou = False
	while not atirou:
		x = random.randint(0,9)
		y = random.randint(0,9)
		if matriz[x][y]<11:
			atirou = True
	return (x,y)

def cria_matriz_de_barcos():
	#cria a matriz 10x10
	matriz = []
	numero_barco = 1
	for i in range(10):
		matriz.append([0,0,0,0,0,0,0,0,0,0])
	#cria barco de 4 pedacos=======================
	barco_criado = False
	while not barco_criado:
		deitado = random.randint(0,1) #define se barco vai ser criado na vertical ou horizontal
		x = random.randint(0,9)
		y = random.randint(0,9)
		if (deitado and x>6) or (not deitado and y>6): #verifica se o barco pode ser criado dentro dos limites do campo
			continue
		if deitado:
			if x>0:
				if y>0:
					matriz[x-1][y-1] = -numero_barco
				if y<9:
					matriz[x-1][y+1] = -numero_barco
				matriz[x-1][y] = -numero_barco
			if x<6:
				if y>0:
					matriz[x+4][y-1] = -numero_barco
				if y<9:
					matriz[x+4][y+1] = -numero_barco
				matriz[x+4][y] = -numero_barco
			for i in range(x,x+4):
				matriz[i][y]=numero_barco
				if y>0:
					matriz[i][y-1] = -numero_barco
				if y<9:
					matriz[i][y+1] = -numero_barco
		else:
			if y>0:
				if x>0:
					matriz[x-1][y-1] = -numero_barco
				if x<9:
					matriz[x+1][y-1] = -numero_barco
				matriz[x][y-1] = -numero_barco
			if y<6:
				if x>0:
					matriz[x-1][y+4] = -numero_barco
				if x<9:
					matriz[x+1][y+4] = -numero_barco
				matriz[x][y+4] = -numero_barco
			for i in range(y,y+4):
				matriz[x][i]=numero_barco		
				if x>0:
					matriz[x-1][i] = -numero_barco
				if x<9:
					matriz[x+1][i] = -numero_barco
		barco_criado = True
		numero_barco+=1
	#cria barco de 4 pedacos=======================
	#cria 2 barcos de 3 pedacos======================
	for i in range(2):
		barco_criado = False
		while not barco_criado:
			deitado = random.randint(0,1) #define se barco vai ser criado na vertical ou horizontal
			x = random.randint(0,9)
			y = random.randint(0,9)
			
			if (deitado and x>7) or (not deitado and y>7): #verifica se o barco pode ser criado dentro dos limites do campo
				continue
			
			try:
				if deitado and matriz[x][y]<>0 or matriz[x+1][y]<>0 or matriz[x+2][y]<>0:
					continue 	
				if not deitado and matriz[x][y]<>0 or matriz[x][y+1]<>0 or matriz[x][y+2]<>0:
					continue
			except:
				continue
			
			if deitado:
				if x>0:
					if y>0:
						matriz[x-1][y-1] = -numero_barco
					if y<9:
						matriz[x-1][y+1] = -numero_barco
					matriz[x-1][y] = -numero_barco
				if x<7:
					if y>0:
						matriz[x+3][y-1] = -numero_barco
					if y<9:
						matriz[x+3][y+1] = -numero_barco
					matriz[x+3][y] = -numero_barco
						
				for i in range(x,x+3):
					matriz[i][y]=numero_barco
					if y>0:
						matriz[i][y-1] = -numero_barco
					if y<9:
						matriz[i][y+1] = -numero_barco
					
			else:
				if y>0:
					if x>0:
						matriz[x-1][y-1] = -numero_barco
					if x<9:
						matriz[x+1][y-1] = -numero_barco
					matriz[x][y-1] = -numero_barco
				if y<7:
					if x>0:
						matriz[x-1][y+3] = -numero_barco
					if x<9:
						matriz[x+1][y+3] = -numero_barco
					matriz[x][y+3] = -numero_barco
				for i in range(y,y+3):
					matriz[x][i]=numero_barco	
					if x>0:
						matriz[x-1][i] = -numero_barco
					if x<9:
						matriz[x+1][i] = -numero_barco
			numero_barco+=1
			barco_criado = True
		#cria barco de 3 pedacos=======================
		#cria 3 barcos de 2 pedacos======================
	for i in range(3):
		barco_criado = False
		while not barco_criado:
			deitado = random.randint(0,1) #define se barco vai ser criado na vertical ou horizontal
			x = random.randint(0,9)
			y = random.randint(0,9)
			
			if (deitado and x>8) or (not deitado and y>8): #verifica se o barco pode ser criado dentro dos limites do campo
				continue
			
			try:
				if deitado and matriz[x][y]<>0 or matriz[x+1][y]<>0:
					continue 	
				if not deitado and matriz[x][y]<>0 or matriz[x][y+1]<>0:
					continue
			except:
				continue
			if deitado:
				if x>0:
					if y>0:
						matriz[x-1][y-1] = -numero_barco
					if y<9:
						matriz[x-1][y+1] = -numero_barco
					matriz[x-1][y] = -numero_barco
				if x<8:
					if y>0:
						matriz[x+2][y-1] = -numero_barco
					if y<9:
						matriz[x+2][y+1] = -numero_barco
					matriz[x+2][y] = -numero_barco
						
				for i in range(x,x+2):
					matriz[i][y]=numero_barco
					if y>0:
						matriz[i][y-1] = -numero_barco
					if y<9:
						matriz[i][y+1] = -numero_barco
				
			else:
				if y>0:
					if x>0:
						matriz[x-1][y-1] = -numero_barco
					if x<9:
						matriz[x+1][y-1] = -numero_barco
					matriz[x][y-1] = -numero_barco
				if y<8:
					if x>0:
						matriz[x-1][y+2] = -numero_barco
					if x<9:
						matriz[x+1][y+2] = -numero_barco
					matriz[x][y+2] = -numero_barco
				for i in range(y,y+2):
					matriz[x][i]=numero_barco	
					if x>0:
						matriz[x-1][i] = -numero_barco
					if x<9:
						matriz[x+1][i] = -numero_barco			
			barco_criado = True
			numero_barco+=1
		#cria 3 barcos de 2 pedacos======================
		#cria 4 barcos de 1 pedacos======================
	for i in range(4):
		barco_criado = False
		while not barco_criado:
			x = random.randint(0,9)
			y = random.randint(0,9)
			
			try:
				if matriz[x][y]<>0:
					continue 
			except:
				continue

			if x>0:
				if y>0:
					matriz[x-1][y-1] = -numero_barco
				if y<9:
					matriz[x-1][y+1] = -numero_barco
				matriz[x-1][y] = -numero_barco
			if x<9:
				if y>0:
					matriz[x+1][y-1] = -numero_barco
				if y<9:
					matriz[x+1][y+1] = -numero_barco
				matriz[x+1][y] = -numero_barco
				
			if y>0:
				matriz[x][y-1] = -numero_barco
			if y<9:
				matriz[x][y+1] = -numero_barco
											
			matriz[x][y]=numero_barco
			barco_criado = True
			numero_barco+=1
		#cria 4 barcos de 1 pedacos======================	
	return matriz
