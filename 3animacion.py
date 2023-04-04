import pygame 
from sys import exit

pygame.init()
altura = 800 
anchura = 400 
ventana = pygame.display.set_mode((altura, anchura))
titulo = pygame.display.set_caption('Pygame First Game ')

clock_tiempo = pygame.time.Clock()
text_font = pygame.font.Font('./DOCS/font/Pixeltype.ttf', 50 )
sky_surface_img = pygame.image.load('./DOCS/graphics/Sky.png').convert_alpha() #Convert() : info en Notion
ground_surface_img = pygame.image.load('./DOCS/graphics/ground.png').convert_alpha() #Convert() : info en Notion
text_surface = text_font.render('My game' , False , 'Black')

# 1 snail = caracol 
snail_caracol = pygame.image.load('./DOCS/graphics/snail/snail1.png').convert_alpha() #Convert() : info en Notion
snail_x_posicicion = 600  #POSICON EN X DEL CARACOL 1 A


while True : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit() 
            exit()
            
    ventana.blit(sky_surface_img, (0,0))        ### LA ORDEN ES IMPORTANTE 
    ventana.blit(ground_surface_img,(0,300))    ### LA ORDEN ES IMPORTANTE 
    ventana.blit(text_surface,(300, 50))        ### LA ORDEN ES IMPORTANTE
    snail_x_posicicion -= 4                   # 2 
    # 3 Par que empieza a terminer seria : 
    if snail_x_posicicion < - 100 :  # Es lo mismo que :  if snail_x_posicicion < - 100 :  snail_x_posicicion = 800
        snail_x_posicicion = 800
    #para que sea y la posicion donde se tiene que ver  
    ventana.blit(snail_caracol,(snail_x_posicicion, 250))    # 1 B    

    pygame.display.update() 
    clock_tiempo.tick(60)   # ES REALMENTE IMPORTATE PORQUE DETERMINA fp DEL VIDEOJUEGO #puedo cambirloa 600 y vere 