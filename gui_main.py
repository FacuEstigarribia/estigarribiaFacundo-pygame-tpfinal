import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form_prueba import FormPrueba
flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()


form_menu = FormPrueba(screen, x=0, y=0, w=500, h=500, color_background=C_BLACK, color_border=C_GREEN, border_size=3,active=True)

while True:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)
    
    
    if form_menu.active:
        form_menu.update(lista_eventos)
        form_menu.draw()
    
    pygame.display.flip()