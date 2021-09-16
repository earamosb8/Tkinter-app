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
import os
from os import remove
import shutil

# creacion de la ventana
ventana =  Tk();
anchoVentana = 500
altoVentana = 450
ventana.title("Sistema fotónico 1D")
ventana.iconbitmap("./img/isotipo.ico")
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


scroll = Style()
scroll.configure('TScrollbar',background='blue')



# Creacion de ventana principal
def createNewWindow():
    clicked=""
    clicked=StringVar()

    def validar(event):
        x = clicked.get()
        if x == "GHz":
            entrys[1] = "1"
        elif x == "THz":
            entrys[1] = "2"
        elif x == "PHz":
            entrys[1] = "3"
    ventana.withdraw()

    menuprincipal = tk.Toplevel(ventana)
    anchoVentana = 830
    altoVentana = 550
    x_ventana = ventana.winfo_screenwidth() // 2 - anchoVentana // 2
    y_ventana = ventana.winfo_screenheight() // 2 - altoVentana // 2
    posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    menuprincipal.geometry(posicion)
    menuprincipal.iconbitmap("./img/isotipo.ico")
    menuprincipal.configure(bg='white')
    menuprincipal.resizable(False, False)
    frameGenerales = tk.LabelFrame(menuprincipal, background="white",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, relief="flat", bd=1)
    frameCapas = tk.LabelFrame(menuprincipal, background="white",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, relief="flat", bd=1)
    titleMenu = tk.Label(menuprincipal, text = "Parámetros", font="Calibri 18 bold", foreground="white", background="#08469B")
    #titleMenu.config(font=("font="Calibri bold"", 18))
    subtitlenombreA = tk.Label(frameGenerales, text="Datos de la simulación", font="Calibri 18 bold", foreground="#08469B", background="white")
    nombreArchivo = tk.Label(frameGenerales, text="Nombre del proyecto", font="Calibri 12", foreground="#08469B", background="white" )
    cajanombreArchivo = tkinter.Entry(frameGenerales, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, relief="flat", bd=1)
    entrys.append(cajanombreArchivo)
    ubicacionArchivo = tk.Label(frameGenerales, text="Ubicación del proyecto", font="Calibri 12", foreground="#08469B", background="white" )
    cajaubicacionArchivo = tk.Label(frameGenerales, text="Tkinter-app\Output", font="Calibri 12", foreground="black", background="white" )
    subtitlegenerales= tk.Label(frameGenerales, text="Generales", font="Calibri 18 bold", foreground="#08469B", background="white")

    titleCapas = tk.Label(frameCapas, text = "Capas", font="Calibri 18 bold", foreground="#08469B", background="white")
    #titleCapas.config(font=("Courier bold", 20))
    piepagina = tk.Label(menuprincipal, background="#F5841F")
    piepagina.place(x=0, y = 530, width=830, height=20)
    opcionBanda = tk.Label(menuprincipal, text="Ancho de banda para la frecuencia", font="Calibri 12", foreground="#08469B", background="white")
    labels.append(opcionBanda)
    #campo float
    cajaBanda = tk.OptionMenu(menuprincipal, clicked, *escala, command=validar)
    entrys.append("1")
    cajaBanda['menu'].invoke(escala[0])
    cajaBanda.config(height= 1 , width=3,relief="flat", bd=1,background="white", highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, font="Calibri 10 bold")
    opcionFinicial = tk.Label(menuprincipal, text="Frecuencia inicial", font="Calibri 12", foreground="#08469B", background="white")
    labels.append(opcionFinicial)

    #campo float
    
    cajaFinicial = tkinter.Entry(menuprincipal, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1) 
    entrys.append(cajaFinicial)
    opcionFfinal = tk.Label(menuprincipal, text="Frecuencia final", font="Calibri 12", foreground="#08469B", background="white",relief="flat", bd=1)
    labels.append(opcionFfinal)
    
    #campo float
    cajaFfinal = tkinter.Entry(menuprincipal, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1)
    entrys.append(cajaFfinal)
    opcionNpFrecuencia = tk.Label(menuprincipal, text="Número de particiones de frecuencia", font="Calibri 12", foreground="#08469B", background="white")
    labels.append(opcionNpFrecuencia)
    #campo entero
    cajaNpFrecuencia = tkinter.Entry(menuprincipal, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1)
    entrys.append(cajaNpFrecuencia)
    opcionNtPeriodos = tk.Label(menuprincipal, text="Número total de periodos", font="Calibri 12", foreground="#08469B", background="white")
    labels.append(opcionNtPeriodos)
    #campo entero
    cajaNtPeriodos = tkinter.Entry(menuprincipal, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1)
    entrys.append(cajaNtPeriodos)
    opcionNCapas = tk.Label(frameCapas, text="Número de capas de la estructura", font="Calibri 12", foreground="#08469B", background="white")
    #campo
    cajaNCapas = tkinter.Entry(frameCapas, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1)
    entrys.append(cajaNCapas)
    
    buttonCrearCapa = tkinter.Button(frameCapas, text = "Crear", width=4,height=1, font="Calibri 11 bold", foreground="black", background="#B7C800", cursor="hand2",relief="flat", bd=1,command = lambda: crearCapas(menuprincipal,cajaNCapas, frameCapas,buttonEnviarDatos))

    #Posicionamiento en pantalla de los elementos
    titleMenu.place(x=0, y=0, width=830, height=50)
    frameGenerales.place(x=10, y=55, width=400, height=400)
    frameCapas.place(x=420, y=55, width=400, height=400)

    #Posicionamiento parametros 
    subtitlenombreA.place(x=10, y=10)
    nombreArchivo.place(x=10, y=60)
    cajanombreArchivo.place(x=170, y=60, width=215)
    ubicacionArchivo.place(x=10, y=100)
    cajaubicacionArchivo.place(x=170, y=100)

    #Parametros Generales
    subtitlegenerales.place(x=10, y=140)

    opcionBanda.place(x=24, y=245)
    cajaBanda.place(x=285, y=245, width=110)

    opcionFinicial.place(x=24, y=285)
    cajaFinicial.place(x=285, y=285, width=110)
    
    opcionFfinal.place(x=24, y=325)
    cajaFfinal.place(x=285, y=325, width=110)

    opcionNpFrecuencia.place(x=24, y=365)
    cajaNpFrecuencia.place(x=285, y=365, width=110)
   
    opcionNtPeriodos.place(x=24, y=405)
    cajaNtPeriodos.place(x=285, y=405, width=110)


    #Posicionamiento parametros Capas
    titleCapas.place(x=10, y=10)

    opcionNCapas.place(x=10, y=60)
    cajaNCapas.place(x=240, y=60, width=65)

    buttonCrearCapa.place(x=310, y=60, width=75, height=27)
    


    
    piepagina = tk.Label(menuprincipal, background="#F5841F")
    piepagina.place(x=0, y = 530, width=830, height=20)
    buttonEnviarDatos = tkinter.Button(menuprincipal, text = "Guardar",cursor="hand2", width=8, height=1,relief="flat", bd=1, font="Calibri 12 bold", foreground="black", background="#B7C800", command=guardar)
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
    if tipo == "float" or tipo == "floatancho":
        try:
            encontrado = (nieto.get().find("."))
            encontrado2 = (nieto.get().find("e"))
            encontrado3 = (nieto.get().find("E"))
            if encontrado > -1 or encontrado2 > -1 or encontrado3 > -1:
                valor =  float(nieto.get())
                if tipo == "floatancho":
                    if valor < 0:
                        nieto.configure(highlightcolor="red")
                        nieto.configure(highlightbackground="red")
                        fallo = 0
                        return fallo
            else:
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
            
            if(i == 1):
                parametros.append(entrys[i])
            else:
                parametros.append(entrys[i].get())
    except:
        parametros.append(str(entrys[i]))
    for hijos in miscapas:
        grupo = []
        for nietos in hijos.winfo_children():
           
            if(type(nietos)==tkinter.Entry):
                x = str(nietos)
                x = x.split(".")
                if x[6] == "!entry2":
                    tipoperfil =  nietos.get()
                if x[6] == "!entry5" and tipoperfil=="1":
                    continue
                grupo.append(nietos.get())
        parametros.append(grupo)
    for p in range(0,len(parametros)):
        if parametros[p] == "":
            camposLlenos = False
            messagebox.showwarning('Campos Vacios', 'Tenga en cuenta que todos los campos son obligatorios.')
            break
        if p >= 6:
            for h in range(0,len(parametros[p])):
                if parametros[p][h] == "":
                    camposLlenos = False
                    messagebox.showwarning('Campos Vacios', 'Tenga en cuenta que todos los campos son obligatorios.')
                    break
    if camposLlenos == True:
        capasFloat = 1
        for i in range(2,6):
            if(i == 2 or i == 3):
                numero = validador(parametros,i,"float")
                if numero == 0:
                    if i == 2:
                        mensaje = "El dato de la Frecuencia Inicial debe ser de tipo decimal positivo. \n"
                        capasFloat = 0
                    if i == 3:
                        mensaje = mensaje + "El dato de la Frecuencia Final debe ser tipo decimal positivo. \n"
                        capasFloat = 0
                    resultado = False
            if(i == 4 or i == 5):
                numero = validador(parametros,i,"int")
                if numero == 0:
                    if i == 4:
                        mensaje = mensaje + "El Numero de Particiones de Frecuencia debe ser de tipo entero positivo. \n"
                    if i == 5:
                        mensaje = mensaje + "El Numero Total de periodos debe ser de tipo entero positivo. \n"
                    resultado = False
        if capasFloat == 1:
            if parametros[2] >= parametros[3]:
                encontrado = mensaje.find("la Frecuencia Final debe ser mayor que la inicial. \n")
                if encontrado > -1:
                    mensaje.replace("la Frecuencia Final debe ser mayor que la inicial. \n","la Frecuencia Final debe ser mayor que la inicial. \n")
                else:
                    mensaje += str("la Frecuencia Final debe ser mayor que la inicial. \n")
                entrys[2].configure(highlightcolor="red")
                entrys[2].configure(highlightbackground="red")
                entrys[3].configure(highlightcolor="red")
                entrys[3].configure(highlightbackground="red")
                resultado = False  
        for hijos in miscapas:
            for nietos in hijos.winfo_children():
                if(type(nietos)==tkinter.Entry):
                    x = str(nietos)
                    x = x.split(".")
                    if x[6] == "!entry":
                        numero = validadornietos(nietos,"floatancho")
                        if numero == 0:
                            mensaje2 = "El Ancho de la Capa debe ser de tipo decimal mayor o igual que 0, puede usar notacion cientifica si lo desea.\n"
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
                        encontrado = mensaje2.find("Los Parametros A,B y C del Tipo de perfil deben ser decimales, y pueden ser positívos o negatívos\n")
                        if encontrado > -1:
                            mensaje2.replace("Los Parametros A,B y C del Tipo de perfil deben ser decimales, y pueden ser positívos o negatívos\n", "Los Parametros A,B y C del Tipo de perfil deben ser decimales, y pueden ser positívos o negatívos\n")
                        else:
                            mensaje2 += str("Los Parametros A,B y C del Tipo de perfil deben ser decimales, y pueden ser positívos o negatívos\n")
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
            print(parametros)
            mostrarParametros(parametros)


