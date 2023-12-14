import pygame
from auxiliar import Auxiliar
from constantes import *

class Item(pygame.sprite.Sprite):
    def __init__(self, item_data) -> None:
        super().__init__()

        self.image_coin = Auxiliar.get_surface_from_spritesheet(r"images/coin/newCoins.jpg", 24, 1)
        self.frame = 0
        self.image = self.image_coin[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = item_data.get("x")
        self.rect.y = item_data.get("y")
        self.rect.topleft = (item_data.get("x"), item_data.get("y"))
        self.tiempo_transcurrido = pygame.time.get_ticks()
        self.collition_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h)
        self.frame_rate_ms = 100
            
    def do_animation(self, delta_ms):
        self.tiempo_transcurrido += delta_ms
        if(self.tiempo_transcurrido >= self.frame_rate_ms):
            self.tiempo_transcurrido = 0
            if(self.frame < len(self.image_coin) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0


    def collect(self, player):
        if self.is_collected(player):
            print("toco")
            player.score += 5
            self.kill()
            
        self.frame = 0
            
    def is_collected(self, player):
        is_collected = False
        if self.collition_rect.colliderect(player.rect):
            print("toco")
            is_collected = True
        return is_collected
    
    def update(self, delta_ms, player):
        self.collect(player)
    
    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen,color=C_BLUE,rect=self.collition_rect)
        screen.blit(self.image, self.rect)

        
    
        

        