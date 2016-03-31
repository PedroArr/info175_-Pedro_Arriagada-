def encrypt(palabra, N):
	encriptado = ""
	if not palabra.isdigit():
		palabra = palabra.lower()
		for letra in palabra:
			letrita = ord(letra)
			if letrita>=97 and letrita<=122:
				letrita = letrita + N
				if letrita > 122:
					letrita = letrita - 26
			encriptado = encriptado + chr(letrita)
	return encriptado

if __name__ == "__main__":
	texto = input("Ingrese frase:")
	n = int(input("Ingrese el numero para el encriptado: "))
	print (encrypt(texto,n))
