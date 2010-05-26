import pygame, sys, os
from pygame.locals import *

import os

data_py = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.normpath(os.path.join(data_py, 'images'))

def filepath(filename):
    return os.path.join(data_dir, filename)
    
def checkclick(posobj,sizeobj,posclick):
	if posclick[0]>=posobj[0] and posclick[0]<=posobj[0]+sizeobj[0]:
		if posclick[1]>=posobj[1] and posclick[1] <= posobj[1]+sizeobj[1]:
			return True
	return False
		
#image.get_size