def mostrarParametros(parametros):
    menuprincipal = ""
    for n in ventana.winfo_children():
        if(type(n)==tkinter.Toplevel):
             menuprincipal = n
             break
    menuprincipal.withdraw()
    ventanaParametros(parametros,menuprincipal)
    return menuprincipal
    
    
def volver(ventana1,ventana2):
    ventana1.destroy()
    ventana2.deiconify()

def gnu_plot_TETMvsAng(nombre,ran_fre,fi_ff):   # funcion para la escritura del script de visualizacion en GNUPLOT
    archivo=open(nombre+".plt","w")
    archivo.write("reset"+"\n")
    archivo.write("arcizq='"+nombre+"-TE.dat'"+"\n")
    archivo.write("arcder='"+nombre+"-TM.dat'"+"\n")
    archivo.write("############################################################"+"\n")
    archivo.write("# parametros comunes de las figuras"+"\n")
    archivo.write("############################################################"+"\n")
    archivo.write("\n")
    archivo.write("tam=.5"+"\n")
    archivo.write("ymin="+str(fi_ff.split(",")[0])+" # valor minimo en las y"+"\n")
    archivo.write("ymax="+str(fi_ff.split(",")[1])+" # valor maximo en las y"+"\n")
    archivo.write("xmin=0 # valor minimo en las x"+"\n")
    archivo.write("xmax=90 # valor maximo en las x"+"\n")
    archivo.write("mtx=2 # No de minor ticks en x"+"\n")
    archivo.write("mty=4 # No de minor ticks en y"+"\n")
    archivo.write("septicx=15 # separaci on ticks en x"+"\n")
    archivo.write("septicy=2 # separacion ticks en y"+"\n")
    archivo.write("scatics=0.5 # tamaño de los ticks en terminos del default que es 1"+"\n")
    archivo.write("titizq='TE' # titulo de la figura izquierda"+"\n")##
    archivo.write("titder='TM' # titulo de la figura derecha"+"\n")##
    archivo.write("fuente='Times-New-Roman, 22' # titulo, tipo y tamaño de la fuente"+"\n")##
    archivo.write("ejexlabel='{Angle X}' # label del eje x"+"\n")##
    if ran_fre=="1":
       archivo.write("ejeylabel='Frequency (THz)' # label del eje y"+"\n")##
    elif ran_fre=="2":
       archivo.write("ejeylabel='Frequency (GHz)' # label del eje y"+"\n")##
    archivo.write("fulabel='Times-New-Roman, 20' # label tipo y tamaño de la fuente"+"\n")##
    archivo.write("fuejes='Times-New-Roman, 18' # fuente de los ejes y el tamaño"+"\n")##
    archivo.write("\n")
    archivo.write("set multiplot # ayuda a pintar muchas figuras en una sola, deben especificarse todas las caracteristicas de cada figura"+"\n")
    archivo.write("\n")
    archivo.write("#########################################"+"\n")
    archivo.write("# caracteristicas figura de la izquierda"+"\n")
    archivo.write("###########################################"+"\n")
    archivo.write("set palette defined (0 'black',1 'white') #gray"+"\n")
    archivo.write("# tipo de colores para el density plot"+"\n")
    archivo.write("set cbrange [0 : 1] # conjunto de valores del rango de colores"+"\n")
    archivo.write("set pm3d interpolate 0,0 map"+"\n")
    archivo.write("# utiliza pm3d e interpola de forma automatica ademas 'map' solo lo muestra visto desde arriba"+"\n")
    archivo.write("set size tam,2*tam # tamaño de la figura con respecto de la terminal"+"\n")
    archivo.write("set origin 0.05,0. # posicion de la figura"+"\n")
    archivo.write("unset key # quita nombre de la serie de datos"+"\n")
    archivo.write("unset colorbox # quita la guia del color, esto pues solo usamos la del lado derecho"+"\n")
    archivo.write("set xrange[xmax:xmin] # rango de los valores en x"+"\n")
    archivo.write("set tics scale scatics # muestra los tics en terminos del tamaño por default"+"\n")
    archivo.write("set xtics septicx nomirror out font fuejes # coloca los tics en x separados por el numero mostrado, sin reflexion en el eje paralelo, con los tics afuera y con su fuente"+"\n")
    archivo.write("set mxtics mtx # numero de minor tics en x"+"\n")
    archivo.write("set yrange[ymin:ymax] "+"\n")
    archivo.write("set ytics septicy nomirror out font fuejes"+"\n")
    archivo.write("set mytics mty"+"\n")
    archivo.write("set title titizq font fuente # coloca el titulo de la figura con su fuente"+"\n")
    archivo.write("set xlabel ejexlabel font fulabel # el titulo del eje x tipo de letra y el tamaño del texto"+"\n")
    archivo.write("set ylabel ejeylabel font fulabel offset -3,0"+"\n")
    archivo.write("splot arcizq u 1:2:4 # para graficar reflectancia se cambia el ultimo número por 3"+"\n")#cambiar ultimo numero
    archivo.write("reset # el dibujo a pintar, en density plot"+"\n")
    archivo.write("\n")
    archivo.write("################################################"+"\n")
    archivo.write("#caracteristicas figura de la derecha"+"\n")
    archivo.write("##############################################"+"\n")
    archivo.write("set palette defined (0 'black',1 'white') #gray"+"\n")
    archivo.write("set cbrange [0 : 1]"+"\n")
    archivo.write("set pm3d interpolate 0,0 map"+"\n")
    archivo.write("set size tam,2*tam"+"\n")
    archivo.write("set origin 0.405,0."+"\n")
    archivo.write("unset key"+"\n")
    archivo.write("set xrange[xmin:xmax]"+"\n")
    archivo.write("set tics scale scatics font fuejes"+"\n")
    archivo.write("set xtics septicx nomirror out font fuejes"+"\n")
    archivo.write("set mxtics mtx"+"\n")
    archivo.write("set yrange[ymin:ymax]"+"\n")
    archivo.write("set noytics"+"\n")
    archivo.write("set title titder font fuente"+"\n")
    archivo.write("set xlabel ejexlabel font fulabel"+"\n")
    archivo.write("splot arcder u 1:2:4"+"\n")#cambiar ultimo numero
    archivo.write("reset"+"\n")
    archivo.write("\n")
    archivo.write("unset multiplot # se debe finalizar el metodo que permite pintar muchas figuras"+"\n")
    


