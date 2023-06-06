import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
import customtkinter as ctk

#?  Retorno al menú
def retornar_Menu(cargarModificar, menu):
    cargarModificar.withdraw()
    menu.deiconify()


def ventana_Carga_Modificacion(menu):
    #?  Ventanas de aviso
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
        #?  Imprime un mensaje al guardar exitosamente
        if (a == 3):
            ventana_error.title("Exito")
            mensaje_error = ttk.Label(
                ventana_error, text="La modificación se ha realizado con éxito")
        mensaje_error.pack(padx=20, pady=20)
        # ? Botón de cerrar ventana de aviso
        boton_cerrar = ttk.Button(ventana_error, 
                                  text="Aceptar", 
                                  command=ventana_error.destroy)
        boton_cerrar.pack(padx=20, pady=10)
        ventana_error.mainloop()

    
    def guardar_Habitacion():
        #*  Conecta a la base de datos y crea un cursor
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel"
        )
        mycursor = mydb.cursor()
        #*  Tomo el contenido de la caja_Descripción ingresada por el usuario y realizo una consulta SELECT
        consulta = "SELECT * FROM tipo WHERE descripcion = %s"
        descripcion = caja_Descripcion.get()
        mycursor.execute(consulta, (descripcion,))
        resultado = mycursor.fetchall()
        #*  Pregunto si hay una coincidencia en la tabla "tipo" para determinar si se está intentando ingresar 2 veces el mismo tipo de habitación
        if not resultado:
        #*  En caso de que no encuentre coincidencias, realiza un INSERT de los valores ingresados
            consulta = "INSERT INTO tipo (descripcion, costo) VALUES(%s, %s)"
            costo = int(caja_Costo.get())
            mycursor.execute(consulta, (descripcion, costo))
            mydb.commit()
            #*  Se llama a la función a actualizar tabla
            actualizar_tabla()
        else:
            #*  Se llama a la función ventana Error y se le envía el valor 1 para imprimir el mensaje correspondiente
            ventana_Error(1)

    def modificar_Habitacion():
        #*  Se conecta a la base de datos
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel"
        )
        #*  Se buscan coincidencias
        mycursor = mydb.cursor()
        consulta = "SELECT * FROM tipo WHERE descripcion = %s"
        descripcion = caja_Descripcion.get()
        mycursor.execute(consulta, (descripcion,))

        resultado = mycursor.fetchall()
        #*  Si no encuentra coincidencias se imprime un mensaje de error
        if not resultado:
            ventana_Error(2)
        #*  Si encuentra coincidencias, actualiza el tipo de habitación
        else:
            consulta = "UPDATE tipo SET costo=%s WHERE descripcion=%s"
            costo = int(caja_Costo.get())
            mycursor.execute(consulta, (costo, descripcion))
            mydb.commit()
            #*  Se actualiza la tabla
            actualizar_tabla()

    def actualizar_tabla():
        #*  Se utiliza un for para recorrer la tabla e ir borrandola en la posición correspondiente
        for i in tabla.get_children():
            tabla.delete(i)
        #*  Se llama a la función cargar tabla
        cargar_tabla()
        #*  Se llama a la función limpiar entry
        limpiar_Entrys()
        #*  Se utiliza la función ventana_Error para informar que se realizó un update
        ventana_Error(3)

    def cargar_tabla():
        #*  Se accede a la base de datos
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT descripcion, costo FROM tipo")
        filas = mycursor.fetchall()
        #*  Se recorre el treeview insertando los elementos de la tabla "tipos"
        for fila in filas:
            tabla.insert("", tk.END, values=(fila[0], fila[1]))

    def seleccion_Tabla(event):
        #*  Se llama a la función limpiar Entrys
        limpiar_Entrys()
        #*  Se asignan los valores de la tabla a los que se les haga click (on focus)
        valores = tabla.item(tabla.focus(), "values")
        #*  Se verifica que valores contenga algún valor
        if valores:
            #*  Inserta el primer valor en caja_Descripcion y el segundo en caja_Costo
            caja_Descripcion.insert(0, valores[0])
            caja_Costo.insert(0, valores[1])

    def limpiar_Entrys():
        #*  Borra el contenido de caja_Costo y caja_Descripcion
        caja_Costo.delete(0, tk.END)
        caja_Descripcion.delete(0, tk.END)

    #?  Construyo y doy estilo a la ventana
    cargarModificar = tk.Tk()
    cargarModificar.title("Cargar y Modificar")
    cargarModificar.geometry("600x300")
    cargarModificar.config(background="#202123")
    cargarModificar.resizable(0, 0)
    cargarModificar.protocol("WM_DELETE_WINDOW", cargarModificar)

    


    # ?  Descripción y su respectiva caja de texto
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
