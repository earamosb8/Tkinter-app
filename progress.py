from tkinter import *
from tkinter.ttk import *
import time
import tkinter
import tkinter.font as font
import tkinter as tk

# creacion de la ventana
ventana =  Tk();
ventana.title("SISTEMA FOTONICO 1D")
ventana.iconbitmap("isotipo.ico")
ventana.configure(bg='white')

# Creacion de ventana vos
def createNewWindow():
    ventana.withdraw()
    menuprincipal = tk.Toplevel(ventana)
    menuprincipal.geometry("1024x1000")
    labelExample = tk.Label(menuprincipal, text = "New Window")
    buttonExample = tk.Button(menuprincipal, text = "New Window button")
    labelExample.pack()
    buttonExample.pack()

s = Style()
s.theme_use('alt')
s.configure("TProgressbar", thickness=10,foreground='red', )
# redimensionar nuestra ventana
ventana.geometry("800x500")
ventana.resizable(False, False)
imagen = PhotoImage(file="logo.png")
etiqueta = Label(ventana,image=imagen, background="white")

titulo = Label(ventana, text="Bienvenido al programa de cálculo de las",background="white")
titulo2 = Label(ventana, text="propiedades ópticas de sistema fotónicos 1D",background="white")
#txt = Label(ventana)
titulo.config(font=("Courier bold", 20))
titulo2.config(font=("Courier bold", 20))
#txt.config(font=("Courier bold", 20))
etiqueta.pack(pady=30)
titulo.pack()
titulo2.pack()
def start():
    task = 10
    x = 0
    while(x < task):
        time.sleep(0.2)
        progress_gg["value"]+=10
        #txt['text']=progress_gg['value'],'%'
        x+=1
        ventana.update_idletasks()
    if(x == 10):
        createNewWindow()

progress_gg = Progressbar(ventana, orient=HORIZONTAL, style="TProgressbar",length=300)
progress_gg.pack(pady=30)
#txt.pack()
buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
button = tkinter.Button(ventana, text = "Entrar", command=start, font=buttonFont,cursor="hand2")

button.pack()

ventana.mainloop()