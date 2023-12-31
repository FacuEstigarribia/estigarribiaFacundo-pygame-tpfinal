from player import *
from constantes import *
from auxiliar import Auxiliar
from bala_enemigo import BalaEnemigo

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self,enemy_data,p_scale=0.08) -> None:
        super().__init__()
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/WALK_00{0}.png",0,7,scale=enemy_data.get("p_scale"))
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/WALK_00{0}.png",0,7,flip=True,scale=enemy_data.get("p_scale"))
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/IDLE_00{0}.png",0,7,scale=enemy_data.get("p_scale"))
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/IDLE_00{0}.png",0,7,flip=True,scale=enemy_data.get("p_scale"))

        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = enemy_data.get("speed_walk")
        self.speed_run =  enemy_data.get("speed_run")
        self.gravity = enemy_data.get("gravity")
        self.jump_power = enemy_data.get("jump_power")
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = enemy_data.get("x")
        self.rect.y = enemy_data.get("y")
        self.collition_rect = pygame.Rect(enemy_data.get("x")+self.rect.width/3,enemy_data.get("y"),self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = enemy_data.get("y") + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = enemy_data.get("frame_rate_ms") 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = enemy_data.get("move_rate_ms")
        self.y_start_jump = 0
        self.jump_height = enemy_data.get("jump_height")

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = enemy_data.get("interval_time_jump")
        
        
        self.balas = pygame.sprite.Group()
        self.tiempo_ultimo_disparo = pygame.time.get_ticks()
   
   
    def set_x_animations_preset(self, move_x, animation_list: list[pygame.surface.Surface], look_r: bool):
        self.move_x = move_x
        self.actual_animation = animation_list
        self.is_looking_right = look_r
    
    #   Animaciones eje Y
    def set_y_animations_preset(self):
        self.move_x = self.speed_run if self.is_looking_right else -self.speed_run
        self.initial_frame = 0
  
    
    #   Seteo de limites de pantalla
    def set_borders_limits(self):
        pixels_move = 0
        if self.move_x > 0:
            pixels_move = self.move_x if self.rect.x < ANCHO_VENTANA - self.image.get_width() else 0
        elif self.move_x < 0:
            pixels_move = self.move_x if self.rect.x > 0 else 0
        return pixels_move
   
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            #self.rect.x += self.set_borders_limits()

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                self.is_fall = False
                self.change_x(self.move_x)
                if self.contador <= 50:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1 
                elif self.contador <= 100:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.contador += 1
                else:
                    self.contador = 0
    
    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno          

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0
                
    def disparar_bala(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_disparo > 5000:  
            bala = BalaEnemigo(self.rect.x, self.rect.centery, 3)  
            self.balas.add(bala)
            self.tiempo_ultimo_disparo = tiempo_actual

    def update(self,delta_ms,plataform_list):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms) 

    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def receive_shoot(self):
        self.lives -= 1