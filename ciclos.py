#Ciclo,interaccion, bucle

#while
""""""
i = 0
while i < 0:
    if i < 6:
        print("El numero", i, "es menor a 6")
    else:
        print("El numero", i, "es menor o igual a 5")
    i += 1
print("Termino la interaccion")
""""""


for x in "Jeymi":
    #print(x)

 while True:
    print("Escribe la opcion deseada")
    print("1: Saludar")
    print("2: Salir")

    respuesta = int(input())

    if respuesta == 1:
       print("Salados chicos!")
    elif respuesta == 2:
       break

print("Terminando programa")
