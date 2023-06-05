### Classes ###

class EmptyPerson:
    pass # Evita el error en clases o funciones sin definir

print(EmptyPerson)
        
class Person:
    # Constructor de la clase Person
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.full_name = f"{name} {surname}"
        
    # Getters
    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    
    # Método de la clase Person que "camina"
    def walk(self):
        print(f"{self.__name} {self.__surname} está caminando")
        
    # Método de la clase persona que saluda a otra persona
    def saludar(self, persona):
        print(f"{self.full_name} saluda a {persona.full_name}")



my_person = Person("Jose", "Fernández")
print(my_person.get_name(), my_person.get_surname())
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Darío", "Fajardo")
my_person.saludar(my_other_person)