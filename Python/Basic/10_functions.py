#FUNCTIONS

def my_function():
    print("Esto es una función")

my_function()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(5,7)
sum_two_values(3.5,2.5)

def print_name(name,surname):
    print(f"{name} {surname}") #Se pone la f para acceder a esos valores, sino solo pondría {name} {surname}
          
print_name("Marina", "Sanchez")     

def print_name_with_default (name, surname, alias = "Sin alias"): #Si no tiene alias, imprime que no tiene alias
     print(f"{name} {surname} {marinas}")

print_name_with_default("Marina,"Sanchez","Marinas")

def print_texts(*text): #La * hace que pueda ser más de 1 texto
    for text in texts:
    print(text)

print_texts("Hola", "Python")
print_texts("Hola")    

def print_upper_texts(*text): 
    for text in texts:
    print(text)

print_upper_texts("Hola")
