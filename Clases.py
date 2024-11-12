
class Arca:
    def __init__(self, capacidad_maxima):
        self.animales = []
        self.alimentos = []
        self.agua = 0
        self.capacidad_maxima = capacidad_maxima

    def agregar_animal(self, animal):
        if len(self.animales) + len(self.alimentos) < self.capacidad_maxima:
            self.animales.append(animal)
            print(f"{animal.nombre} ha sido agregado al arca.")
        else:
            print("No se puede agregar más animales. Capacidad máxima alcanzada.")

    def agregar_alimento(self, alimento):
        if len(self.animales) + len(self.alimentos) < self.capacidad_maxima:
            self.alimentos.append(alimento)
            print(f"{alimento.tipo} ha sido agregado al arca.")
        else:
            print("No se puede agregar más alimentos. Capacidad máxima alcanzada.")

    def agregar_agua(self, cantidad):
        self.agua += cantidad
        print(f"{cantidad} unidades de agua han sido agregadas al arca.")

    def alimentar_animal(self, animal):
        if animal in self.animales:
            for alimento in self.alimentos:
                if alimento.cantidad > 0:
                    animal.alimentar()
                    alimento.usar(1)  # Usar una unidad de alimento
                    print(f"{animal.nombre} ha sido alimentado.")
                    return
            print(f"No hay alimento disponible para {animal.nombre}.")
        else:
            print(f"{animal.nombre} no está en el arca.")

    def dar_agua(self, animal):
        if animal in self.animales and self.agua > 0:
            animal.dar_agua()
            self.agua -= 1  # Usar una unidad de agua
            print(f"{animal.nombre} ha recibido agua.")
        else:
            print(f"No hay agua disponible para {animal.nombre}.")

    @staticmethod
    def estado_arca(arca):
        return {
            "Número de animales": len(arca.animales),
            "Número de alimentos": len(arca.alimentos),
            "Cantidad de agua": arca.agua
        }


class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hambre = 5  # Nivel de hambre inicial
        self.sed = 5     # Nivel de sed inicial

    def alimentar(self):
        self.hambre = max(0, self.hambre - 1)  # Reducir hambre

    def dar_agua(self):
        self.sed = max(0, self.sed - 1)  # Reducir sed

    def estado(self):
        return {
            "Nombre": self.nombre,
            "Tipo": self.tipo,
            "Hambre": self.hambre,
            "Sed": self.sed
        }


class Alimento:
    def __init__(self, tipo, cantidad):
        self.tipo = tipo
        self.cantidad = cantidad

    def usar(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
        else:
            print("No hay suficiente alimento disponible.")

    @staticmethod
    def es_alimento_adecuado(tipo_animal):
        return tipo_animal in ["perro", "gato", "conejo", "pájaro"]


class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Perro")


class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Gato")


class Heno(Alimento):
    def __init__(self, cantidad):
        super().__init__("Heno", cantidad)


class Croquetas(Alimento):
    def __init__(self, cantidad):
        super().__init__("Croquetas", cantidad)
