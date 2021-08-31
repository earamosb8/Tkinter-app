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


venteditgrafica =  Tk();
anchoVentana = 830
altoVentana = 550
venteditgrafica.title("Sistema fotónico 1D")
venteditgrafica.iconbitmap("isotipo.ico")
venteditgrafica.configure(bg='white')

x_ventana = venteditgrafica.winfo_screenwidth() // 2 - anchoVentana // 2
y_ventana = venteditgrafica.winfo_screenheight() // 2 - altoVentana // 2
posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
venteditgrafica.geometry(posicion)
venteditgrafica.resizable(False, False)

titleedit= tk.Label(venteditgrafica, text = "Personalización de Gráfica", font="Calibri 18 bold", foreground="white", background="#08469B")

#Creación de Labels y LabelFrame
labelgenerales = tk.Label(venteditgrafica, text="Generales", font="Calibri 18 bold", foreground="#08469B", background="white")
labeltitulosgrafica = tk.Label(venteditgrafica, text="Títulos", font="Calibri 14 bold", foreground="#08469B", background="white")
labelfuente = tk.Label(venteditgrafica, text="Fuente:", font="Calibri 12", foreground="#08469B", background="white")

framenamearchivo = tk.LabelFrame(venteditgrafica, background="white", highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, relief="flat", bd=1)
framegrafica = tk.LabelFrame(framenamearchivo, background="white", highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, relief="flat", bd=1)

labelarchivonombre = tk.Label(framenamearchivo, text="prueba.plt", font="Calibri 18 bold", foreground="#08469B", background="white")

buttonguardaredit= tkinter.Button(venteditgrafica, text = "Guardar", cursor="hand2", width=8, height=1,relief="flat", bd=1, font="Calibri 12 bold", foreground="black", background="#B7C800")

#Posicionamiento en pantalla de los elementos
titleedit.place(x=0, y=0, width=830, height=50)
labelgenerales.place(x=20, y=68)
labeltitulosgrafica.place(x=20, y=110)
labelfuente.place(x=20, y=145)
framenamearchivo.place(x=370, y=55, width=450, height=400)
framegrafica.place(x=10, y=55, width=425, height=330)

labelarchivonombre.place(x=10, y=10)

buttonguardaredit.place(x=375, y = 477, width=80, height=30)
    
piepagina = tk.Label(venteditgrafica, background="#F5841F")
piepagina.place(x=0, y = 530, width=830, height=20)
    
venteditgrafica.mainloop()