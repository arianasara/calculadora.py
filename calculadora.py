print("calculadora, elija una opcion ingresando un numero")
print("1- suma")
print("2-resta")
print("3-multiplicacion")
print("4-division")

opcion=int(input("elija una opcion"))

def suma(a, b):
    return (a + b)
    
def resta(a, b):
    return(a - b)
    
def multiplicacion(a, b):
    return (a * b)
    
def division(a, b):
    return (a // b)
    
if(opcion==1):
   a=int(input("ingrese primer numero"))
   b=int(input("ingrese segundo numero"))
   print (suma(a,b))
 
elif(opcion==2):
   a=int(input("ingrese primer numero"))
   b=int(input("ingrese segundo numero"))
   print(resta(a,b))
 
elif(opcion==3):
   a=int(input("ingrese primer numero"))
   b=int(input("ingrese segundo numero"))   
   print(multiplicacion(a , b))
 
elif(opcion==4):
   a=int(input("ingrese primer numero"))
   b=int(input("ingrese segundo numero"))
   if(b==0):
        print("no se puede dividir por 0")
   print(division(a,b))
else:
    print("elija una opcion entre 1 y 4")



