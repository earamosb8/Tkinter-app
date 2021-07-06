from tkinter import *
from tkinter.ttk import *
import time
import tkinter
import tkinter.font as font
import tkinter as tk
import tkinter.font as font

# creacion de la ventana
ventana =  Tk();
ventana.title("Sistema fotónico 1D")
ventana.iconbitmap("isotipo.ico")
ventana.configure(bg='white')
ventana.geometry("500x450")
ventana.resizable(False, False)

capaNumero = ""
capaPanel = ""
entrys = []
parametros = []
cajaFinicial = ""
cajaFfinal=""
cajaNpFrecuencia=""
cajaNtPeriodos=""



# Creacion de ventana principal
def createNewWindow():
    
    ventana.withdraw()
    menuprincipal = tk.Toplevel(ventana)
    menuprincipal.geometry("550x860")
    menuprincipal.configure(bg='white')
    menuprincipal.resizable(False, False)
    titleMenu = tk.Label(menuprincipal, text = "Parámetros", font="Roboto 18 bold", foreground="white", background="#08469B")
    #titleMenu.config(font=("font="Roboto bold"", 18))

    subtitlegenerales= tk.Label(menuprincipal, text="Generales", font="Roboto 12 bold", foreground="#08469B", background="white")

    titleCapas = tk.Label(menuprincipal, text = "Capas", font="Roboto 18 bold", foreground="#08469B", background="white")
    #titleCapas.config(font=("Courier bold", 20))

    opcionBanda = tk.Label(menuprincipal, text="Ancho de banda para la frecuencia:", font="Roboto 12", foreground="#08469B", background="white")

    #campo float
    cajaBanda = tkinter.Entry(menuprincipal, font = "Roboto 12")
    entrys.append(cajaBanda)

    opcionFinicial = tk.Label(menuprincipal, text="Frecuencia inicial:", font="Roboto 12", foreground="#08469B", background="white")

    #campo float
    cajaFinicial = tkinter.Entry(menuprincipal, font = "Roboto 12")
    entrys.append(cajaFinicial)
    opcionFfinal = tk.Label(menuprincipal, text="Frecuencia final:", font="Roboto 12", foreground="#08469B", background="white")

    #campo float
    cajaFfinal = tkinter.Entry(menuprincipal, font = "Roboto 12")
    entrys.append(cajaFfinal)
    opcionNpFrecuencia = tk.Label(menuprincipal, text="Número de particiones de frecuencia:", font="Roboto 12", foreground="#08469B", background="white")

    #campo entero
    cajaNpFrecuencia = tkinter.Entry(menuprincipal, font = "Roboto 12")
    entrys.append(cajaNpFrecuencia)
    opcionNtPeriodos = tk.Label(menuprincipal, text="Número total de periodos:", font="Roboto 12", foreground="#08469B", background="white")

    #campo entero
    cajaNtPeriodos = tkinter.Entry(menuprincipal, font = "Roboto 12")
    entrys.append(cajaNtPeriodos)
    opcionNCapas = tk.Label(menuprincipal, text="Número de capas de la estructura:", font="Roboto 12", foreground="#08469B", background="white")
    #campo
    cajaNCapas = tkinter.Entry(menuprincipal, font = "Roboto 12",validate="key")
    capapadre = LabelFrame(menuprincipal,height=180,width=400)
    buttonCrearCapa = tkinter.Button(menuprincipal, text = "Crear", font="Roboto 10", foreground="white", background="#B7C800", cursor="hand2",command = lambda: crearCapas(menuprincipal,cajaNCapas, capapadre))

    #mostrar elementos
    titleMenu.pack(pady=0, fill=tk.X)
    
    subtitlegenerales.place(x=50, y=60)

    opcionBanda.place(x=50, y=100)
    cajaBanda.place(x=330, y=100)

    opcionFinicial.place(x=50, y=140)
    cajaFinicial.place(x=330, y=140)

    opcionFfinal.place(x=50, y=180)
    cajaFfinal.place(x=330, y=180)

    opcionNpFrecuencia.place(x=50, y=220)
    cajaNpFrecuencia.place(x=330, y=220)

    opcionNtPeriodos.place(x=50, y=260)
    cajaNtPeriodos.place(x=330, y=260)

    titleCapas.place(relx=0.5, rely=0.38, anchor=CENTER)

    opcionNCapas.place(x=50, y=380)
    cajaNCapas.place(x=330, y=380)
    buttonCrearCapa.place(x=500, y=380)
    menuprincipal.protocol('WM_DELETE_WINDOW', closeProgram)

def guardar():
    parametros = []
    print(len(entrys))
    for i in entrys:
        parametros.append(i.get())
    print(parametros)
    #parametros.append(str())
    #parametros.append(str(cajaFfinal.get()))
    #parametros.append(str(cajaNpFrecuencia.get()))
    #parametros.append(str(cajaNtPeriodos.get()))
          




# cerrar el programa
def closeProgram():
    ventana.destroy()

#validar combobox



    

# crear capas

