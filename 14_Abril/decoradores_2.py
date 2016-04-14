#-*- config: utf-8 -*-

def avisar(f):
	#Funcion decoradora :)
	def inner(*args, **kwargs):
		f(*args, **kwargs)
		print "Se ha ejecutado %s" %f.__name__
	return inner

LOGIN = False
def autenticar(f):
	def inner(*args,**kwargs):
		if LOGIN:
			f(*args,**kwargs)
		else:
			raise Exception #lanzar excepcion
	return inner

@autenticar #cada vez que se ejecuta la funcion se decora con los @
@avisar #x=avisar(cerrar_puerta())
def abrir_puerta():
	print "Abrir puerta."

@autenticar
@avisar
def cerrar_puerta():
	print "Cerrar puerta."