#-*- config: utf-8 -*-

def abrir_puerta():
	print "Abrir puerta."

def cerrar_puerta():
	print "Cerrar puerta."


#ejemplo de kwargs abrir_puerta(numero=5) se ingresan en cualquier orden
def avisar(f):
	#Funcion decoradora :)
	def inner(*args, **kwargs):
		f(*args, **kwargs)
		print "Se ha ejecutado %s" %f.__name__
	return inner