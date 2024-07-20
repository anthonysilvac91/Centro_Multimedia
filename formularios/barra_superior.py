import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR


class BarraSuperior(tk.Frame):
    def __init__(self, master, toggle_panel_callback):
        super().__init__(master, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.pack(side=tk.TOP, fill='both')
        self.toggle_panel_callback = toggle_panel_callback
        self.crear_controles()

    def crear_controles(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.buttonMenuLateral = tk.Button(self, text="\uf0c9", font=font_awesome, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white", command=self.toggle_panel_callback)
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.labelTitulo = tk.Label(self, text="CENTRO MULTIMEDIA DE ENTRETENIMIENTO")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=100)
        self.labelTitulo.pack(side=tk.LEFT)
