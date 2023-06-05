### Challenges ###

# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# Múltiplos de 3 por la palabra "fizz".
# Múltiplos de 5 por la palabra "buzz".
# Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
def fizz_buzz():
    for iterator in range(1, 101):
        if (iterator % 5 == 0 and iterator % 3 == 0):
            print("fizzbuzz")
        elif (iterator % 5 == 0):
            print("buzz")
        elif (iterator % 3 == 0):
            print("fizz")
        else:
            print(iterator)
        
fizz_buzz()


#  Escribe una función que reciba dos palabras (String) y retorne
#  verdadero o falso (Bool) según sean o no anagramas.
#  - Un Anagrama consiste en formar una palabra reordenando TODAS
#     las letras de otra palabra inicial.
#  - NO hace falta comprobar que ambas palabras existan.
#  - Dos palabras exactamente iguales no son anagrama.
def is_anagram(palabra_a, palabra_b):
    if (palabra_a.lower() == palabra_b.lower()):
        return False
    return sorted(palabra_b.lower()) == sorted(palabra_a.lower())
    
print(is_anagram("Amor", "roma"))


# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
#   la que el siguiente siempre es la suma de los dos anteriores.
#   0, 1, 1, 2, 3, 5, 8, 13...
def fibonacci(n):
    sucesion = [0]
    if (n > 1):
        sucesion.append(1)
    for i in range(2, n):
        sucesion.append(sucesion[i - 1] + sucesion[i - 2])
    return sucesion
        
    
print(fibonacci(50))