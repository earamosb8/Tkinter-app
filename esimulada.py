from tkinter import *
from tkinter.ttk import *
import time
import tkinter
import tkinter.font as font
import tkinter as tk

# creacion de la ventana
ventanaes =  Tk();
ventanaes.title("SISTEMA FOTONICO 1D")
ventanaes.iconbitmap("isotipo.ico")
ventanaes.configure(bg='white')
ventanaes.resizable(False, False)
# redimensionar nuestra ventana
ventanaes.geometry("669x989")

tituloVentanaSimulada = Label(ventanaes, text="Datos de la estructura simulada", background="white")
tituloVentanaSimulada.config(font=("Courier Bold",20))
nombreArchivo = Label(ventanaes, text="Nombre del archivo:", background="white")
nombreArchivo.config(font=("Courier Bold", 14))
nombreArchivo.place(x = 40, y =60 )
datoNombreArchivo = Label(ventanaes, text="xxxxxx", background="white")
datoNombreArchivo.config(font=("Courier Bold", 14))
datoNombreArchivo.place(x=380, y=60)
anchoBanda = Label(ventanaes, text="Ancho de banda para la frecuencia:", background="white")
anchoBanda.config(font=("Courier Bold", 14))
anchoBanda.place(x = 40, y = 100)
datoAnchoBanda = Label(ventanaes, text="xxxxxx", background="white")
datoAnchoBanda.config(font=("Courier Bold", 14))
datoAnchoBanda.place(x = 40, y = 100)
frecuenciaInicial = Label(ventanaes, text="Frecuencia inicial:", background ="white")
frecuenciaInicial.config(font = ("Courier Bold", 14))
frecuenciaInicial.place(x = 40, y = 140)
frecuenciaFinal = Label(ventanaes, text="Frecuencia final:", background ="white")
frecuenciaFinal.config(font = ("Courier Bold", 14))
frecuenciaFinal.place(x = 40, y = 180)
numeroParticionesFrecuencia = Label(ventanaes, text="Número de particiones de frecuencia:", background="white")
numeroParticionesFrecuencia.config(font=("Courier Bold", 14))
numeroParticionesFrecuencia.place(x = 40, y = 220)
numeroTotalPeriodos = Label(ventanaes, text="Número total de períodos:", background="white")
numeroTotalPeriodos.config(font=("Courier Bold", 14))
numeroTotalPeriodos.place(x = 40, y = 260)
numeroCapasEstructura = Label(ventanaes, text="Número de capas de la estructura:", background="white")
numeroCapasEstructura.config(font=("Courier Bold", 14))
numeroCapasEstructura.place(x = 40, y =320)
tituloVentanaSimulada.pack()




ventanaes.mainloop()