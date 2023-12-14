import pygame
from gui_form import Form
from gui_button import Button
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from item import Item


class FormLevel1(Form):
    def __init__(self, screen, x: int, y: int, w: int, h: int, color_background, color_border="Black", border_size: int = -1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        
        self.player = Player(x=0,y=400,speed_walk=6,speed_run=12,gravity=20,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)
        
        self.enemigo1 = Enemy(x=600,y=450,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300)
        self.enemigo2 = Enemy(x=700,y=450,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300)
        self.enemies_group = pygame.sprite.Group()
        self.enemies_group.add(self.enemigo1, self.enemigo2)
        self.plataformas = []
        self.plataformas.append(Plataform(x=100,y=500,width=220,height=50,type=1))
        self.plataformas.append(Plataform(x=500,y=500,width=150,height=50,type=2))   
        self.plataformas.append(Plataform(x=690,y=430,width=230,height=50,type=12))
        self.plataformas.append(Plataform(x=897,y=512,width=100,height=50,type=12))
        self.plataformas.append(Plataform(x=1020,y=540,width=800,height=50,type=12))


        self.coins_sprites = pygame.sprite.Group()

        self.coin1 = Item(170, 470)
        self.coin2 = Item(570, 479)
        self.coin3 = Item(714, 402)
        self.coin4 = Item(1304, 508)
        self.coins_sprites.add(self.coin1, self.coin2, self.coin3, self.coin4)
        
    def update(lista_eventos):
        pass
        
                