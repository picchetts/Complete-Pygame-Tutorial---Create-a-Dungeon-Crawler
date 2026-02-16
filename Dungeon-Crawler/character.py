import pygame
import constants
import math


class Character():
    def __init__(self, x, y):
        #creo una forma básica rectangulo de 40x40 en las coordenadas 0, 0
        self.rect = pygame.Rect(0, 0, 40, 40)
        #posiciono rectangulo en coordenadas pasadas a Init
        self.rect.center = (x, y)

    def move(self, dx, dy):
        """Control Diagonal Speed: si estan activos el movimiento horiz y vertical,
        lo que significa que va en diagonal: calculo la velocidad diagonal usando Teorema de Pitagoras

        """
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2)/2)

        self.rect.x += dx
        self.rect.y  += dy

    def draw(self, surface):
        pygame.draw.rect(surface, constants.RED, self.rect)

