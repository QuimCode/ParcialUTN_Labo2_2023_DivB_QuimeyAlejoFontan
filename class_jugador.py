import pygame

# from utilidades import reiniciar_nivel
from parametros_visual import *

class Personaje:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocidad = 5  # Velocidad de movimiento 
        self.salto = False  #  está saltando
        self.salto_velocidad = 20  # Velocidad de salto 
        self.doble_salto_disponible = True

        self.imagen = self.obtener_imagen_animacion_quieto()[0]
        self.indice_animacion = 0
        self.contador_animacion = 0
        self.movimiento_derecha = False
        self.movimiento_izquierda = False
        self.movimiento_quieto = True

        self.puntos = 0
        self.vida = 100
        self.dano_enemigo = 50
        self.oportunidades_revivir = 3
        self.tiempo_entre_danos = 1000  # Retardo en milisegundos
        self.ultimo_dano = pygame.time.get_ticks()  # Momento en que se recibió el último daño

    # ----------- HITBOX ----------- #
        hitbox_width = 0.8 * self.width
        hitbox_height = 0.8 * self.height
        hitbox_x = self.x + (self.width - hitbox_width) / 2
        hitbox_y = self.y + (self.height - hitbox_height) / 2
        self.hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)
        # self.hitbox_izquierda = pygame.Rect(self.x, self.y, 0.1, self.height)
        # self.hitbox_derecha = pygame.Rect(self.x + self.width - 0.1, self.y, 0.1, self.height)
        # self.hitbox_superior = pygame.Rect(self.x, self.y, self.width, 0.1)
        # self.hitbox_inferior = pygame.Rect(self.x, self.y + self.height - 0.1, self.width, 0.1)

    def obtener_imagen_animacion_derecha(self):
        return [
        pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x48.png"), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x49.png"), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x50.png"), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x51.png"), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x52.png"), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x53.png"), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x54.png"), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x55.png"), (self.width, self.height))
    ]

    def obtener_imagen_animacion_izquierda(self):
            return [pygame.transform.flip(img, True, False) for img in self.obtener_imagen_animacion_derecha()]

    def obtener_imagen_animacion_quieto(self): 
            return [
        pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x48.png'), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x48.png'), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x49.png'), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x50.png'), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x51.png'), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x52.png'), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x53.png'), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x54.png'), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x55.png'), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x56.png'), (self.width, self.height)),
        pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x57.png'), (self.width, self.height))
    ]

    def actualizar_animacion(self):
        self.contador_animacion += 1
        if self.contador_animacion >= VELOCIDAD_ANIMACION:
            self.contador_animacion = 0
            self.indice_animacion += 1
            if self.movimiento_derecha:
                animaciones = self.obtener_imagen_animacion_derecha()
            elif self.movimiento_izquierda:
                animaciones = self.obtener_imagen_animacion_izquierda()
            else:
                animaciones = self.obtener_imagen_animacion_quieto()

            if self.indice_animacion >= len(animaciones):
                self.indice_animacion = 0

            self.imagen = animaciones[self.indice_animacion]

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

        # if self.movimiento_derecha:                                                  #YA NO SIRVE
        #     imagen_jugador = obtener_imagen_animacion_derecha()
        # elif self.movimiento_izquierda:
        #     imagen_jugador = obtener_imagen_animacion_izquierda()
        # else:
        #     imagen_jugador = obtener_imagen_animacion_quieto()

        # pygame.draw.rect(pantalla, (255, 50, 0), self.hitbox)                        #PINTA LIMITES HITBOX
        # pygame.draw.rect(pantalla, (125, 255, 0), self.hitbox_izquierda)
        # pygame.draw.rect(pantalla, (0, 255, 200), self.hitbox_derecha)
        # pygame.draw.rect(pantalla, (20, 255, 0), self.hitbox_superior)
        # pygame.draw.rect(pantalla, (0, 255, 80), self.hitbox_inferior)


    #----------------------MOVIMIENTO#----------------------#
    def mover(self, teclas):
        if teclas[pygame.K_a]:
            self.x -= self.velocidad
            self.movimiento_izquierda = True
            self.movimiento_derecha = False
            self.movimiento_quieto = False
        elif teclas[pygame.K_d]:
            self.x += self.velocidad
            self.movimiento_izquierda = False
            self.movimiento_derecha = True
            self.movimiento_quieto = False
        else:
            self.movimiento_izquierda = False
            self.movimiento_derecha = False
            self.movimiento_quieto = True
        
        # SALTO
        if teclas[pygame.K_w]:
            if not self.salto:
                self.salto = True
                self.salto_velocidad = 20

        # GRAVEDAD
        if self.salto:
            self.y -= self.salto_velocidad
            self.salto_velocidad -= 1

        # LIMITES
        if self.x < 0:
            self.x = 0
        elif self.x > ANCHO - self.width:
            self.x = ANCHO - self.width

        if self.y < 0:
            self.y = 0
        elif self.y > ALTO - self.height:
            self.y = ALTO - self.height
            self.salto = False

    # REFRESH HITBOX
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hitbox_izquierda = pygame.Rect(self.x, self.y, 1, self.height)
        self.hitbox_derecha = pygame.Rect(self.x + self.width - 1, self.y, 1, self.height)
        self.hitbox_superior = pygame.Rect(self.x, self.y, self.width, 1)
        self.hitbox_inferior = pygame.Rect(self.x, self.y + self.height - 1, self.width, 1)

    def recibir_dano(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_dano >= self.tiempo_entre_danos:
            self.vida -= self.dano_enemigo
            self.ultimo_dano = tiempo_actual

    def perder_vida(self):
        if self.vida <= 0:
            if self.oportunidades_revivir > 0:
                self.x = 10  # Posición x inicial
                self.y = 850  # Posición y inicial
                self.vida = 100  # Vida inicial
                self.oportunidades_revivir -= 1

            # elif self.vida <= 0 and self.oportunidades_revivir == 0:
            #             reiniciar_nivel()

    def ganar_vida(self):
        self.vida += 50