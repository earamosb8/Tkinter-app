from tkinter import *
from tkinter.ttk import *
import time
import tkinter
from tkinter import messagebox
import tkinter as tk
import tkinter.font as font
import re
from tkinter import messagebox
from tkinter import ttk
from tkinter import Canvas




venteditgrafica =  Tk();
anchoVentana = 900
altoVentana = 620
venteditgrafica.title("Sistema fotónico 1D")
venteditgrafica.iconbitmap("./img/isotipo.ico")
venteditgrafica.configure(bg='white')

x_ventana = venteditgrafica.winfo_screenwidth() // 2 - anchoVentana // 2
y_ventana = venteditgrafica.winfo_screenheight() // 2 - altoVentana // 2
posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
venteditgrafica.geometry(posicion)
venteditgrafica.resizable(False, False)

titleedit= tk.Label(venteditgrafica, text = "Personalización de Gráfica", font="Calibri 18 bold", foreground="white", background="#08469B")

#Creación de Labels y LabelFrame
labeltitulosgrafica = tk.Label(venteditgrafica, text="Títulos", font="Calibri 14 bold", foreground="#08469B", background="white")
labelfuente = tk.Label(venteditgrafica, text="Fuente:", font="Calibri 15 bold", foreground="#08469B", background="white")
labeltamanoTitulos = tk.Label(venteditgrafica, text="Tamaño de titulos:", font="Calibri 15 bold", foreground="#08469B", background="white")
labeltamanoSubtitulos = tk.Label(venteditgrafica, text="Tamaño de subtitulos:", font="Calibri 16 bold", foreground="#08469B", background="white")
labeltamanoNumeros = tk.Label(venteditgrafica, text="Tamaño de numeros:", font="Calibri 15 bold", foreground="#08469B", background="white")
labeltipoDiagrama = tk.Label(venteditgrafica, text="Tipo de diagrama:", font="Calibri 15 bold", foreground="#08469B", background="white")
labelcambiarTitulos = tk.Label(venteditgrafica, text="Cambiar titulos:", font="Calibri 15 bold", foreground="#08469B", background="white")
labelcambiarTitulosx = tk.Label(venteditgrafica, text="eje X:", font="Calibri 15 bold", foreground="#08469B", background="white")
cajaX = tkinter.Entry(venteditgrafica, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1,width=10)
cajaX.bind("<KeyRelease>", lambda event: validarentry2(event,"etiqueta",cajaX,angle1))
labelcambiarTitulosy = tk.Label(venteditgrafica, text="eje Y:", font="Calibri 15 bold", foreground="#08469B", background="white")
cajaY = tkinter.Entry(venteditgrafica, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1,width=10)
cajaX2 = tkinter.Entry(venteditgrafica, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1,width=10)  
cajaX2.bind("<KeyRelease>", lambda event: validarentry2(event,"etiqueta",cajaX2,angle2))
idtext = ""
def validarentry2(event,elemento,caja,etiquetaopcional=None):
    prueba = caja.get()
    if elemento == "canvas":  
        titulofrecuencia.delete('all')
        global idtext
        if prueba == "":
            titulofrecuencia.delete('all')
            idtext =titulofrecuencia.create_text(18, 253, text = str("Frecuencia" + " GHZ"), angle = 90, anchor = "w",font=(clicked[1].get(),tamanoSub))
        else:
            idtext =titulofrecuencia.create_text(18, 253, text = str(prueba + " GHZ"), angle = 90, anchor = "w",font=(clicked[1].get(),tamanoSub))
    if elemento == "etiqueta":
        if prueba == "":
            etiquetaopcional["text"] = "Angle (y)"
        else:
         etiquetaopcional["text"] = prueba




        
        

labelbarraCalor = tk.Label(venteditgrafica, text="Colores barra de calor:", font="Calibri 15 bold", foreground="#08469B", background="white")


