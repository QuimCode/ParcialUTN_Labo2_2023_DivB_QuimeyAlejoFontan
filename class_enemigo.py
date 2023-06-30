import pygame

from parametros_visual import *

class Enemigo:
    def __init__(self, x, y, width, height, coordenada_inicial, coordenada_final, velocidad):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocidad = 3  # Velocidad de movimiento del enemigo

        self.imagen = pygame.image.load("Recursos\Modelos\PNG Enemigo Respiracion\Iddle1.png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (width, height))
        # self.imagen = pygame.Surface((width, height))
        # self.imagen.fill((255, 0, 0))  # Color de fondo temporal para representar al enemigo

        self.salto = False
        self.salto_velocidad = 0

        self.solido = True 
        self.visible = True
        self.activo = True

        self.coordenada_inicial = coordenada_inicial
        self.coordenada_final = coordenada_final
        self.velocidad = velocidad
        self.direccion = 1

        hitbox_width = 0.8 * width
        hitbox_height = 0.8 * height
        hitbox_x = x + (width - hitbox_width) / 2
        hitbox_y = y + (height - hitbox_height) / 2
        self.hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def mover(self):
        # Lógica de movimiento del enemigo
        if self.salto:
            self.y -= self.salto_velocidad
            self.salto_velocidad -= 1
        else:
            self.y += 8  # Aplicar gravedad

        # Limitar la posición del enemigo dentro de los límites de la pantalla
        if self.x < 0:
            self.x = 0
        elif self.x > ANCHO - self.width:
            self.x = ANCHO - self.width

        if self.y < 0:
            self.y = 0
        elif self.y > ALTO - self.height:
            self.y = ALTO - self.height
            self.salto = False
            self.salto_velocidad = 0

        self.x += self.direccion * self.velocidad

        if self.x <= self.coordenada_inicial or self.x + self.width >= self.coordenada_final:
            self.direccion *= -1

        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def saltar(self):
        if not self.salto:
            self.salto = True
            self.salto_velocidad = 20

    def actualizar(self):
        self.mover()

        # Actualizar posición del hitbox
        self.hitbox.x = self.x + (self.width - self.hitbox.width) / 2
        self.hitbox.y = self.y + (self.height - self.hitbox.height) / 2

enemigos_nivel1 = [ Enemigo(1500, 1010, 60, 60, 1500, 1900, 5),
                    Enemigo(1000, 1010, 60, 60, 1000, 1500, 5)
]