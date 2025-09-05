class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.estado = False 

    def encender(self):
        self.estado = True 
        print(self.nombre, "encendido")

    def apagar(self):
        self.estado = False 
        print(self.nombre, "apagado")


class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.__dispositivos = []

    def agregard(self, dispositivo):
        self.__dispositivos.append(dispositivo)
        print("dispositivo agregado")

    def mostrard(self):
        for dispositivo in self.__dispositivos:
            print(dispositivo.nombre)

class Casa:
    def __init__(self, direcciom):
        self.direccion = direcciom
        self.__espacios = []

    def agregare(self, nombre):
        self.__espacios.append(Espacio(nombre))
        print("espacio agregado")

    def buscare(self, nombre):
        for espacio in self.__espacios:
            if espacio.nombre == nombre:
                return espacio
        return None 
    

    def mostrare(self):
        for espacio in self.__espacios:
            print(espacio.nombre)


mi_casa = Casa("calle 123")
mi_casa.agregare("cocina")
mi_casa.agregare("habitacion")
mi_casa.agregare("baño")
television = Dispositivo("television")            
mi_casa.buscare("habitacion").agregard(television)
mi_casa.buscare("habitacion").mostrard()