def creararchivo(parametros,ventanaes):
    try:
        remove("progresote.dat")
        remove("progresotm.dat")
    except:
        pass
    
    archivo=open("CTETMF.esf","w")
    for p in range(0,len(parametros)):
        if p < 6:
            archivo.write(str(parametros[p])+"\n")
        elif p >=6 :
            for h in parametros[p]:
                archivo.write(str(h)+"\n")
    archivo.close()
    ventanaes.destroy()
   
    ventanaSimulacion(parametros[0])
    
    
    fi_ff = str(parametros[1] +","+ parametros[2])
    gnu_plot_TETMvsAng(parametros[0],parametros[1],fi_ff)
    shutil.move(parametros[0]+'.plt', parametros[0]+'/'+parametros[0]+'.plt')

def ventanaSimulacion(nombre):
    # creacion de la ventana - simulación en proceso modo TE
    ventanaproceso = tk.Toplevel(ventana)
    ventanaproceso.attributes('-disabled', True)
    anchoVentana = 830
    altoVentana = 280
    ventanaproceso.title("Sistema fotónico 1D")
    ventanaproceso.iconbitmap("./img/isotipo.ico")
    ventanaproceso.configure(bg='white')
    def closeProgram():
        ventana.destroy()
    # redimensionar nuestra ventana
    ventanaproceso.protocol('WM_DELETE_WINDOW', closeProgram)
    x_ventana = ventanaproceso.winfo_screenwidth() // 2 - anchoVentana // 2
    y_ventana = ventanaproceso.winfo_screenheight() // 2 - altoVentana // 2
    posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventanaproceso.geometry(posicion)
    ventanaproceso.resizable(False, False)

    titleMenu = tk.Label(ventanaproceso, text = "Simulación en proceso", font="Calibri 18 bold", foreground="white", background="#08469B")

    #Creación de Labels Frame
    framemodoTE = tk.LabelFrame(ventanaproceso, background="white")
    framemodoTM = tk.LabelFrame(ventanaproceso, background="white")

    titulomodoTE = tk.Label(framemodoTE, text="Programa de cálculo modo TE", font="Calibri 16 bold", foreground="#08469B", background="white", anchor="center")
    titulomodoTM = tk.Label(framemodoTM, text="Programa de cálculo modo TM", font="Calibri 16 bold", foreground="#08469B", background="white", anchor="center")

    avancemodoTE = tk.Label(framemodoTE, text="0%", font="Calibri 12 bold", foreground="#08469B", background="white", anchor="center")
    avancemodoTM = tk.Label(framemodoTM, text="0%", font="Calibri 12 bold", foreground="#08469B", background="white", anchor="center")

    #Posicionamiento en pantalla de los elementos
    titleMenu.place(x=0, y=0, width=830, height=50)
    framemodoTE.place(x=10, y=55, width=400, height=200)
    framemodoTM.place(x=420, y=55, width=400, height=200)

    titulomodoTE.place(x=10, y=20, width=370)
    titulomodoTM.place(x=10, y=20, width=370)

    avancemodoTE.place(x=180, y=105)
    avancemodoTM.place(x=180, y=105)
    


    #labelAnchoCapa = tk.Label(myframe, text="Ancho de la capa", font="Calibri 12", foreground="#08469B", background="white" )
    #anchoCapa = tkinter.Entry(myframe, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, relief="flat", bd=1)


    s = Style()
    s.configure("TCombobox", selectBackground='green')
    s.theme_use('alt')
    s.configure("TProgressbar", thickness=7, troughcolor='#a2c4c9',
        background='#b7c800', bordercolor="#a2c4c9", relief="flat", bd=1)

    progress_ggte = Progressbar(framemodoTE, orient=HORIZONTAL, style="TProgressbar",length=200)
    progress_ggte.place(x=95, y=80,height=20)

    progress_ggtm = Progressbar(framemodoTM, orient=HORIZONTAL, style="TProgressbar",length=200)
    progress_ggtm.place(x=95, y=80,height=20)
    piepagina = tk.Label(ventanaproceso, background="#F5841F")
    piepagina.place(x=0, y = 260, width=830, height=20)
   
    x = 0
    while(x < 100):
        os.system("TE")
        archivo=open("progresote.dat")
        lineas = archivo.readlines()
        totalSimulacion = "".join(lineas).strip()
        print(totalSimulacion)
        progress_ggte["value"]=int(totalSimulacion)
        avancemodoTE["text"] = str(totalSimulacion + "%")
        x=int(totalSimulacion)
        ventanaproceso.update_idletasks()
    
    y = 0
    
    while(y < 100):
        os.system("TM")
        archivo=open("progresotm.dat")
        lineas = archivo.readlines()
        totalSimulacion = "".join(lineas).strip()
        print(totalSimulacion)
        progress_ggtm["value"]=int(totalSimulacion)
        avancemodoTM["text"] = str(totalSimulacion + "%")
        y=int(totalSimulacion)
        ventanaproceso.update_idletasks()
        ventanaproceso.attributes('-disabled', False)
    
    shutil.move(nombre+'-TE.dat', nombre+'/'+nombre+'-TE.dat')
    shutil.move(nombre+'-TM.dat', nombre+'/'+nombre+'-TM.dat')
    
    
    
    
    
    
    

    
    


