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

        # Crear todos los frames
        for F in (WelcomeFrame, DataEntryFrame, ResultsFrame, CreditsFrame):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomeFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if cont == ResultsFrame:
            frame.actualizar_resultados()
        elif cont == CreditsFrame:
            frame.actualizar_creditos()