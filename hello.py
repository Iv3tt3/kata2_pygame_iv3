import pygame

#Vamos a crear la pantalla, la ventana del juego
pantalla = pygame.display.set_mode((800,600)) #Medida de la pantalla
pygame.display.set_caption("Hola mundo") #Poner titulo a la pantalla

#Vamos a crear el bucle principal
game_over = False 
azul = 0

while game_over == False: #creamos una variable gameover en False y asi nos deja cerrar el bucle gracias al for siguiente
    for evento in pygame.event.get(): #vaciar el bufer de eventos para que no te pete el pc
        if evento.type == pygame.QUIT: #si el evento es cerrar, pones game over en True y asi sale del bucle
            game_over = True
    azul = azul + 1
    if azul > 255:
        azul = 0

    pantalla.fill((0,0,azul)) #pintamos los colores de azul con rgb
    pygame.display.flip() #para que lo pase a la tarjeta grafica y de ahi al monitor