import pygame
import constants
import math


class Character():
    def __init__(self, x, y,image):
        #creo el campo imagen referenciando el sprite
        self.image = image
        #Creo variable flip para cuando el personaje se gira
        self.flip = False
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

    def draw(self, surface):
        #Dibujo imagen flipeada si aplica
        fipped_image = pygame.transform.flip(self.image, self.flip, False)
        #Agrego imagen en el metodo Draw
        surface.blit(fipped_image, self.rect)
        pygame.draw.rect(surface, constants.RED, self.rect, 1)

