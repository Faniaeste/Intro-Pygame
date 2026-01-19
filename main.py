import pygame as pg

#inicializar todos los modulos de pygame, pantallas, objetos, eventos, sonidos, etc...
pg.init()

#Crear pantallas o surface
pantalla = pg.display.set_mode( (800,600) ) #Definición de tamañpde pantalla.
pg.display.set_caption( "Intro Pygame" )#Agregar titutlo en string a mi ventana

game_over = True
x = 0
vx = 1 #velocidad de x
while game_over:
    for eventos in pg.event.get(): #Captura todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill((219, 50, 185))# Asignar el color de pantalla en rgb

    x = x + vx
    if x == 800 or x == 0:
        vx = vx * -1
    #Agregamos objeto a la pantalla
    #draw.rect(sourface,color en (r,g,b),posiciones(posicionX,posicionY,tamañoX,tamañoY))
    pg.draw.rect( pantalla,(204, 20, 137),(x,300-15,30,30) )

    pg.display.flip()#Función para recargar toda la configuración que va a la pantalla



#Cierre de pantalla
pg.quit()