import pygame

#Pyagme setup stuff
pygame.init
WINDOW_WIDHT = 800
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDHT,WINDOW_HEIGHT))
pygame.display.set_caption("pygame tutorial")
clock = pygame.time.Clock()
running = True

dt = 0
player_pos= pygame.Vector2(screen.get_width()/2,screen.get_height()/2)


while running:
    #poll for events
    #pygame.quit() voglio chiudere la finestra

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #Pick the screen color
    screen.fill("silver")
    #UNDERSTANDING COORDINATE
    #TOP LEFT = 0,0
    #-> X INCREASE DOWN Y INCREASE


    # DRAW A LINE
    pygame.draw.line(screen,"black", (0,50),(800,50),3)

    #DAW A CIRCLE
    pygame.draw.circle(screen,"black",(WINDOW_WIDHT/2,WINDOW_HEIGHT/2),50,1 )

    #DRAW A RECTANGLE
    pygame.draw.rect(screen,"black",(100,400,100,50))

    #flip the display to uotput our worrk to the screen
    pygame.display.flip()

    #set the clock stuff / delta time in seconds since the last fraem
    #used for framerate independent physics
    dt = clock.tick(60) / 1000






pygame.quit()
