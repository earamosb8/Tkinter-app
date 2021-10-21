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
from subprocess import check_output
import sys

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
parametrosGlobales = []
menuprincipal =""
regresar=False



scroll = Style()
scroll.configure('TScrollbar',background='blue')
nombrecarpeta=""


# Creacion de ventana principal
def createNewWindow(ventanaactual):
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
    ventanaactual.withdraw()

    menuprincipal = tk.Toplevel(ventanaactual)
    anchoVentana = 830
    altoVentana = 550
    x_ventana = ventanaactual.winfo_screenwidth() // 2 - anchoVentana // 2
    y_ventana = ventanaactual.winfo_screenheight() // 2 - altoVentana // 2
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
    
    def validarentry(event):
        regex = [",",".","-","{","}","(",")","*","+",";",":","'","´","¿","?","<",">","/",'"',"&","="]
        prueba = cajanombreArchivo.get()
        if event.char in regex:
            cajanombreArchivo.delete(0, tk.END)
            cajanombreArchivo.insert(0,prueba[:-1])
            
        #cajanombreArchivo.delete(0, tk.END)
        #cajanombreArchivo.insert(0,prueba.strip())
        if(event.char != " "):
            cajaubicacionArchivo["text"] ="Tkinter-app/" + prueba
    cajanombreArchivo.bind("<KeyRelease>", validarentry)
    
        
    
    cajaubicacionArchivo = tk.Label(frameGenerales, text="Tkinter-app/", font="Calibri 12", foreground="black", background="white" )
    
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
    global regresar
    if regresar is True:
        posicion = 7
    if regresar is False:
        posicion = 6

    for hijos in miscapas:
        grupo = []
        for nietos in hijos.winfo_children():
           
            if(type(nietos)==tkinter.Entry):
                x = str(nietos)
                x = x.split(".")
                if x[posicion] == "!entry2":
                    tipoperfil =  nietos.get()
                if x[posicion] == "!entry5" and tipoperfil=="1":
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
        print(entrys)
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
                    if x[posicion] == "!entry":
                        numero = validadornietos(nietos,"floatancho")
                        if numero == 0:
                            mensaje2 = "El Ancho de la Capa debe ser de tipo decimal mayor o igual que 0, puede usar notacion cientifica si lo desea.\n"
                            resultado = False
                    if x[posicion] == "!entry2":
                        tipoperfil =  nietos.get()
                    if x[posicion] == "!entry3":
                        numero = validadornietos(nietos,"float")
                    if x[posicion] == "!entry4":
                        numero = validadornietos(nietos,"float")
                    
                    if x[posicion] == "!entry5" and tipoperfil=="2":
                        numero = validadornietos(nietos,"float")

                    if numero == 0:
                        encontrado = mensaje2.find("Los Parametros A,B y C del Tipo de perfil deben ser decimales, y pueden ser positívos o negatívos\n")
                        if encontrado > -1:
                            mensaje2.replace("Los Parametros A,B y C del Tipo de perfil deben ser decimales, y pueden ser positívos o negatívos\n", "Los Parametros A,B y C del Tipo de perfil deben ser decimales, y pueden ser positívos o negatívos\n")
                        else:
                            mensaje2 += str("Los Parametros A,B y C del Tipo de perfil deben ser decimales, y pueden ser positívos o negatívos\n")
                        resultado = False
                    if x[posicion] == "!entry5" and tipoperfil=="1":
                        continue
                    if x[posicion] == "!entry6":
                        numero = validadornietos(nietos,"int")
                        if numero == 0:
                            mensaje2 +=str("El Numero de Particiones debe ser de tipo entero positivo")
                            resultado = False

        if resultado is False:
            mensaje = mensaje + mensaje2
            messagebox.showwarning('Advertencia!!!',mensaje)
            
        

        if resultado is True:
            global parametrosGlobales
            parametrosGlobales = parametros
            regresar = False
            mostrarParametros(parametros)


def mostrarParametros(parametros):
    menuprincipal = ""
    aux = []
    print(entrys[0])
    for n in ventana.winfo_children():
        if(type(n)==tkinter.Toplevel):
           menuprincipal = n
    menuprincipal.withdraw()
    ventanaParametros(parametros,menuprincipal)
    return menuprincipal
    
    
def volver(ventana1,ventana2):
    ventana1.destroy()
    ventana2.deiconify()

     

