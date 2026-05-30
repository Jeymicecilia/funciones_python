import random

def tirar_datos():
    return random.randint(3,13)

def  pedir_respuestas():
     print("Ingresa tu prediccion")
     print("1. par")
     print("2. impar")
     print("3. salir del juego")

     return int( input())

def imprimir_resultado(numero, prediccion):
    es_par = numero % 2 == 0
    if es_par and prediccion == 1:
        print("Ganaste! Numero de os dados:", numero)
    elif not es_par and prediccion == 2:
        print("Ganaste! Numero de los dados:", numero)
    else:
        print("Perdiste! Numero de los dados:", numero)

while True:
    numero = tirar_datos()
    prediccion = pedir_respuestas()
    if prediccion == 3:
        break
    imprimir_resultado(numero, prediccion)

print("Gracias por jugar")


#
