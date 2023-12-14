import pygame
import random
import sys
import json
from controller import *
from pygame.locals import *
from constantes import *
from player import Player
from background import Background
from enemigo import Enemy
from plataforma import Plataform
from item import Item
from gui_form_prueba import FormPrueba

class Nivel:
    
    def __init__(self) -> None:
        self.state_1 = "stage_1"
        self.state_2 = "stage_2"
        self.data = self.load_level_data()  
        self.background_1 = Background(0, 0, ANCHO_VENTANA, ALTO_VENTANA,self.data[self.state_1]["scenario"]["background"])
        self.background_2 = Background(0, 0, ANCHO_VENTANA, ALTO_VENTANA,self.data[self.state_2]["scenario"]["background"])
        self.music_level1 = pygame.mixer.music.load(self.data[self.state_1]["scenario"]["music"])
        self.music_level1 = pygame.mixer.music.play(-1)
        self.music_level1 = pygame.mixer.music.set_volume(0.01)
        self.player = Player(self.data[self.state_1]["player"])
        self.enemies_group_1 = pygame.sprite.Group()
        self.enemies_group_2 = pygame.sprite.Group()
        self.plataformas_1 = pygame.sprite.Group()
        self.plataformas_2 = pygame.sprite.Group()
        self.items_1 = pygame.sprite.Group()
        self.items_2 = pygame.sprite.Group()
        
        # For para cargar enemigos nivel uno
        for index in range(self.data[self.state_1]["enemies"]["enemies_mount"]):
            data = self.data[self.state_1]["enemies"]["enemies_pos"][index]
            enemigo = Enemy(data, 1)
            self.enemies_group_1.add(enemigo)
            
        # For para cargar enemigos nivel dos
        for index in range(self.data[self.state_2]["enemies"]["enemies_mount"]):
            data = self.data[self.state_2]["enemies"]["enemies_pos"][index]
            enemigo = Enemy(data, 1)
            self.enemies_group_2.add(enemigo)
        
        # For para cargar plataformas nivel uno
        for index in range(self.data[self.state_1]["plataformas"]["plataformas_mount"]):
            coords = self.data[self.state_1]["plataformas"]["plataformas_pos"][index]
            plataforma = Plataform(coords, 1)
            self.plataformas_1.add(plataforma)
            
        #For para cargar plataformas nivel dos
        for index in range(self.data[self.state_2]["plataformas"]["plataformas_mount"]):
            coords = self.data[self.state_1]["plataformas"]["plataformas_pos"][index]
            plataforma = Plataform(coords, 1)
            self.plataformas_2.add(plataforma)
            
        # For para cargar items nivel uno
        for index in range(self.data[self.state_1]["items"]["items_mount"]):
            coords = self.data[self.state_1]["items"]["items_pos"][index]
            item = Item(coords)
            self.items_1.add(item)
            
        # For para cargar items nivel dos
        for index in range(self.data[self.state_2]["items"]["items_mount"]):
            coords = self.data[self.state_2]["items"]["items_pos"][index]
            item = Item(coords)
            self.items_2.add(item)

        
        
    def load_level_data(self):
        with open(DATA, "r") as json_file:
            return json.load(json_file)

        
    def stage_1(self):
        running = True
        while running:
            time = int(pygame.time.get_ticks()/1000) #tiempo de juego
            keys = pygame.key.get_pressed()
            delta_ms = clock.tick(FPS)
            lista_eventos = pygame.event.get()
            self.background_1.draw(screen)
            contador_time = fuente.render("Tiempo: " + str(time),0, C_BLACK)
            screen.blit(contador_time, (52, 25))
                
            for event in lista_eventos:
                # Salir
                if event.type == pygame.QUIT:
                    running == False
                    sys.exit()
                # Pausa
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pygame.mixer.music.pause()
                        pause()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
            
            
            # update de los enemigos
            for enemy in self.enemies_group_1:
                enemy.update(delta_ms, self.enemies_group_1)
                enemy.draw(screen)
                
            for platforma in self.plataformas_1:
                platforma.draw(screen)
                
            for bala in self.player.lista_balas:
                bala.update(self.enemies_group_1)
                self.player.lista_balas.draw(screen)


            for coin in self.items_1:
                coin.update(delta_ms, self.player)
                coin.draw(screen)
                
            score_text = fuente.render(f"Puntuación: {self.player.score}", True, C_BLACK)
            screen.blit(score_text, (1200, 25))
                

            self.player.update(delta_ms,self.plataformas_1, keys)
            self.player.draw(screen)

            
            if len(self.enemies_group_1.sprites()) == 0 and len(self.items_1.sprites()) == 0:
                self.stage_2()
            

            if running == True:
                pygame.display.flip()
    
    def stage_2(self):
        print("entre al stage 2")
        running = True
        while running:
            time = int(pygame.time.get_ticks()/1000) #tiempo de juego
            keys = pygame.key.get_pressed()
            delta_ms = clock.tick(FPS)
            lista_eventos = pygame.event.get()
            self.background_2.draw(screen)
            contador_time = fuente.render("Tiempo: " + str(time),0, C_BLACK)
            screen.blit(contador_time, (52, 25))
            
            spawn_timer = pygame.time.get_ticks()
                
            for event in lista_eventos:
                # Salir
                if event.type == pygame.QUIT:
                    running == False
                    sys.exit()
                # Pausa
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pygame.mixer.music.pause()
                        pause()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    
            now = pygame.time.get_ticks()
            if now - spawn_timer > 2000:  # Genera un enemigo cada 2000 milisegundos (2 segundos)
                spawn_timer = now
                new_enemy = Enemy(x=random.randint(40, 1350), y=random.randint(60, 1350), speed_walk=6)
                self.enemies_group_2.add(new_enemy)
            
            # update de los enemigos
            for enemy in self.enemies_group_2:
                enemy.update(delta_ms, self.enemies_group_2)
                enemy.draw(screen)
                
            for platforma in self.plataformas_2:
                platforma.draw(screen)
                
            for bala in self.player.lista_balas:
                bala.update(self.enemies_group_2)
                self.player.lista_balas.draw(screen)


            for coin in self.items_2:
                coin.update(delta_ms, self.player)
                coin.draw(screen)
                
            score_text = fuente.render(f"Puntuación: {self.player.score}", True, C_BLACK)
            screen.blit(score_text, (1200, 25))
                

            self.player.update(delta_ms,self.plataformas_2, keys)
            self.player.draw(screen)

            

            if running == True:
                pygame.display.flip()

    def nivel_manager(self):
        if self.state_1 == "stage_1":
            self.stage_1()
        if self.state_2 == "stage_2":
            self.stage_2()


####################################
pygame.init()
flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
clock = pygame.time.Clock()
fuente = pygame.font.SysFont("Arial", 30, True)
#form_menu = FormPrueba(screen, x=0, y=0, w=500, h=500, color_background=C_BLACK, color_border=C_GREEN, border_size=3,active=True)
nivel = Nivel()
running = True
while running:
    nivel.stage_1()
pygame.quit()
    
    

