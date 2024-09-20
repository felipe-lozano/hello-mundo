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
#ejercicio1 ()

def numeros_impares ():
    print ("tienes 60 segundos en cuanto tiempo lo hara")
    segundo= 60
    segundo = int(input("por favor ingrese los segundos: "))
    segundo1= segundo-60
    for i in range(60, segundo1,-1):
       print(i,end= ",\n")
       time.sleep(0)
       if i == 20 :
           break;
    #if  segundo > 60:
        #print ("\33[46m"+"se acabo el tiempo: ", segundo , "segundos, superaste el limite de tiempo"+"\33[0m")
    #else:
       # segundo < 60
        #print ("\33[41m"+"se acabo el tiempo: ", segundo , "segundos, felicidades lo hiciste en el tiempo maximo"+"\33[0m")

#numeros_impares ()


def calcula_ganancia ():
    pesos_año= float (input ("Cuanto dinero al año: ")) 
    tasa_interes= float(input("Tasa de interés anual: "))
    cantidad_años= int(input ("Cuantos anos: "))
    for i in range(1, cantidad_años+1):
        interes= pesos_año * (tasa_interes/100)
        pesos_año= pesos_año + interes
        print(f"En el año {i}, el dinero acumulado es: ${pesos_año:-2f}")
        time.sleep (1)
#calcula_ganancia()

def numero_trianguos (): 
    numero = int(input("Ingrese un número entero: "))
    for i in range(1, numero+1):
        for j in range(1, i+1):
            print("*", end=" ")
            time.sleep(1)
#numero_trianguos()


def numero_trianguos ():
    numero = int(input("Ingrese un número entero: "))
    for i in range(1, numero+1):
       print (" " * (numero - i) + "*" * (2-1 * i - 1))
       time.sleep(1)
#numero_trianguos()

def nunero_triangulo():
    numero = int(input ("Ingrese un número: "))
    for i in range(numero):
        print ("*" * i)
#nunero_triangulo ()

def descubrir_contraseña():
    contraseña = "123456"
    intentos_ingresado = int(input("por favor ingrese un numero de intentos: "))
    contraseña_ingresada= ""
    intento=3
    while contraseña_ingresada != contraseña:
        contraseña_ingresada = str(input("Ingrese la contraseña: "))
        if intento == intentos_ingresado:
            break
        elif contraseña_ingresada == contraseña:
         print ("Contraseña correcta!")
         break
        else:
         print ("Contraseña incorrecta")
         break
         intento = intento + 1
    
    #print( [contraseña_ingresada = contraseña == "contraseña correcta"] or [contraseña_ingresada != contraseña == "contraseñaincorrecta"])

#descubrir_contraseña()


#def descubrir_contraseña1():
   # contraseña = "123456"
    #intentos = 3
    #contraseña_ingresada=""
    #while contraseña_ingresada != contraseña:
     #   contraseña_ingresada = str(input("Ingrese la contraseña: "))
      #  if contraseña_ingresada != contraseña:
       #     intentos -= 1
        #    if intentos == 0:
         #       print("Contraseña bloqueada!")
          #      break
           # print ("Contraseña incorrecta, quedan", intentos, "intentos")
    #print("Contraseña correcta!")

#def contador_de_caracteres():
    #texto = str(input("Ingrese un texto: "))
    #frecuencia = {}
    #for letra in texto:
        #if letra in frecuencia:
       #     frecuencia[letra] += 1
      #  else:
     #       frecuencia[letra] = 
    #print(frecuencia)
#contador_de_caracteres ()

def contador_letra():
    texto = str(input("Ingrese un texto: "))
    letra = str(input("Ingrese una letra: "))
    contador = 0
    for i in texto:
        if i == letra:
            contador += 1
    print("La letra", letra, "se repite", contador, "veces en el texto")

contador_letra ()