buttonguardaredit= tkinter.Button(venteditgrafica, text = "Guardar", cursor="hand2", width=8, height=1,relief="flat", bd=1, font="Calibri 12 bold", foreground="black", background="#B7C800")
framenamearchivo = tk.LabelFrame(venteditgrafica, background="white", highlightbackground="white", highlightcolor="white", highlightthickness=2, relief="flat", bd=1)

framegrafica = tk.LabelFrame(framenamearchivo, background="white", highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, relief="flat", bd=1,width=700)
imagen = PhotoImage(file="./img/cuadro.PNG")
modostitulo = tk.LabelFrame(framegrafica,background="white",highlightcolor="white",highlightbackground="white", highlightthickness=2,relief="flat")
modostitulo.grid(row=0, column=1)
titulofrecuencia = tkinter.Canvas(framegrafica, width = 30, height = 252,background="white",highlightbackground="white")
idtext = titulofrecuencia.create_text(18, 253, text = "Frecuencia(GHz)", angle = 90, anchor = "w",font=("Times New Roman",22))
cajaY.bind("<KeyRelease>", lambda event: validarentry2(event,"canvas",cajaY))
titulofrecuencia.grid(row=1, column=0)
barracolores= tk.LabelFrame(framegrafica,background="white",relief="flat",highlightbackground="black",highlightcolor="black", highlightthickness=1,bd=1,width= 10, height = 250)
                                                    
segmentosInicial = tk.LabelFrame(barracolores,background="#FAF9F6",relief="flat",bd=0,width= 10, height = 50)
segmentosInicial.pack()
segmentos2 = tk.LabelFrame(barracolores,background="#D5D4D1",relief="flat",bd=0,width= 10, height = 50)
segmentos2.pack()
segmentos3 = tk.LabelFrame(barracolores,relief="flat", height = 50,bd=0)
segmentosaux1 = tk.LabelFrame(segmentos3, width=10, height = 25,bd=0)
segmentosaux2 = tk.LabelFrame(segmentos3,width=10, height = 25,bd=0)
segmentosaux1.pack()
segmentosaux2.pack()
segmentos3.pack()
segmentos4 = tk.LabelFrame(barracolores,background="#80807F",relief="flat",bd=0,width= 10, height = 50)
segmentos4.pack()
segmentosFinal = tk.LabelFrame(barracolores,background="#000000",relief="flat",bd=0,width= 10, height = 50)
segmentosFinal.pack()

barracolores.grid(row=1, column=3)

escalanumeros= tk.Label(framegrafica,text="1\n0.8\n0.6\n0.4\n0.2\n0",background="white")
escalanumeros.config(font=("Times New Roman",2))
escalanumeros.grid(row=1, column=4)
titulosTE = Label(modostitulo,text="TE",anchor=tk.CENTER,background="white")
titulosTE.config(font=("Times New Roman",22))
titulosTE.grid(row=0,column=0)
espacio=Label(modostitulo,width= 30,background="white")
espacio.grid(row=0, column=2)
titulosTM = Label(modostitulo,text="TM",anchor=tk.CENTER,background="white")
titulosTM.config(font=("Arial",22))
titulosTM.grid(row=0,column=3)
etiqueta = Label(framegrafica,image=imagen, background="white")
etiqueta.grid(row=1,column=1)
escalanumeros2= tk.Label(framegrafica,text="90 75 60 45 30 15 0 15 30 45 60 75 90",background="white")
escalanumeros2.config(font=("Arial",18))
escalanumeros2.grid(row=2, column=1)
modostitulo2 = tk.LabelFrame(framegrafica, background="white",highlightbackground="white", highlightcolor="white", highlightthickness=2,relief="flat")
modostitulo2.grid(row=3, column=1)
angle1 = Label(modostitulo2,text="Angle (y)",anchor=tk.CENTER,background="white")
angle1.config(font=("Arial",22))
angle1.grid(row=0,column=0)
espacio=Label(modostitulo2,width= 20,background="white")
espacio.grid(row=0, column=2)
angle2 = Label(modostitulo2,text="Angle (y)",anchor=tk.CENTER,background="white")
angle2.config(font=("Arial",22))
angle2.grid(row=0,column=3)

