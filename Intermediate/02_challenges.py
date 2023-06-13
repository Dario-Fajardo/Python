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
    sucesion = []
    if (n >= 1):
        sucesion = [0]
    if (n > 1):
        sucesion.append(1)
    for i in range(2, n):
        sucesion.append(sucesion[i - 1] + sucesion[i - 2])
    return sucesion
            
print(fibonacci(50))


#  Escribe un programa que se encargue de comprobar si un número es o no primo.
#  Hecho esto, imprime los números primos entre 1 y 100.
def es_primo(number): # Comprueba si un numero es primo
    divisores = []
    for i in range(1, number):
        if (number % i == 0):
            divisores.append(i)
    
    if (divisores == [1]):
        return True
    else:
        return False
    
def imprime_primos(): # Imprime primos entre el 1 y el 100
    for i in range(1, 101):
        if es_primo(i):
            print(i)

# print(es_primo(int(input("Introduzca un número: "))))

imprime_primos()


# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
def invertir_cadena(cadena):
    reversed_cadena = ""
    for i in range(1, len(cadena) + 1):
        reversed_cadena += cadena[-1 * i]
    return reversed_cadena
        
print(invertir_cadena("torpedo acuático"))