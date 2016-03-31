def may_men(x, y):
	if x < y :
		print("El mayor es",y)
	elif y < x :
		print("El mayor es",x)
	else:
		print("Son iguales")

if __name__ == "__main__":
	x = int(input("Ingrese primer numero: "))
	y = int(input("Ingrese segundo numero: "))

	may_men(x,y)