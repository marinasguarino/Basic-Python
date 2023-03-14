
#VARIABLES

my_variable = "My string variable"
my_int_variable = 5
my_int_to_str_variable = str(my_int_variable)

print(my_variable)
print (len(my_int_to_str_variable)) #Len te dice cuantas letras tiene algo, da 1 porque 5 es un caracter
print (len(my_variable)) #Da 18, porque cuenta las letras de "My string variable"
print("Mi primo tiene",my_int_variable,"años") 

name, surname, age = "Marina", "Sanchez", 20
print("Me llamo:", name, surname, ". Mi edad es:", age)

address: str = "Mi dirección" #Esto no sirve para nada, ya que se guarda como el último valor dado (32)
address = 32
print (address)
print(type(address)) #Aunque lo guardamos como string, 32 es int 