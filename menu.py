import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import cargarModificar
import huespedes
import formulario_Tp_C

#?  Llama al archivo con la función de modificación y carga de habitaciones existentes
def ventana_Cargar_Modificar():
    menu.withdraw()
    cargarModificar.ventana_Carga_Modificacion(menu)

#?  Llama al archivo con la función de manejo de huéspedes
def ventana_Huespedes():
    menu.withdraw()
    huespedes.ventana_huespedes(menu)

#?  Llama al archivo con la función de manejo de ingresos por tipo de habitación
def ventana_Formulario():
    menu.withdraw()
    formulario_Tp_C.ventana_Formulario_TP(menu)

#?  Construyo y doy estilo a la ventana
menu = tk.Tk()
menu.title("Menu")
menu.geometry("230x300")
menu.configure(background='#202123')

#?  Evita que se pueda redimensionar, maximizar y cerrar usando los botones propios de windows
menu.resizable(0, 0)
menu.protocol("WM_DELETE_WINDOW", menu)

#?  Botón para ir a la función de manejo de huéspedes
boton_Cargar_Huesped = ctk.CTkButton(
    menu,
    text="Cargar Huesped",
    corner_radius=0,
    font=("Helvetica", 12, "bold"),
    text_color="#fff",
    fg_color="#343541",
    hover_color="#444654",
    command=ventana_Huespedes)
boton_Cargar_Huesped.grid(column=1,
                        row=1,
                        padx=20,
                        pady=20,
                        sticky="nsew",
                        columnspan=3)

#?  Botón para ir a la función de manejo de habitaciones
boton_Carga_Modificar = ctk.CTkButton( menu,
                                    text="Cargar o Modificar Habitaciones",
                                    corner_radius=0,
                                    font=("Helvetica", 12, "bold"),
                                    text_color="#fff",
                                    fg_color="#343541",
                                    hover_color="#444654",
                                    command=ventana_Cargar_Modificar)
boton_Carga_Modificar.grid( column=1,
                            row=2,
                            padx=20,
                            pady=20,
                            sticky="nsew",
                            columnspan=3)

#?  Botón para ir a la función de manejo de ingresos por tipo de habitación
boton_Formulario_Tp = ctk.CTkButton(   menu,
                                    text="Ingresos por Habitacion",
                                    corner_radius=0,
                                    font=("Helvetica", 12, "bold"),
                                    text_color="#fff",
                                    fg_color="#343541",
                                    hover_color="#444654",
                                    command=ventana_Formulario)
boton_Formulario_Tp.grid(   column=1,
                            row=3,
                            padx=20,
                            pady=20,
                            sticky="nsew",
                            columnspan=3)

#?  Botón para salir
boton_Finalizar = ctk.CTkButton(   menu,
                                text="Salir",
                                corner_radius=0,
                                font=("Helvetica", 12, "bold"),
                                text_color="#fff",
                                fg_color="#343541",
                                hover_color="#444654",
                                command=menu.destroy)
boton_Finalizar.grid(   column=1,
                        row=4,
                        padx=20,
                        pady=20,
                        sticky="nsew",
                        columnspan=3)

menu.mainloop()
