import pygame 
from sys import exit

pygame.init()
altura = 800 
anchura = 400 
ventana = pygame.display.set_mode((altura, anchura))
titulo = pygame.display.set_caption('Pygame First Game ')

clock_tiempo = pygame.time.Clock()


################# PLAIN COLOR mostrar superficie o display surface   ################# 
#La S es mayuscula aunque el autocompletado lo ponga en minuscula

#es para saber o entender como se pone los elementos dentro del window
# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')
################# PLAIN COLOR mostrar superficie o display surface   ################# 

######## TRAAJANDO CON TEXTO ### 1. Crear font 2. Escribir text en surface   ################# 
# ( tipo de fondo , tamaño  )
text_font = pygame.font.Font('./DOCS/font/Pixeltype.ttf', 50 )

######## TRAAJANDO CON TEXTO ### 1. Crear font 2. Escribir text en surface   ################# 

##########  IMG   ########
sky_surface_img = pygame.image.load('./DOCS/graphics/Sky.png')
ground_surface_img = pygame.image.load('./DOCS/graphics/ground.png')
####### TEXTO ##
text_surface = text_font.render('My game' , False , 'Black')

while True : 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit() 
            exit()
    ##Posicionamiento  dentro del surface


    ###### Mostrar todo la imagen en la ventan 
    #ventana.blit(test_surface,(200, 100 ))
    ventana.blit(sky_surface_img, (0,0))        ### LA ORDEN ES IMPORTANTE 
    ventana.blit(ground_surface_img,(0,300))    ### LA ORDEN ES IMPORTANTE 
    ventana.blit(text_surface,(300, 50))        ### LA ORDEN ES IMPORTANTE

    pygame.display.update() 
    clock_tiempo.tick(60)