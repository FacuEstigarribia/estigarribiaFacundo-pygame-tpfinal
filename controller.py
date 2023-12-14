import pygame
import json
from constantes import DATA

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    pygame.mixer.music.play()
                    
def load_player_data() -> dict:
        with open(DATA, "r") as json_file:
            data = json.load(json_file)
        return data.get("player")