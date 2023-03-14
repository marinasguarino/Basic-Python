#LISTAS

my_list = list() 
my_other_list = []
print(len(my_list))

my_list = [25, 35, 76, 89, 19, 19, 68]
print(my_list)

my_other_list = [34, 23, 65 ,5, 6, "Marina", 2.55]
print(my_other_list)  
print(my_other_list[0]) #Pongo el número de la posición del caracter que quiero
print(my_other_list[-1]) #Sale el último número de la lista, ya que el -0 no existe

my_list = []
my_list.append("Marina") #Para añadir algo a la lista (lo añade al final)
my_list.insert(1, "Sanchez") #El 1 es la posición donde lo quieres meter, y el otro lo que quieres meter
my_list.remove("Marina") #Borra lo que le des, si hay 2 valores iguales solo borra 1
my_list.pop() #Si no pones nada, elimina el último valor de la lista, si le pones un número elimina lo que hay en esa posción de la lista
del my_list [2] #Borra el elemento en esa posición
my_list.clear() #Borra la lista
my_new_list = my_list.copy() #Copia la lista
my_list.reverse() #Le da la vuelta a la lista (el primero el último y el último el primero)
my_list.sort() #Si no pones nada, ordena de mayor a menor o alfabéticamente
my_list.index("Marina") #Nos dice en que posición esta la palabra