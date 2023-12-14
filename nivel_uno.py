import pygame
from constantes import *
from nivel import Nivel
from background import Background
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from item import Item

class NivelUno(Nivel):
    def __init__(self, pantalla) -> None:
        
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        background = Background(0, 0, ANCHO_VENTANA, ALTO_VENTANA, f"images/locations/goku_house.png")
        player = Player(x=0,y=400,speed_walk=6,speed_run=12,gravity=20,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)

        enemigo1 = Enemy(x=600,y=450,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300)
        enemigo2 = Enemy(x=700,y=450,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300)
        enemies_group = pygame.sprite.Group()
        enemies_group.add(enemigo1, enemigo2)



        plataformas = []
        plataformas.append(Plataform(x=100,y=500,width=220,height=50,type=1))
        plataformas.append(Plataform(x=500,y=500,width=150,height=50,type=2))   
        plataformas.append(Plataform(x=690,y=430,width=230,height=50,type=12))
        plataformas.append(Plataform(x=897,y=512,width=100,height=50,type=12))
        plataformas.append(Plataform(x=1020,y=540,width=800,height=50,type=12))


        coins_sprites = pygame.sprite.Group()

        coin1 = Item(170, 470)
        coin2 = Item(570, 479)
        coin3 = Item(714, 402)
        coin4 = Item(1304, 508)
        coins_sprites.add(coin1, coin2, coin3, coin4)
        super().__init__(pantalla, player, plataformas, background)