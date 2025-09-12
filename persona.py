class Persona:
    def __init__(self, nombre):
        self.nombre = nombre 

    def respirar(self):
        print(f"{self.nombre} esta respirando")

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera 

    def estudiar(self):
        print(f"{self.nombre} esta etudiando {self.carrera} ")

persona1 = Persona("juan")
persona1.respirar()

persona2 = Estudiante("camila", "ingenieria")
persona2.estudiar 
