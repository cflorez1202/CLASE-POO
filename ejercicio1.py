class Estudiante:
    def __init__(self, nombre, edad, nota1, nota2, nota3):
        self.nota2 = nota2
        self.nota3 = nota3
        self.nombre = nombre 
        self.edad = edad 
        self.nota1 = nota1

    def mostrar_datos(self):
        print("nombre:", self.nombre)
        print("edad:", self.edad)
        print("nota1", self.nota1)
        print("nota3", self.nota2)
        print("nota3", self.nota3)

    def calcular_promedio(self):
        promedio = (self.nota1 + self.nota2 + self.nota3)/3
        return promedio 
    
print("bienvenido a la gestion del etudiantes")
print("ingrese el nombre del estudiante")
nombre = input ()
print("ingrese la edad del estudiante")
edad = int(input())
print("ingrese la nota 1")
nota1 = float(input())
print("ingrese la nota 2")
nota2 = float(input())
print("ingrese la nota 3")
nota3 = float(input())
estudiante = Estudiante(nombre, edad, nota1, nota2, nota3)

promedio_estudiantes = estudiante.calcular_promedio()
print("el promedio de:", estudiante.nombre, "es", promedio_estudiantes )




