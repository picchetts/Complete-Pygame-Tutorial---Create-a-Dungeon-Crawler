import pygame
import constants
from character import Character

#Inicio Pygame
pygame.init()


#Incio Game Window
my_screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Patatasan and the Killer Cacona")

#Create Clock for keep game frame rate
clock = pygame.time.Clock()

#Define Movement Variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

#Create Character
player = Character(100, 100)

##Main Game Loop
game_on = True
while game_on:
    #Setear Clock FPS
    clock.tick(constants.FPS)
    #LLenar el background en cada iteración del Clock
    my_screen.fill(constants.BG)

    #Calculate Movement
    dx = 0
    dy = 0
    if moving_right:
        dx = constants.SPEED
    if moving_left:
        dx = -constants.SPEED
    if moving_up:
        dy = -constants.SPEED
    if moving_down:
        dy = constants.SPEED

    # Movimiento de objetos en pantalla (Mueve en c/iteración, lo que varía es la velocidad si están las teclas presionadas)
    player.move(dx, dy)

    #Draw de Objetos en pantalla
    player.draw(my_screen)

    #Event Handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        #Capturar eventos KeyDown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True
        # Capturar eventos KeyUp
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False





    #Update Screen
    pygame.display.update()

pygame.quit()



