import pygame as pg 


class Nave:
    def __init__(self,pos_x,pos_y,color=(255, 0, 0),w=30,h=20,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.vx = vx
        self.vy = vy

    def dibujar(self,surface):
        pg.draw.rect(surface,self.color,(self.pos_x,self.pos_y-(self.h//2),self.w,self.h))

    #FUNCION MOVER NAVE
    def mover(self):
        estado_teclado = pg.key.get_pressed()#CAPTURAR KEY
       
    #-----BLOQUEAR EL PASO SUPERIOR PANTALLA E INFERIOR
        #if self.pos_y == 0+(self.h//2) or self.pos_y == 600-(self.h//2):
            #self.vy *= -1

    #-----MOVIMIENTO-----
    #ARRIBA
        if estado_teclado[pg.K_UP] == True and (self.pos_y >= 0+(self.h//2)):
            self.pos_y -= 1

    #ABAJO
        if estado_teclado[pg.K_DOWN] == True and (self.pos_y <= 600-(self.h//2)):
            self.pos_y += 1


#-----CLASES ENEMIGOS-----
        
class Meteorito:
    def __init__(self,pos_x,pos_y,color=(255,255,255),radio=10):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio 

    def dibujar(self,surface):
        pg.draw.circle(surface,self.color,(self.pos_x,self.pos_y),self.radio)





    
