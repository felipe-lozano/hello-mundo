import time
print("hola mundo \n")
print("segundo reglon")
time.sleep(3)

#print("chao mundo")
print ("mentiras volvi")

print (type("hola"))# esta funcion me dice que tipo de dato es lo que esta entre parentesis 
print (type(6))
print (type(5.5))
print ("pruebagitignore")
print ("--------------------------------------------------------")
bool=True
print (bool)
print (type(bool))
numero= 5
texto= "hola"
suma= str(numero) + texto
print (suma)

bool1=True
bool2=False

suma2= bool1+bool2
print (suma2)
A= False
B= False
C= False
D= True

Resultado= ((A and B)and C) or D
print (Resultado)

A= True
B= True
C= True
D= True
Resultado2= ((A and B)and C) or D
print (Resultado2)

def pitagoras (a,b):
    global hipotenusa
    hipotenusa = (a**2 + b**2)**0.5
    return hipotenusa

#pitagoras (3,4)
#print ( hipotenusa)

def suma_dos_valores (sumando1, sumando2):
    global resultado
    resultado= sumando1 + sumando2
    return resultado 

def despeje_x (): 
    global x
    b= int(input("ingrese ahora el valor de b= ")) 
    c= int(input("ingrese ahora el valor de c= ") )
    x = (c-b)/2
    print ( x )
    return x

#despeje_x()
false=0 
true=1
#A= bool(input ("ingrese el valor de= "))
#B= bool(input ("ingrese el valor de= "))
#C= bool(input ("ingrese el valor de= "))

#Resultado2= (A and B)and C
#print ("resultado= ",Resultado2)

def pitagoras_funcion_sumar():
    global resulpitagoras
    a= int(input("ingrese ahora el valor de a= ")) 
    b= int(input("ingrese ahora el valor de b= ") )

    a2=a**2
    b2=b**2

    suma= suma_dos_valores (a2,b2)
    resulpitagoras= suma**0.5
    print ( "el valor de pitagoras es= ",resulpitagoras)
    return resulpitagoras

pitagoras_funcion_sumar ()

def contador_de_letras (texto):
    letras = texto.split ()
    frecuencia ={}
    for letras in letras:
        if letras in frecuencia:
            frecuencia[letras] += 1
        else:
            frecuencia[letras] = 1
    return frecuencia