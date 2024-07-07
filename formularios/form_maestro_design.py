import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_HOVER, COLOR_MENU_LATERAL
import utilerias.util_ventana as util_ventana
# import utilerias.util_img as util_img

class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        

    def config_window(self):
        #Configuracion inicial de la ventana
        self.title('Centro Multimedia')
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)    
    
    def paneles(self):
        #configuracion de los paneles en la ventana
        self.barra_superior = tk.Frame(self, bg= COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill= 'both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white" )
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.labelTitulo = tk.Label(self.barra_superior, text="CENTRO MULTIMEDIA DE ENTRETENIMIENTO")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=100)
        self.labelTitulo.pack(side=tk.LEFT)

        

    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.buttonPeliculas = tk.Button(self.menu_lateral, text="Películas", font=font_awesome, fg="white", bd=0, bg=COLOR_MENU_LATERAL, width=ancho_menu, height=alto_menu )
        self.buttonPeliculas.pack(side=tk.TOP)
        self.configurar_boton_menu(self.buttonPeliculas)

        self.buttonSeries = tk.Button(self.menu_lateral, text="Series", font=font_awesome, fg="white", bd=0, bg=COLOR_MENU_LATERAL, width=ancho_menu, height=alto_menu  )
        self.buttonSeries.pack(side=tk.TOP)
        self.configurar_boton_menu(self.buttonSeries)

        self.buttonAnime = tk.Button(self.menu_lateral, text="Anime", font=font_awesome, fg="white", bd=0, bg=COLOR_MENU_LATERAL, width=ancho_menu, height=alto_menu  )
        self.buttonAnime.pack(side=tk.TOP)
        self.configurar_boton_menu(self.buttonAnime)

        self.buttonConfiguracion= tk.Button(self.menu_lateral, text="Configuracion", font=font_awesome, fg="white", bd=0, bg=COLOR_MENU_LATERAL, width=ancho_menu, height=alto_menu  )
        self.buttonConfiguracion.pack(side=tk.TOP)
        self.configurar_boton_menu(self.buttonConfiguracion)

    def configurar_boton_menu(self, button):
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))
    
    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_HOVER, fg='white')

    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white')



    
