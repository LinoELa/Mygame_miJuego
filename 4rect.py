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
text_surface = text_font.render('My game' , False , 'Black')


snail_caracol = pygame.image.load('./DOCS/graphics/snail/snail1.png').convert_alpha() 
snail_rect = snail_caracol.get_rect(bottomright = (600, 300 )) # tiene que estar en la misma posicion que ground

#CREANDO JUGADOR 
player_surf = pygame.image.load('./DOCS/graphics/Player/player_walk_1.png').convert_alpha() # 1 
#3 # se puede cambiar de posiciones : midleft= 80 , 200 ,midbottom = 80 , 300 
player_rect = player_surf.get_rect( midbottom= (80, 300 ))   # 3 # izq , der, arri, abaj #tamano de rectangulo


while True : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit() 
            exit()
            
    ventana.blit(sky_surface_img, (0,0))        ### LA ORDEN ES IMPORTANTE 
    ventana.blit(ground_surface_img,(0,300))    ### LA ORDEN ES IMPORTANTE 
    ventana.blit(text_surface,(300, 50))        ### LA ORDEN ES IMPORTANTE
#  snail_rect -= 4                

#     if snail_rect < - 100 :       #Al usar el rectangulo ya no es necesario 
#         snail_rect = 800          #Al usar el rectangulo ya no es necesario 
    snail_rect.x -= 4               #5 Ahora ya no flora esta un poco mas abajo 
    if snail_rect.right <= 0 :      #5A
        snail_rect.left = 800       #5B

    ventana.blit(snail_caracol,snail_rect)  
## ##    player_rect.left  - + 4  # 4 # Es mejor mover el rectangulo que que tiene al individio que al mismo individuo
    ventana.blit(player_surf,player_rect) # 2 

    pygame.display.update() 
    clock_tiempo.tick(60)   