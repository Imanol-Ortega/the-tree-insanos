import tkinter as tk
from tkinter import *
from tkinter import ttk
import cargarModificar

def ventana_Cargar_Modificar():
    menu.withdraw()
    cargarModificar.ventana_Carga_Modificacion(menu)



menu = tk.Tk()

boton = ttk.Button(menu, text="Añadir Modificar", command=ventana_Cargar_Modificar)
boton.pack()


menu.mainloop()