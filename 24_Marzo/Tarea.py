from tkinter import *

def cesar(palabra):
    encriptado = ""
    if not palabra.isdigit():
    	palabra = palabra.lower()
    	for letra in palabra:
    		letrita = ord(letra)
    		if letrita>=97 and letrita<=122:
    			letrita = letrita + salto.get()
    			if letrita > 122:
    				letrita = letrita - 26
    		encriptado = encriptado + chr(letrita)
    return encriptado

def polarcenit(palabra):
    polar = "polarcenit"
    encriptado = ""
    for letra in palabra:
    	cambiada = False
    	for i in range(len(polar)):
    		if letra == polar[i]:
    			if i > 4:
    				encriptado = encriptado + polar[i-5]
    				cambiada = True
    			else:
    				encriptado = encriptado + polar[i-5]
    				cambiada = True
    	if not (cambiada):
    		if letra == " ":
    			encriptado = encriptado + " "
    		else:
    			encriptado = encriptado + letra
    return encriptado


def salto_cesar():
    salto.set(spin.get())

def encriptar():
    if seleccion.get()==1:
        resultado.set(cesar(texto.get()))
    elif seleccion.get()==2:
        resultado.set(polarcenit(texto.get()))

ventana = Tk()
ventana.geometry("400x400")

texto = StringVar()
estado = StringVar()
seleccion = IntVar()
salto = IntVar()
salto.set(1)
resultado = StringVar()

etiqueta1 = Label(ventana,text="Ingrese la frase a encriptar:")
etiqueta1.place(x=20,y=20)

ingreso = Entry(ventana,textvariable=texto)
ingreso.place(x=20,y=40)

etiqueta2 = Label(ventana,text="Seleccione metodo de encriptacion:")
etiqueta2.place(x=20,y=80)

radiocesar = Radiobutton(ventana,text="Cesar",variable=seleccion,value=1)
radiocesar.place(x=20,y=100)

radiopolar = Radiobutton(ventana,text="Polar Cenit",variable=seleccion,value=2)
radiopolar.place(x=100,y=100)

etiqueta3 = Label(ventana,text="Especifique salto para Cesar:")
etiqueta3.place(x=20,y=140)

spin = Spinbox(ventana,from_=1,to=25,state=NORMAL,width=2,command=salto_cesar)
spin.place(x=215,y=135)

boton = Button(ventana,text="ENCRIPTAR",command=encriptar)
boton.place(x=150,y=185)

etiqueta4 = Label(ventana,text="RESULTADO:")
etiqueta4.place(x=20,y=230)

etiqueta5 = Label(ventana,textvariable=resultado)
etiqueta5.place(x=20,y=260)
ventana.mainloop()
