from pygame.locals import *
import menu
from functions import *  #importa as funcoes do functions.py

class Menu_sobre(object):
    
    def __init__(self,screen):
        
        dicionario_elementos_clicaveis_3 = {}
        
        self.screen = screen  #recebe screen do main.py     
        background_menu_3 = pygame.image.load(filepath("sobremenu.png")) #Carrega o Menu2
        
        botao_cancel   = pygame.image.load(filepath("menu2_button3.png")) #Carrega o botao 1
        botao_cancel_vermelho = pygame.image.load(filepath("menu2_button3_r.png")) #Carrega o botao 1
        
        
        dicionario_elementos_clicaveis_3[botao_cancel] = (293,330)
        botao_cancel_pressionado = False
        while True:              #Loop do menu, que pega os eventos.
            menu__ = 2
            for evento in pygame.event.get():
                botao_cancel_pressionado = False
                if evento.type == pygame.QUIT:
                    exit()
                if evento.type == MOUSEMOTION: #Verifica onde o ponteiro do mouse anda...
                    for key,value in dicionario_elementos_clicaveis_3.items():
                        if checkclick(value,key.get_size(),evento.pos) and key==botao_cancel:
                            botao_cancel_pressionado = True
                if evento.type == MOUSEBUTTONDOWN:
                    for key,value in dicionario_elementos_clicaveis_3.items():
                        if checkclick(value,key.get_size(),evento.pos) and key==botao_cancel:
                            menu.Menu(screen)
                            menu__ = 1
            
            if menu__<>2:
                break
        
        
            self.screen.blit(background_menu_3, (222, 140))
            if botao_cancel_pressionado:
                self.screen.blit(botao_cancel_vermelho, (293, 330))
            else:
                self.screen.blit(botao_cancel, (293, 330))
            pygame.display.flip()


        

