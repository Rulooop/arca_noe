
# 🐾 Proyecto: **Arca de Noé**

¡Bienvenido al proyecto **Arca de Noé**! 🌟  
Este es un programa de simulación que te permite gestionar un arca con animales, alimentos y agua. El objetivo es mantener a los animales saludables mientras exploras conceptos básicos de programación orientada a objetos (POO).  
¡Es como tener tu propia versión del Arca de Noé! 🚢🐕🐈🌾

## 📌 **Características principales**
- **Gestión de animales**: Agrega, alimenta y cuida animales dentro del arca.  
- **Recursos limitados**: Administra alimentos y agua para mantener a todos en buen estado.  
- **Estado del arca**: Consulta el número de animales, alimentos disponibles y cantidad de agua.  
- **Estado de los animales**: Verifica los niveles de hambre y sed de cada animal en cualquier momento.  

---

## 🗂️ **Estructura de Clases**

### 🛳️ **Arca**
La clase principal que representa el arca.  
**Atributos clave**:
- Capacidad máxima para animales y alimentos.  
- Inventario de alimentos y cantidad de agua.  

**Métodos principales**:
![image](https://github.com/user-attachments/assets/89f83d64-b7f9-4918-bed6-c0295465e8fa)


#

### 🐾 **Animal**
Clase base para todos los animales del arca.  
**Atributos clave**:
- Nombre y tipo (ejemplo: Perro, Gato).  
- Niveles de hambre y sed.  

**Métodos principales**:
- `alimentar()`: Reduce el hambre del animal.  
- `dar_agua()`: Reduce la sed del animal.  
- `estado()`: Devuelve el estado del animal (nombre, tipo, hambre, sed).  

**Subclases**:
- **Perro**: Tipo predeterminado "Perro".  
- **Gato**: Tipo predeterminado "Gato".  

### 🍴 **Alimento**
Clase que representa alimentos para animales.  
**Métodos principales**:
- `usar(cantidad)`: Reduce la cantidad de alimento disponible.  
- `es_alimento_adecuado(tipo_animal)`: Verifica si el alimento es adecuado para el tipo de animal.  

**Subclases**:
- **Heno**: Alimento para animales herbívoros.  
- **Croquetas**: Alimento para perros y gatos.  

---

## 🚀 **Cómo usar el programa**

Al ejecutar el programa, se mostrará un menú interactivo con las siguientes opciones:  
1. **Agregar Animal**: Agrega un animal (perro o gato) al arca.  
2. **Agregar Alimento**: Añade heno o croquetas al arca.  
3. **Agregar Agua**: Incrementa la cantidad de agua disponible.  
4. **Alimentar Animal**: Alimenta a un animal usando los recursos del arca.  
5. **Dar Agua a Animal**: Da agua a un animal.  
6. **Ver Estado del Arca**: Consulta la cantidad de animales, alimentos y agua disponible.  
7. **Mostrar Estado de Animales**: Muestra el estado actual (hambre y sed) de todos los animales.  
8. **Salir**: Cierra el programa.  

---

## 📖 **Ejemplo de uso**

1. Agrega un perro llamado "Rex" y un gato llamado "Michi".  
2. Suministra croquetas y agua al arca.  
3. Alimenta a Rex y dale agua a Michi.  
4. Consulta el estado del arca y de los animales para verificar su bienestar.  

```python
# Ejemplo en código:
arca = Arca(capacidad_animales=10, capacidad_alimentos=20)
perro = Perro(nombre="Rex")
gato = Gato(nombre="Michi")
arca.agregar_animal(perro)
arca.agregar_animal(gato)
arca.agregar_alimento(Croquetas(cantidad=15))
arca.agregar_agua(30)
arca.alimentar_animal(perro)
arca.dar_agua(gato)
print(arca.estado_arca())
```

---

## ⚙️ **Requisitos**
- Python 3.8 o superior.  

---

## 📦 **Instalación**

1. Clona este repositorio:  
   ```bash
   git clone https://github.com/Rulooop/arca_noe
   cd arca_noe
   ```
2. Ejecuta el programa principal:  
   ```bash
   python arca.py
   ```

---

## 📌 **Notas**
- La capacidad del arca es limitada. Si está llena, no podrás agregar más recursos ni animales.  
- Los animales deben ser alimentados regularmente para evitar que su nivel de hambre o sed sea crítico.  

---

## 🛠️ **Contribuciones**
¡Contribuir es bienvenido! Si tienes ideas para mejorar este proyecto, crea un fork, realiza tus cambios y envía un pull request.  

---

## 📬 **Contacto**
Repositorio: [Arca de Noé](https://github.com/Rulooop/arca_noe)  