def gnu_plot_TETMvsAng(nombre,ran_fre,fi_ff,parametrosGrafica,venteditgrafica):   # funcion para la escritura del script de visualizacion en GNUPLOT
    #print(os.getcwd())
    os.chdir(nombre)
    def closeProgram():
        venteditgrafica.destroy()
    #venteditgrafica.protocol('WM_DELETE_WINDOW', closeProgram())
    print(ran_fre)
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
    archivo.write("fuente='"+parametrosGrafica[0]+", "+parametrosGrafica[1]+"'\n") # titulo, tipo y tamaño de la fuente
    archivo.write("ejexlabel='{"+parametrosGrafica[8]+"}'"" # label del eje x"+"\n")##
    if ran_fre=="1":
       archivo.write("ejeylabel='"+parametrosGrafica[7]+ " (GHz)'"+"\n") # label del eje y"+"\n")##
    elif ran_fre=="2":
       archivo.write("ejeylabel="+parametrosGrafica[7]+ " (THz)"+"\n") # label del eje y"+"\n")##
    elif ran_fre=="3":
       archivo.write("ejeylabel="+parametrosGrafica[7]+ " (PHz)"+"\n") # label del eje y"+"\n")##
    archivo.write("fulabel='"+parametrosGrafica[0]+", "+parametrosGrafica[2]+"'\n") # label tipo y tamaño de la fuente
    archivo.write("fuejes='"+parametrosGrafica[0]+", "+parametrosGrafica[3]+"'\n") # fuente de los ejes y el tamaño
    archivo.write("\n")
    archivo.write("set multiplot # ayuda a pintar muchas figuras en una sola, deben especificarse todas las caracteristicas de cada figura"+"\n")
    archivo.write("\n")
    archivo.write("#########################################"+"\n")
    archivo.write("# caracteristicas figura de la izquierda"+"\n")
    archivo.write("###########################################"+"\n")
    archivo.write("set palette defined (0 '"+parametrosGrafica[6]+"',1 '"+parametrosGrafica[5]+"')"+"\n")
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
    archivo.write("set palette defined (0 '"+parametrosGrafica[6]+"',1 '"+parametrosGrafica[5]+"')"+"\n")
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
    archivo.write("splot arcder u 1:2:"+parametrosGrafica[4]+"\n")#cambiar ultimo numero
    archivo.write("reset"+"\n")
    archivo.write("\n")
    archivo.write("unset multiplot # se debe finalizar el metodo que permite pintar muchas figuras"+"\n")
    os.chdir('..')
    def cerrar():
        ventana.quit()
    botonsalir = tk.Button(venteditgrafica, text = "Salir", font="Calibri 12 bold", background="#B7C800", cursor="hand2",relief="flat", bd=1,width=10,command = lambda:cerrar())
    botonsalir.place(x=750, y = 560)
    mes=messagebox.askquestion(message="la Grafica se ha generado en /Tkinter-app/"+nombre+" ,¿Desea generar otra simulación?", title="Confirmación")
    if mes =='yes':
        entrys.clear()
        createNewWindow(venteditgrafica)
        global regresar
        regresar=True
    elif mes == 'no':
        print("hola")

    


def creararchivo(parametros,ventanaes,menuprincipal):
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
    menuprincipal.destroy()
   
    ventanaSimulacion(parametros[0],menuprincipal)
    

