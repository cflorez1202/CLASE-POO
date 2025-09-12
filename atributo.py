class Animal:
    def __init__(self, nombre):
        self.nombre = nombre 

    def hacer_sonido(self):
        pass
    def orinar(self):
        print(f"{self.nombre}esta orinando")

class Perro(Animal):
    def __init__(self, nombre, color_pelota):
        super().__init__(nombre)
        self.color_pelota = color_pelota
    
    def hacer_sonido(self):
        print(f"´{self.nombre} hace guau guau")

    def salir_a_pasear(self):
        print(f"{self.nombre} esta paseando")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"´{self.nombre} hace miaumiau")

animal1 = Perro("mia", "rojo")
animal1.hacer_sonido()
animal1.salir_a_pasear()
animal1.orinar()

animal2 = Gato("simba")
animal2.hacer_sonido()
animal2.orinar()

print(isinstance(animal2, Perro))
print(isinstance(animal2, Animal))
print(issubclass(Perro, Gato))
print(issubclass(Gato, Animal))