### Functions ###

# Función básica
def mi_funcion():
    print("Esto es una función")

mi_funcion()

# Función con parámetros y retorno
def sum_values(a ,b):
    return a + b

print(sum_values(2, 2)) # 2 + 2 = 4

# Función recursiva
def pot(base, exp):
    if exp == 0:
        return 1
    else:
        return (base * pot(base, exp - 1))
    
print(pot(2, 10)) # 2^10 = 1024

# Orden de parámetros
def print_name(name, surname):
    print(f"mi nombre es {name} {surname}")

print_name(surname = "Fajardo", name = "Darío") # Si especificamos el valor con el nombre del parámetro da igual el orden

# Parámetros por defecto
def print_name_alias(name, surname, alias = "Sin alias"):
    print(f"{name}, {surname}, {alias}")
    
print_name_alias("Darío", "Fajardo") # Los parámetros con valor por defecto no han de ser pasados obligatoriamente

# Parámetros ilimitados
def print_upper_texts(*text):
    for element in text:
        print(element.upper())

print_upper_texts("Hola", "Adiós", "Papaya", "nose")