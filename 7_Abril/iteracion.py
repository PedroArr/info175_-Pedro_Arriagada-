# -*- coding: utf-8 -*-

l = [1,2,3]

##map##
#utilizando funcion
def elevar(l,n):
	tmp_l = list()
	for x in l:
		tmp_l.append(x**n)
	return tmp_l

#Esto se puede hacer todo en una linea
tl = map(lambda x: x**2,l)

print tl

l = [1,2,3,4,5,6,7,8,9]

##filter##
#usando funcion
def es_par(n):
	return n%2 == 0

fl = filter(es_par,l)
print fl

#usando lambda
fl = filter(lambda x: x%2==0,l)
print fl

##reduce##
print reduce(lambda x,y:x + y,l)