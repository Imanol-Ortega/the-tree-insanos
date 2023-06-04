from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter as tk
import customtkinter
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hotel"
    )
mycursor = mydb.cursor()
datos={}
ventana= Tk()
ventana.geometry("1000x400")
ventana.config(bg="#808080")
ventana.title("Lista")

def cargar_combo():
    mycursor= mydb.cursor()
    mycursor.execute("SELECT id, descripcion FROM tipo")
    filas = mycursor.fetchall()
    combo['values']=tuple([" "])
    for fila in filas:
        llave= str(fila[1])+"-"+str(fila[0])
        valor = fila[1]
        datos[llave]=valor
         
        
    combo['values'] += tuple(list(datos.keys()))
    
def seleccioncombo(event):
    llaveselecionada = combo.get()
    seleccionado= datos.get(llaveselecionada)
    print(seleccionado)
    label2.configure(text=seleccionado)
    for i in tabla.get_children():
        tabla.delete(i)
    mycursor.execute("SELECT NuHabitacion, Tipo, SUM(Dias),SUM(Total) FROM cliente WHERE Estado=2 AND Tipo LIKE %s ",["%"+seleccionado+"%"])
    fi= mycursor.fetchall()
    for f in fi:
        tabla.insert("", tk.END, values=(
             f[0], f[1], f[2], f[3]))
    
def limpiar():
    for i in tabla.get_children():
        tabla.delete(i)
    cargar_tabla2()
    combo.current(0)

def cargar_tabla2():
    mycursor.execute("SELECT NuHabitacion, Tipo, SUM(Dias),SUM(Total) FROM cliente WHERE Estado=2 GROUP BY Tipo ")
    fi= mycursor.fetchall()
    for f in fi:
        tabla.insert("", tk.END, values=(
             f[0], f[1], f[2], f[3]))


label2=ttk.Label(ventana,text="")
etiqueta =customtkinter.CTkLabel(master=ventana, text="Tipo de habitación", width=120, height=30, text_color="#fff", font=("Arial",18))
etiqueta.grid(column=0, row=2)
button=customtkinter.CTkButton(master=ventana,command=limpiar,text="Limpiar",corner_radius=10, font=("Arial",16),fg_color="#cc1919")
button.grid(column=2, row=2)

combo= ttk.Combobox(ventana, state="reandoly")
combo.bind("<<ComboboxSelected>>",seleccioncombo)
combo.grid(column=1,row=2)

columns = ('Numero','Tipo','Dias','Totales')
tabla = ttk.Treeview(ventana, columns=columns, show='headings')
tabla.heading('Numero', text='Numero')
tabla.heading('Tipo', text='Tipo')
tabla.heading('Dias', text='TotalesDias')
tabla.heading('Totales', text='Totales')
tabla.grid(row=9,column=1, columnspan=2,padx=10, rowspan=8,pady=10, sticky="nsew")

cargar_combo()
cargar_tabla2()
ventana.mainloop()