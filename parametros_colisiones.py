import pygame

def verificar_colisiones(jugador, plataformas, cajas, enemigos, trampas, teclas):
    jugador_colisionado = False

    for plataforma in plataformas:
        if jugador.hitbox.colliderect(plataforma.hitbox):
            # Verificar colisión desde abajo 
            if jugador.hitbox_inferior.colliderect(plataforma.hitbox):
                jugador.y = plataforma.rect.y - jugador.height - 1
                jugador.salto = False
                jugador.salto_velocidad = 0
            # Verificar colisión desde arriba 
            elif jugador.hitbox_superior.colliderect(plataforma.hitbox):
                jugador.y = plataforma.rect.y + plataforma.rect.height + 0.5
                jugador.salto_velocidad = 0
                jugador_colisionado = True
            # Verificar colisión desde los lados 
            elif jugador.hitbox_izquierda.colliderect(plataforma.hitbox) or jugador.hitbox_derecha.colliderect(plataforma.hitbox):
                if jugador.hitbox_izquierda.colliderect(plataforma.hitbox) and teclas[pygame.K_a]:
                    if jugador.hitbox_inferior.colliderect(plataforma.hitbox):
                        jugador.y = plataforma.rect.y - jugador.height - 0.5
                        jugador.x += jugador.velocidad
                elif jugador.hitbox_derecha.colliderect(plataforma.hitbox) and teclas[pygame.K_d]:
                    if jugador.hitbox_inferior.colliderect(plataforma.hitbox):
                        jugador.y = plataforma.rect.y - jugador.height - 0.5
                        jugador.x -= jugador.velocidad

    for caja in cajas:
        if jugador.hitbox.colliderect(caja.hitbox):
            if caja.solido:
                # Verificar colisión desde abajo, arriba y los lados
                if jugador.hitbox_inferior.colliderect(caja.hitbox):
                    jugador.y = caja.rect.y - jugador.height - 1
                    jugador.salto = False
                    jugador.salto_velocidad = 0
                elif jugador.hitbox_superior.colliderect(caja.hitbox):
                    jugador.y = caja.rect.y + caja.rect.height + 0.5
                    jugador.salto_velocidad = 0
                    jugador_colisionado = True
                else:
                    if jugador.hitbox_izquierda.colliderect(caja.hitbox) and teclas[pygame.K_a]:
                        jugador.y = caja.rect.y - jugador.height - 0.5
                        jugador.x += jugador.velocidad
                        jugador.direccion_colision = "izquierda"
                        print("Colisión en el lado izquierdo")
                    elif jugador.hitbox_derecha.colliderect(caja.hitbox) and teclas[pygame.K_d]:
                        jugador.y = caja.rect.y - jugador.height - 0.5
                        jugador.x -= jugador.velocidad
                        jugador.direccion_colision = "derecha"
                        print("Colisión en el lado derecho")
            else:
                # Permitir que el personaje camine encima de la caja sin colisionar
                jugador.y = caja.rect.y - jugador.height
                jugador.direccion_colision = None

    for enemigo in enemigos:
        if jugador.hitbox.colliderect(enemigo.hitbox):
            # Verificar colisiones con enemigos
            if enemigo.solido:
                # Verificar colisión desde abajo, arriba y los lados
                if jugador.salto and jugador.hitbox_inferior.colliderect(enemigo.hitbox):
                    jugador.puntos += 1
                    print("Punto ganado:", jugador.puntos)
                    enemigo.activo = False
                    enemigo.eliminado = True

                if jugador.rect.right > enemigo.rect.left:
                    jugador.recibir_dano()
                    jugador.perder_vida()
                elif jugador.rect.left < enemigo.rect.right:
                    jugador.recibir_dano()
                    jugador.perder_vida()

                if jugador.hitbox_inferior.colliderect(enemigo.hitbox):
                    jugador.y = enemigo.rect.y - jugador.height - 1
                    jugador.salto = False 
                    jugador.salto_velocidad = 0

                elif jugador.hitbox_superior.colliderect(enemigo.hitbox):
                    jugador.y = enemigo.rect.y + enemigo.rect.height + 0.5
                    jugador.salto_velocidad = 0

    for trampa in trampas:
        if jugador.hitbox.colliderect(trampa.hitbox):
            jugador.recibir_dano()
            jugador.perder_vida()
            print("¡Has sido atrapado por una trampa!")


    if not jugador_colisionado:
        # Aplicar gravedad si el jugador no está colisionando
        jugador.y += 8

    # for objeto_curacion in objetos_curacion:
    #     if objeto_curacion.activo and jugador.hitbox.colliderect(objeto_curacion.rect):
    #         jugador.ganar_vida()
    #         objeto_curacion.desactivar()

        # # Verificar colisión izquierda 
        # if jugador.hitbox_izquierda.colliderect(plataforma.hitbox):
        #     jugador.x = plataforma.rect.right
        # # Verificar colisión desde derecha 
        # elif jugador.hitbox_derecha.colliderect(plataforma.hitbox):
        #     jugador.x = plataforma.rect.left - jugador.width



    #             else:
    #                 if jugador.hitbox_izquierda.colliderect(enemigo.hitbox) and teclas[pygame.K_a]:
    #                     jugador.y = enemigo.rect.y - jugador.height - 0.5
    #                     jugador.x += jugador.velocidad
    #                     jugador.direccion_colision = "izquierda"
    #                     print("Colisión en el lado izquierdo con enemigo")
    #                 elif jugador.hitbox_derecha.colliderect(enemigo.hitbox) and teclas[pygame.K_d]:
    #                     jugador.y = enemigo.rect.y - jugador.height - 0.5
    #                     jugador.x -= jugador.velocidad
    #                     jugador.direccion_colision = "derecha"
    #                     print("Colisión en el lado derecho con enemigo")
    #         else:
    #             # Permitir que el personaje camine encima del enemigo sin colisionar
    #             jugador.y = enemigo.rect.y - jugador.height
    #             jugador.direccion_colision = None