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


# creacion de la ventana - sesión inicio

ventana =  Tk();
anchoVentana = 500
altoVentana = 450
ventana.title("Sistema fotónico 1D")
ventana.iconbitmap("isotipo.ico")
ventana.configure(bg='white')

# redimensionar nuestra ventana

x_ventana = ventana.winfo_screenwidth() // 2 - anchoVentana // 2
y_ventana = ventana.winfo_screenheight() // 2 - altoVentana // 2
posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.resizable(False, False)
clicked = []
capaNumero = ""
capaPanel = ""
entrys = []
parametros = []
cajaFinicial = ""
cajaFfinal=""
cajaNpFrecuencia=""
cajaNtPeriodos=""
capas = ""
elements = []
miscapas = []
escala = ["GHz","THz","PHz"]
labels= []

s = Style()
s.configure("TCombobox", selectBackground='green')
s.theme_use('alt')
s.configure("TProgressbar", thickness=7, troughcolor='#a2c4c9',
    background='#b7c800', bordercolor="#a2c4c9")
    
imagen = PhotoImage(file="logo.png")
etiqueta = Label(ventana,image=imagen, background="white")

titulo = tk.Label(ventana, text="Bienvenido al programa de cálculo de las"
"\npropiedades ópticas de sistemas fotónicos 1D" 
"\nformados por capas materiales de perfil gradativo")
titulo.configure(font="Calibri 16 bold", foreground="#08469B", background="white")

etiqueta.pack(pady=25)
titulo.pack()

def start():
    task = 10
    x = 0
    while(x < task):
        time.sleep(0.2)
        progress_gg["value"]+=10
        x+=1
        ventana.update_idletasks()
    if(x == 10):
        createNewWindow()

progress_gg = Progressbar(ventana, orient=HORIZONTAL, style="TProgressbar",length=300)
progress_gg.pack(pady=35)

button = tkinter.Button(ventana, text = "Entrar", font="Calibri 12 bold", foreground="black", background="#B7C800",  command=start, cursor="hand2", width=8, height=1)
button.pack(pady=5)
piepagina = tk.Label(ventana, background="#F5841F")
piepagina.pack(side=tk.BOTTOM, fill= tk.X)

# cerrar el programa
def closeProgram():
    ventana.destroy()


