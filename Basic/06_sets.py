### Sets ###

# Los sets representan conjuntos matemáticos, tienen todas sus operaciones báasicas tales como
# unión, intersección, diferencia, diferencia simétrica, etc.

# Definición
my_set = set()
my_other_set = {}

print(type(my_other_set)) # Inicialmente es un dict

# Python entenderá que es un set y no un diccionario según el formato de los datos introducidos
my_other_set = {"Darío", "Fajardo", 18}
print(my_other_set)
print(type(my_other_set)) # Ahora es un set

# Añadir elementos
my_other_set.add(1.8)
print(my_other_set) # Un set no es un listado ordenado

my_other_set.add(1.8)
print(my_other_set) # Un set no admite repetidos

# Comprobar si un elemento existe dentro de un set
print("Darío" in my_other_set) # True
print("Papaya" in my_other_set) # False

# Eliminar un elemento
my_other_set.remove(1.8)
print(my_other_set)

# Limpiar un set
my_other_set.clear()
print(len(my_other_set)) # 0

# Borrar set (o cualquier variable)
del my_other_set # Elimina el conjunto

# Operaciones
A = {1, 2, 3, 4}
B = {3, 5, 6}

C = A.union(B) # Unión (C = AUB)
print(C)

C = A.difference(B) # Diferencia (C = A/B)
print(C)