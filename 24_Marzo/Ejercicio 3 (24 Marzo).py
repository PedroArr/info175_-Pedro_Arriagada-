def cenit_polar(palabra):
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

if __name__ == "__main__":
	texto = input("Ingrese palabra: ")
	print (cenit_polar(texto))