labelarchivonombre = tk.Label(framenamearchivo, text="prueba.plt", font="Arial 18 bold", foreground="#08469B", background="white")
tipo = ["Arial","Calibri","Times New Roman"]
tamf = [" 8 "," 10 "," 12 "," 14 "," 16 "," 18 "," 20 "," 22 "," 24 "]
colores = {"white":"FFFFFF","red":"FF0000","blue":"0000FF","magenta":"FF00FF","green":"088A08","yellow":"FFFF00","cyan":"00FFFF","orange":"FF8000","gray":"848484"}
coloresauxiliares = [["#FAFAFA","#F2F2F2"],["#FA5858","#F5A9A9"],["#5858FA","#A9A9F5"],["#FA58F4","#F5A9F2"],["#01DF01","#2EFE2E"],["#F4FA58","#F2F5A9"],["#58FAF4","#A9F5F2"],["#FAAC58","#F5D0A9"],["#BDBDBD","#E6E6E6"]]
tipd = ["Trasmitancia","Reflectancia"]
tamanoSub = 18
tamanoTitulos = 20
tamanoNumeros = 18
tipoDiagrama = ""
colorSelected=""
colorSelected2=""
clicked=[]
clicked=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
claves = list(colores.keys())
valores = list(colores.values())



def validar(event):
    titulosTE.config(font=(clicked[0].get(),tamanoTitulos))
    titulosTM.config(font=(clicked[0].get(),tamanoTitulos))
    escalanumeros.config(font=(clicked[0].get(),tamanoNumeros))
    escalanumeros2.config(font=(clicked[0].get(),tamanoNumeros))
    titulofrecuencia.itemconfigure(idtext, font=(clicked[0].get(),tamanoSub))
    angle1.config(font=(clicked[0].get(),tamanoSub))
    angle2.config(font=(clicked[0].get(),tamanoSub))

def validartamano(event,seccion):
    if seccion == "titulos":
        global tamanoTitulos
        tamanoTitulos = clicked[1].get()
        titulosTE.config(font=(clicked[1].get(),tamanoTitulos))
        titulosTM.config(font=(clicked[1].get(),tamanoTitulos))
    if seccion == "subtitulos":
        global tamanoSub
        tamanoSub = clicked[2].get()
        titulofrecuencia.itemconfigure(idtext, font=(clicked[2].get(),tamanoSub))
        angle1.config(font=(clicked[2].get(),tamanoSub))
        angle2.config(font=(clicked[2].get(),tamanoSub))
        
    if seccion == "numeros":
        global tamanoNumeros
        tamanoNumeros = clicked[3].get()
        escalanumeros.config(font=(clicked[3].get(),tamanoNumeros))
        escalanumeros2.config(font=(clicked[3].get(),tamanoNumeros))
    if seccion == "tipodiagrama":
        global tipoDiagrama
        if clicked[4].get() == "Trasmitancia":
            tipoDiagrama = "4"
        if clicked[4].get() == "Reflectancia":
            tipoDiagrama = "3"
    if seccion == "colores":
        global colorSelected
        colorSelected = clicked[5].get()
        opcionColor.config(bg=clicked[5].get(),activebackground=clicked[5].get())
        segmentosInicial.config(bg=clicked[5].get())
        indice=claves.index(clicked[5].get())
        segmentos2.config(bg=coloresauxiliares[indice][0])
        segmentosaux1.config(bg=coloresauxiliares[indice][1])

    if seccion == "colores2":
        global colorSelected2
        colorSelected2 = clicked[6].get()
        opcionColor2.config(bg=clicked[6].get(),activebackground=clicked[6].get())
        indice=claves.index(clicked[6].get())
        segmentosFinal.config(bg=clicked[6].get())
        #print(valores[indice])
        segmentos4.config(bg=coloresauxiliares[indice][0])
        segmentosaux2.config(bg=coloresauxiliares[indice][1])
        #print(claves.index(clicked[6].get()))
        
        
        
