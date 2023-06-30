# import pygame

# # Velocidad de la animación (número de actualizaciones antes de cambiar de imagen)
# VELOCIDAD_ANIMACION = 5

# contador_animacion = 0
# indice_animacion = 0

# jugador_animacion_derecha = [
#     pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x48.png"), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x49.png"), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x50.png"), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x51.png"), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x52.png"), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x53.png"), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x54.png"), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x55.png"), (Personaje.width, Personaje.height))
# ]

# jugador_animacion_izquierda = [pygame.transform.flip(img, True, False) for img in jugador_animacion_derecha]

# jugador_animacion_quieto = [
#     pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x48.png'), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x48.png'), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x49.png'), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x50.png'), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x51.png'), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x52.png'), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x53.png'), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x54.png'), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x55.png'), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x56.png'), (Personaje.width, Personaje.height)),
#     pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x57.png'), (Personaje.width, Personaje.height))
# ]

# def actualizar_animacion(personaje):
#     global contador_animacion, indice_animacion
    
#     contador_animacion += 1
#     if contador_animacion >= VELOCIDAD_ANIMACION:
#         contador_animacion = 0
#         indice_animacion += 1
#         if indice_animacion >= len(jugador_animacion_derecha):
#             indice_animacion = 0

#     if personaje.movimiento_derecha:
#         personaje.imagen = jugador_animacion_derecha[indice_animacion]
#     elif personaje.movimiento_izquierda:
#         personaje.imagen = jugador_animacion_izquierda[indice_animacion]
#     else:
#         personaje.imagen = jugador_animacion_quieto[indice_animacion]
