def mayusculas(texto):
	return texto.upper()


if __name__ == "__main__":
	texto = ""
	linea = input("Ingrese una linea de texto: (linea vacia terminara el ingreso)")
	while linea != "":
		texto = texto + linea + "\n"
		linea = input("Ingrese una linea de texto:")

	mayusculas(texto)
