import pygame
from auxiliar import Auxiliar
from constantes import *
from bala import Bala
from item import Item

class Player(pygame.sprite.Sprite):
    def __init__(self,player_data, p_scale = 0.2) -> None:
        super().__init__()
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/cowgirl/Idle ({0}).png",1,10,flip=False,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/cowgirl/Idle ({0}).png",1,10,flip=True,scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/cowgirl/Jump ({0}).png",1,10,flip=False, scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/cowgirl/Jump ({0}).png",1,10,flip=True,scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/cowgirl/Run ({0}).png",1,8,flip=False,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/cowgirl/Run ({0}).png",1,8,flip=True,scale=p_scale)

        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  player_data.get("speed_walk")
        self.speed_run =  player_data.get("speed_run")
        self.gravity = player_data.get("gravity")
        self.jump_power = player_data.get("jump_power")
        ##############################
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = player_data.get("coord_x")
        self.rect.y = player_data.get("coord_y")
        self.rect.centery = player_data.get("coord_y")
        self.rect.topleft = (player_data.get("coord_x"), player_data.get("coord_y"))
        self.direction = DIRECTION_R
        self.collition_rect = pygame.Rect(player_data.get("coord_x")+self.rect.width/3,player_data.get("coord_y"),self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = player_data.get("coord_y") + self.rect.height - GROUND_COLLIDE_H
    
        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False
        self.is_stand = True
        
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = player_data.get("frame_rate_ms") 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = player_data.get("move_rate_ms")
        self.y_start_jump = 0
        self.jump_height = player_data.get("jump_height")

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = player_data.get("interval_time_jump")
        self.is_looking_right = True
        
        self.lista_balas = pygame.sprite.Group()
        self.last_shoot_time = 0
        self.shoot_cooldown = 1000
        
    
    def __set_x_animations_preset(self, move_x, animation_list: list[pygame.surface.Surface], look_r: bool):
        self.move_x = move_x
        self.animation = animation_list
        self.is_looking_right = look_r
        
    
    def __set_y_animations_preset(self):
        self.move_y = -self.jump_power
        self.move_x = self.speed_run if self.is_looking_right else -self.speed_run
        self.animation = self.jump_r if self.is_looking_right else self.jump_l
        self.initial_frame = 0
        self.is_jumping = True
        
    def __set_borders_limits(self):
        pixels_move = 0
        if self.move_x > 0:
            pixels_move = self.move_x if self.rect.x < ANCHO_VENTANA - self.image.get_width() else 0
        elif self.move_x < 0:
            pixels_move = self.move_x if self.rect.x > 0 else 0
        return pixels_move
    
    
    def walk(self,direction):
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.__set_x_animations_preset(self.speed_walk, self.walk_r, look_r=True)
                    
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.__set_x_animations_preset(-self.speed_walk, self.walk_l, look_r=False)
    
    #### BALAS #####    
    
    def crear_bala(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shoot_time > self.shoot_cooldown:
            self.last_shoot_time = current_time
            x = self.rect.x  
            y = self.rect.centery
            dir = self.direction
            return Bala(x, y, dir, 10)  
        else:
            return None        
    #### BALAS ##### 

    def receive_shoot(self):
        self.lives -= 1

    def knife(self,on_off = True):
        
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                    print("entre al metodo knife")
                else:
                    self.animation = self.knife_l
                    
    def shoot(self,on_off = True):
        
        self.is_shoot = on_off
        if on_off == True and  self.is_jump == False and self.is_fall == False:
            
            if self.animation != self.shoot_r and self.animation != self.shoot_l:
                self.frame = 0
                #self.is_shoot = True
                if self.direction == DIRECTION_R:
                    print("Método shoot llamado.")
                    self.animation = self.shoot_r
                    self.create_bala(DIRECTION_R)
                else:
                    self.animation = self.shoot_l
                    self.create_bala(DIRECTION_L)
      

    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()
            
    def stay(self):
        if(self.is_knife or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

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
           
            #self.move_x += self.__set_borders_limits()
            
            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False            

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
 
    def update(self,delta_ms,plataform_list, keys):
        self.events(delta_ms, keys)
        #self.actualizar_proyectil(screen)
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        
    
    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect.topleft)
        

    def events(self,delta_ms,keys,):
        self.tiempo_transcurrido += delta_ms
        
        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

        if(not keys[pygame.K_a]):
            self.shoot(False)  

        if(not keys[pygame.K_a]):
            self.knife(False)  

        if(keys[pygame.K_s] and not keys[pygame.K_a]) and not self.is_shoot:
            nueva_bala = self.crear_bala()
            if nueva_bala:
                self.lista_balas.add(nueva_bala)
                print('estoy disparando')
        if(keys[pygame.K_a] and not keys[pygame.K_s]):
            self.knife()