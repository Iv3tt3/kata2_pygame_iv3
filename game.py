import pygame
import random
import math

class Bolas:
    def __init__(self):
        pygame.init
        self.screen = pygame.display.set_mode((800,600)) 
        pygame.display.set_caption("Juego de bolas")

        self.players = []
        '''
        Escondemos esta parte del codigo porque queremos probar si colisionan dos bolas, por lo que necesitamos crear dos bolas que colisionen

        for i in range(random.randint(1,11)):
            self.players.append(Ball(random.randint(0,800), random.randint(0,600), random.randint(10,30)))
        '''
       #Creamos dos bolas que colisionen, para probar el metodo ball_colision
        self.players.append(Ball(150,150,15,10,10))
        self.players.append(Ball(200,200,20,-10,-10))
        

        self.metronomo = pygame.time.Clock()


    def main_loop(self):
        game_over = False
        while game_over == False: 
            self.metronomo.tick(60) 
            for evento in pygame.event.get(): 
                if evento.type == pygame.QUIT: 
                    game_over = True
            
            self.screen.fill((200,250,200))

            self.players[0].ball_collision(self.players[1]) #Forzamos la comprovacion

            for bola in self.players:
                bola.draw(self.screen) #Dibujamos la bola en la screen
                bola.move(self.screen) #Cambiamos la posicion de la bola

            pygame.display.flip()
    
    


class Ball:
    def __init__(self, x, y, radio, dx, dy):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.dy = dy #random.randint(-11,20)
        self.dx = dx #random.randint(-10,15) 

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radio)

    def move(self, surface):
        self.x += self.dx
        self.y += self.dy
        if self.y >= surface.get_height() - self.radio or self.y <= self.radio: #substituimos 
            self.dy = -self.dy
        if self.x >= surface.get_width() - self.radio or self.x <= self.radio:
            self.dx = -self.dx

    def ball_collision(self, otra):
        # Quiza tambien funciona esto
        # distanciax = abs(self.x - otra.x) - (self.radio + otra.radio)
        #distanciay = abs(self.y - otra.y) - (self.radio + otra.radio)
        #if distanciax <=0 and distanciay <=0:

        distancia = math.sqrt((otra.x - self.x) ** 2 + (otra.y - self.y) **2)
        if distancia <= self.radio + otra.radio:

            self.dx = -self.dx
            self.dy = -self.dy
            otra.dx = -otra.dx
            otra.dy = -otra.dy



if __name__ == "__main__":

    juego = Bolas()
    juego.main_loop()
