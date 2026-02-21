import pygame
import constants
from character import Character

#Inicio Pygame
pygame.init()


#Incio Game Window
my_screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("sarasasdasdas")

#Create Clock for keep game frame rate
clock = pygame.time.Clock()

#Define Movement Variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False


#Helper Function to Scale Up/ Down image
def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

#Load characters images
mob_animations = []
mob_types = ["patatasan", "poo"]

animation_types = ["iddle", "run"]
for mob in mob_types:
    #Create Animation List for each mob
    animation_list = []
    for animation in animation_types:
        #Reset Temporary list of images
        temp_list = []
        for i in range(16):
            img = pygame.image.load(f"assets/images/characters/{mob}/{animation}/{i}.png").convert_alpha()
            img = scale_img(img, constants.SCALE)
            #Añado secuencia de imagenes a lista temporal de cada animacion de movimiento
            temp_list.append(img)
        #Añado lista temporal de animacion de c/movimiento  a animation_list
        animation_list.append(temp_list)
    #Añado animation_list de cada mob a lista de mob_animations
    mob_animations.append(animation_list)

#Create Characters (uso index para elegi el personaje en base a la lista mob_animations)
player = Character(100, 100, mob_animations, 0)
###### POO TEST
from random import randint
enemies = []
for i in range(4):
    poo = Character(100, 100, mob_animations, 1)
    poo.rect.x = randint(0, 400)
    poo.rect.y = randint(0, 300)
    enemies.append(poo)
##############

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

    # Move Player
    player.move(dx, dy)

    ###### POO TEST

    for enemy in enemies:
        random_module = randint(1, 16)
        if (pygame.time.get_ticks() % random_module == 0):
            poo_x = dx + randint(-random_module, random_module)
            poo_y = dy + randint(-random_module, random_module)
            enemy.move(poo_x, poo_y)

        #####POO TEST
        enemy.update()
        enemy.draw(my_screen)
        #######

    ###########

    # Update Player animation
    player.update()


    #Draw Player on screen
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



