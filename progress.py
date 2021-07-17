from os import error
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

# creacion de la ventana
ventana =  Tk();
anchoVentana = 500
altoVentana = 450
ventana.title("Sistema fotónico 1D")
ventana.iconbitmap("isotipo.ico")
ventana.configure(bg='white')

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
labels = []


# Creacion de ventana principal
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
    anchoVentana = 550
    altoVentana = 800
    x_ventana = ventana.winfo_screenwidth() // 2 - anchoVentana // 2
    y_ventana = ventana.winfo_screenheight() // 2 - altoVentana // 2
    posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    menuprincipal.geometry(posicion)
    menuprincipal.configure(bg='white')
    menuprincipal.resizable(False, False)
    titleMenu = tk.Label(menuprincipal, text = "Parámetros", font="Calibri 18 bold", foreground="white", background="#08469B")
    #titleMenu.config(font=("font="Calibri bold"", 18))

    subtitlegenerales= tk.Label(menuprincipal, text="Generales", font="Calibri 18 bold", foreground="#08469B", background="white")

    titleCapas = tk.Label(menuprincipal, text = "Capas", font="Calibri 18 bold", foreground="#08469B", background="white")
    #titleCapas.config(font=("Courier bold", 20))
    piepagina = tk.Label(menuprincipal, background="#F5841F")
    piepagina.place(x=0, y = 780, width=550, height=20)
    opcionBanda = tk.Label(menuprincipal, text="Ancho de banda para la frecuencia", font="Calibri 12", foreground="#08469B", background="white")
    labels.append(opcionBanda)
    #campo float
    cajaBanda = tk.OptionMenu(menuprincipal, clicked, *escala, command=validar)
    entrys.append("1")
    cajaBanda['menu'].invoke(escala[0])
    cajaBanda.config(height= 1 , width=3,background="white", highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, font="Calibri 10 bold")
    

    
    

    opcionFinicial = tk.Label(menuprincipal, text="Frecuencia inicial", font="Calibri 12", foreground="#08469B", background="white")
    labels.append(opcionFinicial)

    #campo float
    
    cajaFinicial = tkinter.Entry(menuprincipal, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2) 
    entrys.append(cajaFinicial)
    opcionFfinal = tk.Label(menuprincipal, text="Frecuencia final", font="Calibri 12", foreground="#08469B", background="white")
    labels.append(opcionFfinal)
    
    #campo float
    cajaFfinal = tkinter.Entry(menuprincipal, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
    entrys.append(cajaFfinal)
    opcionNpFrecuencia = tk.Label(menuprincipal, text="Número de particiones de frecuencia", font="Calibri 12", foreground="#08469B", background="white")
    labels.append(opcionNpFrecuencia)
    #campo entero
    cajaNpFrecuencia = tkinter.Entry(menuprincipal, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
    entrys.append(cajaNpFrecuencia)
    opcionNtPeriodos = tk.Label(menuprincipal, text="Número total de periodos", font="Calibri 12", foreground="#08469B", background="white")
    labels.append(opcionNtPeriodos)
    #campo entero
    cajaNtPeriodos = tkinter.Entry(menuprincipal, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
    entrys.append(cajaNtPeriodos)
    opcionNCapas = tk.Label(menuprincipal, text="Número de capas de la estructura", font="Calibri 12", foreground="#08469B", background="white")
    #campo
    cajaNCapas = tkinter.Entry(menuprincipal, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
    entrys.append(cajaNCapas)
    capapadre = LabelFrame(menuprincipal,height=180,width=400)
    buttonCrearCapa = tkinter.Button(menuprincipal, text = "Crear", width=4,height=1, font="Calibri 11 bold", foreground="black", background="#B7C800", cursor="hand2",command = lambda: crearCapas(menuprincipal,cajaNCapas, capapadre))

    #mostrar elementos
    #titleMenu.pack(pady=0, fill=tk.X)
    titleMenu.place(x=0, y=0, width=550, height=50)
    
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

    titleCapas.place(relx=0.5, rely=0.40, anchor=CENTER)

    opcionNCapas.place(x=50, y=360)
    cajaNCapas.place(x=330, y=360)
    buttonCrearCapa.place(x=500, y=360)
    menuprincipal.protocol('WM_DELETE_WINDOW', closeProgram)

def validador(parametro,pos,tipo):
    entrys[pos].configure(highlightcolor="#a2c4c9")
    entrys[pos].configure(highlightbackground="#a2c4c9")
    if parametro[pos]:
        # float(valor)
        if tipo == "float":
            try:
                encontrado = parametro[pos].find(".")
                if encontrado > -1:
                    valor = float(parametro[pos])
                    if valor <= 0:
                        entrys[pos].configure(highlightcolor="red")
                        entrys[pos].configure(highlightbackground="red")
                        fallo = 0
                        return fallo
                if encontrado == -1:
                    entrys[pos].configure(highlightcolor="red")
                    entrys[pos].configure(highlightbackground="red")
                    fallo = 0
                    return fallo
            except:
                entrys[pos].configure(highlightcolor="red")
                entrys[pos].configure(highlightbackground="red")
                fallo = 0
                return fallo

        if tipo == "int":
            try:
                valor = int(entrys[pos].get())
                print(valor)
                if valor <= 0:
                    entrys[pos].configure(highlightcolor="red")
                    entrys[pos].configure(highlightbackground="red")
                    fallo = 0
                    return fallo
            except:
                entrys[pos].configure(highlightcolor="red")
                entrys[pos].configure(highlightbackground="red")
                fallo = 0
                return fallo
            #try:    
                #
                #else:
                    #if tipo == "float":
                        #entrys[pos].insert(0,float(entrys[pos].get()))
            #except:
                    #fallo = 0
                    #return fallo

def validadornietos(nieto,tipo):
    nieto.configure(highlightcolor="#a2c4c9")
    nieto.configure(highlightbackground="#a2c4c9")
    if tipo == "float":
        try:
            encontrado = (nieto.get().find("."))
            print(encontrado)
            if encontrado > -1:
                valor =  float(nieto.get())
            if encontrado == -1:
                nieto.configure(highlightcolor="red")
                nieto.configure(highlightbackground="red")
                fallo = 0
                return fallo

        except:
                nieto.configure(highlightcolor="red")
                nieto.configure(highlightbackground="red")
                fallo = 0
                return fallo

    if tipo == "int":
        try:
            valor = int(nieto.get())
            if valor <= 0:
                    nieto.configure(highlightcolor="red")
                    nieto.configure(highlightbackground="red")
                    fallo = 0
                    return fallo
        except:
            nieto.configure(highlightcolor="red")
            nieto.configure(highlightbackground="red")
            fallo = 0
            return fallo

       
            


def guardar():
    parametros = []
    tipoperfil=""
    camposLlenos = True
    resultado = True
    mensaje = ""
    mensaje2 = ""
    try:
        for i in range(0,len(entrys)):
            if(i == 0):
                parametros.append(entrys[i])
            else:
                parametros.append(entrys[i].get())
    except:
        parametros.append(str(entrys[i]))
    for hijos in miscapas:
        for nietos in hijos.winfo_children():
            if(type(nietos)==tkinter.Entry):
                x = str(nietos)
                x = x.split(".")
                if x[6] == "!entry2":
                    tipoperfil =  nietos.get()
                if x[6] == "!entry5" and tipoperfil=="1":
                    continue
                parametros.append(nietos.get())
    for parametro in parametros:
        if parametro == "":
            camposLlenos = False
            messagebox.showwarning('Campos Vacios', 'Tenga en cuenta que todos los campos son obligatorios.')
            break
    if camposLlenos == True:
        for i in range(1,5):
            if(i == 1 or i == 2):
                numero = validador(parametros,i,"float")
                if numero == 0:
                    if i == 1:
                        mensaje = "El dato de la Frecuencia Inicial debe ser de tipo decimal positivo. \n"
                    if i == 2:
                        mensaje = mensaje + "El dato de la Frecuencia Final debe ser tipo decimal positivo. \n"
                    resultado = False
            if(i == 3 or i == 4):
                numero = validador(parametros,i,"int")
                if numero == 0:
                    if i == 3:
                        mensaje = mensaje + "El Numero de Particiones de Frecuencia debe ser de tipo entero positivo. \n"
                    if i == 4:
                        mensaje = mensaje + "El Numero Total de periodos debe ser de tipo entero positivo. \n"
                    resultado = False    
        for hijos in miscapas:
            for nietos in hijos.winfo_children():
                if(type(nietos)==tkinter.Entry):
                    x = str(nietos)
                    x = x.split(".")
                    if x[6] == "!entry":
                        numero = validadornietos(nietos,"float")
                        if numero == 0:
                            mensaje2 = "El Ancho de la Capa debe ser de tipo decimal positivo o negativo, puede usar notacion cientifica si lo desea.\n"
                            resultado = False
                            
                    if x[6] == "!entry2":
                        tipoperfil =  nietos.get()
                    if x[6] == "!entry3":
                        numero = validadornietos(nietos,"float")
                    if x[6] == "!entry4":
                        numero = validadornietos(nietos,"float")
                    
                    if x[6] == "!entry5" and tipoperfil=="2":
                        numero = validadornietos(nietos,"float")

                    if numero == 0:
                        encontrado = mensaje2.find("Los Parametros A,B y C del Tipo de perfil deben ser decimales\n")
                        if encontrado > -1:
                            mensaje2.replace("Los Parametros A,B y C del Tipo de perfil deben ser decimales\n", "Los Parametros A,B y C del Tipo de perfil deben ser decimales\n")
                        else:
                            mensaje2 += str("Los Parametros A,B y C del Tipo de perfil deben ser decimales\n")
                        resultado = False
                        #tipoperfil =  nietos.get()
                        #print(tipoperfil)
                    if x[6] == "!entry5" and tipoperfil=="1":
                        continue
                    if x[6] == "!entry6":
                        numero = validadornietos(nietos,"int")
                        if numero == 0:
                            mensaje2 +=str("El Numero de Particiones debe ser de tipo entero positivo")
                            resultado = False

        if resultado is False:
            mensaje = mensaje + mensaje2
            messagebox.showwarning('Advertencia!!!',mensaje)
        

        if resultado is True:
            messagebox.showwarning('Advertencia!!!',"Datos correctos")    
            archivo=open("CTETMF.esf","w")
            for p in parametros:

                archivo.write(p+"\n")
            archivo.close()

          




# cerrar el programa
def closeProgram():
    ventana.destroy()

#validar combobox

# Patrones de validaciones de cajas de texto

#def patrones_validaciones():


    
    

# crear capas

def crearCapas(vista,numerodecapas,capapadre):
    esnumero = True
    numerodecapas.configure(highlightcolor="#a2c4c9")
    numerodecapas.configure(highlightbackground="#a2c4c9")
    if(numerodecapas.get() != ""):
        try:
            numero = int(numerodecapas.get())
        except:
            esnumero = False
            numerodecapas.configure(highlightcolor="red")
            numerodecapas.configure(highlightbackground="red")
            messagebox.showwarning('Dato Incorrecto', 'Tenga en cuenta que el Numero de capas debe se un dato de tipo entero y mayor que 0')
        if esnumero == True and numero > 0:
            for i in range(0, len(miscapas)):
                miscapas.pop()
            capapadre = LabelFrame(vista)
            capapadre.place(x=75, y=430)
            mycanvas = Canvas(capapadre,height=400,width=400)
            mycanvas.pack(side=LEFT, fill="both", expand="yes")
            yscrollbar = tk.Scrollbar(capapadre, orient="vertical", command=mycanvas.yview)
            yscrollbar.pack(side=RIGHT, fill="y")
            mycanvas.configure(yscrollcommand=yscrollbar.set,height=320,width=400,bg="white")
            mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
            myframe = Frame(mycanvas)
            elements.append(myframe)
            mycanvas.create_window((0,0), window=myframe, anchor="nw")
            capapadre.place(x=75, y=410)
        
            options = [
                "Lineal Ax+B", 
                "Exponencial: Aexp(Bx)+C",
            ]
            
            parametro3 = []
            labelparametroC = []
            dropdowntipo=[]
            indice = []
            
            def validar(event,i,optiondropdown):
                x = clicked[i-1].get()
                if x == "Exponencial: Aexp(Bx)+C":
                    optiondropdown.delete(0, "end")
                    optiondropdown.insert(0,"2")
                    parametro3[i-1].place(x=280, y=180)
                    labelparametroC[i-1].place(x=315, y=150)
                elif x == "Lineal Ax+B":
                    optiondropdown.delete(0, "end")
                    optiondropdown.insert(0,"1")
                    parametro3[i-1].place_forget()
                    labelparametroC[i-1].place_forget()
                    parametro3[i-1].delete(0, "end")
                

        
            for hijo in myframe.winfo_children():
                hijo.destroy()
            for i in range(1,numero + 1):
                capaPanel = tk.LabelFrame(myframe,height=270,width=400,bg = "white")
                labelAnchoCapa = tk.Label(capaPanel, text="Ancho de la capa:", font="Calibri 12", foreground="#08469B", background="white" )
                anchoCapa = tkinter.Entry(capaPanel, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
                tipodeperfil = tk.Label(capaPanel, text="Tipo de perfil:", font="Calibri 12", foreground="#08469B", background="white")
                clicked.append(StringVar())
                indice.append(i-1)
                optiontipoperfil = tkinter.Entry(capaPanel, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
                optiontipoperfil.insert(0, "1")
                #entrys.append(optiontipoperfil)
                d = tk.OptionMenu(capaPanel, clicked[i-1], *options, command=lambda event,i=i,optiondropdown=optiontipoperfil:validar(event, i,optiondropdown))
                d['menu'].invoke(options[0])
                d.config(background="white", highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, font="Calibri 10 bold")
                #d.widgetName= str(indice[i-1])
                dropdowntipo.append(d)
                dropdowntipo[i-1].widgetName= str(indice[i-1])
               
                
                labelparametros = tk.Label(capaPanel, text="Parametros del tipo de perfil:", font="Calibri 12", foreground="#08469B", background="white")

                labelparametroA = tk.Label(capaPanel, text="A", font="Calibri 12 bold", foreground="#08469B", background="white")
                labelparametroB = tk.Label(capaPanel, text="B", font="Calibri 12 bold", foreground="#08469B", background="white")
                parametro1 = tkinter.Entry(capaPanel, font = "Calibri 12",width=10,highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
                parametro2 = tkinter.Entry(capaPanel, font = "Calibri 12",width=10,highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
                parametro3.append(tkinter.Entry(capaPanel, font = "Calibri 12",width=10,highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2))
                labelparametroC.append(tk.Label(capaPanel, text="C", font="Calibri 12 bold", foreground="#08469B", background="white"))
                labelparticiones = tk.Label(capaPanel, text="Número de particiones:", font="Calibri 12", foreground="#08469B", background="white")
                particiones = tkinter.Entry(capaPanel, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2)
                capaNumero = tk.Label(capaPanel, text="Capa " + str(i),font = "Calibri 12 bold",width=50 ,foreground="white", background="#08469B")
                miscapas.append(capaPanel)
                capaNumero.place(x=0, y=2)
                labelAnchoCapa.place(x=45, y=40)
                anchoCapa.place(x=210, y=40)
                tipodeperfil.place(x=45, y=80)
                dropdowntipo[i-1].place(x=210,y=80)
                labelparametros.place(x=45, y=120)
                labelparametroA.place(x=80, y=150)
                labelparametroB.place(x=198, y=150)
                parametro1.place(x=45, y=180)
                parametro2.place(x=162, y=180)
                labelparticiones.place(x=45, y=220)
                particiones.place(x=210, y=220)
                capaPanel.pack(pady=5)
            if len(entrys)==6:
                entrys.pop(5)
                entrys.append(i)
                print(entrys)
            else:
                entrys.append(i)  
            
            buttonEnviarDatos = tkinter.Button(myframe, text = "Guardar",cursor="hand2", width=8, height=1, font="Calibri 12 bold", foreground="black", background="#B7C800", command=guardar)
            buttonEnviarDatos.pack()



        

    


s = Style()
s.configure("TCombobox", selectBackground='green')
s.theme_use('alt')
s.configure("TProgressbar", thickness=7, troughcolor='#a2c4c9',
    background='#b7c800', bordercolor="#a2c4c9")
    #darkcolor="#a2c4c9",
    #lightcolor="#a2c4c9" )
# redimensionar nuestra ventana

imagen = PhotoImage(file="logo.png")
etiqueta = Label(ventana,image=imagen, background="white")

titulo = Label(ventana, text="Bienvenido al programa de cálculo de las", font="Calibri 16 bold", foreground="#08469B", background="white")
titulo2 = Label(ventana, text="propiedades ópticas de sistemas fotónicos 1D", font="Calibri 16 bold", foreground="#08469B", background="white")
titulo3 = Label(ventana, text="formados por capas materiales de perfil gradativo", font="Calibri 16 bold", foreground="#08469B", background="white")
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
button = tkinter.Button(ventana, text = "Entrar", font="Calibri 12 bold", foreground="black", background="#B7C800",  command=start, cursor="hand2", width=8, height=1)
button.pack()
piepagina = tk.Label(ventana, background="#F5841F")
piepagina.pack(side=tk.BOTTOM, fill= tk.X)
ventana.mainloop()