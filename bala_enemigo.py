import pygame
from constantes import *

class BalaEnemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()

        self.image = pygame.Surface((10, 5))  # Ajusta el tamaño según tus necesidades
        self.image.fill(C_RED)  # Color rojo
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.centery = y
        self.speed = speed # Ajusta la velocidad de la bala según tus necesidades

    def update(self):
        self.rect.x += self.speed
