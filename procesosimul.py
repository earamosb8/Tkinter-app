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

ventanaproceso =  Tk();
anchoVentana = 830
altoVentana = 550
ventanaproceso.title("Sistema fotónico 1D")
ventanaproceso.iconbitmap("isotipo.ico")
ventanaproceso.configure(bg='white')

# redimensionar nuestra ventana

x_ventana = ventanaproceso.winfo_screenwidth() // 2 - anchoVentana // 2
y_ventana = ventanaproceso.winfo_screenheight() // 2 - altoVentana // 2
posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventanaproceso.geometry(posicion)
ventanaproceso.resizable(False, False)

titleMenu = tk.Label(ventanaproceso, text = "Simulación en proceso", font="Calibri 18 bold", foreground="white", background="#08469B")

#Creación de Labels Frame
framemodoTE = tk.LabelFrame(ventanaproceso, background="white")
framemodoTM = tk.LabelFrame(ventanaproceso, background="white")

titulomodoTE = tk.Label(framemodoTE, text="Programa de cálculo modo TE", font="Calibri 18 bold", foreground="#08469B", background="white")
titulomodoTM = tk.Label(framemodoTM, text="Programa de cálculo modo TM", font="Calibri 18 bold", foreground="#08469B", background="white")

#Posicionamiento en pantalla de los elementos
titleMenu.place(x=0, y=0, width=830, height=50)
framemodoTE.place(x=10, y=55, width=400, height=400)
framemodoTM.place(x=420, y=55, width=400, height=400)

titulomodoTE.place(x=10, y=10)
titulomodoTM.place(x=10, y=10)


#labelAnchoCapa = tk.Label(myframe, text="Ancho de la capa", font="Calibri 12", foreground="#08469B", background="white" )
#anchoCapa = tkinter.Entry(myframe, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, relief="flat", bd=1)


s = Style()
s.configure("TCombobox", selectBackground='green')
s.theme_use('alt')
s.configure("TProgressbar", thickness=7, troughcolor='#a2c4c9',
    background='#b7c800', bordercolor="#a2c4c9", relief="flat", bd=1)
    

def start():
    task = 10
    x = 0
    while(x < task):
        time.sleep(0.2)
        progress_gg["value"]+=10
        x+=1
        ventanaproceso.update_idletasks()
    if(x == 10):
        createNewWindow()

progress_gg = Progressbar(framemodoTE, orient=HORIZONTAL, style="TProgressbar",length=300)
progress_gg.place(x=10, y=100)

#button = tk.Button(ventanaproceso, text = "Entrar", font="Calibri 12 bold", foreground="black", background="#B7C800", activebackground="#a2c4c9", command=start, cursor="hand2", width=8, height=1, anchor="center", relief="flat", bd=1)
#button.pack(pady=5)
   
    
piepagina = tk.Label(ventanaproceso, background="#F5841F")
piepagina.place(x=0, y = 530, width=830, height=20)

    
    
ventanaproceso.mainloop()