def ventanaSimulacion(nombre,menuprincipal):
    # creacion de la ventana - simulación en proceso modo TE
    ventanaproceso = tk.Toplevel(ventana)
    def deshabilitar():
        return
    
    
    menuprincipal.destroy()
    ventanaproceso.attributes('-disabled', True)
    anchoVentana = 830
    altoVentana = 280
    ventanaproceso.title("Sistema fotónico 1D")
    ventanaproceso.iconbitmap("./img/isotipo.ico")
    ventanaproceso.configure(bg='white')
    def closeProgram():
        ventana.quit()
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
    framemensaje = tk.LabelFrame(ventanaproceso, background="white")
    mensaje = tk.Label(framemensaje, text="Archivos "+nombre+'-TE.dat '+"y "+nombre+'-TM.dat', font="Calibri 12 bold", foreground="#08469B", background="white", anchor="center")
    mensaje2 = tk.Label(framemensaje, text="se crearon exitosamente" , font="Calibri 12 bold", foreground="#08469B", background="white", anchor="center")
    buttonVentanagraf = tk.Button(framemensaje, text = "Configurar grafica", font="Calibri 12 bold", background="#B7C800", cursor="hand2",relief="flat", bd=1,width=20,command = lambda: ventanaEdicionGrafica(ventanaproceso,nombre))
   
    x = 0
    while(x < 100):
        os.system("TE")
        archivo=open("progresote.dat")
        lineas = archivo.readlines()
        totalSimulacion = "".join(lineas).strip()
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
        progress_ggtm["value"]=int(totalSimulacion)
        avancemodoTM["text"] = str(totalSimulacion + "%")
        y=int(totalSimulacion)
        ventanaproceso.update_idletasks()
        ventanaproceso.attributes('-disabled', False)
    
    ventanaproceso.protocol('WM_DELETE_WINDOW', lambda: deshabilitar())
    
    shutil.move(nombre+'-TE.dat', nombre+'/'+nombre+'-TE.dat')
    shutil.move(nombre+'-TM.dat', nombre+'/'+nombre+'-TM.dat')

    if x == 100 and y == 100:
        
        mensaje.pack()
        mensaje2.pack()
        buttonVentanagraf.pack()
        framemensaje.place(x=215, y=183, width=400, height=100)
        
