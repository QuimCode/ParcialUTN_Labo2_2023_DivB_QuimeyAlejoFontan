import pygame

class Trampa:
    def __init__(self, posicion, radio):
        self.image = pygame.image.load("Recursos\Modelos\PNG Objetos\Botella.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (radio*2, radio*2))
        self.rect = self.image.get_rect(center=posicion)
        self.hitbox = self.rect.inflate(-10, -10)  # Ajusta el tamaño de la hitbox
        
    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)
        
    def colision(self, rect_jugador):
        return self.hitbox.colliderect(rect_jugador)
    
trampas_nivel1 = [
    Trampa((620, 1050), 20),
    Trampa((680, 1050), 20),
    Trampa((1380, 1050), 20),
]