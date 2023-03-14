#CLASSES

class MyPerson: #Las clases siguen el CamelCase
    pass
print(MyPerson()) #Se puede poner MyPerson() con paréntesis o sin ellos

class MyEmptyPerson: #Las clases siguen el CamelCase
    pass
print(MyEmptyPerson())
print(MyEmptyPerson)

class Person: #Siempre hay que usar self
    def __init__(self, name, surname = "Sin apellido"):
        self.full_name = f"{name} {surname}"
    def walk(self):
        print(f"{self.full_name} Está caminando")    

my_person = Person("Marina", "Sanchez")
print(my_person.full_name)
my_person.walk()