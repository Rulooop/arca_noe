# Funcionalidad.py

from Clases import Arca, Animal, Alimento, Perro, Gato, Heno, Croquetas

def mostrar_estado_animales(arca):
    if arca.animales:
        for animal in arca.animales:
            print(animal.estado())
    else:
        print("No hay animales en el arca.")

def menu():
    arca = Arca(capacidad_maxima=10)

    while True:
        print("\n--- Menú del Arca de Noé ---")
        print("1. Agregar Animal")
        print("2. Agregar Alimento")
        print("3. Agregar Agua")
        print("4. Alimentar Animal")
        print("5. Dar Agua a Animal")
        print("6. Ver Estado del Arca")
        print("7. Mostrar Estado de Animales")
        print("8. Salir")

        opcion = input("Seleccione una opción (1-8): ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del animal: ")
            tipo = input("Ingrese el tipo de animal (perro/gato): ").lower()
            if tipo == 'perro':
                animal = Perro(nombre)
            elif tipo == 'gato':
                animal = Gato(nombre)
            else:
                print("Tipo de animal no válido.")
                continue
            arca.agregar_animal(animal)

        elif opcion == '2':
            tipo_alimento = input("Ingrese el tipo de alimento (heno/croquetas): ").lower()
            cantidad = int(input("Ingrese la cantidad de alimento: "))
            if tipo_alimento == 'heno':
                alimento = Heno(cantidad)
            elif tipo_alimento == 'croquetas':
                alimento = Croquetas(cantidad)
            else:
                print("Tipo de alimento no válido.")
                continue
            arca.agregar_alimento(alimento)

        elif opcion == '3':
            cantidad = int(input("Ingrese la cantidad de agua a agregar: "))
            arca.agregar_agua(cantidad)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del animal a alimentar: ")
            for animal in arca.animales:
                if animal.nombre == nombre:
                    arca.alimentar_animal(animal)
                    break
            else:
                print(f"No se encontró un animal llamado {nombre}.")

        elif opcion == '5':
            nombre = input("Ingrese el nombre del animal a dar agua: ")
            for animal in arca.animales:
                if animal.nombre == nombre:
                    arca.dar_agua(animal)
                    break
            else:
                print(f"No se encontró un animal llamado {nombre}.")

        elif opcion == '6':
            estado = Arca.estado_arca(arca)
            print(f"Número de animales: {estado['Número de animales']}")
            print(f"Número de alimentos: {estado['Número de alimentos']}")
            print(f"Cantidad de agua: {estado['Cantidad de agua']}")

        elif opcion == '7':
            mostrar_estado_animales(arca)

        elif opcion == '8':
            print("Saliendo del programa. ¡Adiós!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 8.")


# Ejecutar el menú
menu()
