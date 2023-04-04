#llamar a pygame 
import pygame 
#importamos al salida de la ventana 
from sys import exit

#incializar ppygame 
pygame.init()

#################  variable basicas  ################# 
altura = 800 
anchura = 400 
ventana = pygame.display.set_mode((altura, anchura))
titulo = pygame.display.set_caption('Pygame First Game ')
#################  clock  tiempo  ################# 
#Es para que nuestro juego no vaya tan rapido 
clock_tiempo = pygame.time.Clock()

#################  variable basicas  ################# 
#################  variable basicas  ################# 






#creamos un blucle para que las variables basicas y otras creadas puedasn 
#estar o funcionar dentro de un bucle y que no paren 
while True : 
    #bucle para que haga un geto de lo que esta dentro.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #salida de pygame 
            pygame.quit()
            #salida del sistema 
            exit()
            
    #dibujar todos nuesteos elementos 
    #actualizar todo 
    pygame.display.update() 
    #clock tiempo la cantidad de fp que quiero (60fp para ese ejemeplo )
    clock_tiempo.tick(60)