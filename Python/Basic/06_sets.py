#SETS

my_set = set() #Un set no es una estructura ordenada que no admite repetidos
my_other_set = {} #En realidad esto es un diccionario, pero cuando le das valores se convierte en un set
my_other_set = {"Marina", "Sanchez", 20}

my_set[0] #No se puede acceder a un elemento de un set
my_other_set.add("Guarino") #Añade la palabra al principio del set, no puede haber 2 palabras repetidas
my_other_set.remove("Marina") #Elimina la palabra del set
my_other_set.clear() #Borra el contenido del set
del my_other_set #Ya no existe my_oher_set
my_list = list(my_set)
my_list[0]
my_other_set = {"Laura", "Martin", 34} 
my_new_set = my_set.union(my_other_set) #No funciona porque lo que quiero añadir ya está en la lista
my_set = my_new_set.union(my_new_set).union({1.73, 30.000}) #Si añade estos elementos ({1.73, 30.000.000})porque son nuevos
my_new_set.difference(my_set) #Solo guarda los elementos que no esta en común