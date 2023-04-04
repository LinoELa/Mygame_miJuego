#SE HABLA DE :
#KEYBOARD INPUT : se puede usar pygame.key or event loop 
#SALTAR Y GRAVEDAD 
#CREAR EL SUELO

######## CLASS 
# se usa las clases para controlar inside of the relevant class. 
#Pygame.mouse and pygame.keys are great for that
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


while True : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit() 
            exit()
# keyboard manejos de los teclados :
#ayuda a mirar si el boton a sido pulsado 
# ha mantenido el boton pulsado 

        # if event.type == pygame.KEYDOWN:
        #     if event.type == pygame.QUIT:
        #         print('Jump')

        # if event.type == pygame.KEYUP:
        #     print('Key Up')

        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
                print('Jump')

        elif event.type == pygame.KEYUP:
            print('Key Up')

            
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
    ventana.blit(player_surf,player_rect) 
    
    # keys = pygame.key.get_pressed()
    # if keys [pygame.K_SPACE]:
    #     print('jump')



    pygame.display.update() 
    clock_tiempo.tick(60)   