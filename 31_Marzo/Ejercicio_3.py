from datetime import datetime

class Persona(object):
    def __init__(self,rut,nombre,nacimiento,genero):
        self.rut = rut
        self.nombre = nombre
        self.nacimiento = nacimiento #"DD/MM/AAAA"
        self.genero = genero

    def obtener_edad(self):
        actual = datetime.now()
        año = actual.year
        mes = actual.month
        dia = actual.day
        cumplidos = False
        if mes > int(self.nacimiento[3:5]):
            cumplidos = True
        elif mes == int(self.nacimiento[3:5]):
            if dia >= int(self.nacimiento[0:2]):
                cumplidos = True
        edad = año - int(self.nacimiento[6:])
        if cumplidos == False:
            edad = edad - 1
        return edad
            
class Nota(object):
    def __init__(self,valor,ponderacion,ramo,carrera):
        self.valor = valor
        self.ponderacion = ponderacion
        self.ramo = ramo
        self.carrera = carrera

    def obtener_valor(self):
        return self.valor
    def obtener_ponderacion(self):
        return self.ponderacion
    def modificar(self,valor):
        if valor >= 1 and valor <= 7:
            self.valor = valor
        else:
            print("Nota fuera de rango.")

class Alumno(Persona):
    def __init__(self,rut,nombre,nacimiento,genero,correo,carrera,promocion,notas):
        super(Alumno,self).__init__(rut,nombre,nacimiento,genero)
        self.correo = correo
        self.carrera = carrera
        self.promocion = promocion
        self.notas = notas

    def agregar_nota(self,nota):
        if nota.valor >= 1 and nota.valor <= 7:
            self.notas.append(nota)
        else:
            print("Nota fuera de rango.")
    def PGA(self):
        pga = 0
        for i in range(0,len(self.notas)):
            pga = pga + self.notas[i].obtener_valor()*self.notas[i].obtener_ponderacion()
        pga = pga/len(self.notas)
        return pga
    def promedio_por_ramo(self):
        pass

#Ejemplos de utilizacion
yo = Alumno("18776373-8","Pedro","12/09/1995","Hombre","petros.arriagada@gmail.com","Informatica",2013,[])
nota1 = Nota(5,0.3,"Taller","Informatica")
nota2 = Nota(5.5,0.3,"Taller","Informatica")
nota3 = Nota(6,0.4,"Taller","Informatica")
yo.agregar_nota(nota1)
yo.agregar_nota(nota2)
yo.agregar_nota(nota3)

print("Nombre Alumno: "+yo.nombre)
print("RUT Alumno: "+yo.rut)
print("Fecha de Nacimiento: "+yo.nacimiento+" --> Edad: "+str(yo.obtener_edad()))
print("E-mail Alumno: "+yo.correo)
print("Carrera: "+yo.carrera+", Promocion "+str(yo.promocion))
