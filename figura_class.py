import pygame as pg 


class Nave:
    def __init__(self,pos_x,pos_y,color=(255, 0, 0),w=30,h=15):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h

    def dibujar(self,surface):
        pg.draw.rect(surface,self.color,(self.pos_x,self.pos_y-(self.h//2),self.w,self.h))




#-----CLASES ENEMIGOS-----
        
class Meteorito:
    def __init__(self,pos_x,pos_y,color=(255,255,255),radio=10):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio 

    def dibujar(self,surface):
        pg.draw.circle(surface,self.color,(self.pos_x,self.pos_y),self.radio)





    
