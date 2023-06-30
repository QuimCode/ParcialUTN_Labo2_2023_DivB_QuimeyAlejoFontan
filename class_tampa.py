import pygame

from class_enemigo import Enemigo

class Trampa(Enemigo):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)


trampas_nivel_1 = [ Trampa(x=100, y=200, width=50, height=50),
                    Trampa(x=300, y=150, width=50, height=50),
                    Trampa(x=500, y=250, width=50, height=50),
                    Trampa(x=700, y=200, width=50, height=50)]