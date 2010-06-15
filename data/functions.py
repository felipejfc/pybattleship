import pygame, sys, os
from pygame.locals import *

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
