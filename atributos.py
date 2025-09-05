class Persona:
    def __init__(self, nombre, cedula, TI):
        self.nombre = nombre 
        self._cedula = cedula
        self._TI = TI

    def obtener_documento(self):
        if self._cedula is not None:
          return self._cedula
        else:
            return self._TI 
        

persona1 = Persona("juan", 1111, None)
persona2 = Persona("maria", 2222, None)
niño1 = Persona("isaac", None, 333)

print("el nombre de la primera persona es", persona1.nombre)
print("el documento de la primera persona es", persona1.obtener_documento())

print("el nombre de la segunda persona es", persona2.nombre)
print("el documento del primer niño es", niño1.obtener_documento())


