# import pygame
# from controller import pause
# from pygame.locals import *
# import sys
# from nivel import Nivel
# from player import Player
# from enemigo import Enemy
# from plataforma import Plataform
# from background import Background
# from item import Item
# from constantes import *
# from gui_form_prueba import FormPrueba

# flags = DOUBLEBUF
# screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
# pygame.init()
# pygame.mixer.music.load(r"sounds/sonido_intergalactic_odyssey.ogg")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.01)

# #form_menu = FormPrueba(screen, x=0, y=0, w=500, h=500, color_background=C_BLACK, color_border=C_GREEN, border_size=3,active=True)

# fuente = pygame.font.SysFont("Arial", 30, True)
# clock = pygame.time.Clock()
# # background = Background(0, 0, ANCHO_VENTANA, ALTO_VENTANA, f"images/locations/goku_house.png")
# # player = Player(x=0,y=400,speed_walk=6,speed_run=12,gravity=20,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)

# # enemigo1 = Enemy(x=600,y=450,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300)
# # enemigo2 = Enemy(x=700,y=450,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300)
# # enemies_group = pygame.sprite.Group()
# # enemies_group.add(enemigo1, enemigo2)
# # lista_balas_enemigos = pygame.sprite.Group()



# # plataformas = []
# # plataformas.append(Plataform(x=100,y=500,width=220,height=50,type=1))
# # plataformas.append(Plataform(x=500,y=500,width=150,height=50,type=2))   
# # plataformas.append(Plataform(x=690,y=430,width=230,height=50,type=12))
# # plataformas.append(Plataform(x=897,y=512,width=100,height=50,type=12))
# # plataformas.append(Plataform(x=1020,y=540,width=800,height=50,type=12))


# # coins_sprites = pygame.sprite.Group()

# # coin1 = Item(170, 470)
# # coin2 = Item(570, 479)
# # coin3 = Item(714, 402)
# # coin4 = Item(1304, 508)
# # coins_sprites.add(coin1, coin2, coin3, coin4)

# running = True
# while running:
#     time = int(pygame.time.get_ticks()/1000) #tiempo de juego
#     keys = pygame.key.get_pressed()
#     delta_ms = clock.tick(FPS)
#     lista_eventos = pygame.event.get()
#     #background.draw(screen)
#     contador_time = fuente.render("Tiempo: " + str(time),0, C_BLACK)
#     screen.blit(contador_time, (52, 25))
        
#     for event in lista_eventos:
#         # Salir
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         # Pausa
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_p:
#                 pygame.mixer.music.pause()
#                 pause()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             print(event.pos)
        
    
#     if form_menu.active:
#         form_menu.update(lista_eventos)
#         form_menu.draw()
    
    
#     # update de los enemigos
#     for enemy in enemies_group:
#         enemy.disparar_bala()
#         lista_balas_enemigos.add(enemy.balas)
#         enemy.balas.update()
#         enemy.balas.draw(screen)
#         enemy.update(delta_ms, enemies_group)
#         enemy.draw(screen)
        
#     for platforma in plataformas:
#         platforma.draw(screen)
        
#     for bala in player.lista_balas:
#         bala.update(enemies_group)
#         # Dibujar balas
#         player.lista_balas.draw(screen)


#     for coin in coins_sprites:
#         coin.update(delta_ms, player)
#         coin.draw(screen)
        
#     score_text = fuente.render(f"Puntuación: {player.score}", True, C_BLACK)
#     screen.blit(score_text, (1200, 25))
        

#     player.update(delta_ms,plataformas, keys)
#     player.draw(screen)

#     if running == True:
#         pygame.display.flip()
        
# pygame.quit()
    

