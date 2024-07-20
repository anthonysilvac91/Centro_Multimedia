import tkinter as tk
from tkinter import font
from config import COLOR_CUERPO_PRINCIPAL
import utilerias.util_ventana as util_ventana
from formularios.barra_superior import BarraSuperior
from formularios.menu_lateral import MenuLateral


class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config_window()
        self.create_panels()

    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Centro Multimedia')
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    def create_panels(self):
        self.barra_superior = BarraSuperior(self, self.toggle_panel)
        self.menu_lateral = MenuLateral(self)
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    
