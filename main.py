import pygame as pg 
from figura_class import Meteorito,Nave

pg.init()#INICIAR MODULO


#-----TAMAÑO PANTALLA 1
pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("METABIRDS-SPACETERROR-ONE")


#-----TIEMPO TASA DE REFRESCO--FPS----
tasa_refresco = pg.time.Clock()


#CREAR VARIABLE DE OBJETO
#-----ENEMIGOS-----
meteorito = Meteorito(800,300,(0, 68, 255),25)#AZUL
meteorito2 = Meteorito(800,100,(247, 99, 255),40)#ROSA
meteorito3 = Meteorito(800,500,(141, 99, 255 ),15)#LILA
#-----NAVE-----
nave = Nave(10 ,300)











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
