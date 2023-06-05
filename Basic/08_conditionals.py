### Conditionals ###

# Estructura if
condition = True
if condition:
    print("La condición es verdadera") # Solo se ejecuta si condition es True

# Encadenar condiciones
var = 15
if var == 15:
    print("La variable tiene valor 15")
elif var == -15:
    print("La variable tiene valor -15") # Se ejecuta si no se cumple el if y si se cumple la condicion (como escribir else if)
else:
    print("La variable tiene un valor distinto a 15") # Se ejecuta si la primera condicion del if no se cumple
    
# Comprobar si una variable tiene contenido
my_string = ""
if my_string:
    print("La cadena de texto (%s) tiene contenido" %(my_string))

### EJERCICIOS ### 
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 25,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# a) b) y c)
if 'skills' in person:
    print("La persona tiene habilidades de programación")
    if 'Python' in person['skills']:
        print("Además, domina Python")
    elif person['skills'] == ['JavaScript', 'React']:
        print("Es un desarrollador FrontEnd")
# d)
if person['is_marred'] and person['country'] == 'Finland':
    print("%s %s lives in Finland. He is married" %(person['first_name'], person['last_name']))