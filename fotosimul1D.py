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
entrys = []
cajaFinicial = ""
cajaFfinal=""
cajaNpFrecuencia=""
cajaNtPeriodos=""
escala = ["GHz","THz","PHz"]

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
    #entrys.append("1")
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

    #Creación del Canvas
    #mycanvas = Canvas(frameCapas, height=250, width=350, background="white")
    #mycanvas.pack(side=LEFT, fill="both", expand="yes")

    #Creación del Scrollbar
    #yscrollbar = ttk.Scrollbar(frameCapas, orient="vertical", command=mycanvas.yview)
    #yscrollbar.pack(side=RIGHT, fill="y")

    #mycanvas.configure(yscrollcommand=yscrollbar.set)
    #mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

    #myframe = Frame(mycanvas, height=250, width=350, background="white")
    #mycanvas.create_window((0,0), window=myframe, anchor="nw")


    #titleCapas = tk.Label(frameCapas, text = "Capas", font="Calibri 18 bold", foreground="#08469B", background="white")
  

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
    #titleCapas.place(x=10, y=0)

    

    
    piepagina = tk.Label(menuprincipal, background="#F5841F")
    piepagina.place(x=0, y = 430, width=830, height=20)

    
    




ventana.mainloop()