import tkinter as tk
from tkinter import *
from tkinter import ttk
import cargarModificar
import huespedes

def ventana_Cargar_Modificar():
    menu.withdraw()
    cargarModificar.ventana_Carga_Modificacion(menu)

def ventana_Huespedes():
    menu.withdraw()
    huespedes.ventana_huespedes(menu)

menu = tk.Tk()
forma = ttk.Frame(menu, padding=10)
menu.config(bg="#000")
forma.grid()

boton_Cargar_Huesped = ttk.Button(forma, text="Cargar Huesped", command=ventana_Huespedes)
boton_Cargar_Huesped.grid(column=1, row=1, padx=20, pady=20, sticky="nsew", columnspan = 3)

boton_Carga_Modificar = ttk.Button(forma, text="Cargar o Modificar Habitaciones", command=ventana_Cargar_Modificar)
boton_Carga_Modificar.grid(column=1, row=2, padx=20, pady=20, sticky="nsew", columnspan = 3)

boton_Finalizar = ttk.Button(forma, text="Salir", command=menu.destroy)
boton_Finalizar.grid(column=1, row=3, padx=20, pady=20, sticky="nsew", columnspan = 3)

menu.mainloop()