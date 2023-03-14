#DICTS

my_dict =  dict() #Almacenamos datos de tipo clave-valor
my_other_dict = {}

my_other_dict = {"Nombre" : "Marina", "Apellido" : "Sanchez", "Edad": 20}
my_dict = {
    "Nombre" : "Marina",
    "Apellido" : "Sanchez",
    "Edad": 20
    }

print(len(my_other_dict)) #No se empieza a contar desde 0, sino que la primera clave es la nº 1
print(len(my_dict))
print(my_dict["Nombre"]) #Se usa para imprimir el valor que hay guardado en la clave "Nombre"

my_dict["Nombre"] = "Juan" #Cambia "Marina" por "Juan"
my_dict["Altura"] = 1.59 #Añade una nuva clave al diccionario
print(my_dict)

del my_dict["Altura"] #Elimina solo la altura del diccionario 
print("Marina" in my_dict) #Te dice True si esta o False si no
my_dict.items() #Nos devuelve un listado del las claves y valores
my_dict.values() #Nos devuelve solo las claves
my_dict.keys() #Nos devuelve solo los valores
my_new_dict = (my_dict.fromkeys(("Nombre", "Edad", "Peso", "Calle"))) #Crea un diccionario sin valores
print(my_new_dict) 
my_new_dict = dict.fromkeys(my_dict,("Marina", "Sanchez"))
print(my_new_dict)