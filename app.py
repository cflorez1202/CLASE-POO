class perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("el perro que esta ladrando es:", self.nombre)


class persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre 
        self.edad = edad
        self.sexo = sexo 
        




# Vamos a instanciar un objeto desde la clase perro 
print("mi primer perrito:")
mi_perrito = perro("mia", "golden")
print(mi_perrito.nombre)
print(mi_perrito.raza)

print("mi segundo perrito:")
el_perrito = perro("shaira", "cocker")
print(el_perrito.nombre)
print(el_perrito.raza)

print("ingrese lo datos del tercer perito:")
nombre = input("ingrese el nombre:")
raza = input("ingrese la raza:")

mi_tercer_perrito = perro(nombre, raza)
print("los datos del tercer perrito son:")
print(mi_tercer_perrito.nombre)
print(mi_tercer_perrito.raza)

print("ahora los perros van a ladrar")
mi_perrito.ladrar()
el_perrito.ladrar()
mi_tercer_perrito.ladrar()
