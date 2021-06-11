import tkinter
# creacion de la ventana
ventana =  tkinter.Tk();

# redimensionar nuestra ventana



# posicionamiento de elementos con grid
boton1 = tkinter.Button(ventana, text = "boton 1", width= 10, height = 5)
boton2 = tkinter.Button(ventana, text = "boton 2", width= 10, height = 5)
boton3 = tkinter.Button(ventana, text = "boton 3", width= 10, height = 5)
boton4 = tkinter.Button(ventana, text = "boton 4", width= 10, height = 5)
boton5 = tkinter.Button(ventana, text = "boton 5", width= 10, height = 5)
boton6 = tkinter.Button(ventana, text = "boton 6", width= 10, height = 5)

boton1.grid(row=0, column=0)
boton2.grid(row=0, column=1)
boton3.grid(row=0, column=2)
boton4.grid(row=3, column=0)
boton5.grid(row=4, column=0)
boton6.grid(row=5, column=0)

ventana.mainloop()