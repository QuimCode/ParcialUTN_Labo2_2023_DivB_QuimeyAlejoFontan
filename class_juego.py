import pygame

class Juego:
    def __init__(self):
        self.objetos_curacion1 = []

        # if self.Jugador.puntos == 1:
            # objeto_curacion = ObjetoCuracion(500, 900, 30, 30)  # Ajusta los valores adecuados
            # self.objetos_curacion.append(objeto_curacion)

    # def verificar_colisiones(self):
    #     for objeto_curacion in self.objetos_curacion:
    #         if objeto_curacion.activo and objeto_curacion.rect.colliderect(self.jugador.hitbox):
    #             self.jugador.ganar_vida()
    #             objeto_curacion.desactivar()
    #             self.objetos_curacion.remove(objeto_curacion)