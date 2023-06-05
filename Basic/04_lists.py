### Lists ###

# Maneras de definir una lista:
my_list = list()
my_other_list = []

print(len(my_list)) # Salida 0, lista vacía

my_list = [33, 33, 33, 33, 33, 33]
print(len(my_list)) # Salida 6
print(my_list) # Imprime la lista

my_other_list = [18, 1.8, "Darío", "Fajardo"] # Las listas pueden guardar distintos elementos
print(type(my_other_list)) # Salida "list"

# Acceder a un elemento de la lista
print(my_other_list[1]) # 1.8
print(my_other_list[-1]) # Imprime el último elemento
# print(my_other_list[7]) IndexError
# print(my_other_list[-5]) IndexError

# Contar ocurrencias
print(my_other_list.count("Darío")) # 1
print(my_list.count(33))

# Índice de un elemento concreto
print(my_other_list.index("Darío")) # 2

# Asignación de valores a variables respecto de una lista
age, height, name, surname = my_other_list
print(name) # Darío

# Concatenación
print(my_list + my_other_list) # Una lista tras otra
print(my_list * 5) # Una lista n veces (n = 5, en este caso)

# Añadir, quitar y modificar elementos de una lista
my_other_list.append("FC Barcelona") # Añade un elemento al final
print(my_other_list)

my_other_list.insert(2, "Rojo") # Inserta un elemento en una posición
print(my_other_list)

my_other_list.remove("FC Barcelona") # Elimina la primera ocurrencia de un elemento
print(my_other_list)

print(my_other_list.pop()) # Elimina el último elemento de una lista, pero también lo retorna (si se le añade un número 
                           # como parámetro hace el pop del elemento con ese índice)
print(my_other_list)
my_other_list.append(surname)

my_list.clear() # Limpiar lista
print(my_list)

my_other_list[2] = "Azul" # Cambia el valor del elemento en el ínice n

# Copiar una lista
my_copy_list = my_other_list.copy()
print(my_copy_list)

# Revertir una lista
my_copy_list.reverse()
print(my_copy_list)

# Ordenar lista
number_list = [3, 5, 4, 2, 1]
number_list.sort() # Orden numérico
print(number_list)

string_list = ["a", "c", "d", "b"]
string_list.sort() # Orden alfabético
print(string_list)

# Crear "sublistas"
print(my_copy_list[1:3]) # Igual que las strings, coge el primer índice e imprime hasta el último sin incluirlo
print(my_copy_list[::-1]) # Otra manera de revertir listas, igual que las cadenas de texto