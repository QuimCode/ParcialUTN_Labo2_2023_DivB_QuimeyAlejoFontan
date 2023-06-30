import pygame

from class_jugador import ganar_vida

class ObjetoCura:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.activo = False
        self.color = (0, 255, 0)  # Color verde
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False

    def dibujar(self, pantalla):
        if self.activo:
            pygame.draw.rect(pantalla, self.color, self.rect)
