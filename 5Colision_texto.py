#SE HABAL DE: 
#colision 
#text 
#colores 
#lineas
#dibujos 


import pygame 
from sys import exit

pygame.init()
altura = 800 
anchura = 400 
ventana = pygame.display.set_mode((altura, anchura))
titulo = pygame.display.set_caption('Pygame First Game ')

clock_tiempo = pygame.time.Clock()
text_font = pygame.font.Font('./DOCS/font/Pixeltype.ttf', 50 )
sky_surface_img = pygame.image.load('./DOCS/graphics/Sky.png').convert_alpha() 
ground_surface_img = pygame.image.load('./DOCS/graphics/ground.png').convert_alpha() 

score_surf = text_font.render('My game' , False , (64,64,64))  ### COLOR RGB: NEGRO
score_rect = score_surf.get_rect(center = (400 ,50 ))  # 3 

#PYGAME.DRAW = draw rectangles , circles , lines, pointes, ellipses 

snail_caracol = pygame.image.load('./DOCS/graphics/snail/snail1.png').convert_alpha() 
snail_rect = snail_caracol.get_rect(bottomright = (600, 300 )) 


player_surf = pygame.image.load('./DOCS/graphics/Player/player_walk_1.png').convert_alpha() # 1 
player_rect = player_surf.get_rect( midbottom= (80, 300 ))  


while True : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit() 
            exit()

        # # 2 Enteneder la movivliad y enter el mause
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('Colision')
        #      # A bueno para aprender donde esta el raton 

            
    ventana.blit(sky_surface_img, (0,0))        
    ventana.blit(ground_surface_img,(0,300))   

    # ENTENDER BIEN ESO SOBRE LAS LINEAS Y EL CURSOOR 
    #MINUTO 1:23:26 
#   PYGAME.DRAW = draw rectangles , circles , lines, pointes, ellipses     
    pygame.draw.rect(ventana, '#c0e8ec'  , score_rect)       #### COLOR CUSTOM : PINK 
    pygame.draw.rect(ventana, '#c0e8ec'  , score_rect,10)     #### COLOR CUSTOM : PINK 
#   pygame.draw.line(ventana, 'Gold'  , (0,0),pygame.mouse.get_pos(),10)  #### MUY IMPORTANTE 
#   pygame.draw.ellipse(ventana, 'brown ', pygame.Rect(50,200,100, 100))  #### MUY IMPORTANTE




    ventana.blit(score_surf,score_rect)       
    # 

    snail_rect.x -= 4              
    if snail_rect.right <= 0 :      
        snail_rect.left = 800       

    ventana.blit(snail_caracol,snail_rect)  
    ventana.blit(player_surf,player_rect) 

    # 1 colision con el metodo  ###colliderect  ### Tambien esxite COLLIDEPOINT((X,Y))

    # A PYGAME.MOUSE = MOUSE POSITION , CLICK BOTON , VISIBILIDAD 
    # B : GET MOUSEMOTION , CLICK , POSITION ETC

    # if player_rect.colliderect(snail_rect):
    #     print('Se colicionana')

    # mouse_pos = pygame.mouse.get_pos() # B 
    # if player_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update() 
    clock_tiempo.tick(60)   