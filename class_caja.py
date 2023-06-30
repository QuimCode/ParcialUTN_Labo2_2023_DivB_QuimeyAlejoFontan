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
        pass

cajas_nivel1 = [
    Caja(315, 1010, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1140, 800, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1380, 800, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(370, 1010, 60, 60, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(788, 1010, 70, 70, "Recursos\Super Grotto Escape Files\Props\Sprites\\big-crate.png"),
    Caja(1105, 850, 70, 70, "Recursos\Super Grotto Escape Files\Props\Sprites\\big-crate.png"),
    # Agrega más objetos 
]