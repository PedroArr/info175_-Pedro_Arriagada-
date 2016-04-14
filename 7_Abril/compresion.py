#Compresion de listas
s = [x**2 for x in range(10)]
v = [2**i for i in range(13)]
m = [x for x in s if x%2==0]
print s
print v
print m

texto = "hello 12345 world"
lista = [int(x) for x in texto if x.isdigit()]
print lista

texto2 = "Si buscas resultados distintos no hagas siempre lo mismo"
lista2 = [[x.upper(),x.lower(),len(x)] for x in texto2.split(" ")]
print lista2

#tarda mucho para numeros grandes
#def firstn(n):
#	num,nums = 0,[]
#	while num<n:
#		nums.append(num)
#		num += 1
#	return nums

#tarda menos :P
def firstn(n):
	num=0
	while num<n:
		yield num
		num += 1

