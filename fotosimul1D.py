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

    #Posicionamiento en pantalla de los elementos
    titleMenu.place(x=0, y=0, width=830, height=50)

    #Posicionamiento en pantalla del LabelFrame
    frameGenerales.place(x=10, y=55, width=400, height=300)
    frameCapas.place(x=420, y=55, width=400, height=300)

    #Posicionamiento parametros Generales
    subtitlegenerales.place(x=10, y=0)

    

    
    piepagina = tk.Label(menuprincipal, background="#F5841F")
    piepagina.place(x=0, y = 430, width=830, height=20)

    
    




ventana.mainloop()