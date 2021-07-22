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


# creacion de la ventana - simulación en proceso modo TE

ventanaprocesote =  Tk();
anchoVentana = 400
altoVentana = 250
ventanaprocesote.title("Sistema fotónico 1D")
ventanaprocesote.iconbitmap("isotipo.ico")
ventanaprocesote.configure(bg='white')

# redimensionar nuestra ventana

x_ventana = ventanaprocesote.winfo_screenwidth() // 2 - anchoVentana // 2
y_ventana = ventanaprocesote.winfo_screenheight() // 2 - altoVentana // 2
posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventanaprocesote.geometry(posicion)
ventanaprocesote.resizable(False, False)

titleMenu = tk.Label(ventanaprocesote, text = "Simulación en proceso", font="Calibri 18 bold", foreground="white", background="#08469B")

#Creación de Labels 

titulomodoTE = tk.Label(ventanaprocesote, text="Programa de cálculo modo TE", font="Calibri 18 bold", foreground="#08469B", background="white", anchor="center")
#titulomodoTM = tk.Label(framemodoTM, text="Programa de cálculo modo TM", font="Calibri 18 bold", foreground="#08469B", background="white", anchor="center")

avancemodoTE = tk.Label(ventanaprocesote, text="25%", font="Calibri 12 bold", foreground="#08469B", background="white", anchor="center")
#avancemodoTM = tk.Label(framemodoTM, text="25%", font="Calibri 12 bold", foreground="#08469B", background="white", anchor="center")

#Posicionamiento en pantalla de los elementos
titleMenu.place(x=0, y=0, width=400, height=50)

titulomodoTE.place(x=15, y=80, width=370)
#titulomodoTM.place(x=10, y=10, width=370)

avancemodoTE.place(x=180, y=170)
#avancemodoTM.place(x=180, y=170)


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
        ventanaprocesote.update_idletasks()
    if(x == 10):
        createNewWindow()

progress_gg = Progressbar(ventanaprocesote, orient=HORIZONTAL, style="TProgressbar",length=300)
progress_gg.place(x=50, y=150)
   
    
piepagina = tk.Label(ventanaprocesote, background="#F5841F")
piepagina.place(x=0, y = 230, width=500, height=20)

    
    
ventanaprocesote.mainloop()