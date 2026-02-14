import pygame
import constants


class Character():
    def __init__(self, x, y):
        #creo una forma básica rectangulo de 40x40 en las coordenadas 0, 0
        self.rect = pygame.Rect(0, 0, 40, 40)
        #posiciono rectangulo en coordenadas pasadas a Init
        self.rect.center = (x, y)

    def draw(self, surface):
        pygame.draw.rect(surface, constants.RED, self.rect)

