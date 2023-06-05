### Dictionaries ###

# Definición
my_dict = dict()
my_other_dict = {}

print(type(my_other_dict))

# Almacena datos de tipo clave:valor
my_other_dict = {"Nombre" : "Darío", "Apellido" : "Fajardo", "Edad" : 35}
print(my_other_dict)

# Se pueden guardar datos mas complejos dentro de un dict
my_dict = {
    "Nombre" : "Darío", 
    "Apellido" : "Fajardo", 
    "Edad" : 35,
    "Lenguajes" : {"Python", "C++", "Assembly"},
    1:1.8
    }
print(my_dict)

# Acceder a un valor por su clave
print(my_other_dict["Nombre"]) # Darío

my_dict["Nombre"] = "Jose Juan"
print(my_dict["Nombre"])

# Se añade un elemento con una nueva clave y valor
my_dict["Hola"] = "Adiós"
print(my_dict)

# Borrar elementos
del my_dict["Hola"]
print(my_dict)

# Comprobar si un elemento existe (Igual que un set)
print("Nombre" in my_dict) # Solo se puede buscar por las claves
print("Darío" in my_dict) # False

# Imprimir elementos de un diccionario
print(my_dict.items()) # Elementos (Pares clave:valor)
print(my_dict.keys()) # Claves
print(my_dict.values()) # Valores

# Crear diccionario sin valores
my_new_dict = dict.fromkeys(("Nombre", 1)) # dict es una palabra reservada, la usamos para acceder a métodos de la clase dict
print(my_new_dict)

my_new_dict = dict.fromkeys(my_other_dict) # dict de valores vacíos con las keys de otro
print(my_new_dict)

my_list = list(my_other_dict) # Al convertir permanecen siempre las claves
print(my_list)
my_new_dict = dict.fromkeys(my_list) # Se puede hacer con listas
print(my_new_dict)

# Meter un valor a un fromkeys
my_new_dict = dict.fromkeys(my_dict, "pene") # Se le asigna un valor a todas las claves
print(my_new_dict)

# Guardar valores de un dict en una lista
my_list = list(my_new_dict.values()) # Si no convertimos en lista, el tipo sera 'dict_values'
print(my_list)

# Limpiar
my_dict.clear()
print(my_dict)