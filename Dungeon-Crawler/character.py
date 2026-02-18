import pygame
import constants
import math


class Character():
    def __init__(self, x, y,animation_list):
        # Creo variable flip para cuando el personaje se gira
        self.flip = False
        #Almaceno la lista de frames en un field de la clase
        self.animation_list = animation_list
        #DEV
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        #creo el campo imagen referenciando la lista de frames del sprite
        self.image = self.animation_list[self.frame_index]

        #creo una forma básica rectangulo de 40x40 en las coordenadas 0, 0
        self.rect = pygame.Rect(0, 0, 40, 40)
        #posiciono rectangulo en coordenadas pasadas a Init
        self.rect.center = (x, y)

    def move(self, dx, dy):
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
        animation_cooldown = 70
        #Handle animation
        #Update image
        self.image = self.animation_list[self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        # SCheck if animation has finished
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0



    def draw(self, surface):
        #Dibujo imagen flipeada si aplica
        fipped_image = pygame.transform.flip(self.image, self.flip, False)
        #Agrego imagen en el metodo Draw
        surface.blit(fipped_image, self.rect)
        #pygame.draw.rect(surface, constants.RED, self.rect, 1)

