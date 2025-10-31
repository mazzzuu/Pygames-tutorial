import pygame

#Pyagme setup stuff
pygame.init
screen = pygame.display.set_mode((800,500))
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

    #RENDER OUT GAME
    pygame.draw.circle(screen,"blue",player_pos,40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt


    #flip the display to uotput our worrk to the screen
    pygame.display.flip()

    #set the clock stuff / delta time in seconds since the last fraem
    #used for framerate independent physics
    dt = clock.tick(60) / 1000






pygame.quit()