claves = list(colores.keys())
valores = list(colores.values())
print(valores)
fuente = tk.OptionMenu(venteditgrafica, clicked[0], *tipo, command=validar)
fuente['menu'].invoke(tipo[0])

opcionTamanoTitulo = tk.OptionMenu(venteditgrafica, clicked[1],  *tamf,command=lambda event,seccion="titulos":validartamano(event,seccion))
opcionTamanoTitulo['menu'].invoke(tamf[6])
opcionTamanoSubtitulo = tk.OptionMenu(venteditgrafica, clicked[2], *tamf,command=lambda event,seccion="subtitulos":validartamano(event,seccion))
opcionTamanoSubtitulo['menu'].invoke(tamf[5])
opcionTamanoNumeros = tk.OptionMenu(venteditgrafica, clicked[3], *tamf,command=lambda event,seccion="numeros":validartamano(event,seccion))
opcionTamanoNumeros['menu'].invoke(tamf[5])
opcionTipoDiagrama = tk.OptionMenu(venteditgrafica, clicked[4], *tipd,command=lambda event,seccion="tipodiagrama":validartamano(event,seccion))
opcionTipoDiagrama['menu'].invoke(tipd[0])

opcionColor = tk.OptionMenu(venteditgrafica, clicked[5], *colores,command=lambda event,seccion="colores":validartamano(event,seccion))
opcionColor.config(bg=claves[0],activebackground=opcionColor.cget('bg'),width=7)
opcionColor['menu'].invoke(claves[0])
opcionColor2 = tk.OptionMenu(venteditgrafica, clicked[6], *colores,command=lambda event,seccion="colores2":validartamano(event,seccion))
opcionColor2.config(bg=claves[8],activebackground=opcionColor.cget('bg'),width=7)
print(colores.get(9))
opcionColor2['menu'].invoke(claves[8])







#Posicionamiento en pantalla de los elementos
titleedit.place(x=0, y=0, width=900, height=50)
labelfuente.place(x=14, y=60)

framenamearchivo.place(x=230, y=58, width=660, height=440)
labelarchivonombre.pack()
framegrafica.pack()


fuente.place(x=14, y = 90,width=150, height=30)
labeltamanoTitulos.place(x=14, y = 130)
opcionTamanoTitulo.place(x=14, y=160)
labeltamanoSubtitulos.place(x=14, y=200)
opcionTamanoSubtitulo.place(x=14, y=230)
labeltamanoNumeros.place(x=14, y=270)
opcionTamanoNumeros.place(x=14, y=300)
labeltipoDiagrama.place(x=14, y=340)
opcionTipoDiagrama.place(x=14, y=370)
labelcambiarTitulos.place(x=275, y=500)
labelcambiarTitulosy.place(x=420, y=500)
cajaY.insert(0,"Frecuencia")
cajaY.place(x=480, y=500)
labelcambiarTitulosx.place(x=580,y=500)
cajaX.insert(0, "Angle (y)")
cajaX.place(x=640, y=500)
cajaX2.insert(0, "Angle (y)")
cajaX2.place(x=750, y=500)
            
#labelcambiarTitulosx.place(x=420, y=520)
labelbarraCalor.place(x=14, y=410)

opcionColor.place(x=14,y=440)
opcionColor2.place(x=100,y=440)
buttonguardaredit.place(x=440, y = 560, width=80, height=30)
    
piepagina = tk.Label(venteditgrafica, background="#F5841F")
piepagina.place(x=0, y = 600, width=900, height=20)
    
venteditgrafica.mainloop()