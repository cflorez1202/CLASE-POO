import random
class cuenta:
    def __init__(self, nombre_titular):
        self.nombre_titular = nombre_titular 
        self.numero_cuenta = random.randint(10000, 99999)
        self.saldo = 0

    def depositar(self,cantidad):
        self.saldo = self.saldo + cantidad 
        return self.saldo 

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo = self.saldo - cantidad
            return self.saldo
        else:
            print("no hay dinero para ese retiro")
            return -1
        
    def consultar(self):
        return self.saldo 
    

#programa principal 

lista_cuentas = []

print("bienvenido al banco")
while True:
    print("ingrese la opcion deseada")
    print("1. ingresar la cuenta")
    print("2. depositar")
    print("3. retirar")
    print("4. consultar saldo")
    print("0. salir")

    opcion = int(input())

    if opcion == 1:
        nombre = input("ingrese el nombre deñ titular")
        nueva_cuenta = cuenta(nombre)
        lista_cuentas.append(nueva_cuenta)
        print("cuenta creada exitosamente, su numero de cuenta es", nueva_cuenta.numero_cuenta)

    if opcion == 2:
        numero_cuenta = int(input("ingrese el numero de cuenta"))
        existe = False
        for cuenta in lista_cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                camtidad = float(input("ingrese la cantidad a epositar"))
                nuevo_saldo = cuenta.depositar (cantidad)
                print("el nuevo saldo es:", nuevo_saldo)

        if existe == False:
            print("cuenta no existe")


    if opcion == 3:
         numero_cuenta = int(input("ingrese el numero de cuenta"))
         existe = False
         for cuenta in lista_cuentas:
             if cuenta.numero_cuenta == numero_cuenta:
                 existe == True
                 cantidad = float(input("ingrese la cantidad a retirar"))
                 numero_saldo = cuenta.retirar(cantidad)

                 if numero_saldo >= 0:
                     print("retiro exioso. Su nuevo saldo es", nuevo_saldo)

         if existe == False:
             print("cuenta no existe")


    elif opcion == 4:
        numero_cuenta = int(input("ingrese el numero de cuenta"))
        existe = False
        for cuenta in lista_cuentas:
             if cuenta.numero_cuenta == numero_cuenta:
                 existe == True
                 print("su saldo es", cuenta.consultar())

        if existe == False:
            print("cuenta no existe")

    elif opcion == 0:
        print("hasta luego")
        break
    else:
        print("opcion incorrecta")






        
        






