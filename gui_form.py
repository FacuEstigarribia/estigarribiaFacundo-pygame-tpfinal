import pygame
from constantes import *
from pygame.locals import *
from gui_widget import Widget


#No se instancia. Es la base de la jerarquia
class Form(Widget):
    forms_dict = {}
    def __init__(self, screen:pygame.Surface, x: int, y:int, w:int ,h: int, color_background,color_border = "Black", border_size: int = -1, active = True):
        super().__init__(screen, x,y,w,h, color_background, color_border, border_size)
        
        self._slave = pygame.Surface((w,h))
        self.slave_rect = self._slave.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.lista_widgets = []
        self.hijo = None
        self.dialog_result = None
        self.padre = None
    
    @staticmethod
    def set_active(name):
        for aux_form in Form.forms_dict.values():
            aux_form.active = False
        Form.forms_dict[name] = True
        
    @staticmethod
    def get_active():
        for aux_form in Form.forms_dict.values():
            if aux_form.active:
                return aux_form
        return None
    
    def show_dialog(self, formulario):
        self.hijo = formulario
        self.hijo.padre = self

    def end_dialog(self):
        self.dialog_result = "OK"
        self.close()

    def close(self):
        self.active = False

    def verificar_dialog_result(self):
        return self.hijo == None or self.hijo.dialog_result != None
    
    def render(self):
        pass
    
    def update(self, lista_eventos):
        pass
    
    def draw(self):
        self._master.blit(self._slave, self.slave_rect)