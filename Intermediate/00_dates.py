### Dates ###

from os import system
from datetime import datetime

# Hora actual
now = datetime.now()
print(now)

# Componentes de un momento
print(now.year)
print(now.month)
print(now.second) # etc...

# Timestamp (segundos desde 1970, se usa en algunos programas y demás)
timestamp = now.timestamp()
print(timestamp)

# Crear una fecha
year_2024 = datetime(2024, 1, 1, 0, 0, 0, 0) # Fecha de inicio de 2024
print(year_2024)

from datetime import time # Hora individualmente
current_time = time(20, 5, 0)
print(current_time)

from datetime import date # Fecha individualmente
current_date = date.today()
print(current_date)

# Modificar fecha
current_date = date(current_date.year + 5, current_date.month, current_date.day)
print(current_date)

# Diferencias de fecha
print (year_2024 - now)

# Time delta
from datetime import timedelta # Un time delta no es una fecha o momento concreto sino representa un periodo de tiempo (o la diferencia entre dos momentos)
init_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta)

# Programa para imprimir la hora infinitamente cada segundo
# now = datetime.now()
# while True: 
#     old = now
#     now = datetime.now()
#     if now.second != old.second:
#         system('cls')
#         print(now.date())
#         print(f"{now.hour}:{now.minute}:{now.second}")