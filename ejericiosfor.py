import time
def ejercicio1 ():
    palabra = str(input("por favor ingrese su edad: "))
    cantidad= int(input("por favor ingresar cantidad de veces: "))
    for i in range(palabra):
        print( "valor de la variable: ", i+1)
        time.sleep(2)
        print (palabra)
    return palabra
#ejercicio1 ()

#un programa que pida la edad de nosotros igual a 5 
import time
def ejercicio1 ():
    edad = int(input("por favor ingrese su edad: "))
    for i in range(edad):
        print( "valor de la variable: ", i+1)
        print (i+1)
        time.sleep(2)
    return edad
#ejercicio1 ()

import time
def ejercicio1 ():
    añoNacimiento = int(input("por favor ingrese el año de nacimiento: "))
    añoactual = int(input("por favor ingrese el año actual: "))
    edad = añoactual - añoNacimiento
    print ("su edad es : ", edad)
    for i in range(edad):
        print(i+1)
    return edad
ejercicio1 ()