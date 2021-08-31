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
imagen = PhotoImage(file="cuadro.PNG")
modostitulo = tk.LabelFrame(framegrafica,background="white",highlightcolor="white")
modostitulo.grid(row=0, column=1)
titulofrecuencia = tkinter.Canvas(framegrafica, width = 30, height = 250,background="white",highlightbackground="white")
titulofrecuencia.create_text(15, 230, text = "Frecuencia(GHz)", angle = 90, anchor = "w",font=("Times New Roman",22))

titulofrecuencia.grid(row=1, column=0)
barracolores=tk.LabelFrame(framegrafica,background="red",width= 10, height = 250)
barracolores.grid(row=1, column=3)
escalanumeros= tk.Label(framegrafica,text="1\n0.8\n0.6\n0.4\n0.2\n0",background="white")
escalanumeros.config(font=("Times New Roman",18))
escalanumeros.grid(row=1, column=4)
titulosTE = Label(modostitulo,text="TE",anchor=tk.CENTER,background="white")
titulosTE.config(font=("Times New Roman",22))
titulosTE.grid(row=0,column=0)
espacio=Label(modostitulo,width= 30,background="white")
espacio.grid(row=0, column=2)
titulosTM = Label(modostitulo,text="TM",anchor=tk.CENTER,background="white")
titulosTM.config(font=("Times New Roman",22))
titulosTM.grid(row=0,column=3)
etiqueta = Label(framegrafica,image=imagen, background="white")
etiqueta.grid(row=1,column=1)
escalanumeros2= tk.Label(framegrafica,text="90 75 60 45 30 15 0 15 30 45 60 75 90",background="white")
escalanumeros2.config(font=("Times New Roman",18))
escalanumeros2.grid(row=2, column=1)
modostitulo2 = tk.LabelFrame(framegrafica, background="white",highlightbackground="white")
modostitulo2.grid(row=3, column=1)
angle1 = Label(modostitulo2,text="Angle (y)",anchor=tk.CENTER,background="white")
angle1.config(font=("Times New Roman",22))
angle1.grid(row=0,column=0)
espacio=Label(modostitulo2,width= 20,background="white")
espacio.grid(row=0, column=2)
angle2 = Label(modostitulo2,text="Angle (y)",anchor=tk.CENTER,background="white")
angle2.config(font=("Times New Roman",22))
angle2.grid(row=0,column=3)

labelarchivonombre = tk.Label(framenamearchivo, text="prueba.plt", font="Calibri 18 bold", foreground="#08469B", background="white")

buttonguardaredit= tkinter.Button(venteditgrafica, text = "Guardar", cursor="hand2", width=8, height=1,relief="flat", bd=1, font="Calibri 12 bold", foreground="black", background="#B7C800")

#Posicionamiento en pantalla de los elementos
titleedit.place(x=0, y=0, width=830, height=50)
labelgenerales.place(x=20, y=68)
labeltitulosgrafica.place(x=20, y=110)
labelfuente.place(x=20, y=145)
framenamearchivo.place(x=210, y=58, width=600, height=500)
labelarchivonombre.pack()
framegrafica.pack(expand=True, fill=tk.BOTH)




buttonguardaredit.place(x=375, y = 477, width=80, height=30)
    
piepagina = tk.Label(venteditgrafica, background="#F5841F")
piepagina.place(x=0, y = 530, width=830, height=20)
    
venteditgrafica.mainloop()