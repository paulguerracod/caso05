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

        # Frame de bienvenida
        class WelcomeFrame(tk.Frame):
            def __init__(self, parent, controller):
                super().__init__(parent)
        self.controller = controller
        
        lbl_titulo = tk.Label(self, text="¡Bienvenido a la Tienda de la Música!", font=('Arial', 14))
        lbl_titulo.pack(pady=20)
        
        lbl_nombre = tk.Label(self, text="¿Cuál es tu nombre?")
        lbl_nombre.pack(pady=5)
        
        self.entry_nombre = tk.Entry(self, width=30)
        self.entry_nombre.pack(pady=5)
        
        btn_continuar = ttk.Button(self, text="Continuar", command=self.continuar)
        btn_continuar.pack(pady=10)

    def continuar(self):
        nombre = self.entry_nombre.get()
        if nombre.strip():
            self.controller.usuario = nombre
            self.controller.show_frame(DataEntryFrame)
        else:
            messagebox.showwarning("Campo requerido", "Por favor ingresa tu nombre")
        
        # Frame de entrada de datos
        class DataEntryFrame(tk.Frame):
            def __init__(self, parent, controller):
                super().__init__(parent)
        self.controller = controller
        
        lbl_titulo = tk.Label(self, text="Datos de la compra", font=('Arial', 12))
        lbl_titulo.pack(pady=10)
        
        # Cantidad
        lbl_cantidad = tk.Label(self, text="Cantidad de discos:")
        lbl_cantidad.pack(pady=5)
        
        self.entry_cantidad = ttk.Entry(self)
        self.entry_cantidad.pack(pady=5)

                # Género
        lbl_genero = tk.Label(self, text="Género musical:")
        lbl_genero.pack(pady=5)
        
        self.genero_var = tk.StringVar()
        cbx_genero = ttk.Combobox(self, textvariable=self.genero_var, 
                                 values=["Salsa", "Rock", "Pop", "Folclore"])
        cbx_genero.pack(pady=5)
        
        btn_calcular = ttk.Button(self, text="Calcular", command=self.calcular)
        btn_calcular.pack(pady=20)

        def calcular(self):
        try:
            cantidad = int(self.entry_cantidad.get())
            genero = self.genero_var.get().lower()
            
            if cantidad <= 0:
                messagebox.showerror("Error", "La cantidad debe ser mayor a 0")
                return
                
            if not genero:
                messagebox.showerror("Error", "Selecciona un género musical")
                return
                
            precios = {
                "salsa": 56.00,
                "rock": 63.00,
                "pop": 87.00,
                "folclore": 120.50
            }
            
            self.controller.datos_compra = {
                "cantidad": cantidad,
                "genero": genero,
                "precio_unitario": precios[genero]
            }
            
            self.controller.show_frame(ResultsFrame)
            
        except ValueError:
            messagebox.showerror("Error", "Ingresa una cantidad válida")

        # Frame de resultados
class ResultsFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.lbl_genero = tk.Label(self, text="")
        self.lbl_genero.pack(pady=5)
        
        self.lbl_importe = tk.Label(self, text="")
        self.lbl_importe.pack(pady=5)
        
        self.lbl_descuento = tk.Label(self, text="")
        self.lbl_descuento.pack(pady=5)
        
        self.lbl_total = tk.Label(self, text="")
        self.lbl_total.pack(pady=5)
        
        self.lbl_obsequio = tk.Label(self, text="")
        self.lbl_obsequio.pack(pady=5)
        
        btn_continuar = ttk.Button(self, text="Ver créditos", command=lambda: controller.show_frame(CreditsFrame))
        btn_continuar.pack(pady=20)

    def actualizar_resultados(self):
        datos = self.controller.datos_compra
        cantidad = datos["cantidad"]
        genero = datos["genero"]
        precio = datos["precio_unitario"]
        
        def calcular_descuento(cant):
            if cant == 1:
                return 0
            elif cant == 4:
                return 0.06
            elif 5 <= cant <= 10:
                return 0.08
            elif cant > 10:
                return 0.102
            return 0
        
        def determinar_obsequio(gen, cant):
            if (gen == "pop" or gen == "rock") and cant > 6:
                return "Poster"
            return "Ninguno"
        
        importe_compra = cantidad * precio
        descuento = calcular_descuento(cantidad)
        importe_descuento = importe_compra * descuento
        total = importe_compra - importe_descuento
        obsequio = determinar_obsequio(genero, cantidad)
        
        self.lbl_genero.config(text=f"Género: {genero.capitalize()}")
        self.lbl_importe.config(text=f"Importe compra: S/. {importe_compra:.2f}")
        self.lbl_descuento.config(text=f"Descuento: S/. {importe_descuento:.2f}")
        self.lbl_total.config(text=f"Total a pagar: S/. {total:.2f}")
        self.lbl_obsequio.config(text=f"Obsequio: {obsequio}")