from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import time
import tkinter
import tkinter.font as font
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as font


# creacion de la ventana
ventanaes =  Tk();
ventanaes.title("SISTEMA FOTONICO 1D")
ventanaes.iconbitmap("isotipo.ico")
ventanaes.configure(bg='white')
ventanaes.resizable(False, False)
# redimensionar nuestra ventana
ventanaes.geometry("500x600")

#Agregar LabelFrame Padre
framePadre = LabelFrame(ventanaes)

#Creación del Canvas
mycanvas = Canvas(framePadre, height=500, width=400, background="white")
mycanvas.pack(side=LEFT, fill="both", expand="yes")

#Creación del Scrollbar
yscrollbar = ttk.Scrollbar(framePadre, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myframe = Frame(mycanvas, height=700, width=500, background="white")
mycanvas.create_window((0,0), window=myframe, anchor="nw")

#Posicionamiento en pantalla del LabelFrame
framePadre.pack(fill="both", expand="yes", padx=2, pady=2)

tituloVentanaSimulada = tk.Label(myframe, text="Estructura simulada", font="Roboto 18 bold", foreground="#032e42", background="white")
tituloVentanaSimulada.place(x=130, y=0)

nombreArchivo = tk.Label(myframe, text="Nombre del archivo:", font="Roboto 12", foreground="#012e67", background="white")
nombreArchivo.place(x=70, y=50)
datoNombreArchivo = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoNombreArchivo.place(x=350, y=50)

anchoBanda = tk.Label(myframe, text="Ancho de banda para la frecuencia:", font="Roboto 12", foreground="#193439", background="white")
anchoBanda.place(x=70, y=90)
datoAnchoBanda = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoAnchoBanda.place(x=350, y=90)

frecuenciaInicial = tk.Label(myframe, text="Frecuencia inicial:", font="Roboto 12", foreground="#233237", background="white")
frecuenciaInicial.place(x=70, y=130)
datoFrecuenciaInicial = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoFrecuenciaInicial.place(x=350, y=130)

frecuenciaFinal = tk.Label(myframe, text="Frecuencia final:", font="Roboto 12", foreground="#024f94", background="white")
frecuenciaFinal.place(x=70, y=170)
datoFrecuenciaFinal = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoFrecuenciaFinal.place(x=350, y=170)

NumeroParticiones = tk.Label(myframe, text="Número de particiones de frecuencia:", font="Roboto 12", foreground="#012e67", background="white")
NumeroParticiones.place(x=70, y=210)
datoNumeroParticiones = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoNumeroParticiones.place(x=350, y=210)

NumeroTotalPeriodos = tk.Label(myframe, text="Número total de períodos:", font="Roboto 12", foreground="#101629", background="white")
NumeroTotalPeriodos.place(x=70, y=250)
datoNumeroTotalPeriodos = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoNumeroTotalPeriodos.place(x=350, y=250)

NumeroCapas = tk.Label(myframe, text="Número de capas de la estructura:", font="Roboto 12", foreground="#10133a", background="white")
NumeroCapas.place(x=70, y=310)
datoNumeroCapas = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoNumeroCapas.place(x=350, y=310)

capa = tk.Label(myframe, text="Capa n", font="Roboto 12 bold", foreground="#000e21", background="white")
capa.place(x=70, y=350)

tipoPerfil = tk.Label(myframe, text="Tipo de perfil para la capa n:", font="Roboto 12", foreground="#00202e",background="white")
tipoPerfil.place(x=70, y=390)
datoTipoPerfil = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoTipoPerfil.place(x=350, y=390)

parametrosTipoPerfil = tk.Label(myframe, text="Parámetros del tipo de perfil:", font="Roboto 12", background="white")
parametrosTipoPerfil.place(x=70, y=430)

parametroA = tk.Label(myframe, text="A", font="Roboto 12", background="white")
parametroA.place(x=130, y=470)
datoParametroA = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoParametroA.place(x=110, y=510)

parametroB = tk.Label(myframe, text="B", font="Roboto 12", background="white")
parametroB.place(x=240, y=470)
datoParametroB = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoParametroB.place(x=220, y=510)

parametroC = tk.Label(myframe, text="C", font="Roboto 12", background="white")
parametroC.place(x=340, y=470)
datoParametroC = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoParametroC.place(x=320, y=510)

numeroParticiones = tk.Label(myframe, text="Número de particiones:", font="Roboto 12", background="white")
numeroParticiones.place(x=70, y=550)
datoNumeroParticiones = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoNumeroParticiones.place(x=350, y=550)

pregunta = tk.Label(myframe, text="¿Está seguro que desea realizar la simulación?", font="Roboto 14 bold", background="white")
pregunta.place(x=35, y=610)

buttonSi = tk.Button(myframe, text = "Si", font="Roboto 12 bold", cursor="hand2")
buttonSi.place(x=200, y = 650)

buttonNo = tk.Button(myframe, text = "No", font="Roboto 12 bold", cursor="hand2")
buttonNo.place(x=250, y = 650)


ventanaes.mainloop()