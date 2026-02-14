import pygame
import constants
from character import Character

#Inicio Pygame
pygame.init()


#Incio Game Window
my_screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("El Cavernas y Dragones")

#Create Character
player = Character(100, 100)

##Main Game Loop
game_on = True
while game_on:

    #Draw Player
    player.draw(my_screen)

    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    #Update Screen
    pygame.display.update()

pygame.quit()



