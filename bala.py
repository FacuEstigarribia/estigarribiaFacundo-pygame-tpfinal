import pygame
from constantes import *

class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion, speed_shoot) -> None:
        super().__init__()
        self.image = pygame.image.load(r"images/bullet/bala2.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.centery = y
        self.direccion = direccion
        self.speed_shoot = speed_shoot
        
    def update(self, lista_enemigos):
        if self.direccion == DIRECTION_R:
            self.rect.x += self.speed_shoot
        elif self.direccion == DIRECTION_L:
            self.rect.x -= self.speed_shoot
        
        lista_colisiones = pygame.sprite.spritecollide(self, lista_enemigos, True)
        if lista_colisiones:
            
            self.kill()
        
        if self.direccion == DIRECTION_R and self.rect.x > ANCHO_VENTANA or \
            self.direccion == DIRECTION_L and self.rect.left < 0:
            self.kill()
            
        
        
    def draw(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect)
        