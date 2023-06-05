### List Comprehension ###

# Lista con elementos de otra
my_original_list = [1, 2, 6, 9, 14, 2, 65]

my_list = [i for i in my_original_list]
print(my_list)

# Lista con rango
my_list = [i for i in range(8)] # [0 - 7]
print(my_list)

my_list = [i + 1 for i in range(8)] # [1 - 8]
print(my_list)

my_list = [i * 2 for i in range(8)] # De dos en dos
print(my_list)

my_list = [i * i for i in range(8)] # por si mismo
print(my_list)