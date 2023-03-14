#STRINGS

my_string = "Mi string"
my_other_string = "Mi otra string"
print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

new_string = "Este es un string \ncon salto de línea" #Se pone \n para hacer que lo que va después de la \n vaya abajo en otra línea
print(new_string)

my_tab_string = "\tEste es un string tabulado" #Tabula la línea
print(my_tab_string)

name, surname, age = "Marina", "Sanchez", 20
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) #S para string y D para int y F para float 
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #Fromas inútiles de escribirlo, se puede usar para emails, apps...
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #Esta es la mejor forma, f de formateo

language = "Python"
language_slice = language [1:3] #Pilla de la letra 1 a la 3 sin incluir la 3
print(language_slice)
language_slice = language [1:] #Pilla hasta el final si no pones un segundo número
print(language_slice)  

print(language.capitalize()) #Pone la primera letra en mayúculas
print(language.upper()) #Pone todo en mayúsuclas
print(language.count("y")) #Cuenta cuantas "y" hay
print(language.isnumeric()) #Pone True is es numero y pone False si es otra cosa (se puede hacer isupper, islower...)
print(language.lower()) #Pone todo minúsculas 
print(language.capitalize())
print(language.startswith("py")) #Pone True si empieza por "py" y False so no
