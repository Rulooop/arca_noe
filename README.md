# arca_noe

Este es un proyecto de simulación de un arca donde se gestionan animales, alimentos y agua para mantener a los animales en buen estado. La idea es poder agregar animales, alimentarlos, darles agua y revisar el estado de todo el sistema. ¡Es como tener tu propia versión del Arca de Noé!

Descripción de clases
Arca: Es la clase principal que representa el arca en sí. Tiene una capacidad máxima (máximo de animales y alimentos que se pueden almacenar).

Métodos importantes:
agregar_animal(animal): Agrega un animal al arca si hay espacio.
agregar_alimento(alimento): Agrega alimento al arca.
agregar_agua(cantidad): Agrega agua al arca.
alimentar_animal(animal): Alimenta a un animal, usando uno de los alimentos disponibles.
dar_agua(animal): Da agua a un animal, si hay suficiente.
estado_arca(): Muestra el estado actual del arca (número de animales, alimentos y agua).
Animal: Esta clase es la base de todos los animales del arca (perros, gatos, etc.). Cada animal tiene un nombre, tipo (perro, gato, etc.), y niveles de hambre y sed.

Métodos importantes:
alimentar(): Reduce el nivel de hambre del animal.
dar_agua(): Reduce el nivel de sed del animal.
estado(): Devuelve el estado del animal (nombre, tipo, hambre, sed).
Alimento: Representa los alimentos que pueden ser usados para alimentar a los animales.

Métodos importantes:
usar(cantidad): Usar una cierta cantidad de alimento.
es_alimento_adecuado(tipo_animal): Verifica si un alimento es adecuado para un tipo de animal.
Perro y Gato: Son clases hijas de Animal. Tienen el tipo asignado por defecto a "Perro" y "Gato", respectivamente.

Heno y Croquetas: Son clases hijas de Alimento, representando tipos específicos de alimentos para animales.

Cómo usar el programa
Al ejecutar el programa, se muestra un menú con varias opciones para interactuar con el arca. Aquí están las opciones disponibles:

Agregar Animal: Te permite agregar un animal (perro o gato) al arca.
Agregar Alimento: Puedes agregar heno o croquetas como alimento.
Agregar Agua: Añadir agua al arca.
Alimentar Animal: Alimenta a un animal si hay suficiente comida disponible.
Dar Agua a Animal: Da agua a un animal si hay suficiente agua.
Ver Estado del Arca: Muestra el número de animales, alimentos y la cantidad de agua disponible.
Mostrar Estado de Animales: Muestra el estado (hambre y sed) de todos los animales que están en el arca.
Salir: Salir del programa.
Ejemplo de uso
Se agrega un perro y un gato al arca.
Se agrega alimento (como croquetas) y agua al arca.
Se puede alimentar a los animales, y también darles agua.
Se puede ver el estado de los animales y del arca en cualquier momento.
Notas
La capacidad del arca está limitada por la cantidad de animales y alimentos que puede almacenar. Si el arca está llena, no podrás agregar más animales ni más comida.
Los animales tienen niveles de hambre y sed que disminuyen cuando se les da comida o agua.
Este es un proyecto simple pero divertido para aprender sobre clases, objetos y cómo organizar un sistema básico de gestión. ¡Espero que lo disfrutes! 😄
