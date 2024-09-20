
def separador_contador ():
   global resultado_contador
   palabras = str(input("palabra"))
   letra = str(input("letra"))
   resultado_contador = palabras.count(letra)
   print ("la cantidad de letras", letra , "es= " , resultado_contador )
   print ("la cantidad de letras de la palabra es= ", len(palabras))
   print ("palabras separada por letra= ", list(palabras))
   return resultado_contador

#separador_contador ()

import random
print("¡Bienvenido al juego de piedra, papel o tijera!") 
print("Elije tu opción:") 
print ("1. Piedra") 
print("2. Papel") 
print("3. Tijera")
 
# Generar la elección del ordenador 
jugador = random.randint(1, 3)
 
# Asignar valores numéricos a las opciones 
if jugador == 1: 
      opcion_computadora1 = "Piedra" 
elif jugador == 2: 
      opcion_computadora1 = "Papel" 
else: 
      opcion_computadora1 = "Tijera"


# Generar la elección del ordenador 
computadora = random.randint(1, 3)
 
# Asignar valores numéricos a las opciones 
if computadora == 1: 
      opcion_computadora = "Piedra" 
elif computadora == 2: 
      opcion_computadora = "Papel" 
else: 
      opcion_computadora = "Tijera"

# Determinar el ganador 
if jugador == computadora: 
     print("Empate. la computadora escogio= ", opcion_computadora , "y tu =", opcion_computadora1) 
elif (jugador == 1 and computadora == 3) or (jugador == 2 and computadora == 1) or (jugador == 3 and computadora == 2): 
     print("¡Ganaste! la computadora escogio= ", opcion_computadora , "y tu =", opcion_computadora1) 
else: 
     print("Perdiste. la computadora escogio= ", opcion_computadora , "y tu =", opcion_computadora1)  