def ventanaEdicionGrafica(ventanaproceso,nombre):
    
    esc = ""
    datosgrafica = []
    if parametrosGlobales[1]=="1":
        esc = " (Ghz)"
    if parametrosGlobales[1]=="2":
        esc = " (Thz)"
    if parametrosGlobales[1]=="3":
        esc = " (Phz)"
    
    
    venteditgrafica =  tk.Toplevel(ventana)
    
    def nothing():
        return

    venteditgrafica.protocol('WM_DELETE_WINDOW', lambda:nothing())
    
    ventanaproceso.withdraw()
    anchoVentana = 900
    altoVentana = 620
    venteditgrafica.title("Sistema fotónico 1D")
    venteditgrafica.iconbitmap("./img/isotipo.ico")
    venteditgrafica.configure(bg='white')

    x_ventana = venteditgrafica.winfo_screenwidth() // 2 - anchoVentana // 2
    y_ventana = venteditgrafica.winfo_screenheight() // 2 - altoVentana // 2
    posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    venteditgrafica.geometry(posicion)
    venteditgrafica.resizable(False, False)

    titleedit= tk.Label(venteditgrafica, text = "Personalización de Gráfica", font="Calibri 18 bold", foreground="white", background="#08469B")

    #Creación de Labels y LabelFrame
    labeltitulosgrafica = tk.Label(venteditgrafica, text="Títulos", font="Calibri 14 bold", foreground="#08469B", background="white")
    labelfuente = tk.Label(venteditgrafica, text="Fuente:", font="Calibri 15 bold", foreground="#08469B", background="white")
    labeltamanoTitulos = tk.Label(venteditgrafica, text="Tamaño de titulos:", font="Calibri 15 bold", foreground="#08469B", background="white")
    labeltamanoSubtitulos = tk.Label(venteditgrafica, text="Tamaño de subtitulos:", font="Calibri 16 bold", foreground="#08469B", background="white")
    labeltamanoNumeros = tk.Label(venteditgrafica, text="Tamaño de numeros:", font="Calibri 15 bold", foreground="#08469B", background="white")
    labeltipoDiagrama = tk.Label(venteditgrafica, text="Tipo de diagrama:", font="Calibri 15 bold", foreground="#08469B", background="white")
    labelcambiarTitulos = tk.Label(venteditgrafica, text="Cambiar titulos:", font="Calibri 15 bold", foreground="#08469B", background="white")
    labelcambiarTitulosx = tk.Label(venteditgrafica, text="eje X:", font="Calibri 15 bold", foreground="#08469B", background="white")
    cajaX = tkinter.Entry(venteditgrafica, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1,width=10)
    cajaX.bind("<KeyRelease>", lambda event: validarentry2(event,"etiqueta",cajaX,angle1,angle2))
    labelcambiarTitulosy = tk.Label(venteditgrafica, text="eje Y:", font="Calibri 15 bold", foreground="#08469B", background="white")
    cajaY = tkinter.Entry(venteditgrafica, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1,width=10)
    cajaY.bind("<KeyRelease>", lambda event: validarentry2(event,"canvas",cajaY))
    #cajaX2 = tkinter.Entry(venteditgrafica, font="Calibri 12",highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2,relief="flat", bd=1,width=10)  
    #cajaX2.bind("<KeyRelease>", lambda event: validarentry2(event,"etiqueta",cajaX2,angle2))
    idtext = ""
    def validarentry2(event,elemento,caja,etiquetaopcional=None,etiquetaopcional2=None):
        prueba = caja.get()
        if elemento == "canvas":  
            titulofrecuencia.delete('all')
            global idtext
            if prueba == "":
                titulofrecuencia.delete('all')
                idtext =titulofrecuencia.create_text(18, 253, text = str("Frecuencia" + esc), angle = 90, anchor = "w",font=(clicked[1].get(),tamanoSub))
                #caja.insert(0, "Frecuencia")
                parametrosGrafica[7] = "Frecuencia"
            else:
                idtext =titulofrecuencia.create_text(18, 253, text = str(prueba+esc), angle = 90, anchor = "w",font=(clicked[1].get(),tamanoSub))
                parametrosGrafica[7] = prueba
        if elemento == "etiqueta":
            if prueba == "":
                etiquetaopcional["text"] = "Angle (y)"
                etiquetaopcional2["text"] = "Angle (y)"
                parametrosGrafica[8] = "Angle (y)"
                #caja.insert(0, "Angle (y)")

            else:
                etiquetaopcional["text"] = prueba
                etiquetaopcional2["text"] = prueba
                parametrosGrafica[8] = prueba
        #print(parametrosGrafica)
        




            
            

    labelbarraCalor = tk.Label(venteditgrafica, text="Colores barra de calor:", font="Calibri 15 bold", foreground="#08469B", background="white")
    fi_ff = str(parametrosGlobales[2] +","+ parametrosGlobales[3])
    print (parametrosGlobales)
    buttonguardaredit= tkinter.Button(venteditgrafica, text = "Guardar", cursor="hand2", width=8, height=1,relief="flat", bd=1, font="Calibri 12 bold", foreground="black", background="#B7C800",command=lambda: gnu_plot_TETMvsAng(nombre,parametrosGlobales[1],fi_ff,parametrosGrafica,venteditgrafica))
   
    #gnu_plot_TETMvsAng(parametros[0],parametros[1],fi_ff)
    
    framenamearchivo = tk.LabelFrame(venteditgrafica, background="white", highlightbackground="white", highlightcolor="white", highlightthickness=2, relief="flat", bd=1)

    framegrafica = tk.LabelFrame(framenamearchivo, background="white", highlightbackground="#a2c4c9", highlightcolor="#a2c4c9", highlightthickness=2, relief="flat", bd=1,width=700)
    
    modostitulo = tk.LabelFrame(framegrafica,background="white",highlightcolor="white",highlightbackground="white", highlightthickness=2,relief="flat")
    modostitulo.grid(row=0, column=1)
    titulofrecuencia = tkinter.Canvas(framegrafica, width = 30, height = 252,background="white",highlightbackground="white")
    idtext = titulofrecuencia.create_text(18, 253, text = "Frecuencia"+esc, angle = 90, anchor = "w",font=("Times New Roman",22))
    
    titulofrecuencia.grid(row=1, column=0)
    barracolores= tk.LabelFrame(framegrafica,background="white",relief="flat",highlightbackground="black",highlightcolor="black", highlightthickness=1,bd=1,width= 10, height = 250)
                                                        
    segmentosInicial = tk.LabelFrame(barracolores,background="#FAF9F6",relief="flat",bd=0,width= 10, height = 50)
    segmentosInicial.pack()
    segmentos2 = tk.LabelFrame(barracolores,background="#D5D4D1",relief="flat",bd=0,width= 10, height = 50)
    segmentos2.pack()
    segmentos3 = tk.LabelFrame(barracolores,relief="flat", height = 50,bd=0)
    segmentosaux1 = tk.LabelFrame(segmentos3, width=10, height = 25,bd=0)
    segmentosaux2 = tk.LabelFrame(segmentos3,width=10, height = 25,bd=0)
    segmentosaux1.pack()
    segmentosaux2.pack()
    segmentos3.pack()
    segmentos4 = tk.LabelFrame(barracolores,background="#80807F",relief="flat",bd=0,width= 10, height = 50)
    segmentos4.pack()
    segmentosFinal = tk.LabelFrame(barracolores,background="#000000",relief="flat",bd=0,width= 10, height = 50)
    segmentosFinal.pack()

    barracolores.grid(row=1, column=3)

    escalanumeros= tk.Label(framegrafica,text="1\n0.8\n0.6\n0.4\n0.2\n0",background="white")
    escalanumeros.config(font=("Times New Roman",2))
    escalanumeros.grid(row=1, column=4)
    titulosTE = Label(modostitulo,text="TE",anchor=tk.CENTER,background="white")
    titulosTE.config(font=("Times New Roman",22))
    titulosTE.grid(row=0,column=0)
    espacio=Label(modostitulo,width= 30,background="white")
    espacio.grid(row=0, column=2)
    titulosTM = Label(modostitulo,text="TM",anchor=tk.CENTER,background="white")
    titulosTM.config(font=("Arial",22))
    titulosTM.grid(row=0,column=3)
    
    bloquegrafica = tk.LabelFrame(framegrafica,width=300,height = 250, background="white",highlightbackground="black", highlightcolor="black", highlightthickness=2,relief="flat")
    #etiqueta = Label(framegrafica,image=imagen2, background="white")
    colorframeaux = tk.LabelFrame(bloquegrafica, background="red",highlightbackground="white", highlightcolor="white", highlightthickness=2,relief="flat",width=110,height=246)
    colorframeaux2 = tk.LabelFrame(bloquegrafica, background="red",highlightbackground="black", highlightcolor="black", highlightthickness=1,relief="flat",width=110,height=246)
    colorframe1 = tk.LabelFrame(bloquegrafica, background="black",highlightbackground="black", highlightcolor="black", highlightthickness=1,relief="flat",width=110,height=246)
    colorframeaux.grid(row=0,column=0)
    colorframe1.grid(row=0,column=1)
    colorframe2 = tk.LabelFrame(bloquegrafica, background="red",highlightbackground="white", highlightcolor="white", highlightthickness=2,relief="flat",width=110,height=246)
    colorframe2.grid(row=0,column=3)
    colorframeaux2.grid(row=0,column=4)
    bloquegrafica.grid(row=1,column=1,columnspan=1,rowspan=1)
    escalanumeros2= tk.Label(framegrafica,text="90 75 60 45 30 15 0 15 30 45 60 75 90",background="white")
    escalanumeros2.config(font=("Arial",18))
    escalanumeros2.grid(row=2, column=1)
    modostitulo2 = tk.LabelFrame(framegrafica, background="white",highlightbackground="white", highlightcolor="white", highlightthickness=2,relief="flat")
    modostitulo2.grid(row=3, column=1)
    angle1 = Label(modostitulo2,text="Angle (y)",anchor=tk.CENTER,background="white")
    angle1.config(font=("Arial",22))
    angle1.grid(row=0,column=0)
    espacio=Label(modostitulo2,width= 20,background="white")
    espacio.grid(row=0, column=2)
    angle2 = Label(modostitulo2,text="Angle (y)",anchor=tk.CENTER,background="white")
    angle2.config(font=("Arial",22))
    angle2.grid(row=0,column=3)
    

    labelarchivonombre = tk.Label(framenamearchivo, text=nombre+".plt", font="Arial 18 bold", foreground="#08469B", background="white")
    tipo = ["Arial","Calibri","Times New Roman"]
    tamf = [" 8 "," 10 "," 12 "," 14 "," 16 "," 18 "," 20 "," 22 "," 24 "]
    colores = {"white":"FFFFFF","red":"FF0000","blue":"0000FF","magenta":"FF00FF","green":"088A08","yellow":"FFFF00","cyan":"00FFFF","orange":"FF8000","gray":"848484"}
    coloresauxiliares = [["#FAFAFA","#F2F2F2"],["#FA5858","#F5A9A9"],["#5858FA","#A9A9F5"],["#FA58F4","#F5A9F2"],["#01DF01","#2EFE2E"],["#F4FA58","#F2F5A9"],["#58FAF4","#A9F5F2"],["#FAAC58","#F5D0A9"],["#BDBDBD","#E6E6E6"]]
    tipd = ["Trasmitancia","Reflectancia"]
    tamanoSub = 18
    tamanoTitulos = 20
    tamanoNumeros = 18
    tipoDiagrama = ""
    colorSelected=""
    colorSelected2=""
    clicked=[]
    clicked=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
    
    parametrosGrafica = ['Arial','20','18','18','3','white','gray','Frecuencia',"Angle (y)"] 
    claves = list(colores.keys())
    valores = list(colores.values())
    
    



    def validar(event):
        titulosTE.config(font=(clicked[0].get(),tamanoTitulos))
        titulosTM.config(font=(clicked[0].get(),tamanoTitulos))
        escalanumeros.config(font=(clicked[0].get(),tamanoNumeros))
        escalanumeros2.config(font=(clicked[0].get(),tamanoNumeros))
        titulofrecuencia.itemconfigure(idtext, font=(clicked[0].get(),tamanoSub))
        angle1.config(font=(clicked[0].get(),tamanoSub))
        angle2.config(font=(clicked[0].get(),tamanoSub))
        parametrosGrafica[0] = clicked[0].get()
    

    def validartamano(event,seccion):
        if seccion == "titulos":
            global tamanoTitulos
            tamanoTitulos = clicked[1].get()
            titulosTE.config(font=(clicked[1].get(),tamanoTitulos))
            titulosTM.config(font=(clicked[1].get(),tamanoTitulos))
            parametrosGrafica[1] = clicked[1].get().strip()

        if seccion == "subtitulos":
            global tamanoSub
            tamanoSub = clicked[2].get()
            titulofrecuencia.itemconfigure(idtext, font=(clicked[2].get(),tamanoSub))
            angle1.config(font=(clicked[2].get(),tamanoSub))
            angle2.config(font=(clicked[2].get(),tamanoSub))
            parametrosGrafica[2] = clicked[2].get().strip()
            
        if seccion == "numeros":
            global tamanoNumeros
            tamanoNumeros = clicked[3].get()
            escalanumeros.config(font=(clicked[3].get(),tamanoNumeros))
            escalanumeros2.config(font=(clicked[3].get(),tamanoNumeros))
            parametrosGrafica[3] = clicked[3].get().strip()
        if seccion == "tipodiagrama":
            global tipoDiagrama
            if clicked[4].get() == "Trasmitancia":
                tipoDiagrama = "4"
                parametrosGrafica[4] = tipoDiagrama
                indice=claves.index(clicked[5].get())
                colorframe2.config(bg=coloresauxiliares[indice][0],highlightbackground=coloresauxiliares[indice][0], highlightcolor=coloresauxiliares[indice][0])
                indice2=claves.index(clicked[6].get())
                colorframeaux.config(bg=coloresauxiliares[indice2][0],highlightbackground=coloresauxiliares[indice2][0], highlightcolor=coloresauxiliares[indice2][0])
                colorframeaux2.config(bg=coloresauxiliares[indice2][0],highlightbackground=coloresauxiliares[indice2][0], highlightcolor=coloresauxiliares[indice2][0])
                
            
            if clicked[4].get() == "Reflectancia":
                tipoDiagrama = "3"
                parametrosGrafica[4] = tipoDiagrama
                indice2=claves.index(clicked[5].get())
                colorframeaux2.config(bg=coloresauxiliares[indice2][0],highlightbackground=coloresauxiliares[indice2][0], highlightcolor=coloresauxiliares[indice2][0])
                colorframe1.config(bg=coloresauxiliares[indice2][0],highlightbackground=coloresauxiliares[indice2][0], highlightcolor=coloresauxiliares[indice2][0])  
                indice=claves.index(clicked[6].get())
                colorframeaux.config(bg=coloresauxiliares[indice][0],highlightbackground=coloresauxiliares[indice][0], highlightcolor=coloresauxiliares[indice][0])
                colorframe2.config(bg=coloresauxiliares[indice][0],highlightbackground=coloresauxiliares[indice][0], highlightcolor=coloresauxiliares[indice][0])  
        if seccion == "colores":
            global colorSelected
            colorSelected = clicked[5].get()

            parametrosGrafica[5] = clicked[5].get()
            opcionColor.config(bg=clicked[5].get(),activebackground=clicked[5].get())
            segmentosInicial.config(bg=clicked[5].get())
            indice=claves.index(clicked[5].get())
            segmentos2.config(bg=coloresauxiliares[indice][0])
            segmentosaux1.config(bg=coloresauxiliares[indice][1])
            if clicked[4].get() == "Trasmitancia":
                indice=claves.index(clicked[5].get())
                colorframe1.config(bg=coloresauxiliares[indice][0],highlightbackground=coloresauxiliares[indice][0], highlightcolor=coloresauxiliares[indice][0])  
                colorframe2.config(bg=coloresauxiliares[indice][0],highlightbackground=coloresauxiliares[indice][0], highlightcolor=coloresauxiliares[indice][0])
                indice2=claves.index(clicked[6].get())
                colorframeaux.config(bg=coloresauxiliares[indice2][0],highlightbackground=coloresauxiliares[indice2][0], highlightcolor=coloresauxiliares[indice2][0])
                colorframeaux2.config(bg=coloresauxiliares[indice2][0],highlightbackground=coloresauxiliares[indice2][0], highlightcolor=coloresauxiliares[indice2][0])
            if clicked[4].get() == "Reflectancia":
                indice2=claves.index(clicked[5].get())
                colorframeaux2.config(bg=coloresauxiliares[indice2][0],highlightbackground=coloresauxiliares[indice2][0], highlightcolor=coloresauxiliares[indice2][0])
                colorframe1.config(bg=coloresauxiliares[indice2][0],highlightbackground=coloresauxiliares[indice2][0], highlightcolor=coloresauxiliares[indice2][0])  
                indice=claves.index(clicked[6].get())
                colorframeaux.config(bg=coloresauxiliares[indice][0],highlightbackground=coloresauxiliares[indice][0], highlightcolor=coloresauxiliares[indice][0])
                colorframe2.config(bg=coloresauxiliares[indice][0],highlightbackground=coloresauxiliares[indice][0], highlightcolor=coloresauxiliares[indice][0])
                
                


            

        if seccion == "colores2":
            global colorSelected2
            colorSelected2 = clicked[6].get()
            parametrosGrafica[6] = clicked[6].get()
            opcionColor2.config(bg=clicked[6].get(),activebackground=clicked[6].get())
            indice=claves.index(clicked[6].get())
            segmentosFinal.config(bg=clicked[6].get())
            #print(valores[indice])
            segmentos4.config(bg=coloresauxiliares[indice][0])
            segmentosaux2.config(bg=coloresauxiliares[indice][1])
            if clicked[4].get() == "Trasmitancia":
                indice=claves.index(clicked[5].get())
                colorframe2.config(bg=coloresauxiliares[indice][0],highlightbackground=coloresauxiliares[indice][0], highlightcolor=coloresauxiliares[indice][0])
                indice2=claves.index(clicked[6].get())
                colorframeaux.config(bg=coloresauxiliares[indice2][0],highlightbackground=coloresauxiliares[indice2][0], highlightcolor=coloresauxiliares[indice2][0])
                colorframeaux2.config(bg=coloresauxiliares[indice2][0],highlightbackground=coloresauxiliares[indice2][0], highlightcolor=coloresauxiliares[indice2][0])
            if clicked[4].get() == "Reflectancia":
                indice2=claves.index(clicked[5].get())
                colorframeaux2.config(bg=coloresauxiliares[indice2][0],highlightbackground=coloresauxiliares[indice2][0], highlightcolor=coloresauxiliares[indice2][0])
                colorframe1.config(bg=coloresauxiliares[indice2][0],highlightbackground=coloresauxiliares[indice2][0], highlightcolor=coloresauxiliares[indice2][0])  
                indice=claves.index(clicked[6].get())
                colorframeaux.config(bg=coloresauxiliares[indice][0],highlightbackground=coloresauxiliares[indice][0], highlightcolor=coloresauxiliares[indice][0])
                colorframe2.config(bg=coloresauxiliares[indice][0],highlightbackground=coloresauxiliares[indice][0], highlightcolor=coloresauxiliares[indice][0])
                
            
            
            #print(claves.index(clicked[6].get()))
            
            
            
    claves = list(colores.keys())
    valores = list(colores.values())
    fuente = tk.OptionMenu(venteditgrafica, clicked[0], *tipo, command=validar)
    fuente['menu'].invoke(tipo[0])

    opcionTamanoTitulo = tk.OptionMenu(venteditgrafica, clicked[1],  *tamf,command=lambda event,seccion="titulos":validartamano(event,seccion))
    opcionTamanoTitulo['menu'].invoke(tamf[6])
    opcionTamanoSubtitulo = tk.OptionMenu(venteditgrafica, clicked[2], *tamf,command=lambda event,seccion="subtitulos":validartamano(event,seccion))
    opcionTamanoSubtitulo['menu'].invoke(tamf[5])
    opcionTamanoNumeros = tk.OptionMenu(venteditgrafica, clicked[3], *tamf,command=lambda event,seccion="numeros":validartamano(event,seccion))
    opcionTamanoNumeros['menu'].invoke(tamf[5])
    opcionTipoDiagrama = tk.OptionMenu(venteditgrafica, clicked[4], *tipd,command=lambda event,seccion="tipodiagrama":validartamano(event,seccion))
    opcionTipoDiagrama['menu'].invoke(tipd[1])

    opcionColor = tk.OptionMenu(venteditgrafica, clicked[5], *colores,command=lambda event,seccion="colores":validartamano(event,seccion))
    opcionColor.config(bg=claves[0],activebackground=opcionColor.cget('bg'),width=7)
    opcionColor['menu'].invoke(claves[0])
    opcionColor2 = tk.OptionMenu(venteditgrafica, clicked[6], *colores,command=lambda event,seccion="colores2":validartamano(event,seccion))
    opcionColor2.config(bg=claves[8],activebackground=opcionColor.cget('bg'),width=7)
    opcionColor2['menu'].invoke(claves[8])

    #Posicionamiento en pantalla de los elementos
    titleedit.place(x=0, y=0, width=900, height=50)
    labelfuente.place(x=14, y=60)

    framenamearchivo.place(x=230, y=58, width=660, height=440)
    labelarchivonombre.pack()
    framegrafica.pack()


    fuente.place(x=14, y = 90,width=150, height=30)
    labeltamanoTitulos.place(x=14, y = 130)
    opcionTamanoTitulo.place(x=14, y=160)
    labeltamanoSubtitulos.place(x=14, y=200)
    opcionTamanoSubtitulo.place(x=14, y=230)
    labeltamanoNumeros.place(x=14, y=270)
    opcionTamanoNumeros.place(x=14, y=300)
    labeltipoDiagrama.place(x=14, y=340)
    opcionTipoDiagrama.place(x=14, y=370)
    labelcambiarTitulos.place(x=275, y=500)
    labelcambiarTitulosy.place(x=420, y=500)
    cajaY.insert(0,"Frecuencia")
    cajaY.place(x=480, y=500)
    labelcambiarTitulosx.place(x=580,y=500)
    cajaX.insert(0, "Angle (y)")
    cajaX.place(x=640, y=500)
    #cajaX2.insert(0, "Angle (y)")
    #cajaX2.place(x=750, y=500)
                
    #labelcambiarTitulosx.place(x=420, y=520)
    labelbarraCalor.place(x=14, y=410)

    opcionColor.place(x=14,y=440)
    opcionColor2.place(x=100,y=440)
    buttonguardaredit.place(x=440, y = 560, width=80, height=30)
        
    piepagina = tk.Label(venteditgrafica, background="#F5841F")
    piepagina.place(x=0, y = 600, width=900, height=20)
    
    
    
    
    
    

    
    


