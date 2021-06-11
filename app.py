import tkinter
# creacion de la ventana
ventana =  tkinter.Tk();

# redimensionar nuestra ventana
ventana.geometry("500x500")

# agregar una etiqueta, parametros = donde la voy a poner y que texto
etiqueta =  tkinter.Label(ventana, text = "Bienvenidos", bg = "red")

# mostrar elemento y centrado automatico, defino tambien si ocupa todo el ancho de la pantalla con fill
etiqueta.pack(fill=tkinter.X)
# o tambien expandirlo en le eje y
# etiqueta.pack(fill=tkinter.Y, expand=True)
# o que ocupe todo el ancho y el largo disponibke
#etiqueta.pack(fill=tkinter.BOTH, expand=True)
# si deseo posicionar abajo el elemento :
#etiqueta.pack(side= tkinter.BOTTOM)

#etiqueta.pack(side= tkinter.RIGHT)
def saludo():
    print("hola")

def obtenerTexto():
    # con get obtengo el texto dento del campo
    texto = cajaTexto.get()
    mensaje["text"] = texto
    print(texto)

#crear un input o caja de texto

cajaTexto = tkinter.Entry(ventana, font = "Helvetica 10")
cajaTexto.pack()

# crear un boton, puedo definir su ancho y largo con padx y pady.
# con command asocio la funcion que quiero que se ejecute al presionar el botton
boton1 = tkinter.Button(ventana, text = "presiona" , bg = "gray" , padx = 50, pady = 1, command = obtenerTexto)
# si la funcion que voy a utilizar recibe parametros
# boton1 = tkinter.Button(ventana, text = "presiona" , bg = "gray" , padx = 100, pady = 200, command = lambda: saludo("andres"))
boton1.pack()

#creo una etiqueta para poner en pantalla un mensaje capturado
mensaje = tkinter.Label(ventana)
mensaje.pack()

# mainloop lleva el registro de todo lo que sucede en la ventana
ventana.mainloop()
