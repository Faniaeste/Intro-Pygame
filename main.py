import pygame as pg
from figura_class import Figura


#inicializar todos los modulos de pygame, pantallas, objetos, eventos, sonidos, etc...
pg.init()
x_pos = 800
y_pos = 600
#mejor poner el tamaño de la pantalla en variables por si el dia de mañana quieres cambiar el tamaño de tu pantalla

#Crear pantallas o surface
pantalla = pg.display.set_mode( (x_pos,y_pos) ) #Definición de tamañpde pantalla.
pg.display.set_caption( "Intro Pygame" )#Agregar titutlo en string a mi ventana

game_over = True
rectangulo1 = Figura(0,300,(201, 95, 56))
rectangulo2 = Figura(20,500)
rectangulo3 = Figura(0,400, (176, 0, 0))
circulo1 = Figura(200,500,(131, 214, 71))

while game_over:
    for eventos in pg.event.get(): #Captura todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill((219, 50, 185))# Asignar el color de pantalla en rgb

    rectangulo1.mover(x_pos,y_pos)
    rectangulo2.mover(x_pos,y_pos)
    rectangulo3.mover(x_pos, y_pos)
    circulo1.mover(x_pos,y_pos)

    #Agregamos objeto a la pantalla
    #draw.rect(sourface,color en (r,g,b),posiciones(posicionX,posicionY,tamañoX,tamañoY))
    rectangulo1.dibujar_rectagulo(pantalla)
    rectangulo2.dibujar_rectagulo(pantalla)
    rectangulo3.dibujar_rectagulo(pantalla)
    circulo1.dibujar_circulo(pantalla)

    pg.display.flip()#Función para recargar toda la configuración que va a la pantalla



#Cierre de pantalla
pg.quit()