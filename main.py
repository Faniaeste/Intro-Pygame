import pygame as pg

#inicializar todos los modulos de pygame, pantallas, objetos, eventos, sonidos, etc...
pg.init()

#Crear pantallas o surface
pg.display.set_mode( (800,600) ) #Definición de tamañpde pantalla.
pg.display.set_caption( "Intro Pygame" )#Agregar titutlo en string a mi ventana

game_over = True

while game_over:
    for eventos in pg.event.get(): #Captura todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

#Cierre de pantalla
pg.quit()

