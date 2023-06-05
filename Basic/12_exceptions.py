### Exceptions ###

number_one, number_two = 5, "1"

# try except
try: # Se ejecuta siempre, si da error, produce una excepción
    print(number_one + number_two)
except: # Se ejecuta si ocurre una excepción
    print("Se ha producido un error")
    
# try except else finally
try:
    print(number_one + number_two)
except:
    print("Se ha producido un error")
else: # Se ejecuta solo si el try no se produce excepción
    print("La ejecución continua correctamente")
finally: # Se ejecuta siempre
    print("La ejecución continua")

# Excepciones por tipo de error
try:
    print(number_one + number_two)
except TypeError:
    print("Se ha producido un error de tipo TypeError")
except ValueError:
    print("Se ha producido un error de tipo ValueError")

# Captura de la información de la excepción
try:
    print(number_one + number_two)
except ValueError as error:
    print(error)
except TypeError as error:
    print(error)
except Exception as error:
    print(error)