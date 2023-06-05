### Strings ###
my_string = "Mi cadena de texto"
my_other_string = "Otra cadena de texto"

# Longitud
print(len(my_string))

# Unión de varias string
print(my_string + " " + my_other_string)

# Retorno de carro o salto de línea
my_new_line_string = "Esto es una cadena\ncon salto de línea"
print(my_new_line_string)

# Tabulación
my_tab_string = "\tEsto es una cadena con tabulación"
print(my_tab_string)

# Formateo de cadenas
name, surname, age = "Darío", "Fajardo", 18
print("Mi nombre es {} {} y tengo {} años".format(name, surname, age))
print("Mi nombre es %s %s y tengo %d años" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y tengo {age} años")

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División
language_slice = language[0:3] # Imprime del caracter 0 al 3
print(language_slice)

language_slice = language[1:] # Omite el caracter 0
print(language_slice)

language_slice = language[-2] # Segundo caracter empezando por el final
print(language_slice)

language_slice = language[0:6:2] # Damos los que no queremos que imprima
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

# Funciones
print(language.capitalize()) # Mayúscula a la primera
print(language.upper()) # Todas a mayus
print(language.lower()) # Todas a minus
print(language.count("n")) # Número de ocurrencias de algo en la cadena (es case sensitive)
print(language.isnumeric()) # Cadena de texto contiene números?
print(language.lower().islower()) # Comprueba si todos los caracteres de una cadena son minus (existe también isupper())
print(language.startswith("py")) # Comprueba si empieza con lo introducido por parámetro (es case sensitive)