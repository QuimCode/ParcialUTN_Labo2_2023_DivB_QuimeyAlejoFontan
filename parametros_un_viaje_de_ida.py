##-------------MODULOS-------------##

import pygame
import sys

##-------------ARCHIVOS-------------##

from parametros_visual import *
from parametros_nivel1 import iniciar_nivel1
from parametros_sonido import reproducir_musica_menu

##-------------CODIGO-------------##

def mostrar_menu():
    menu = True 

    pygame.init()
    pygame.display.set_caption("Microcentro un viaje de ida - Menu")

    fondo_del_menu = fondo_menu() # Debe ser una guardado como una variable, ya que no se puede pasar como funcion en el blit
    reproducir_musica_menu() 

    while menu:
        frames.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif evento.key == pygame.K_RETURN:
                    iniciar_nivel1()

        PANTALLA.fill(Colores.NEGRO.value)
        PANTALLA.blit(fondo_del_menu, (0, 0))
        pygame.display.flip()

mostrar_menu()