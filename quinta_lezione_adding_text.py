import pygame

#Pyagme setup stuff
pygame.init
WINDOWS_WIDTH = 800
WINDOWS_HEIGHT = 500
screen = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGHT))
pygame.display.set_caption("pygame tutorial")
clock = pygame.time.Clock()
running = True

dt = 0
player_pos= pygame.Vector2(screen.get_width()/2,screen.get_height()/2)

#load our images
goblin_r = pygame.image.load("0_Goblin_Walking_000.png")

#ridimensionare le immagini con:
goblin_right = pygame.transform.scale(goblin_r,(80,80))
#adesso flippo l'immagine
goblin_left = pygame.transform.flip(goblin_right,1,0)

#get rect surrounding our images
goblin_right_rect = goblin_right.get_rect()
goblin_left_rect = goblin_left.get_rect()
#position our images
goblin_right_rect.topleft = (0,0)
goblin_left_rect.topright = (WINDOWS_WIDTH,0)


while running:
    #poll for events
    #pygame.quit() voglio chiudere la finestra

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #Pick the screen color
    screen.fill("silver")

    #RENDER OUT GAME
    # pygame.draw.circle(screen,"blue",player_pos,40)

    # Blit (copy) screen object at some given coordinate
    screen.blit(goblin_right, goblin_right_rect)
    screen.blit(goblin_left, goblin_left_rect)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        goblin_right_rect.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        goblin_right_rect.y += 300 * dt


    if keys[pygame.K_LEFT]:
        goblin_right_rect.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        goblin_right_rect.x += 300 * dt


    # #CHECK TO SEE IF THE MOUSE HAS BEEN PRESSED
    # if pygame.mouse.get_pressed()[0]:
    #     # print(pygame.mouse.get_pressed()) ti da un array con i bottoni del mouse ogni tick
    #     if event.type == pygame.MOUSEMOTION:
    #         pos = pygame.mouse.get_pos()
    #         player_pos.x = pos[0]
    #         player_pos.y = pos[1]

    '''
    #NOW WE USE THE MOUSEEEE!!!!
    if event.type == pygame.MOUSEBUTTONDOWN:
        # print(event)
        # se stampo vedo l'ogetto dell'evento tipo che bottone(mouse) è stato premuto

        pos = pygame.mouse.get_pos()
        #Move the circle
        player_pos.x = pos[0]
        player_pos.y = pos[1]

    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,"red",player_pos,40)


    #MOTION!!!!!
    if event.type == pygame.MOUSEMOTION:
        pos = pygame.mouse.get_pos()
        #Move the circle
        player_pos.x = pos[0]
        player_pos.y = pos[1]
    '''
    #flip the display to uotput our worrk to the screen
    pygame.display.flip()

    #set the clock stuff / delta time in seconds since the last fraem
    #used for framerate independent physics
    dt = clock.tick(60) / 1000






pygame.quit()