# Creacion de ventana principal - sesión menu
def createNewWindow():
    clicked=""
    clicked=StringVar()

    def validar(event):
        x = clicked.get()
        if x == "GHz":
            entrys[0] = "1"
        elif x == "THz":
            entrys[0] = "2"
        elif x == "PHz":
            entrys[0] = "3"
        print(x)
    ventana.withdraw()

    menuprincipal = tk.Toplevel(ventana)
    anchoVentana = 830
    altoVentana = 450
    x_ventana = ventana.winfo_screenwidth() // 2 - anchoVentana // 2
    y_ventana = ventana.winfo_screenheight() // 2 - altoVentana // 2
    posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    menuprincipal.geometry(posicion)
    menuprincipal.configure(bg='white')
    menuprincipal.resizable(False, False)

    titleMenu = tk.Label(menuprincipal, text = "Parámetros", font="Calibri 18 bold", foreground="white", background="#08469B")
    #Creación de Labels Frame
    frameGenerales = tk.LabelFrame(menuprincipal, background="white")
    frameCapas = tk.LabelFrame(menuprincipal, background="white")

    subtitlegenerales= tk.Label(frameGenerales, text="Generales", font="Calibri 18 bold", foreground="#08469B", background="white")
    
    opcionBanda = tk.Label(frameGenerales, text="Ancho de banda para la frecuencia", font="Calibri 12", foreground="#08469B", background="white")
    cajaBanda = tk.OptionMenu(frameGenerales, clicked, *escala, command=validar)
    entrys.append("1")
    cajaBanda['menu'].invoke(escala[0])
    cajaBanda.config(height= 1 , width=3,background="white", highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, font="Calibri 10 bold")

    opcionFinicial = tk.Label(frameGenerales, text="Frecuencia inicial", font="Calibri 12", foreground="#08469B", background="white")
    cajaFinicial = tkinter.Entry(frameGenerales, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2) 

    opcionFfinal = tk.Label(frameGenerales, text="Frecuencia final", font="Calibri 12", foreground="#08469B", background="white")   
    cajaFfinal = tkinter.Entry(frameGenerales, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
    
    opcionNpFrecuencia = tk.Label(frameGenerales, text="Número de particiones de frecuencia", font="Calibri 12", foreground="#08469B", background="white")
    cajaNpFrecuencia = tkinter.Entry(frameGenerales, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
    
    opcionNtPeriodos = tk.Label(frameGenerales, text="Número total de periodos", font="Calibri 12", foreground="#08469B", background="white")
    cajaNtPeriodos = tkinter.Entry(frameGenerales, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)

    titleCapas = tk.Label(frameCapas, text = "Capas", font="Calibri 18 bold", foreground="#08469B", background="white")

    opcionNCapas = tk.Label(frameCapas, text="Número de capas de la estructura", font="Calibri 12", foreground="#08469B", background="white")
    cajaNCapas = tkinter.Entry(frameCapas, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
    buttonCrearCapa = tkinter.Button(frameCapas, text = "Crear", width=4,height=1, font="Calibri 11 bold", foreground="black", background="#B7C800", cursor="hand2")

    capapadre = tk.LabelFrame(frameCapas, height=180, width=400, bg="white")

    #Creación del Canvas
    mycanvas = Canvas(capapadre, height=400, width=400, bg="white")
    mycanvas.pack(side=LEFT, fill="both", expand="yes")

    #Creación del Scrollbar
    yscrollbar = tk.Scrollbar(capapadre, orient="vertical", command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")
    mycanvas.configure(yscrollcommand=yscrollbar.set, width=350, height=180, bg="white")
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    myframe = tk.Frame(mycanvas, height=760, width=500, bg="white")
    mycanvas.create_window((0,0), window=myframe, anchor="nw")

    titulocapaN = tk.Label(myframe, text="Capa n", font="Calibri 12 bold", foreground="white", background="#08469B")
    labelAnchoCapa = tk.Label(myframe, text="Ancho de la capa:", font="Calibri 12", foreground="#08469B", background="white" )
    anchoCapa = tkinter.Entry(myframe, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
    
    labeltipodeperfil = tk.Label(myframe, text="Tipo de perfil:", font="Calibri 12", foreground="#08469B", background="white")
    labelparametrosTipoPerfil = tk.Label(myframe, text="Parámetros del tipo de perfil:", font="Calibri 12", foreground="#08469B", background="white")
    
    labelparametroA = tk.Label(myframe, text="A", font="Calibri 12 bold", foreground="#08469B", background="white")
    parametroA = tkinter.Entry(myframe, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)

    labelparametroB = tk.Label(myframe, text="B", font="Calibri 12 bold", foreground="#08469B", background="white")
    parametroB = tkinter.Entry(myframe, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)

    labelparametroC = tk.Label(myframe, text="C", font="Calibri 12 bold", foreground="#08469B", background="white")
    parametroC = tkinter.Entry(myframe, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)

    labelnumeroParticiones = tk.Label(myframe, text="Número de particiones:", font="Calibri 12", foreground="#08469B", background="white")
    numeroParticiones = tkinter.Entry(myframe, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
  

   #Posicionamiento en pantalla de los elementos
    titleMenu.place(x=0, y=0, width=830, height=50)
    frameGenerales.place(x=10, y=55, width=400, height=300)
    frameCapas.place(x=420, y=55, width=400, height=300)

    #Posicionamiento parametros Generales
    subtitlegenerales.place(x=10, y=10)

    opcionBanda.place(x=10, y=60)
    cajaBanda.place(x=270, y=60, width=110)

    opcionFinicial.place(x=10, y=100)
    cajaFinicial.place(x=270, y=100, width=110)
    
    opcionFfinal.place(x=10, y=140)
    cajaFfinal.place(x=270, y=140, width=110)

    opcionNpFrecuencia.place(x=10, y=180)
    cajaNpFrecuencia.place(x=270, y=180, width=110)
   
    opcionNtPeriodos.place(x=10, y=220)
    cajaNtPeriodos.place(x=270, y=220, width=110)


    #Posicionamiento parametros Capas
    titleCapas.place(x=10, y=10)

    opcionNCapas.place(x=10, y=60)
    cajaNCapas.place(x=240, y=60, width=65)

    buttonCrearCapa.place(x=310, y=60, width=75, height=27)
    capapadre.place(x=12, y=105)

    titulocapaN.place(x=0, y=0, width=360, height=30)
    
    labelAnchoCapa.place(x=10, y=50)
    anchoCapa.place(x=180, y=50, width=110)

    labeltipodeperfil.place(x=10, y=90)


    labelparametrosTipoPerfil.place(x=10, y=130)

    labelparametroA.place(x=42, y=170)
    parametroA.place(x=10, y=210, width=80)

    labelparametroB.place(x=145, y=170)
    parametroB.place(x=112, y=210, width=80)

    labelparametroC.place(x=240, y=170)
    parametroC.place(x=210, y=210, width=80)

    labelnumeroParticiones.place(x=10, y=250)
    numeroParticiones.place(x=180, y=250, width=110)

    buttonEnviarDatos = tkinter.Button(menuprincipal, text = "Guardar",cursor="hand2", width=8, height=1, font="Calibri 12 bold", foreground="black", background="#B7C800")
    buttonEnviarDatos.place(x=375, y = 380, width=80, height=30)

    
    piepagina = tk.Label(menuprincipal, background="#F5841F")
    piepagina.place(x=0, y = 430, width=830, height=20)

    
    




ventana.mainloop()