import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
import customtkinter as ctk

def retornar_Menu(cargarModificar, menu):
    cargarModificar.withdraw()
    menu.deiconify()


def ventana_Carga_Modificacion(menu):
    def ventana_Error(a):
        ventana_error = tk.Toplevel()
        # ?  Mensaje de error
        if (a == 1):
            ventana_error.title("Error")
            mensaje_error = ttk.Label(
                ventana_error, text="Ya existe el tipo de habitación")
        if (a == 2):
            ventana_error.title("Error")
            mensaje_error = ttk.Label(
                ventana_error, text="No se encontró el tipo de habitación")
        if (a == 3):
            ventana_error.title("Exito")
            mensaje_error = ttk.Label(
                ventana_error, text="La modificación se ha realizado con éxito")
        mensaje_error.pack(padx=20, pady=20)
        # ? Botón de cerrar
        boton_cerrar = ttk.Button(
            ventana_error, text="Aceptar", command=ventana_error.destroy)
        boton_cerrar.pack(padx=20, pady=10)
        ventana_error.mainloop()

    def guardar_Habitacion():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel"
        )
        mycursor = mydb.cursor()
        consulta = "SELECT * FROM tipo WHERE descripcion = %s"
        descripcion = caja_Descripcion.get()
        mycursor.execute(consulta, (descripcion,))

        resultado = mycursor.fetchall()
        if not resultado:
            consulta = "INSERT INTO tipo (descripcion, costo) VALUES(%s, %s)"
            costo = int(caja_Costo.get())
            mycursor.execute(consulta, (descripcion, costo))
            mydb.commit()
            actualizar_tabla()
        else:
            ventana_Error(1)

    def modificar_Habitacion():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel"
        )
        mycursor = mydb.cursor()
        consulta = "SELECT * FROM tipo WHERE descripcion = %s"
        descripcion = caja_Descripcion.get()
        mycursor.execute(consulta, (descripcion,))

        resultado = mycursor.fetchall()
        if not resultado:
            ventana_Error(2)
        else:
            consulta = "UPDATE tipo SET costo=%s WHERE descripcion=%s"
            costo = int(caja_Costo.get())
            mycursor.execute(consulta, (costo, descripcion))
            mydb.commit()
            actualizar_tabla()

    def actualizar_tabla():
        for i in tabla.get_children():
            tabla.delete(i)
        cargar_tabla()
        limpiar_Entrys()
        ventana_Error(3)

    def cargar_tabla():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT descripcion, costo FROM tipo")
        filas = mycursor.fetchall()
        for fila in filas:
            tabla.insert("", tk.END, values=(fila[0], fila[1]))

    def seleccion_Tabla(event):
        limpiar_Entrys()
        valores = tabla.item(tabla.focus(), "values")
        if valores:
            caja_Descripcion.insert(0, valores[0])
            caja_Costo.insert(0, valores[1])

    def limpiar_Entrys():
        caja_Costo.delete(0, tk.END)
        caja_Descripcion.delete(0, tk.END)

    cargarModificar = Tk()
    frm = ttk.Frame(cargarModificar, padding=10)
    cargarModificar.title("Cargar y Modificar")
    cargarModificar.resizable(0, 0)
    cargarModificar.protocol("WM_DELETE_WINDOW", cargarModificar)

    estiloMarco = ttk.Style()
    estiloMarco.configure('fondo.TFrame', background='#202123')
    frm = ttk.Frame(cargarModificar, padding=10, style='fondo.TFrame')

    frm.grid()

    # ?  Descripción y su respectiva caja de texto
    titulo = ttk.Label(frm, text="Descripción").grid(
        column=1, row=3, columnspan=2)
    caja_Descripcion = ttk.Entry(frm)
    caja_Descripcion.grid(column=1, row=4, padx=20,
                          pady=20, sticky="nsew", columnspan=2)

    # ?  Costo y su respectiva caja de texto
    ttk.Label(frm, text="Costo").grid(column=1, row=5, columnspan=2)
    caja_Costo = ttk.Entry(frm)
    caja_Costo.grid(column=1, row=6, padx=20, pady=20,
                    columnspan=2, sticky="nsew")

    # ?  Botones para guardar
    ttk.Button(frm, text="Guardar", command=guardar_Habitacion).grid(
        column=1, row=7, columnspan=2, padx=20, pady=20, sticky="nsew")
    # ?  Y modificar
    ttk.Button(frm, text="Modificar", command=modificar_Habitacion).grid(
        column=1, row=8, columnspan=2, padx=20, pady=20, sticky="nsew")
    # ?  salir/retroceder
    ttk.Button(frm, text="Atras", command=lambda: retornar_Menu(cargarModificar, menu)).grid(
        column=1, row=9, padx=20, pady=20, sticky="nsew", columnspan=2)

    #!  SI MUEVEN ESTAS COSAS DE LA TABLA DE LUGAR PETA, NO TOCAR XD
    columns = ('descripcion', 'costo')
    tabla = ttk.Treeview(frm, columns=columns, show='headings')
    tabla.heading('descripcion', text='Descripcion')
    tabla.heading('costo', text='Costo')
    tabla.grid(row=10, column=1, columnspan=2, padx=10,
               rowspan=8, pady=10, sticky="nsew")
    tabla.bind("<<TreeviewSelect>>", seleccion_Tabla)
    cargar_tabla()
    #!  IMANOL SI ESTÁS LEYENDO ESTO ES PORQUE ESTAS MOVIENDO COSAS, NO MUEVAS MIS COSAS CARAJO!!!!!!!!!!!!!!! 
    #NOTA DE IMANOL: EL MAINLOOP DE UN TOPLEVEL NO HACE FALTA XD
    #!!!       https://youtube.com/shorts/GsKhI30n3zA?feature=share
