class vehiculo(object):
    def __init__(self,kilometraje,bencina,rendimiento,encendido):
        self.kilometraje = kilometraje
        self.bencina = bencina
        self.rendimiento = rendimiento
        self.encendido = encendido
    def encender(self):
        print("Encendido.")
    def apagar(self):
        print("Apagado.")
    def mover(self,dist):
        if self.rendimiento  < dist/self.bencina and self.encendido:
            self.kilometraje = self.kilometraje + dist
            self.bencina = self.bencina - dist/self.rendimiento
        else:
            if self.encendido == False:
                print("Encienda el auto...")
            else:
                print("Falta bencina.")
    def obtener_kilometraje(self):
        return self.kilometraje
    def obtener_bencina(self):
        return self.bencina
    def cargar_bencina(self,x):
        if self.encendido == False:
            self.bencina = self.bencina + x
        else:
            print("Apague el motor.")

class acoplado(object):
    def __init__(self,ruedas,peso,carga):
        self.ruedas = ruedas
        self.peso = peso
        self.carga = carga

class camion(vehiculo):
    def __init__(self,kilometraje,bencina,rendimiento,encendido,peso,ruedas,acoplados):
        self.kilometraje = kilometraje
        self.bencina = bencina
        self.rendimiento = rendimiento
        self.encendido = encendido
        self.peso = peso
        self.ruedas = ruedas
        self.acoplados = acoplados
    def agregar_acoplado(self,acoplado):
        self.acoplados.append(acoplado)
    def quitar_acoplado(self):
        del self.acoplados[len(self.acoplados)-1]
    def obtener_acoplados(self):
        return self.acoplados
    def obtener_ruedas(self):
        return self.ruedas
    def obtener_peso(self):
        return self.peso
