#LOOPS

my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 1 

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución") 
        break
    print(my_condition)   
print("La ejecución continúa")    

my_list = [34, 67, 5, 89, 15]
my_dict = {"Nombre" : "Marina", "Apellido" : "Sanchez", "Edad": 20}
for element in my_list:
    print(element)
for element in list(my_dict.values()):
    print(element)
else:
    print("El bucle for para mi diccionario ha finalizado")    

for element in my_list: #Si el elemento es edad para la ejecución
    print(element)    
    if element == "Edad":
        break
for element in my_list: #Si el elemento es edad continua la ejecución
    print(element)    
    if element == "Edad":
        continue    