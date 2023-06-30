import pygame

class Caja:
    def __init__(self, x, y, width, height, image_path):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hitbox = pygame.Rect(x, y, width, height)
        self.solido = True 

        # ----------- HITBOX ----------- #
        self.hitbox = pygame.Rect(x, y, width, height)

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect.topleft)
        # pygame.draw.rect(pantalla, self.color, self.rect)

    def actualizar(self):
        # Lógica de actualización de la caja si es necesaria
        pass

cajas_nivel1 = [
    Caja(315, 1010, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(230, 1000, 60, 60, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(600, 1000, 70, 70, "Recursos\Super Grotto Escape Files\Props\Sprites\\big-crate.png"),
    # Agrega más objetos de caja según tus necesidades
]