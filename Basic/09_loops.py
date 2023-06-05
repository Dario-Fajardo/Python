### Loops ###

# While
my_condition = 0
while my_condition <= 10:
    print(my_condition)
    my_condition += 1
else: # En Python a los whiles se les puede añadir un else
    print("my_condition ha superado el valor 10")
    
iterator = 0
while iterator < 20:
    if iterator == 13:
        print("Se rompe el bucle porque me sale de los cojones", iterator)
        break # Palabra reservada que rompe un bucle
    print("iterator es menor que 20", iterator)
    iterator += 1
    
# For
my_list = [23, 56, 34, 33, 99, 69, 0]
print("Elementos de la lista:")
for element in my_list:
    print(element)
    
my_dict = {
    "Nombre" : "Darío", 
    "Apellido" : "Fajardo", 
    "Edad" : 35,
    "Lenguajes" : {"Python", "C++", "Assembly"},
    1:1.8
    }
for element in my_dict:
    if element == 'Edad':
        break # El break funciona para el bucle for también (no se ejecuta el else)
    print(element, ":", my_dict[element]) # Formato clave:valor
else: # Para el for también se puede usar el else
    print("El bucle for ha finalizado") 
    
for element in my_dict:
    if my_dict[element] == "Álvarez":
        break
    else: 
        continue # Continue hace que termine la iteración, el print nunca se imprimirá
        print("Esto no se va a imprimir nunca")
        
### EJERCICIOS ###
# 1-.
number = 0
fin = int(input("Introduce un número para sumar todos hasta él"))
sum = 0
while number <= fin:
    sum += number
    number += 1
print("La suma de los números entre 0 y %d es %s" %(fin, sum))