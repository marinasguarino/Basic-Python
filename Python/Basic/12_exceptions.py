#EXCEPTION HANDLING

numberOne, numberTwo = 5,1
numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: #Se ejecuta si se produce una excepción
    print("Se ha producido un error")   
    
    
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")        
else: #Se ejecuta si no se produce ninguna excepción
    print("La ejecución continúa correctamente")  
    
#Else y Finally son opcionales 
 
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")        
else: #Se ejecuta si no se produce ninguna excepción
    print("La ejecución continúa correctamente") 
finally: #Se ejecuta siempre
    print("La ejecución continúa")        


try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError: #Se ejecuta si se produce una excepción
    print("Se ha producido un ValueError")  
except TypeError: #Se ejecuta si se produce una excepción
    print("Se ha producido un TypeError")     