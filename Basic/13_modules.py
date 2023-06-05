### Modules ###

# import 10_functions Da error, los módulos no pueden contener números al inicio de su nombre
import my_module
from my_other_module import pot
# from my_other_module import print_upper_texts

my_module.sum(5, 7, 8) # Usar . para acceder a una función del módulo

print(pot(2, 10)) # Si se importa una función concreta desde un módulo no hace falta usar .
# print_upper_texts("hola", "adiós") Solo esta importado pot desde my_other_module

# Módulos propios de python
import math

print(math.pi)

from math import pi as PI_VALUE

print(PI_VALUE)