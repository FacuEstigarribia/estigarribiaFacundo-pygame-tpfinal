import pygame
from constantes import *
from auxiliar import Auxiliar


class Plataform(pygame.sprite.Sprite):
    def __init__(self, plataforma_data,  type=1):
        super().__init__()
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images/surfaces/{0}.png",1,18,flip=False,w=plataforma_data.get("width"),h=plataforma_data.get("height"))
        
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = plataforma_data.get("x")
        self.rect.y = plataforma_data.get("y")
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H

    def get_top_collision(self):
        return self.collition_rect.top

    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        screen.blit(self.image,self.rect)