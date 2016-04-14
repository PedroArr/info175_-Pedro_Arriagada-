# -*- coding: utf-8 -*-

def funcion_original(valor):
	return valor

#las funciones pueden ser asignadas

una_variable = funcion_original #para asignar la función no debe ser evaluada
print(una_variable)
print(una_variable(4))

#las funciones pueden ser traspasadas como argumentos de otras funciones
def suma(x,y):
	return x + y

def cuadrado(x):
	return x ** 2

def evaluar(f, *args):
	return f(*args)

print(evaluar(suma,3,5))
print(evaluar(cuadrado,5))

def saludar(lang):
	def saludar_es():
		return "Hola"
	def saludar_en():
		return "Hi"
	def saludar_de():
		return "Hallo"

	lang_func = {
		"es": saludar_es,
		"en":saludar_en,
		"de":saludar_de}

	return lang_func[lang]

#Esto retorna una funcion
print(saludar("es"))
#Puedo pasar la funcion retornada a una variable e invocarla
f = saludar("es")
print(f())
#Para evitar la asignacion
print(saludar("de")())

#las funciones anonmas poseen nombre
print(evaluar(lambda x,y: x+y, 3 , 4))
			 #lambda variables: que hacer, evaluar)

print(evaluar(lambda x: x**2,9))
print(evaluar(lambda x,y: x*y,3,4))