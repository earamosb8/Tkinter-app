from tkinter.ttk import *
import time
import tkinter
import tkinter.font as font
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as font


# creacion de la ventana
ventanaes =  Tk();
ventanaes.title("Sistema fotónico 1D")
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

myframe = Frame(mycanvas, height=760, width=500, background="white")
mycanvas.create_window((0,0), window=myframe, anchor="nw")

#Posicionamiento en pantalla del LabelFrame
framePadre.pack(fill="both", expand="yes", padx=2, pady=2)

tituloVentanaSimulada = tk.Label(myframe, text="Estructura simulada", font="Roboto 18 bold", foreground="white", background="#08469B")
tituloVentanaSimulada.place(x=0, y=0, width=500, height=50)

nombreArchivo = tk.Label(myframe, text="Nombre del archivo:", font="Roboto 12", foreground="#08469B", background="white")
nombreArchivo.place(x=70, y=65)
datoNombreArchivo = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoNombreArchivo.place(x=350, y=65)

anchoBanda = tk.Label(myframe, text="Ancho de banda para la frecuencia:", font="Roboto 12", foreground="#08469B", background="white")
anchoBanda.place(x=70, y=100)
datoAnchoBanda = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoAnchoBanda.place(x=350, y=100)

frecuenciaInicial = tk.Label(myframe, text="Frecuencia inicial:", font="Roboto 12", foreground="#08469B", background="white")
frecuenciaInicial.place(x=70, y=135)
datoFrecuenciaInicial = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoFrecuenciaInicial.place(x=350, y=135)

frecuenciaFinal = tk.Label(myframe, text="Frecuencia final:", font="Roboto 12", foreground="#08469B", background="white")
frecuenciaFinal.place(x=70, y=170)
datoFrecuenciaFinal = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoFrecuenciaFinal.place(x=350, y=170)

NumeroParticiones = tk.Label(myframe, text="Número de particiones de frecuencia:", font="Roboto 12", foreground="#08469B", background="white")
NumeroParticiones.place(x=70, y=205)
datoNumeroParticiones = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoNumeroParticiones.place(x=350, y=205)

NumeroTotalPeriodos = tk.Label(myframe, text="Número total de períodos:", font="Roboto 12", foreground="#08469B", background="white")
NumeroTotalPeriodos.place(x=70, y=240)
datoNumeroTotalPeriodos = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoNumeroTotalPeriodos.place(x=350, y=240)

NumeroCapas = tk.Label(myframe, text="Número de capas de la estructura:", font="Roboto 12", foreground="#08469B", background="white")
NumeroCapas.place(x=70, y=310)
datoNumeroCapas = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoNumeroCapas.place(x=350, y=310)

capa = tk.Label(myframe, text="Capa n", font="Roboto 12 bold", foreground="#08469B", background="white")
capa.place(x=70, y=350)

Labelframecapa = tk.LabelFrame(myframe, background="white")
Labelframecapa.place(x=40, y=380, height=246, width=400,)

anchocapa = tk.Label(myframe, text="Ancho de la capa n:", font="Roboto 12", foreground="#08469B", background="white")
anchocapa.place(x=70, y=390)
datoanchocapa = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoanchocapa.place(x=350, y=390)

tipoPerfil = tk.Label(myframe, text="Tipo de perfil para la capa n:", font="Roboto 12", foreground="#08469B",background="white")
tipoPerfil.place(x=70, y=430)
datoTipoPerfil = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoTipoPerfil.place(x=350, y=430)

parametrosTipoPerfil = tk.Label(myframe, text="Parámetros del tipo de perfil:", font="Roboto 12", foreground="#08469B", background="white")
parametrosTipoPerfil.place(x=70, y=470)

parametroA = tk.Label(myframe, text="A", font="Roboto 12", foreground="#08469B", background="white")
parametroA.place(x=130, y=510)
datoParametroA = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoParametroA.place(x=110, y=550)

parametroB = tk.Label(myframe, text="B", font="Roboto 12", foreground="#08469B", background="white")
parametroB.place(x=240, y=510)
datoParametroB = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoParametroB.place(x=220, y=550)

parametroC = tk.Label(myframe, text="C", font="Roboto 12", foreground="#08469B", background="white")
parametroC.place(x=340, y=510)
datoParametroC = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoParametroC.place(x=320, y=550)

numeroParticiones = tk.Label(myframe, text="Número de particiones:", font="Roboto 12", foreground="#08469B", background="white")
numeroParticiones.place(x=70, y=590)
datoNumeroParticiones = tk.Label(myframe, text="xxxxxx", font="Roboto 12", background="white")
datoNumeroParticiones.place(x=350, y=590)

pregunta = tk.Label(myframe, text="¿Está seguro que desea realizar la simulación?", font="Roboto 14 bold", foreground="#08469B", background="white")
pregunta.place(x=35, y=660)

buttonSi = tk.Button(myframe, text = "Si", font="Roboto 12 bold", foreground="white", background="#B7C800", cursor="hand2")
buttonSi.place(x=180, y = 700, width=50, height=30)

buttonNo = tk.Button(myframe, text = "No", font="Roboto 12 bold", foreground="white", background="#B7C800", cursor="hand2")
buttonNo.place(x=250, y = 700, width=50, height=30)

piepagina = tk.Label(myframe, background="#F5841F")
piepagina.place(x=0, y = 750, width=500, height=30)


ventanaes.mainloop()