def ventanaParametros(parametros,menuprincipal):
    ventanaes = tk.Toplevel(ventana)
    ventanaes.title("Sistema fotónico 1D")
    ventanaes.iconbitmap("./img/isotipo.ico")
    ventanaes.configure(bg='white')
    ventanaes.resizable(False, False)
    ventanaes.protocol('WM_DELETE_WINDOW', closeProgram)
    # redimensionar nuestra ventana
    anchoVentana = 500
    altoVentana = 600
    x_ventana = ventanaes.winfo_screenwidth() // 2 - anchoVentana // 2
    y_ventana = ventanaes.winfo_screenheight() // 2 - altoVentana // 2
    posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventanaes.geometry(posicion)

    #Agregar LabelFrame Padre
    framePadre = tk.LabelFrame(ventanaes, background="white", relief="flat", bd=1)

    #Creación del Canvas
    mycanvas = Canvas(framePadre, height=500, width=500, background="white")
    mycanvas.pack(side=LEFT, fill="both", expand="yes")

    #Creación del Scrollbar
    yscrollbar = ttk.Scrollbar(framePadre, orient="vertical", command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")

    mycanvas.configure(yscrollcommand=yscrollbar.set,height=760, width=280)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

    myframe = tk.Frame(mycanvas, width=500, background="white", relief="flat", bd=1)
    mycanvas.create_window((0,0), window=myframe, anchor="nw")

    #Posicionamiento en pantalla del LabelFrame
    
    
    frameGenerales = tk.LabelFrame(myframe,background="white",width=500,height=300, relief="flat", bd=1)
    
    tituloVentanaSimulada = tk.Label(frameGenerales, text="Estructura simulada", font="Calibri 18 bold", foreground="white", background="#08469B",anchor="center")
    tituloVentanaSimulada.place(x=0, y=0, width=500, height=50)
    

    nombreArchivo = tk.Label(frameGenerales, text="Nombre del archivo:", font="Calibri 12", foreground="#08469B", background="white")
    nombreArchivo.place(x=30, y=65)
    datoNombreArchivo = tk.Label(frameGenerales, text=parametros[0], font="Calibri 12", background="white")
    datoNombreArchivo.place(x=290, y=65)

    anchoBanda = tk.Label(frameGenerales, text="Ancho de banda para la frecuencia:", font="Calibri 12", foreground="#08469B", background="white")
    anchoBanda.place(x=30, y=100)
    if parametros[1] == "1":
        datoAnchoBanda = tk.Label(frameGenerales, text="GHz", font="Calibri 12", background="white")
        datoAnchoBanda.place(x=290, y=100)
    elif parametros[1] == "2":
        datoAnchoBanda = tk.Label(frameGenerales, text="THz", font="Calibri 12", background="white")
        datoAnchoBanda.place(x=290, y=100)
    elif parametros[1] == "3":
        datoAnchoBanda = tk.Label(frameGenerales, text="PHz", font="Calibri 12", background="white")
        datoAnchoBanda.place(x=290, y=100)

    frecuenciaInicial = tk.Label(frameGenerales, text="Frecuencia inicial:", font="Calibri 12", foreground="#08469B", background="white")
    frecuenciaInicial.place(x=30, y=135)
    datoFrecuenciaInicial = tk.Label(frameGenerales, text=parametros[2], font="Calibri 12", background="white")
    datoFrecuenciaInicial.place(x=290, y=135)

    frecuenciaFinal = tk.Label(frameGenerales, text="Frecuencia final:", font="Calibri 12", foreground="#08469B", background="white")
    frecuenciaFinal.place(x=30, y=170)
    datoFrecuenciaFinal = tk.Label(frameGenerales, text=parametros[3], font="Calibri 12", background="white")
    datoFrecuenciaFinal.place(x=290, y=170)

    NumeroParticiones = tk.Label(frameGenerales, text="Número de particiones de frecuencia:", font="Calibri 12", foreground="#08469B", background="white")
    NumeroParticiones.place(x=30, y=205)
    datoNumeroParticiones = tk.Label(frameGenerales, text=parametros[4], font="Calibri 12", background="white")
    datoNumeroParticiones.place(x=290, y=205)

    NumeroTotalPeriodos = tk.Label(frameGenerales, text="Número total de períodos:", font="Calibri 12", foreground="#08469B", background="white")
    NumeroTotalPeriodos.place(x=30, y=240)
    datoNumeroTotalPeriodos = tk.Label(frameGenerales, text=parametros[5], font="Calibri 12", background="white")
    datoNumeroTotalPeriodos.place(x=290, y=240)

    NumeroCapas = tk.Label(frameGenerales, text="Número de capas de la estructura:", font="Calibri 12", foreground="#08469B", background="white")
    NumeroCapas.place(x=30, y=275)
    datoNumeroCapas = tk.Label(frameGenerales, text=parametros[6], font="Calibri 12", background="white")
    datoNumeroCapas.place(x=290, y=275)
    framePadre.pack(fill='x')
    frameGenerales.pack(fill=BOTH,expand=True)
    
    frameCapas = tk.LabelFrame(myframe,background="white",width=500, height=500, relief="flat", bd=1)
    frameCapas.pack(fill='x')
    for c in range (7, len(parametros)):
        Labelframecapa = tk.LabelFrame(frameCapas, background="white", width=440, height=275, highlightbackground="white", highlightcolor="white", highlightthickness=2, relief="flat", bd=1)
        capa = tk.Label(Labelframecapa, text="Parametros de la Capa "+ str(c - 6), font="Calibri 12 bold", foreground="white", background="#08469B",anchor="center")
        capa.place(x=0, y=0, width=425)
        anchocapa = tk.Label(Labelframecapa, text="Ancho de la capa:", font="Calibri 12", foreground="#08469B", background="white")
        anchocapa.place(x=0, y=35)
        datoanchocapa = tk.Label(Labelframecapa, text=parametros[c][0], font="Calibri 12", background="white")
        datoanchocapa.place(x=260, y=35)
        tipoPerfil = tk.Label(Labelframecapa, text="Tipo de perfil:", font="Calibri 12", foreground="#08469B",background="white")
        tipoPerfil.place(x=0, y=70)
        if parametros[c][1] == "1":
            datoTipoPerfil = tk.Label(Labelframecapa, text="Lineal: Ax+B",  font="Calibri 12", background="white")
            datoTipoPerfil.place(x=260, y=70)
        elif parametros[c][1] == "2":
            datoTipoPerfil = tk.Label(Labelframecapa, text="Exponencial: Aexp(Bx)+C",  font="Calibri 12", background="white")
            datoTipoPerfil.place(x=260, y=70)
        parametrosTipoPerfil = tk.Label(Labelframecapa, text="Parámetros del tipo de perfil:", font="Calibri 12", foreground="#08469B", background="white")
        parametrosTipoPerfil.place(x=0, y=105)
        parametroA = tk.Label(Labelframecapa, text="A:", font="Calibri 12", foreground="#08469B", background="white")
        parametroA.place(x=55, y=140)
        datoParametroA = tk.Label(Labelframecapa, text=parametros[c][2], font="Calibri 12", background="white")
        datoParametroA.place(x=85, y=140)
        parametroB = tk.Label(Labelframecapa, text="B:", font="Calibri 12", foreground="#08469B", background="white")
        parametroB.place(x=55, y=175)
        datoParametroB = tk.Label(Labelframecapa, text=parametros[c][3], font="Calibri 12", background="white")
        datoParametroB.place(x=85, y=175)
        if len(parametros[c]) == 6:
            parametroC = tk.Label(Labelframecapa, text="C:", font="Calibri 12", foreground="#08469B", background="white")
            parametroC.place(x=55, y=210)
            datoParametroC = tk.Label(Labelframecapa, text=parametros[c][4], font="Calibri 12", background="white")
            datoParametroC.place(x=85, y=210)
            numeroParticiones = tk.Label(Labelframecapa, text="Número de particiones:", font="Calibri 12", foreground="#08469B", background="white")
            numeroParticiones.place(x=0, y=245)
            datoNumeroParticiones = tk.Label(Labelframecapa, text=parametros[c][5], font="Calibri 12", background="white")
            datoNumeroParticiones.place(x=260, y=245)
        elif len(parametros[c]) == 5:
            numeroParticiones = tk.Label(Labelframecapa, text="Número de particiones:", font="Calibri 12", foreground="#08469B", background="white")
            numeroParticiones.place(x=0, y=210)
            datoNumeroParticiones = tk.Label(Labelframecapa, text=parametros[c][4], font="Calibri 12", background="white")
            datoNumeroParticiones.place(x=260, y=210)
            Labelframecapa.configure(height=250)
        Labelframecapa.pack()
        frameCapas.pack()
    pregunta = tk.Label(frameCapas, text="¿Está seguro que desea realizar la simulación?", font="Calibri 14 bold", foreground="#08469B", background="white")
    pregunta.pack()
    Labelbotones = tk.LabelFrame(frameCapas, background="white", width=500, height=30, highlightbackground="white", highlightcolor="white", highlightthickness=2, relief="flat", bd=1)
    Labelbotones.pack()
    buttonSi = tk.Button(Labelbotones, text = "Si", font="Calibri 12 bold", background="#B7C800", cursor="hand2",relief="flat", bd=1,width=10,command= lambda: creararchivo(parametros,ventanaes))
    buttonSi.pack(side=LEFT,padx=5)
    buttonNo = tk.Button(Labelbotones, text = "No", font="Calibri 12 bold", background="#B7C800", cursor="hand2",relief="flat", bd=1,width=10,command= lambda: volver(ventanaes,menuprincipal))
    buttonNo.pack(side=RIGHT,padx=5)
    
    piepagina = tk.Label(frameCapas, background="#F5841F")
    piepagina.pack(fill="x")
    
             

          




# cerrar el programa
def closeProgram():
    ventana.destroy()

#validar combobox

# Patrones de validaciones de cajas de texto

#def patrones_validaciones():


    
    

# crear capas

def crearCapas(vista,numerodecapas,capapadre,buttonEnviarDatos):
    
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
        if  numero == 0:
            numerodecapas.configure(highlightcolor="red")
            numerodecapas.configure(highlightbackground="red")
            messagebox.showwarning('Dato Incorrecto', 'Tenga en cuenta que el Numero de capas debe se un dato de tipo entero y mayor que 0')
        if esnumero == True and numero > 0:
            for i in range(0, len(miscapas)):
                miscapas.pop()
            capapadre = tk.LabelFrame(vista,highlightbackground="white", highlightcolor="white", highlightthickness=1, relief="flat", bd=1)
            #capapadre.place(x=75, y=430)
            mycanvas = Canvas(capapadre, background="white",highlightbackground="white", highlightcolor="white", highlightthickness=2, relief="flat", bd=1)
            mycanvas.pack(side=LEFT, fill="both", expand="yes")
            yscrollbar = tk.Scrollbar(capapadre, orient="vertical", command=mycanvas.yview)
            yscrollbar.pack(side=RIGHT, fill="y")
            mycanvas.configure(yscrollcommand=yscrollbar.set,height=290,width=349,bg="white")
            mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
            myframe = tk.Frame(mycanvas, background="white",highlightbackground="white", highlightcolor="white", highlightthickness=2, relief="flat", bd=1)
            elements.append(myframe)
            mycanvas.create_window((0,0), window=myframe, anchor="nw")
            capapadre.place(x=434, y=150)
        
            options = [
                "Lineal: Ax+B", 
                "Exponencial: Aexp(Bx)+C",
            ]
            
            parametro3 = []
            labelparametroC = []
            dropdowntipo=[]
            indice = []
            
            def validar(event,i,optiondropdown):
                x = clicked[i-1].get()
                if x == "Exponencial: Aexp(Bx)+C":
                    print("entre")
                    optiondropdown.delete(0, "end")
                    optiondropdown.insert(0,"2")
                    parametro3[i-1].place(x=230, y=206)
                    labelparametroC[i-1].place(x=266, y=176)
                elif x == "Lineal: Ax+B":
                    print("line")
                    optiondropdown.delete(0, "end")
                    optiondropdown.insert(0,"1")
                    parametro3[i-1].place_forget()
                    labelparametroC[i-1].place_forget()
                    parametro3[i-1].delete(0, "end")
                

        
            for hijo in myframe.winfo_children():
                hijo.destroy()
            for i in range(1,numero + 1):
                capaPanel = tk.LabelFrame(myframe,height=285,width=352,bg = "white",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, relief="flat", bd=1)
                labelAnchoCapa = tk.Label(capaPanel, text="Ancho de la capa:", font="Calibri 12", foreground="#08469B", background="white" )
                anchoCapa = tkinter.Entry(capaPanel, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1)
                labelTextoEjemplo = Label(capaPanel, text="Escribir en notación científica \nEjemplo: 8e06", anchor="nw", font="Calibri 8", foreground="#08469B", background="white" )
                tipodeperfil = tk.Label(capaPanel, text="Tipo de perfil:", font="Calibri 12", foreground="#08469B", background="white")
                clicked.append(StringVar())
                indice.append(i-1)
                optiontipoperfil = tkinter.Entry(capaPanel, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1)
                optiontipoperfil.insert(0, "1")
                #entrys.append(optiontipoperfil)
                d = tk.OptionMenu(capaPanel, clicked[i-1], *options, command=lambda event,i=i,optiondropdown=optiontipoperfil:validar(event, i,optiondropdown))
                d['menu'].invoke(options[0])
                d.config(background="white", highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, font="Calibri 10 bold",relief="flat", bd=1)
                #d.widgetName= str(indice[i-1])
                dropdowntipo.append(d)
                dropdowntipo[i-1].widgetName= str(indice[i-1])
               
                
                labelparametros = tk.Label(capaPanel, text="Parametros del tipo de perfil:", font="Calibri 12", foreground="#08469B", background="white")

                labelparametroA = tk.Label(capaPanel, text="A", font="Calibri 12 bold", foreground="#08469B", background="white")
                labelparametroB = tk.Label(capaPanel, text="B", font="Calibri 12 bold", foreground="#08469B", background="white")
                parametro1 = tkinter.Entry(capaPanel, font = "Calibri 12",width=10,highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1)
                parametro2 = tkinter.Entry(capaPanel, font = "Calibri 12",width=10,highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1)
                parametro3.append(tkinter.Entry(capaPanel, font = "Calibri 12",width=10,highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1))
                labelparametroC.append(tk.Label(capaPanel, text="C", font="Calibri 12 bold", foreground="#08469B", background="white"))
                labelparticiones = tk.Label(capaPanel, text="Número de particiones:", font="Calibri 12", foreground="#08469B", background="white")
                particiones = tkinter.Entry(capaPanel, font = "Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1)
                capaNumero = tk.Label(capaPanel, text="Capa " + str(i),font = "Calibri 12 bold",width=50 ,foreground="white", background="#08469B")
                miscapas.append(capaPanel)
                capaNumero.place(x=0, y=0, width=347, height=30)
                labelAnchoCapa.place(x=5, y=40)
                anchoCapa.place(x=165, y=40, width=105)
                labelTextoEjemplo.place(x=165, y=68)
                tipodeperfil.place(x=5, y=110)
                dropdowntipo[i-1].place(x=165,y=110)
                labelparametros.place(x=5, y=150)
                labelparametroA.place(x=60, y=176)
                labelparametroB.place(x=165, y=176)
                parametro1.place(x=25, y=206)
                parametro2.place(x=128, y=206)
                labelparticiones.place(x=5, y=246)
                particiones.place(x=165, y=246, width=105)
                capaPanel.pack(pady=5)
            if len(entrys)==7:
                entrys.pop(6)
                entrys.append(i)
            else:
                entrys.append(i)  
            
            
            buttonEnviarDatos.place(x=375, y = 477, width=80, height=30)



        

    


s = Style()
s.configure("TCombobox", selectBackground='green')
s.theme_use('alt')
s.configure("TProgressbar", thickness=7, troughcolor='#a2c4c9',
    background='#b7c800', bordercolor="#a2c4c9")
    #darkcolor="#a2c4c9",
    #lightcolor="#a2c4c9" )
# redimensionar nuestra ventana

imagen = PhotoImage(file="./img/logo.png")
etiqueta = Label(ventana,image=imagen, background="white")

titulo = tk.Label(ventana, text="Bienvenido al programa de cálculo de las"
"\npropiedades ópticas de sistemas fotónicos 1D" 
"\nformados por capas materiales de perfil gradativo")
titulo.configure(font="Calibri 16 bold", foreground="#08469B", background="white")

#txt = Label(ventana)
#titulo.config(font=("Courier bold", 20))
#titulo2.config(font=("Courier bold", 20))
#txt.config(font=("Courier bold", 20))
etiqueta.pack(pady=30)
titulo.pack()
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
button = tkinter.Button(ventana, text = "Entrar", font="Calibri 12 bold", foreground="black", background="#B7C800",  command=start, cursor="hand2", width=8, height=1,relief="flat", bd=1)
button.pack()
piepagina = tk.Label(ventana, background="#F5841F")
piepagina.pack(side=tk.BOTTOM, fill= tk.X)
ventana.mainloop()