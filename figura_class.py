import pygame as pg 
import random
import time


class Nave:
    def __init__(self, pos_x, pos_y, color=(255, 0, 0), w=30, h=20, vx=1, vy=1, vidas=3):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.vx = vx
        self.vy = vy
        self.vidas = vidas

    def dibujar(self, surface):
        pg.draw.rect(surface, self.color, (self.pos_x, self.pos_y - (self.h // 2), self.w, self.h))

    def mover(self):
        estado_teclado = pg.key.get_pressed()

        # ARRIBA
        if estado_teclado[pg.K_UP] and (self.pos_y >= 0 + (self.h // 2)):
            self.pos_y -= 3

        # ABAJO
        if estado_teclado[pg.K_DOWN] and (self.pos_y <= 600 - (self.h // 2)):
            self.pos_y += 3

    def verificar_colision(self, meteorito):
        # Coordenadas del rectángulo que representa la nave
        rect_nave = pg.Rect(self.pos_x - (self.w // 2), self.pos_y - (self.h // 2), self.w, self.h)

        rect_meteorito = pg.Rect(meteorito.pos_x - meteorito.radio, meteorito.pos_y - meteorito.radio,
                                 2 * meteorito.radio, 2 * meteorito.radio)
        
        return rect_nave.colliderect(rect_meteorito)
    
    def restar_vida(self):
        self.vidas -= 1
        return self.vidas >= 0

class Meteorito:
    def __init__(self, pos_x, pos_y, color=(255, 255, 255), radio=10, vx=1, vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy

    def dibujar(self, surface):
        pg.draw.circle(surface, self.color, (self.pos_x, self.pos_y), self.radio)

    def mover(self, puntuacion, velocidad=1.0, x_max=800, y_max=600):
        self.pos_x -= velocidad * self.vx

        # Resto del código (sin cambios)

        # Asegúrate de devolver la puntuación actualizada
        return puntuacion

        # Reiniciar meteorito cuando sale de la pantalla por la izquierda
        if self.pos_x < 0 - (2 * self.radio):
            self.pos_x = x_max
            self.pos_y = random.randint(0, y_max)
            self.vx = random.uniform(0.5, 2.0)
            self.vy = random.uniform(0.5, 2.0)

            # Incrementar puntuación al reiniciar meteorito
            puntuacion += 1

        return puntuacion  # Devolver la puntuación actualizada

            
    def dibujar(self, surface):
        pg.draw.circle(surface, self.color, (self.pos_x, self.pos_y), self.radio)
    """
    def mover(self,x_max=800,y_max=600):
        self.pos_x -= self.vx
        self.pos_y == self.vy
    """


    #------REBOTE METEORITOS-----
       
    """ if self.pos_x >= x_max+ (2*self.radio) or self.pos_x <= 0-(5*self.radio):
            self.pos_x = 800
            self.pos_y = 300
            self.vx *= -1
        
        if  self.pos_y >= y_max or self.pos_y <=0:
            self.vy *= -1
    """

    
    #-----GENERAR METEORITO ALEATORIO-----
    
    

