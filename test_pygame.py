from game import Bolas, Ball
from pygame import Surface
import pygame

def test_create_screen():
    bolas = Bolas()
    assert isinstance(bolas.screen, Surface)
# Estamos comprobando que la pantalla es de clase Surface

def test_screen_size():
    bolas = Bolas()
    assert bolas.screen.get_width() == 800
    assert bolas.screen.get_height() == 600
# Estamos comprobando que la medida de la pantalla. 
# Screenn es una instancia Surface, por lo que estamos comprobando atributos

def test_screen_caption():
    bolas = Bolas() 
    assert pygame.display.get_caption()[0] == "Juego de bolas"
#Comprobamos solo el primer elemento de la tupla. Porque en la documentacion vemos que pygame.display.get_caption nos devuelve una tupla de (titulo, icono)
#Seria lo mismo que hacer:
# tupla = pygame.display.get_caption()
# titulo = tupla[0]

def test_exist_one_ball():
    bolas = Bolas()

    assert isinstance(bolas.players[0], Ball)
    assert bolas.players[0].x == 150
    assert bolas.players[0].y == 150
    assert bolas.players[0].radio == 15
