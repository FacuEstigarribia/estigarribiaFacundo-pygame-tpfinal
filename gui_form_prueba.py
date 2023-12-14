import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox



class FormPrueba(Form):
    
    
    def __init__(self, screen: pygame.Surface, x: int, y: int, w:int, h: int, color_background, color_border = "Black", border_size: int = -1, active = True):
    
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)

        self.flag_play = True
        
        self.volumen = 0.2
                
        pygame.mixer.init()
        
        pygame.mixer.music.load(r"resources/Vengeance (Loopable).wav")
        
        pygame.mixer.music.set_volume(self.volumen)
        
        pygame.mixer.music.play(-1)
        


        self.txt_nombre = TextBox(self._slave, x, y, 
                                  50, 50, 150, 30, 
                                  "gray","white","red","blue",2,
                                  "Comic Sans MS", 15, "black")
        
        self.btn_play_music = Button(self._slave, x, y, 100, 600,
                               100, 50,
                               "red", "blue", 
                               self.btn_play_music_click, "",
                               "Pause", "Verdana",15, "white"
                               )
        
        self.btn_play_game = Button(self._slave, x, y, 100, 300,
                               100, 50,
                               "red", "blue", 
                               self.btn_play_game_click, "",
                               "Play Game", "Verdana",15, "white"
                               )

            
        self.lista_widgets.append(self.txt_nombre)
        self.lista_widgets.append(self.btn_play_music)
        self.lista_widgets.append(self.btn_play_game)
    
    
    def btn_play_music_click(self, param):
        if self.flag_play:
           pygame.mixer.music.pause()
           self.btn_play_music._color_background = "blue"
           
           self.btn_play_music.set_text("Play")
        else:
            
            pygame.mixer.music.unpause()
            self.btn_play_music._color_background = "red"
            self.btn_play_music.set_text("Pause")
            
        
        self.flag_play = not self.flag_play
        
    def btn_play_game_click(self, param):
        self.active = False
     
        
        