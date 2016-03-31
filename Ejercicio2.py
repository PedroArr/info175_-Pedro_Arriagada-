def palabras(lista):
	lista.sort()
	texto = "Las palabras ordenadas son:\n"
	for i in range (0,len(lista)):
		if i != len(lista)-1:
			texto = texto + lista[i] + ", "
		else:
			texto = texto + lista[i]
	print(texto)

if __name__ == "__main__":
	lista = []
	palabra = input("Ingrese palabra: (ingreso vacio terminara la lista)")
	while palabra != "":
		lista.append(palabra)
		palabra = input("Ingrese palabra: ")

	palabras(lista)
	

