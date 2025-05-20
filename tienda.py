import tkinter as tk 
from tkinter import ttk, messagebox

# Clase principal de la aplicación
class MusicStoreApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tienda de la Música")
        self.geometry("500x400")
        self.resizable(False, False)
        
        # Contenedor principal
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.usuario = ""
        self.datos_compra = {}