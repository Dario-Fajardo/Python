### Type Hints ###

my_int_var = 6
print(type(my_int_var)) # int

my_int_var = "Hola"
print(type(my_int_var)) # str

# Tipado débil, FastApi recomienda utilizarlo para facilitar al backend distintas 
# operaciones entendiendo los tipos de datos que se utilizan en el código
my_typed_var: str = "Variable tipada"