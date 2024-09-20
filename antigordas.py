print ("este es un codigo que mide tu peso y te dice que tan saludable estas")
# Generar la elección del ordenador 
def estado_de_salud():
    salud = int(input("cuanto pesa usted")) 
    if salud >= 60:
        print ("\33[41m"+"usted es una focking gorda"+"\33[0m")
    if salud <= 60:
        print ("\33[46m"+"mamazota "+"\33[0m")
    return salud
estado_de_salud() 

