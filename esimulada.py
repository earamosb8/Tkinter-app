from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
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
ventanaes.geometry("550x500")

#Agregar LabelFrame Padre
#framePadre = LabelFrame(ventanaes)
#framePadre.pack(fill = "both", expand="yes")

tituloVentanaSimulada = Label(ventanaes, text="Datos de la estructura simulada", background="white")
tituloVentanaSimulada.config(font=("Courier Bold",20))
tituloVentanaSimulada.pack()

#Scrollbar
mycanvas = Canvas(ventanaes, background="white")
yscrollbar = ttk.Scrollbar(ventanaes, orient="vertical", command =mycanvas.yview)
mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
mycanvas.pack(side=LEFT, fill="both", expand="true")
yscrollbar.pack(side=RIGHT, fill=Y)

#Agregar LabelFrame
pCapas = LabelFrame(ventanaes, width=425, height=310)
pCapas.place(x=55, y =350)


nombreArchivo = Label(ventanaes, text="Nombre del archivo:", background="white")
nombreArchivo.config(font=("Courier Bold", 12))
nombreArchivo.place(x = 100, y =60 )
datoNombreArchivo = Label(ventanaes, text="xxxxxx", background="white")
datoNombreArchivo.config(font=("Courier Bold", 12))
datoNombreArchivo.place(x=380, y=60)

anchoBanda = Label(ventanaes, text="Ancho de banda para la frecuencia:", background="white")
anchoBanda.config(font=("Courier Bold", 12))
anchoBanda.place(x = 100, y = 100)
datoAnchoBanda = Label(ventanaes, text="xxxxxx", background="white")
datoAnchoBanda.config(font=("Courier Bold", 12))
datoAnchoBanda.place(x = 380, y = 100)

frecuenciaInicial = Label(ventanaes, text="Frecuencia inicial:", background ="white")
frecuenciaInicial.config(font = ("Courier Bold", 12))
frecuenciaInicial.place(x = 100, y = 140)
datoFrecuenciaInicial = Label(ventanaes, text="xxxxxx", background ="white")
datoFrecuenciaInicial.config(font = ("Courier Bold", 12))
datoFrecuenciaInicial.place(x = 380, y = 140)

frecuenciaFinal = Label(ventanaes, text="Frecuencia final:", background ="white")
frecuenciaFinal.config(font = ("Courier Bold", 12))
frecuenciaFinal.place(x = 100, y = 180)
datoFrecuenciaFinal = Label(ventanaes, text="xxxxxx", background ="white")
datoFrecuenciaFinal.config(font = ("Courier Bold", 12))
datoFrecuenciaFinal.place(x = 380, y = 180)

numeroParticionesFrecuencia = Label(ventanaes, text="Número de particiones de frecuencia:", background="white")
numeroParticionesFrecuencia.config(font=("Courier Bold", 12))
numeroParticionesFrecuencia.place(x = 100, y = 220)
datoNumeroParticionesFrecuencia = Label(ventanaes, text="xxxxxx", background="white")
datoNumeroParticionesFrecuencia.config(font=("Courier Bold", 12))
datoNumeroParticionesFrecuencia.place(x = 380, y = 220)

numeroTotalPeriodos = Label(ventanaes, text="Número total de períodos:", background="white")
numeroTotalPeriodos.config(font=("Courier Bold", 12))
numeroTotalPeriodos.place(x = 100, y = 260)
datoNumeroTotalPeriodos = Label(ventanaes, text="xxxxxx", background="white")
datoNumeroTotalPeriodos.config(font=("Courier Bold", 12))
datoNumeroTotalPeriodos.place(x = 380, y = 260)

numeroCapasEstructura = Label(ventanaes, text="Número de capas de la estructura:", background="white")
numeroCapasEstructura.config(font=("Courier Bold", 12))
numeroCapasEstructura.place(x = 100, y =300)
datoNumeroCapasEstructura = Label(ventanaes, text="xxxxxx", background="white")
datoNumeroCapasEstructura.config(font=("Courier Bold", 12))
datoNumeroCapasEstructura.place(x = 380, y =300)

capa =Label(ventanaes, text ="Capa n", background="white")
capa.config(font=("Courier Bold", 17))
capa.place(x=100, y =360)

anchoCapa = Label(ventanaes, text ="Ancho de la capa n:", background="white")
anchoCapa.config(font =("Courier Bold", 12))
anchoCapa.place(x =100, y =400)
datoAnchoCapa = Label(ventanaes, text ="xxxxxx", background="white")
datoAnchoCapa.config(font =("Courier Bold", 12))
datoAnchoCapa.place(x =380, y =400)

tipoPerfil = Label(ventanaes, text ="Tipo de perfil de la capa n:", background="white")
tipoPerfil.config(font =("Courier Bold", 12))
tipoPerfil.place(x =100, y =440)
datoTipoPerfil = Label(ventanaes, text ="xxxxxx", background="white")
datoTipoPerfil.config(font =("Courier Bold", 12))
datoTipoPerfil.place(x = 380, y =440)

parametrosTipoPerfil = Label(ventanaes, text ="Parametros del tipo de perfil:", background="white")
parametrosTipoPerfil.config(font =("Courier Bold", 12))
parametrosTipoPerfil.place(x =100, y =480)
datoParametrosTipoPerfil = Label(ventanaes, text ="xxxxxx", background="white")
datoParametrosTipoPerfil.config(font =("Courier Bold", 12))
datoParametrosTipoPerfil.place(x =380, y =480)

parametroA = Label(ventanaes, text ="A", background="white")
parametroA.config(font =("Courier Bold", 12))
parametroA.place(x=120, y = 520)
datoParametroA = Label(ventanaes, text ="xx", background="white")
datoParametroA.config(font =("Courier Bold", 12))
datoParametroA.place(x=120, y = 560)

parametroB = Label(ventanaes, text ="B", background="white")
parametroB.config(font =("Courier Bold", 12))
parametroB.place(x=240, y = 520)
datoParametroB = Label(ventanaes, text ="xx", background="white")
datoParametroB.config(font =("Courier Bold", 12))
datoParametroB.place(x=240, y = 560)

parametroC = Label(ventanaes, text ="C", background="white")
parametroC.config(font =("Courier Bold", 12))
parametroC.place(x=360, y = 520)
datoParametroC = Label(ventanaes, text ="xx", background="white")
datoParametroC.config(font =("Courier Bold", 12))
datoParametroC.place(x=360, y = 560)

numeroParticiones = Label(ventanaes, text ="Número de particiones:", background="white")
numeroParticiones.config(font =("Courier Bold", 12))
numeroParticiones.place(x=100, y = 620)
datoNumeroParticiones = Label(ventanaes, text ="xxxxxx", background="white")
datoNumeroParticiones.config(font =("Courier Bold", 12))
datoNumeroParticiones.place(x=380, y = 620)

pregunta = Label(ventanaes, text ="¿Está seguro que desea realizar la simulación?", background="white")
pregunta.config(font =("Courier Bold", 17))
pregunta.place(x=30, y = 680)

buttonSi = Button(ventanaes, text = "Si",cursor="hand2")
buttonSi.place(x=90, y = 720)

buttonNo = Button(ventanaes, text = "No",cursor="hand2")
buttonNo.place(x=90, y = 720)


ventanaes.mainloop()