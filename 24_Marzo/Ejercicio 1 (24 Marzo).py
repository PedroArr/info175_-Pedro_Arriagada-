def funcion(size):
	lista = []
	for i in range(1,size+1):
		if i%3==0 and i%7==0:
			lista.append(i)
	return lista

if __name__ == "__main__":
	n = int(input("Ingrese numero: "))
	print (funcion(n))