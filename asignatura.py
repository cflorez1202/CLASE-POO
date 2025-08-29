class estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre 
        self.edad = edad 
        self.nota = nota

class Profesor:
     def __init__(self, nombre, edad, experiencia):
        self.nombre = nombre 
        self.edad = edad 
        self.experiencia = experiencia

class grupoAsignatura:
     def __init__(self, nombre, horario, codigo, profesor):
        self.nombre = nombre 
        self.horario = horario 
        self.codigo = codigo
        self.profesor = profesor 
        self.estudiantes = []

     def agregar_estudiante(self, estudiante):
         self.estudiantes.append(estudiante)
         print("estudiante agregado exitosamente")

     def promedio(self):
         acumulador = 0
         for estudiante in self.estudiantes:
             acumulador = acumulador + estudiante.nota
         promedio = acumulador/len(self.estudiantes)
         return promedio 
     
     def mostrar_estudiantes(self):
         for estudiante in self.estudiantes:
             print(estudiante.nombre)
     
profesor = Profesor("juan esteban", 35, 5)
poo = grupoAsignatura("programacion orientada a objetos", "M-V 10-12", 62, profesor)
estudiante1 = estudiante("esteban diaz", 17, 5)
estudiante2 = estudiante("jorge", 20, 2.5)
estudiante3 = estudiante("luis", 21, 3)

poo.agregar_estudiante(estudiante1)
poo.agregar_estudiante(estudiante2)
poo.agregar_estudiante(estudiante3)

print(poo.promedio())
poo.mostrar_estudiantes()

 