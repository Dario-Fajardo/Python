### Tuplas ###

# Definición
my_tuple = tuple()
my_tuple = ()

# Asignación de valores
my_tuple = (18, 1.8, "Darío", "Fajardo") # No podrá ser modificada en otro lugar del código
print(my_tuple)
print(type(my_tuple))

# Acceso a un elemento
print(my_tuple[0]) # Elemento 0 (18)
print(my_tuple[-1]) # Último elemento ("Fajardo")

# Contar ocurrencias
print(my_tuple.count(1.8))

# Índice de un elemento concreto
print(my_tuple.index("Darío"))

# ¿Modificar tuplas?
# my_tuple[1] = 19 Error, las tuplas SON INMUTABLES

# Concatenación
my_other_tuple = (1, 2, 3, 4, 5)
print(my_tuple + my_other_tuple)

# Acceder a un fragmento de la tupla
print(my_tuple[1:3])
print(my_tuple[::-1]) # Reverse

# Para hacer mutable una tupla podemos convertirla en lista
my_other_tuple = list(my_other_tuple) # Conversión a lista
print(type(my_other_tuple))
my_other_tuple.append("Nuevo elemento") # Modificación
my_other_tuple = tuple(my_other_tuple) # Reconversión a tupla
print(type(my_other_tuple))
print(my_other_tuple)

# Borrar tupla
del my_other_tuple # La palabra clave del sirve para borrar cualquier variable (incluso un elemento de una lista)