#LIST COMPREHENSION

my_original_list = [0,1,2,3,4,5,6,7]
print(my_original_list)

my_range =range(8)
print(list(my_range))

my_list = [i for i in range(8)]
print(my_list)

my_list = [i + 1 for i in range(8)] #Le suma 1 a los elementos de la lista
print(my_list)

my_list = [i * 2 for i in range(8)] #Multiplica por 2 los elemntos de la lista
print(my_list)

 
def sum_five(number): #Se modifica el valor antes de añadirlo a la lista
    return number + 5 
my_list = [sum_five(i) for i in range(8)] 
print(my_list)