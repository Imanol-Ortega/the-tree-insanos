import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter
import mysql.connector


def ventana_huespedes():
    root_tk = tk.Toplevel()
    root_tk.geometry("1200x500")
    root_tk.title("Huespedes")
    root_tk.config(bg="#000")
    datos = {}
    seleccion = 0
    descuento = 0
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hotel"
    )
    mycursor = mydb.cursor()

    def filtrado(event):
        for i in tree.get_children():
            tree.delete(i)
        tecla = event.char
        tecla_presionada = cajaHabitacion.get()
        tecla_presionada = tecla_presionada + tecla
        print("tecla: ", tecla_presionada)
        cargar_tabla1(tecla_presionada,
                      "SELECT id,NuHabitacion,Tipo,Costo,Dias,SubTotal,Descuento,Total FROM cliente WHERE Estado = 1 AND NuHabitacion LIKE")

    def guardar():
        global descuento
        if cajaHabitacion.get() != '' and item_selected2(True) != 0 and cajaDias.get() != '' and radio_var.get() != 0:
            Nuero = int(cajaHabitacion.get())
            tipo = item_selected2(True)
            dias = int(cajaDias.get())
            tipoPago = int(radio_var.get())
            mycursor.execute("SELECT id FROM cliente")
            id = mycursor.fetchall()
            for ids in id:
                if Nuero in ids:
                    mycursor.execute("UPDATE cliente SET Estado =%s WHERE id = %s",
                                     (2, ids[0]))
                    mydb.commit()
            if tipoPago == 1:
                if dias > 5:
                    descuento = 0.05
            elif tipoPago == 2:
                descuento = 0.1
            if dias > 10:
                descuento = descuento + 0.02
            subtotal = dias*int(tipo[1])
            total = subtotal - (subtotal*descuento)
            mycursor.execute("INSERT INTO cliente (NuHabitacion,Tipo,Costo,Dias,SubTotal,Descuento,Total,Estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                             (Nuero, tipo[0], tipo[1], dias, subtotal, descuento*100, total, 1))
            mydb.commit()
            for i in tree.get_children():
                tree.delete(i)
            cargar_tabla1(
                '', "SELECT id,NuHabitacion,Tipo,Costo,Dias,SubTotal,Descuento,Total FROM cliente WHERE Estado = 1 AND NuHabitacion LIKE")

    def limpiar():
        cajaDias.delete(0, tk.END)
        cajaHabitacion.delete(0, tk.END)
        credito._variable.set(0)
        contado._variable.set(0)
        tree2.selection_remove(tree2.focus())
        tree.selection_remove(tree.focus())

    def borrar():
        seleccionado = item_selected1(True)
        if seleccionado:
            mycursor.execute("DELETE FROM cliente WHERE id=%s ", [
                             seleccionado[0]])
            mydb.commit()
            for i in tree.get_children():
                tree.delete(i)
            cargar_tabla1(
                '', "SELECT id,NuHabitacion,Tipo,Costo,Dias,SubTotal,Descuento,Total FROM cliente WHERE Estado = 1 AND NuHabitacion LIKE")

    def modificar():
        if seleccion:
            mycursor.execute("UPDATE cliente SET Dias = %s WHERE id = %s",
                             (int(cajaDias.get()), int(seleccion)))
            mydb.commit()
            for i in tree.get_children():
                tree.delete(i)
            cargar_tabla1(
                '', "SELECT id,NuHabitacion,Tipo,Costo,Dias,SubTotal,Descuento,Total FROM cliente WHERE Estado = 1 AND NuHabitacion LIKE")

    def cargar_tabla1(tecla, sql):
        mycursor.execute(sql+"%s", ['%'+tecla+'%'])
        filas = mycursor.fetchall()
        for fila in filas:
            tree.insert("", tk.END, values=(
                fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7]))

    def cargar_tabla2():
        mycursor.execute("SELECT id,descripcion,costo FROM tipo")
        fi = mycursor.fetchall()
        for f in fi:
            tree2.insert("", tk.END, values=(
                f[1], f[2]))

    def item_selected1(event):
        global seleccion
        record = 0
        cajaDias.delete(0, tk.END)
        cajaHabitacion.delete(0, tk.END)
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            cajaHabitacion.insert(0, record[1])
            cajaDias.insert(0, record[4])
            seleccion = record[0]
        return record

    def item_selected2(event):
        record = 0
        for selected_item in tree2.selection():
            item = tree2.item(selected_item)
            record = item['values']
        return record

    labelHabitacion = ttk.Label(root_tk, text="Nro Habitacion",
                                background="#000", foreground="#fff")
    labelHabitacion.place(x=30, y=20, width=120, height=30)
    labelDias = ttk.Label(root_tk, text="Dias de Estadia",
                          background="#000", foreground="#fff")
    labelDias.grid(column=0, row=3)
    cajaHabitacion = customtkinter.CTkEntry(
        master=root_tk, width=120, height=25)
    cajaHabitacion.place(x=130, y=20)
    cajaHabitacion.bind('<Key>', filtrado)
    cajaDias = customtkinter.CTkEntry(master=root_tk, width=120, height=25)
    cajaDias.grid(column=1, row=3)
    radio_var = tk.IntVar(value=0)
    credito = customtkinter.CTkRadioButton(
        master=root_tk, text="Credito", variable=radio_var, value=1)
    credito.grid(row=4, column=1, pady=10)
    contado = customtkinter.CTkRadioButton(
        master=root_tk, text="Contado", variable=radio_var, value=2)
    contado.grid(row=5, column=1, pady=10)
    buttonLimpiar = customtkinter.CTkButton(
        master=root_tk, corner_radius=10, text="Limpiar", command=limpiar)
    buttonGuardar = customtkinter.CTkButton(
        master=root_tk, corner_radius=10, text="Guardar", command=guardar)
    buttonBorrar = customtkinter.CTkButton(
        master=root_tk, corner_radius=10, text="Borrar", command=borrar)
    buttonModificar = customtkinter.CTkButton(
        master=root_tk, corner_radius=10, text="Modificar", command=modificar)
    buttonSalir = customtkinter.CTkButton(
        master=root_tk, corner_radius=10, text="Atras", command=root_tk.destroy)
    buttonLimpiar.grid(column=0, row=6, padx=5, pady=5)
    buttonGuardar.grid(column=1, row=6, padx=5, pady=5)
    buttonBorrar.grid(column=0, row=7, padx=5, pady=5)
    buttonModificar.grid(column=1, row=7, padx=5, pady=5)
    buttonSalir.grid(column=1, row=8, padx=5, pady=5)
    columns1 = ('Id', 'Nuero', 'Tipo', 'Costo', 'Dias',
                'SubTotal', 'Descuento', 'Total')
    tree = ttk.Treeview(root_tk, columns=columns1, show='headings')
    tree.heading('Id', text='Id')
    tree.heading('Nuero', text='Nuero')
    tree.heading('Tipo', text='Tipo')
    tree.heading('Costo', text='Precio')
    tree.heading('Dias', text='Dias')
    tree.heading('SubTotal', text='SubTotal')
    tree.heading('Descuento', text='%Descuento')
    tree.heading('Total', text='Total')
    tree.column('Id', width=100, anchor='center')
    tree.column('Nuero', width=100, anchor='center')
    tree.column('Tipo', width=100, anchor='center')
    tree.column('Costo', width=100, anchor='center')
    tree.column('Dias', width=100, anchor='center')
    tree.column('SubTotal', width=100, anchor='center')
    tree.column('Descuento', width=100, anchor='center')
    tree.column('Total', width=100, anchor='center')
    tree.grid(row=0, column=3, pady=40)
    tree.bind('<<TreeviewSelect>>', item_selected1)
    columns2 = ('Descripcion', 'Costo')
    tree2 = ttk.Treeview(root_tk, columns=columns2, show='headings')
    tree2.heading('Descripcion', text='Tipo Habitacion')
    tree2.heading('Costo', text='Precio')
    tree2.column('Descripcion', width=120, anchor='center')
    tree2.column('Costo', width=100, anchor='center')
    tree2.place(x=30, y=55)
    tree2.bind('<<TreeviewSelect>>', item_selected2)
    cargar_tabla1(
        '', "SELECT id,NuHabitacion,Tipo,Costo,Dias,SubTotal,Descuento,Total FROM cliente WHERE Estado = 1 AND NuHabitacion LIKE")
    cargar_tabla2()
