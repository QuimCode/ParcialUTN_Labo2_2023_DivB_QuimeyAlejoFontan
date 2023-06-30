import pygame
import sys

from parametros_visual import *
from class_enemigo import enemigos_nivel1
from class_jugador import Personaje
from class_caja import cajas_nivel1
from class_juego import Juego
from class_plataforma import plataformas_nivel1
from parametros_sonido import reproducir_musica_nivel1
from parametros_colisiones import verificar_colisiones

pygame.init()

reloj = pygame.time.Clock()


def mostrar_puntos(pantalla, puntos, tiempo_restante, vida, oportunidades_revivir):
    fuente = pygame.font.Font(None, 36)
    texto_puntos = fuente.render("Puntos: " + str(puntos), True, (255, 255, 255))
    texto_tiempo = fuente.render("Tiempo: " + str(tiempo_restante), True, (255, 255, 255))
    texto_vida = fuente.render("Vida: " + str(vida), True, (255, 255, 255))
    texto_vidas_generales = fuente.render("Vidas Generales: " + str(oportunidades_revivir), True, (255, 255, 255))

    pantalla.blit(texto_puntos, (10, 10))
    pantalla.blit(texto_tiempo, (10, 40))
    pantalla.blit(texto_vida, (10, 70))
    pantalla.blit(texto_vidas_generales, (10, 100))


def nivel_1(tiempo_total):
    nivel = True

    reproducir_musica_nivel1()
    fondo_de_nivel = fondo_nivel1()

    Jugador = Personaje(10, 850, 100, 100)

    plataformas_del_nivel = plataformas_nivel1
    cajas_del_nivel = cajas_nivel1

    tiempo_inicial = pygame.time.get_ticks()  # tiempo inicial

    while nivel:
        frames.tick(FPS)
        teclas = pygame.key.get_pressed()
        Jugador.mover(teclas)

        verificar_colisiones(Jugador, plataformas_nivel1, cajas_nivel1, enemigos_nivel1, teclas)

        Jugador.actualizar_animacion()
        Jugador.perder_vida()

        tiempo_transcurrido = pygame.time.get_ticks() - tiempo_inicial  # milisegundos
        tiempo_restante = tiempo_total - tiempo_transcurrido // 1000  # convertir a segundos



        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Clic izquierdo del mouse
                    pos_mouse = pygame.mouse.get_pos()
                    print(f"Posición del clic: ({pos_mouse[0]}, {pos_mouse[1]})")

        tiempo_restante -= 1
        if tiempo_restante <= 0:
            tiempo_restante = 0

        PANTALLA.fill(Colores.NEGRO.value)
        PANTALLA.blit(fondo_de_nivel, (0, 0))

        for plataforma in plataformas_del_nivel:
            plataforma.dibujar(PANTALLA)
            plataforma.actualizar()

        for caja in cajas_del_nivel:
            caja.dibujar(PANTALLA)
            caja.actualizar()

        for enemigo in enemigos_nivel1:
            if enemigo.activo:
                enemigo.dibujar(PANTALLA)
                enemigo.mover()

        Jugador.dibujar(PANTALLA)
        mostrar_puntos(PANTALLA, Jugador.puntos, tiempo_restante, Jugador.vida, Jugador.oportunidades_revivir)
        pygame.display.flip()


def iniciar_nivel1():
    pygame.display.set_caption("Microcentro: Un Viaje de Ida - Cap.1")
    tiempo_total = 40  # Tiempo total para el nivel
    nivel_1(tiempo_total)
