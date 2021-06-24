from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import time
import tkinter
import tkinter.font as font
import tkinter as tk
from tkinter import *
from tkinter import ttk


# creacion de la ventana
ventanaes =  Tk();
ventanaes.title("SISTEMA FOTONICO 1D")
ventanaes.iconbitmap("isotipo.ico")
ventanaes.configure(bg='white')
ventanaes.resizable(False, False)
# redimensionar nuestra ventana
ventanaes.geometry("500x550")

#Agregar LabelFrame Padre
framePadre = LabelFrame(ventanaes)
#frameHijo = LabelFrame(ventanaes)

#Creación del Canvas
mycanvas = Canvas(framePadre)
mycanvas.pack(side=LEFT, fill="both", expand="yes")

#Creación del Scrollbar
yscrollbar = ttk.Scrollbar(framePadre, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")


mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0,0), window=myframe, anchor="nw")

#Posicionamiento en pantalla de los LabelFrame
framePadre.pack(fill="both", expand="yes", padx=2, pady=2)
#frameHijo.pack(fill="both", expand="yes", padx=10, pady=10)

tituloVentanaSimulada = Label(myframe, text="Datos de la estructura simulada", background="white")
tituloVentanaSimulada.config(font=("Courier Bold",20))
tituloVentanaSimulada.pack()

nombreArchivo = Label(myframe, text="Nombre del archivo:", background="white")
nombreArchivo.config(font=("Courier Bold", 12))
nombreArchivo.pack(padx=15, pady=8, side=LEFT)
datoNombreArchivo = Label(myframe, text="xxxxxx", background="white")
datoNombreArchivo.config(font=("Courier Bold", 12))
datoNombreArchivo.pack(padx=45, pady=8, side=LEFT)

anchoBanda = Label(myframe, text="Ancho de banda para la frecuencia:", background="white")
anchoBanda.config(font=("Courier Bold", 12))
anchoBanda.pack(padx=15, pady=8, side=LEFT)




ventanaes.mainloop()