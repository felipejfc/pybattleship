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
	matriz_tela = {}
	x_tela = xtela
	for x in range(1,11):
		y_tela = ytela
		for y in range(1,11):
			matriz_tela[(x,y)] = (x_tela,y_tela)
			y_tela+=30
		x_tela += 30
			
	return matriz_tela
	
def verifica_quadrado_clicado(matriz_tela,evento):
	for chave,valor in matriz_tela.items():
		if evento.pos[0] >= valor[0] and evento.pos[0]<=valor[0]+30:
			if evento.pos[1] >= valor[1] and evento.pos[1]<=valor[1]+30:
				return chave	

def cria_matriz_de_barcos():
	#cria a matriz 10x10
	matriz = []
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
					matriz[x-1][y-1] = -1
				if y<9:
					matriz[x-1][y+1] = -1
				matriz[x-1][y] = -1
			if x<6:
				if y>0:
					matriz[x+4][y-1] = -1
				if y<9:
					matriz[x+4][y+1] = -1
				matriz[x+4][y] = -1
			for i in range(x,x+4):
				matriz[i][y]=4
				if y>0:
					matriz[i][y-1] = -1
				if y<9:
					matriz[i][y+1] = -1
		else:
			if y>0:
				if x>0:
					matriz[x-1][y-1] = -1
				if x<9:
					matriz[x+1][y-1] = -1
				matriz[x][y-1] = -1
			if y<6:
				if x>0:
					matriz[x-1][y+4] = -1
				if x<9:
					matriz[x+1][y+4] = -1
				matriz[x][y+4] = -1
			for i in range(y,y+4):
				matriz[x][i]=4		
				if x>0:
					matriz[x-1][i] = -1
				if x<9:
					matriz[x+1][i] = -1
		barco_criado = True
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
						matriz[x-1][y-1] = -1
					if y<9:
						matriz[x-1][y+1] = -1
					matriz[x-1][y] = -1
				if x<7:
					if y>0:
						matriz[x+3][y-1] = -1
					if y<9:
						matriz[x+3][y+1] = -1
					matriz[x+3][y] = -1
						
				for i in range(x,x+3):
					matriz[i][y]=3
					if y>0:
						matriz[i][y-1] = -1
					if y<9:
						matriz[i][y+1] = -1
					
			else:
				if y>0:
					if x>0:
						matriz[x-1][y-1] = -1
					if x<9:
						matriz[x+1][y-1] = -1
					matriz[x][y-1] = -1
				if y<7:
					if x>0:
						matriz[x-1][y+3] = -1
					if x<9:
						matriz[x+1][y+3] = -1
					matriz[x][y+3] = -1
				for i in range(y,y+3):
					matriz[x][i]=3	
					if x>0:
						matriz[x-1][i] = -1
					if x<9:
						matriz[x+1][i] = -1
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
						matriz[x-1][y-1] = -1
					if y<9:
						matriz[x-1][y+1] = -1
					matriz[x-1][y] = -1
				if x<8:
					if y>0:
						matriz[x+2][y-1] = -1
					if y<9:
						matriz[x+2][y+1] = -1
					matriz[x+2][y] = -1
						
				for i in range(x,x+2):
					matriz[i][y]=2
					if y>0:
						matriz[i][y-1] = -1
					if y<9:
						matriz[i][y+1] = -1
				
			else:
				if y>0:
					if x>0:
						matriz[x-1][y-1] = -1
					if x<9:
						matriz[x+1][y-1] = -1
					matriz[x][y-1] = -1
				if y<8:
					if x>0:
						matriz[x-1][y+2] = -1
					if x<9:
						matriz[x+1][y+2] = -1
					matriz[x][y+2] = -1
				for i in range(y,y+2):
					matriz[x][i]=2	
					if x>0:
						matriz[x-1][i] = -1
					if x<9:
						matriz[x+1][i] = -1			
			barco_criado = True
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
					matriz[x-1][y-1] = -1
				if y<9:
					matriz[x-1][y+1] = -1
				matriz[x-1][y] = -1
			if x<9:
				if y>0:
					matriz[x+1][y-1] = -1
				if y<9:
					matriz[x+1][y+1] = -1
				matriz[x+1][y] = -1
				
			if y>0:
				matriz[x][y-1] = -1
			if y<9:
				matriz[x][y+1] = -1
											
			matriz[x][y]=1
			barco_criado = True
		#cria 4 barcos de 1 pedacos======================	
	return matriz
