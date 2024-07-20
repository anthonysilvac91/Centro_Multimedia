import tkinter as tk
from tkinter import font
from config import COLOR_MENU_LATERAL, COLOR_MENU_HOVER

class MenuLateral(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=COLOR_MENU_LATERAL, width=150)
        self.pack(side=tk.LEFT, fill='both', expand=False)
        self.crear_controles()

    def crear_controles(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=12)

        botones = ["Películas", "Series", "Anime", "Configuracion"]
        for texto in botones:
            boton = tk.Button(self, text=texto, font=font_awesome, fg="white", bd=0, bg=COLOR_MENU_LATERAL, width=ancho_menu, height=alto_menu)
            boton.pack(side=tk.TOP)
            self.configurar_boton_menu(boton)

    def configurar_boton_menu(self, button):
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_HOVER, fg='white')

    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

