### Higher order funcitions ###

# Funciones que pueden ejecutar otras funciones como parámetro
def sum_two(value):
    return value + 2

def sum_one(value):
    return value + 1

def sum_two_values_and_sum_one(a, b, f_sum): # Paso una función como parámetro
    return f_sum((a + b))

print(sum_two_values_and_sum_one(2, 2, sum_one)) # 5
print(sum_two_values_and_sum_one(2, 2, sum_two)) # 6

# Closures
def sum_ten(): # Función que retorna una función
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))

# Built-in higher order functions

numbers = [1, 2, 30, 400, 5]

# Map
def double(number):
    return number * 2

print(list(map(double, numbers)))
print(list(map(lambda number: number * 2, numbers))) # Usando una lambda

# Filter
from functools import reduce

def filter_greaters_than_ten(value): # Condición de filtrado
    if value > 10:
        return True
    else:
        return False

print(list(filter(filter_greaters_than_ten, numbers))) # Filtra elementos según diga una función que se pasa por parámetro
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
def sum_two_values(a, b): # Suma de dos valores
    return a + b

print(reduce(sum_two_values, numbers)) # Acumula el valor de la función y va añadiendo un valor distinto del iterable