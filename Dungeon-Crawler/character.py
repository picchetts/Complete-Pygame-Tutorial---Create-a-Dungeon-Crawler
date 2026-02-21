import pygame
import constants
import math


class Character():
    def __init__(self, x, y,mob_animations, char_type):
        #Creo variable mob type
        self.char_type = char_type
        # Creo variable flip para cuando el personaje se gira
        self.flip = False
        #Almaceno la animation list para el tipo específico de Mob
        self.animation_list = mob_animations[self.char_type]
        self.frame_index = 0
        self.action = 0 #0:iddle, 1:run
        self.update_time = pygame.time.get_ticks()
        self.running = False
        #creo el campo imagen referenciando la lista animaciones correspondiente
        self.image = self.animation_list[self.action][self.frame_index]
        #creo una forma básica rectangulo de 40x40 en las coordenadas 0, 0
        self.rect = pygame.Rect(0, 0, 40, 40)
        #posiciono rectangulo en coordenadas pasadas a Init
        self.rect.center = (x, y)

    def move(self, dx, dy):
        #Player to not showing movement unless keys are pressed
        self.running = False
        #player must show movement when keys are pressed
        if dx != 0 or dy != 0:
            self.running = True
        #Flipeo Imagen si se mueve hacia la izquierda
        if dx < 0:
            self.flip = True
        if dx > 0:
            self.flip = False

        #Reduzco Diagonal Speed
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2)/2)

        self.rect.x += dx
        self.rect.y  += dy

    def update(self):
        #Check what action is performing the player
        if self.running == True:
            self.update_action(1)#1:run
        else:
            self.update_action(0)#0:iddle
        animation_cooldown = 70
        #Handle animation
        #Update image
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        # Check if animation has finished
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        #check if the new action is different from preview one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, surface):
        #Dibujo imagen flipeada si aplica
        fipped_image = pygame.transform.flip(self.image, self.flip, False)
        #Agrego imagen en el metodo Draw
        surface.blit(fipped_image, self.rect)
        #pygame.draw.rect(surface, constants.RED, self.rect, 1)

