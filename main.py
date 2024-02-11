import pygame as pg
from figura_class import Meteorito, Nave
import random
import time

pg.init()  # INICIAR MODULO

# -----TAMAÑO PANTALLA 1
pantalla_principal = pg.display.set_mode((800, 600))
pg.display.set_caption("METABIRDS-SPACETERROR-ONE")

# -----TIEMPO TASA DE REFRESCO--FPS----
tasa_refresco = pg.time.Clock()

# CREAR VARIABLE DE OBJETO

# Lista para almacenar meteoritos
meteoritos = []

# -----NAVE-----
nave = Nave(10, 300)

# -----CONTADOR-----
puntuacion = 0

# -----BUCLE
game_over = False

# Velocidad inicial de los meteoritos
velocidad_meteoritos = 4

# Tiempo máximo permitido (25 segundos)
tiempo_limite = 25
tiempo_inicio = time.time()

# Radio de los círculos de vidas
radio_vida = 15

# Lista de coordenadas para los círculos de vidas
coordenadas_vidas = [(20 + i * 35, 60) for i in range(nave.vidas)]

# Bucle principal
while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    # Verificar condición de tiempo y vidas
    tiempo_actual = time.time() - tiempo_inicio
    if tiempo_actual > tiempo_limite or nave.vidas == 0:
        game_over = True

    # Verificar colisiones con la nave y restar/sumar vidas
    for meteorito in meteoritos:
        puntuacion = meteorito.mover(puntuacion, velocidad_meteoritos)

        if nave.verificar_colision(meteorito):
            if not nave.restar_vida():
                game_over = True  # Termina el juego si las vidas son 0
            else:
                meteorito.pos_x = 800
                meteorito.pos_y = random.randint(0, 600)
                # Restar -1 a la puntuación por colisión con la nave
                puntuacion -= 1
                # Eliminar una coordenada de vida cuando se pierde una vida
                coordenadas_vidas.pop()
        else:
            # Sumar +1 si no hay colisión
            puntuacion += 1

    # Mover la nave después de verificar las colisiones
    nave.mover()

    # Agregar nuevos meteoritos a la lista
    if random.randint(0, 100) < 2:  # Probabilidad de agregar un nuevo meteorito (ajusta según tu preferencia)
        nuevo_meteorito = Meteorito(800, random.randint(0, 600), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), random.randint(10, 40))
        meteoritos.append(nuevo_meteorito)

    # Dibujar los objetos del juego
    pantalla_principal.fill((255, 177, 0))  # PONER COLOR PANTALLA FONDO
    nave.dibujar(pantalla_principal)

    # Dibujar cada meteorito en la lista
    for meteorito in meteoritos:
        meteorito.dibujar(pantalla_principal)

    # Dibujar marcador de puntuación
    fuente_puntuacion = pg.font.Font(None, 36)
    texto_puntuacion = fuente_puntuacion.render(f"Puntuación: {puntuacion}", True, (0, 0, 255))
    pantalla_principal.blit(texto_puntuacion, (10, 10))

    # Dibujar círculos de vidas
    for coordenada in coordenadas_vidas:
        pg.draw.circle(pantalla_principal, (255, 0, 0), coordenada, radio_vida)

    pg.display.flip()

    pg.time.delay(10)  # Añadir un pequeño retraso para controlar la velocidad del juego

    tasa_refresco.tick(1000)  # Limitar a 60 FPS

    # Terminar el juego si las vidas llegan a 0
    if nave.vidas == 0:
        game_over = True

pg.quit()





#-----BUCLE

game_over = True

while game_over:
    valor_tasa = tasa_refresco.tick()
    #print(valor_tasa)


    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = False

    #-----CAPTURAR CONTROLES TECLADO-----
            
           
    """  
    estado_teclado = pg.key.get_pressed()#CAPTURAR KEY
    print("estado teclado: ",estado_teclado[pg.K_UP])
    
    #ARRIBA
    if estado_teclado[pg.K_UP] == True:
        nave.pos_y -= 1

    #ABAJO
    if estado_teclado[pg.K_DOWN] == True:
        nave.pos_y += 1

    """


    pantalla_principal.fill((255, 177, 0))#PONER COLOR PANTALLA FONDO

    #-----DIBUJAR LOS OBJETOS-----
    nave.dibujar(pantalla_principal)#PINTAR NAVE ROJA
    meteorito.dibujar(pantalla_principal)#PINTAR METEORITO1 EN LA PANTALLA
    meteorito2.dibujar(pantalla_principal)#PINTAR METEORITO2 EN LA PANTALLA
    meteorito3.dibujar(pantalla_principal)#PINTAR METEORITO3 EN LA PANTALLA
    
    nave.mover()

    pg.display.flip()#ACTIVAR COLOR

pg.quit()
