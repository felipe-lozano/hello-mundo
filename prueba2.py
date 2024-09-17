def suma_dos_valores (sumando1, sumando2):
    global resultado
    resultado= sumando1 + sumando2
    return resultado 

#suma_dos_valores (4,5)
#print ("primera suma")
#print (resultado )
#suma_dos_valores (1,2)
#print ("segunda suma")
#print (resultado)

def calculadores_dos_valores (numero1,numero2,operador):
    global resultado1
    if operador == "suma": #si el operador es 1 es suma
        resultado1= numero1 + numero2
        return resultado1
    elif operador == "resta": #si el operador es 2 es resta
        resultado1= numero1 - numero2
        return resultado1
    elif operador == "multiplicacion" :#si el operador es 2 es multiplicacion 
        resultado1= numero1 * numero2
        return resultado1
    elif operador == "division": #si el operador es 2 es division 
        if numero2 == 0:
            return "Error: División por cero"
        else:
            resultado1= numero1 / numero2
            return resultado1     
    else:
        print ("el numero ingresado no  es valido")
        return resultado1

calculadores_dos_valores(1,2,1)
print ("suma", resultado1)


calculadores_dos_valores(1,2,2)
print ("resta", resultado1)

calculadores_dos_valores(1,2,3)
print ("multiplicacion", resultado1)

calculadores_dos_valores(1,2,4) 
print ("division", resultado1)


def calculador_de_teoremas (n1,n2):
    global resultado_final
    resultado= (n1*n1) + (n2*n2) 
    resultado_final= resultado * resultado
    return resultado_final

calculador_de_teoremas (4,5)
print (resultado_final)