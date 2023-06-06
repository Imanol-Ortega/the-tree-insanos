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

    cargarModificar = tk.Tk()
    cargarModificar.title("Cargar y Modificar")
    cargarModificar.geometry("600x300")
    cargarModificar.config(background="#202123")
    cargarModificar.resizable(0, 0)
    cargarModificar.protocol("WM_DELETE_WINDOW", cargarModificar)

    


    # ?  Descripción y su respectiva caja de texto
    #Think fast chukklenuts
    #blank = ttk.Label(cargarModificar, text="blank")
    #blank.grid(column=1,row=1,columnspan=2)
    #blank.configure(background="#202123",foreground="#202123")
    
    titulo = ttk.Label(cargarModificar, 
                       text="Descripción")
    titulo.grid(column=1,
                row=3,
                pady= 5,
                columnspan=2)
    titulo.configure(font=("Helvetica", 12, "bold"),
                     background="#202123",
                     foreground="#fff")
    caja_Descripcion = ttk.Entry(cargarModificar)
    caja_Descripcion.grid(column=1, 
                          row=4, 
                          padx=20,
                          pady=10, 
                          sticky="nsew", 
                          columnspan=2)

    # ?  Costo y su respectiva caja de texto
    label_Costo = ttk.Label(cargarModificar,
                            text="Costo")
    label_Costo.configure(font=("Helvetica", 12, "bold"),
                     background="#202123",
                     foreground="#fff")
    label_Costo.grid(column=1,
                     row=5,
                     pady=5,
                     columnspan=2)
    caja_Costo = ttk.Entry(cargarModificar)
    caja_Costo.grid(column=1, 
                    row=6,
                    padx=20, 
                    pady=10,
                    columnspan=2,
                    sticky="nsew")

    # ?  Botones para guardar
    boton_Guardar = ctk.CTkButton(cargarModificar, 
                                  text="Guardar",
                                    corner_radius=0,
                                    font=("Helvetica", 12, "bold"),
                                    text_color="#fff",
                                    fg_color="#343541",
                                    hover_color="#444654",
                                  command=guardar_Habitacion)
    boton_Guardar.grid(column=1, 
                       row=7, 
                       columnspan=2, 
                       padx=20, 
                       pady=10, 
                       sticky="nsew")
    # ?  Y modificar
    boton_Modificar = ctk.CTkButton(cargarModificar, 
                                    text="Modificar",
                                    corner_radius=0,
                                    font=("Helvetica", 12, "bold"),
                                    text_color="#fff",
                                    fg_color="#343541",
                                    hover_color="#444654", 
                                    command=modificar_Habitacion)
    boton_Modificar.grid(column=1, 
                         row=8, 
                         columnspan=2, 
                         padx=20, 
                         pady=10, 
                         sticky="nsew")
    # ?  salir/retroceder
    boton_Salir = ctk.CTkButton(cargarModificar, 
                                text="Atras",
                                corner_radius=0,
                                font=("Helvetica", 12, "bold"),
                                text_color="#fff",
                                fg_color="#343541",
                                hover_color="#444654",
                                command=lambda: retornar_Menu(cargarModificar, menu))
    boton_Salir.grid(column=1, 
                     row=9, 
                     padx=20, 
                     pady=10, 
                     sticky="nsew", 
                     columnspan=2)

    #!  SI MUEVEN ESTAS COSAS DE LA TABLA DE LUGAR PETA, NO TOCAR XD
    columns = ('descripcion', 'costo')
    tabla = ttk.Treeview(cargarModificar, columns=columns, show='headings', style="estiloArboreo.Treeview")
    tabla.heading('descripcion', text='Descripcion')
    tabla.heading('costo', text='Costo')
    tabla.grid(row=1, column=10, columnspan=2, padx=10,
               rowspan=8, pady=10, sticky="nsew")
    tabla.bind("<<TreeviewSelect>>", seleccion_Tabla)



    cargar_tabla()
    #!  IMANOL SI ESTÁS LEYENDO ESTO ES PORQUE ESTAS MOVIENDO COSAS, NO MUEVAS MIS COSAS CARAJO!!!!!!!!!!!!!!
    #! NOTA DE IMANOL: EL MAINLOOP DE UN TOPLEVEL NO HACE FALTA XD
    #?  Eddie: Ah... xD
    #!!!       https://youtube.com/shorts/GsKhI30n3zA?feature=share
