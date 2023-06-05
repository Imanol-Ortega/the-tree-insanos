import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import cargarModificar
import huespedes
import formulario_Tp_C


def ventana_Cargar_Modificar():
    menu.withdraw()
    cargarModificar.ventana_Carga_Modificacion(menu)


def ventana_Huespedes():
    menu.withdraw()
    huespedes.ventana_huespedes(menu)

def ventana_Formulario():
    menu.withdraw()
    formulario_Tp_C.ventana_Formulario_TP(menu)

menu = tk.Tk()
forma = ttk.Frame(menu, padding=10)
menu.title("Menu")

estiloFreim = ttk.Style()
estiloFreim.configure('fondo.TFrame', background='#202123')
forma = ttk.Frame(menu, padding=10, style='fondo.TFrame')

forma.grid()
menu.resizable(0, 0)
menu.protocol("WM_DELETE_WINDOW", menu)

boton_Cargar_Huesped = ctk.CTkButton(
    forma,
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

boton_Carga_Modificar = ctk.CTkButton( forma,
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

boton_Formulario_Tp = ctk.CTkButton(   forma,
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

boton_Finalizar = ctk.CTkButton(   forma,
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
