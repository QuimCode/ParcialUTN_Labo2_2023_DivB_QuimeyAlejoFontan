# class_plataforma.py

import pygame

class Plataforma:
    def __init__(self, x, y, width, height, image_path):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))


        hitbox_width = 0.6 * width
        hitbox_height = 0.8 * height
        hitbox_x = x + (width - hitbox_width) / 2
        hitbox_y = y + (height - hitbox_height) / 2


        # ----------- HITBOX ----------- #
        self.hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)
        # self.hitbox_left = pygame.Rect(x, y, 0.5, height)
        # self.hitbox_right = pygame.Rect(x + width - 0.5, y, 0.5, height)
        # self.hitbox_top = pygame.Rect(x, y, width, 0.5)
        # self.hitbox_bottom = pygame.Rect(x, y + height - 0.5, width, 0.5)

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect.topleft)
        # pygame.draw.rect(pantalla, self.color, self.rect)
        # pygame.draw.rect(pantalla, (255, 0, 0), self.hitbox_left)
        # pygame.draw.rect(pantalla, (255, 0, 0), self.hitbox_right)
        # pygame.draw.rect(pantalla, (255, 0, 0), self.hitbox_top)
        # pygame.draw.rect(pantalla, (255, 0, 0), self.hitbox_bottom)

    def actualizar(self):
        # Lógica de actualización de la plataforma si es necesaria
        pass

# Crear objetos de plataforma
plataformas_nivel1 = [
    Plataforma(453, 627, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(82, 720, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(449, 903, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(884, 825, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(874, 525, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(1205, 418, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(421, 627, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(1369, 766, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(1607, 395, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(587, 336, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(123, 163, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(1077, 173, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
]

        # pygame.draw.rect(pantalla, self.color, self.rect)
        # pygame.draw.rect(pantalla, (255, 0, 0), self.hitbox_left)
        # pygame.draw.rect(pantalla, (255, 0, 0), self.hitbox_right)
        # pygame.draw.rect(pantalla, (255, 0, 0), self.hitbox_top)
        # pygame.draw.rect(pantalla, (255, 0, 0), self.hitbox_bottom)