def ventanaParametros(parametros,menuprincipal):
    ventanaes = tk.Toplevel(ventana)
    ventanaes.grab_set()
    menuprincipal.iconify()
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
    buttonSi = tk.Button(Labelbotones, text = "Si", font="Calibri 12 bold", background="#B7C800", cursor="hand2",relief="flat", bd=1,width=10,command= lambda: creararchivo(parametros,ventanaes,menuprincipal))
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
                    optiondropdown.delete(0, "end")
                    optiondropdown.insert(0,"2")
                    parametro3[i-1].place(x=230, y=206)
                    labelparametroC[i-1].place(x=266, y=176)
                elif x == "Lineal: Ax+B":
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
imagen2 = PhotoImage(file="./img/cuadro.PNG")
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
        createNewWindow(ventana)

progress_gg = Progressbar(ventana, orient=HORIZONTAL, style="TProgressbar",length=300)
progress_gg.pack(pady=30)
#txt.pack()
#buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
button = tkinter.Button(ventana, text = "Entrar", font="Calibri 12 bold", foreground="black", background="#B7C800",  command=start, cursor="hand2", width=8, height=1,relief="flat", bd=1)
button.pack()
piepagina = tk.Label(ventana, background="#F5841F")
piepagina.pack(side=tk.BOTTOM, fill= tk.X)
ventana.mainloop()