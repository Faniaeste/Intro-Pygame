import pygame as pg
from figura_class import Figura
import random as ra


#inicializar todos los modulos de pygame, pantallas, objetos, eventos, sonidos, etc...
pg.init()
x_pos = 800
y_pos = 600
#mejor poner el tamaño de la pantalla en variables por si el dia de mañana quieres cambiar el tamaño de tu pantalla

#Crear pantallas o surface
pantalla = pg.display.set_mode( (x_pos,y_pos) ) #Definición de tamañpde pantalla.
pg.display.set_caption( "Intro Pygame" )#Agregar titutlo en string a mi ventana

game_over = True
"""
rectangulo1 = Figura(0,300,(201, 95, 56))
rectangulo2 = Figura(20,500)
rectangulo3 = Figura(0,400, (176, 0, 0))
circulo1 = Figura(200,500,(131, 214, 71))
"""
#Creando mi lista de circulos para guardar los 100 objetos
lista_circulos = []
lista_rectangulos = []
#por cada vuelta del for voy guardando en lista un objeto figura con datos de entradas diferentes con el random.randinit
for i in range(1,101):
    lista_circulos.append(Figura(ra.randint(0,800),ra.randint(0,600), color =(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)),radio = ra.randint(10,100)))
    lista_rectangulos.append(Figura(ra.randint(0,800),ra.randint(0,600), color =(ra.randint(0,255),ra.randint(0,255), ra.randint(0,255)), w = ra.randint(10,100), h = ra.randint(10,100)))


while game_over:
    for eventos in pg.event.get(): #Captura todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill((219, 50, 185))# Asignar el color de pantalla en rgb

#recorremos la lista de circulos cargadas, llamabmos a los metodos, mover y dibujar para que lo muestre en pantalla
    for i in range(0,100):
        lista_circulos[i].mover(x_pos,y_pos)
        lista_rectangulos[i].mover(x_pos,y_pos)
        lista_circulos[i].dibujar_circulo(pantalla)
        lista_rectangulos[i].dibujar_rectangulo(pantalla)
    """
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
    """
    pg.display.flip()#Función para recargar toda la configuración que va a la pantalla



#Cierre de pantalla
pg.quit()