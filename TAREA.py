class Persona:
    def _init_(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def presentarse(self):
        return "Hola, soy " + self.nombre + " Mi correo es " + self.correo


class Empleado(Persona):
    def _init_(self, nombre, correo, salario):
        Persona._init_(self, nombre, correo)
        self.salario = salario

    def calcular_bono(self):
        return 0


class Desarrollador(Empleado):
    def _init_(self, nombre, correo, salario, lenguaje):
        Empleado._init_(self, nombre, correo, salario)
        self.lenguaje = lenguaje

    def calcular_bono(self, proyecto=None):
        bono = self.salario * 0.10
        if proyecto is not None and len(proyecto.tareas) > 5:
            bono = bono + (self.salario * 0.01)
        return bono



class Analista(Empleado):
    def _init_(self, nombre, correo, salario, nivel):
        Empleado._init_(self, nombre, correo, salario)
        self.nivel = nivel

    def calcular_bono(self):
        bono = self.salario * 0.08
        if self.nivel.lower() == "senior":
            bono = bono + (self.salario * 0.03)
        return bono


class Gerente(Empleado):
    def _init_(self, nombre, correo, salario):
        Empleado._init_(self, nombre, correo, salario)
        self.equipo = []

    def agregar_empleado(self, empleado):
        if empleado not in self.equipo and empleado != self:
            self.equipo.append(empleado)

    def remover_empleado(self, empleado):
        if empleado in self.equipo:
            self.equipo.remove(empleado)

    def listar_equipo(self):
        nombres = []
        indice = 0
        while indice < len(self.equipo):
            nombres.append(self.equipo[indice].nombre)
            indice = indice + 1
        return nombres

    def calcular_bono(self):
        return self.salario * 0.15


class Tarea:
    def _init_(self, id_tarea, descripcion, horas):
        if horas < 0:
            print("error: no se pueden poner horas negativas en tareas ")
            horas = 0
        self.id_tarea = id_tarea
        self.descripcion = descripcion
        self.horas = horas
        self.asignado_a = None


class Proyecto:
    def _init_(self, nombre, presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.tareas = []
        self.contador_de_tareas = 0

    def agregar_tarea(self, descripcion, horas):
        self.contador_de_tareas = self.contador_de_tareas + 1
        tarea = Tarea(self.contador_de_tareas, descripcion, horas)
        self.tareas.append(tarea)

    def asignar_empleado(self, id_tarea, empleado):
        indice = 0
        while indice < len(self.tareas):
            tarea = self.tareas[indice]
            if tarea.id_tarea == id_tarea:
                tarea.asignado_a = empleado
            indice = indice + 1

    def listar_tareas(self):
        lista = []
        indice = 0
        while indice < len(self.tareas):
            tarea = self.tareas[indice]
            if tarea.asignado_a is not None:
                asignado = tarea.asignado_a.nombre
            else:
                asignado = "Nadie"
            texto = "Tarea " + str(tarea.id_tarea) + ": " + tarea.descripcion + ", " + str(tarea.horas) + " horas, asignada a " + asignado
            lista.append(texto)
            indice = indice + 1
        return lista


class Empresa:
    def _init_(self):
        self.empleados = []
        self.proyectos = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def crear_proyecto(self, nombre, presupuesto):
        proyecto = Proyecto(nombre, presupuesto)
        self.proyectos.append(proyecto)
        return proyecto

    def asignar_empleado_a_proyecto(self, proyecto, id_tarea, empleado):
        proyecto.asignar_empleado(id_tarea, empleado)


empresa = Empresa()


desarrollador1 = Desarrollador("Ana", "ana@gmail.com", 3000, "Python")
analista1 = Analista("Luis", "luis@gmail.com", 2500, "senior")
gerente1 = Gerente("Marta", "marta@gmail.com", 5000)

empresa.agregar_empleado(desarrollador1)
empresa.agregar_empleado(analista1)
empresa.agregar_empleado(gerente1)

gerente1.agregar_empleado(desarrollador1)
gerente1.agregar_empleado(analista1)

proyecto1 = empresa.crear_proyecto("Sistema Web", 20000)

proyecto1.agregar_tarea("diseñar base de datos", 10)
proyecto1.agregar_tarea("Programar backend", 20)
proyecto1.agregar_tarea("Programar frontend", -5) 


empresa.asignar_empleado_a_proyecto(proyecto1, 1, analista1)
empresa.asignar_empleado_a_proyecto(proyecto1, 2, desarrollador1)


print("Equipo de la gerente:", gerente1.listar_equipo())

print("Tareas del proyecto:")
indice = 0
tareas = proyecto1.listar_tareas()
while indice < len(tareas):
    print(" - " + tareas[indice])
    indice = indice + 1

print("Bono del desarrollador:", desarrollador1.calcular_bono(proyecto1))
print("Bono del analista:", analista1.calcular_bono())
print("Bono de la gerente:", gerente1.calcular_bono())


empresa = Empresa()

def menu():
    while True:
        print("menu empresa ")
        print("1. Agregar desarrollador")
        print("2. Agregar analista")
        print("3. Agregar gerente")
        print("4. Crear proyecto")
        print("5. Agregar tarea a proyecto")
        print("6. Asignar empleado a tarea")
        print("7. Listar equipo de un gerente")
        print("8. Listar tareas de un proyecto")
        print("9. Calcular Bonos")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            salario = float(input("Salario: "))
            lenguaje = input("Lenguaje: ")
            desarrollador = Desarrollador(nombre, correo, salario, lenguaje)
            empresa.agregar_empleado(desarrollador)
            print("Desarrollador agregado")

        elif opcion == "2":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            salario = float(input("Salario: "))
            nivel = input("Nivel junior/senior: ")
            analista = Analista(nombre, correo, salario, nivel)
            empresa.agregar_empleado(analista)
            print("Analista agregado")

        elif opcion == "3":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            salario = float(input("Salario: "))
            gerente = Gerente(nombre, correo, salario)
            empresa.agregar_empleado(gerente)
            print("Gerente agregado")

        elif opcion == "4":
            nombre = input("Nombre del proyecto: ")
            presupuesto = float(input("Presupuesto: "))
            proyecto = empresa.crear_proyecto(nombre, presupuesto)
            print("Proyecto creado:", proyecto.nombre)

        elif opcion == "5":
            if not empresa.proyectos:
                print("No hay proyectos creados")
            else:
                for indice_proyecto, proyecto in enumerate(empresa.proyectos):
                    print(indice_proyecto, "-", proyecto.nombre)
                numero_proyecto = int(input("Elige el proyecto: "))
                descripcion = input("Descripción de la tarea: ")
                horas = int(input("Horas estimadas: "))
                empresa.proyectos[numero_proyecto].agregar_tarea(descripcion, horas)
                print("Tarea agregada")

        elif opcion == "6":
            if not empresa.proyectos or not empresa.empleados:
                print("Hay que tener proyectos y empleados creados")
            else:
                for indice_proyecto, proyecto in enumerate(empresa.proyectos):
                    print(indice_proyecto, "-", proyecto.nombre)
                numero_proyecto = int(input("Elige el proyecto: "))
                proyecto_seleccionado = empresa.proyectos[numero_proyecto]

                tareas = proyecto_seleccionado.listar_tareas()
                for tarea in tareas:
                    print(tarea)
                id_tarea = int(input("ID de la tarea a asignar: "))

                for indice_empleado, empleado in enumerate(empresa.empleados):
                    print(indice_empleado, "-", empleado.nombre, type(empleado)._name_)
                numero_empleado = int(input("Elige el empleado: "))
                empleado_seleccionado = empresa.empleados[numero_empleado]

                empresa.asignar_empleado_a_proyecto(proyecto_seleccionado, id_tarea, empleado_seleccionado)
                print("Al empleado se le asigno la tarea")

        elif opcion == "7":
            for indice_empleado, empleado in enumerate(empresa.empleados):
                if isinstance(empleado, Gerente):
                    print(indice_empleado, "-", empleado.nombre)
            numero_gerente = int(input("Elige un gerente: "))
            gerente_seleccionado = empresa.empleados[numero_gerente]
            print("Equipo de", gerente_seleccionado.nombre, ":", gerente_seleccionado.listar_equipo())

        elif opcion == "8":
            for indice_proyecto, proyecto in enumerate(empresa.proyectos):
                print(indice_proyecto, "-", proyecto.nombre)
            numero_proyecto = int(input("Elige el proyecto: "))
            lista_tareas = empresa.proyectos[numero_proyecto].listar_tareas()
            for tarea in lista_tareas:
                print("-", tarea)

        elif opcion == "9":
            for empleado in empresa.empleados:
                if isinstance(empleado, Desarrollador):
                    for proyecto in empresa.proyectos:
                        print("Bono de", empleado.nombre, ":", empleado.calcular_bono(proyecto))
                elif isinstance(empleado, Analista):
                    print("Bono de", empleado.nombre, ":", empleado.calcular_bono())
                elif isinstance(empleado, Gerente):
                    print("Bono de", empleado.nombre, ":", empleado.calcular_bono())

        elif opcion == "0":
            print("Saliendo")
            break
        else:
            print("esta opcion no es valida")

menu()