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
ventana.geometry("800x500")
ventana.resizable(False, False)


# Creacion de ventana principal
def createNewWindow():
    ventana.withdraw()
    menuprincipal = tk.Toplevel(ventana)
    menuprincipal.geometry("600x989")
    menuprincipal.resizable(False, False)
    titleMenu = tk.Label(menuprincipal, text = "Parámetros")
    titleMenu.config(font=("Courier bold", 20))

    titleCapas = tk.Label(menuprincipal, text = "Capas")
    titleCapas.config(font=("Courier bold", 20))
    opcionBanda = tk.Label(menuprincipal, text="Ancho de banda para la frecuencia")
    cajaBanda = tkinter.Entry(menuprincipal, font = "Helvetica 10")

    opcionFinicial = tk.Label(menuprincipal, text="Frecuencia inicial")
    cajaFinicial = tkinter.Entry(menuprincipal, font = "Helvetica 10")
    opcionFfinal = tk.Label(menuprincipal, text="Frecuencia final")
    cajaFfinal = tkinter.Entry(menuprincipal, font = "Helvetica 10")
    opcionNpFrecuencia = tk.Label(menuprincipal, text="Número de particiones de frecuencia")
    cajaNpFrecuencia = tkinter.Entry(menuprincipal, font = "Helvetica 10")
    opcionNtPeriodos = tk.Label(menuprincipal, text="Número total de periodos")
    cajaNtPeriodos = tkinter.Entry(menuprincipal, font = "Helvetica 10")

    opcionNCapas = tk.Label(menuprincipal, text="Número de capas de la estructura")
    cajaNCapas = tkinter.Entry(menuprincipal, font = "Helvetica 10")
    buttonCrearCapa = tkinter.Button(menuprincipal, text = "Crear",cursor="hand2")

    #mostrar elementos
    titleMenu.pack(pady=30)
    
    opcionBanda.place(x=60, y=100)
    cajaBanda.place(x=280, y=100)

    opcionFinicial.place(x=60, y=140)
    cajaFinicial.place(x=280, y=140)

    opcionFfinal.place(x=60, y=180)
    cajaFfinal.place(x=280, y=180)

    opcionNpFrecuencia.place(x=60, y=220)
    cajaNpFrecuencia.place(x=280, y=220)

    opcionNtPeriodos.place(x=60, y=260)
    cajaNtPeriodos.place(x=280, y=260)

    titleCapas.place(x=260, y=320)

    opcionNCapas.place(x=60, y=380)
    cajaNCapas.place(x=280, y=380)
    buttonCrearCapa.place(x=460, y=380)
    
    menuprincipal.protocol('WM_DELETE_WINDOW', closeProgram)


# cerrar el programa

def closeProgram():
    ventana.destroy()



s = Style()
s.theme_use('alt')
s.configure("TProgressbar", thickness=10,foreground='red', )
# redimensionar nuestra ventana

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