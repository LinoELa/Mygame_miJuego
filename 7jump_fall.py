#Saltar 
#gavedad

import pygame 
from sys import exit

pygame.init()
altura = 800 
anchura = 400 
ventana = pygame.display.set_mode((altura, anchura))
titulo = pygame.display.set_caption('Pygame First Game ')

clock_tiempo = pygame.time.Clock()
text_font = pygame.font.Font('./DOCS/font/Pixeltype.ttf', 50 )

sky_surface_img = pygame.image.load('./DOCS/graphics/Sky.png').convert() 
ground_surface_img = pygame.image.load('./DOCS/graphics/ground.png').convert() 

score_surf = text_font.render('My game' , False , (64,64,64))  
score_rect = score_surf.get_rect(center = (400 ,50 )) 


snail_caracol = pygame.image.load('./DOCS/graphics/snail/snail1.png').convert_alpha() 
snail_rect = snail_caracol.get_rect(bottomright = (600, 300 )) 


player_surf = pygame.image.load('./DOCS/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect( midbottom= (80, 300 ))  

#gravedad 
Player_Gravity = 0



while True : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit() 
            exit()
        #el raton al bulsar al jugador el salta 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos)  and player_rect.bottom >= 300:
                Player_Gravity = -20


        #Al pulsar espacion pues el salta 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300: # PLAYER_RECT.BOTTOM >= 300para hacer que el player salte solo despues de haber toocado el suelo. 
                Player_Gravity = -20

        # elif event.type == pygame.KEYUP:
        #     print('Key Up')

            
    ventana.blit(sky_surface_img, (0,0))        
    ventana.blit(ground_surface_img,(0,300))   
    pygame.draw.rect(ventana, '#c0e8ec'  , score_rect)       
    pygame.draw.rect(ventana, '#c0e8ec'  , score_rect,10)     
    ventana.blit(score_surf,score_rect)       
    # 

    snail_rect.x -= 4              
    if snail_rect.right <= 0 :      
        snail_rect.left = 800       
    ventana.blit(snail_caracol,snail_rect)  
# Gravedad 
    Player_Gravity += 1 #Incrementeo de gravedad #1
    player_rect.y += Player_Gravity
#Creando el floor o el suelo 
    if player_rect.bottom >= 300 : # EL 300 viene de la posicion en Y del GROUND SURFACE
        player_rect.bottom = 300

    ventana.blit(player_surf,player_rect) 
    
#creating the flow f


    pygame.display.update() 
    clock_tiempo.tick(60)   

#Creating the  floor 
###Lo que de verdar se necesita es checkear la posicion del jugador 
#Player.bottom > 300 