def crearCapas(vista,numerodecapas,capapadre):
    if(numerodecapas.get() != ""):
        numero = int(numerodecapas.get())
        if numero > 0:
            capapadre = LabelFrame(vista)
            capapadre.place(x=75, y=430)
            mycanvas = Canvas(capapadre,height=400,width=400)
            mycanvas.pack(side=LEFT, fill="both", expand="yes")
            yscrollbar = tk.Scrollbar(capapadre, orient="vertical", command=mycanvas.yview)
            yscrollbar.pack(side=RIGHT, fill="y")
            mycanvas.configure(yscrollcommand=yscrollbar.set,height=400,width=400)
            mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
            myframe = Frame(mycanvas)
            mycanvas.create_window((0,0), window=myframe, anchor="nw")
            capapadre.place(x=75, y=430)
        
            options = [
                "Lineal Ax+B",
                "Lineal Ax+B", 
                "Exponencial: Aexp(Bx)+C",
            ]
            clicked = []
            parametro3 = []
            dropdowntipo=[]
            indice = []
            
            def validar(event,i):
                x = clicked[i-1].get()
                if x == "Exponencial: Aexp(Bx)+C":
                    parametro3[i-1].place(x=280, y=120)
                elif x == "Lineal Ax+B":
                    parametro3[i-1].place_forget()
                

        
            for hijo in myframe.winfo_children():
                hijo.destroy()
            for i in range(1,numero + 1):
                capaPanel = LabelFrame(myframe,height=250,width=400)

                labelAnchoCapa = tk.Label(capaPanel, text="Ancho de la capa", font="Roboto 12", foreground="#08469B", background="white" )
                anchoCapa = tkinter.Entry(capaPanel, font = "Roboto 12")
                tipodeperfil = tk.Label(capaPanel, text="Tipo de perfil", font="Roboto 12", foreground="#08469B", background="white")
                clicked.append(StringVar())
                indice.append(i-1)
                parametro3.append(tkinter.Entry(capaPanel, font = "Roboto 12",width=10))
                d = OptionMenu(capaPanel, clicked[i-1], *options, command=lambda event,i=i:validar(event, i))
                #d.widgetName= str(indice[i-1])
                dropdowntipo.append(d)
                dropdowntipo[i-1].widgetName= str(indice[i-1])
                
                labelparametros = tk.Label(capaPanel, text="Parametros del tipo de perfil:", font="Roboto 12", foreground="#08469B", background="white")
                parametro1 = tkinter.Entry(capaPanel, font = "Roboto 12",width=10)
                parametro2 = tkinter.Entry(capaPanel, font = "Roboto 12",width=10)
                labelparticiones = tk.Label(capaPanel, text="Número de particiones", font="Roboto 10", foreground="#08469B", background="white")
                particiones = tkinter.Entry(capaPanel, font = "Roboto 12")
                capaNumero = tk.Label(capaPanel, text="Capa " + str(i),font = "Helvetica 11 bold",width=43)

                capaNumero.place(x=0, y=2)
                labelAnchoCapa.place(x=45, y=30)
                anchoCapa.place(x=190, y=30)
                tipodeperfil.place(x=45, y=60)
                dropdowntipo[i-1].place(x=190,y=60)
                labelparametros.place(x=45, y=90)
                parametro1.place(x=45, y=120)
                parametro2.place(x=162, y=120)
                labelparticiones.place(x=45, y=150)
                particiones.place(x=190, y=150)
                capaPanel.pack(pady=5)
            if len(entrys)==6:
                entrys.pop(5)
                entrys.append(numerodecapas)
                print(entrys)
            else:
                entrys.append(numerodecapas)  
            print(entrys)
            
            buttonEnviarDatos = tkinter.Button(myframe, text = "Enviar",cursor="hand2", command=guardar)
            buttonEnviarDatos.pack()
        

    


s = Style()
s.theme_use('alt')
s.configure("TProgressbar", thickness=10,foreground='red', )
# redimensionar nuestra ventana

imagen = PhotoImage(file="logo.png")
etiqueta = Label(ventana,image=imagen, background="white")

titulo = Label(ventana, text="Bienvenido al programa de cálculo de las", font="Roboto 12 bold", foreground="#08469B", background="white")
titulo2 = Label(ventana, text="propiedades ópticas de sistemas fotónicos 1D", font="Roboto 12 bold", foreground="#08469B", background="white")
titulo3 = Label(ventana, text="formados por capas materiales de perfil gradativo", font="Roboto 12 bold", foreground="#08469B", background="white")
#txt = Label(ventana)
#titulo.config(font=("Courier bold", 20))
#titulo2.config(font=("Courier bold", 20))
#txt.config(font=("Courier bold", 20))
etiqueta.pack(pady=30)
titulo.pack()
titulo2.pack()
titulo3.pack()
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
#buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
button = tkinter.Button(ventana, text = "Entrar", font="Roboto 12 bold", foreground="white", background="#B7C800",  command=start, cursor="hand2", width="10")
button.pack()
piepagina = tk.Label(ventana, background="#F5841F")
piepagina.pack(side=tk.BOTTOM, fill= tk.X)
ventana.mainloop()