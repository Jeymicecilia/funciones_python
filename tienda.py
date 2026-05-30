from datetime import detetime

print('***************************')
print('**     BIENVENIDO A      **')
print('** LA TIENDA DE MAQUILLAJE **')
print('***************************')

inventario= {
    "gloss": 23,
    "rubor": 20,
    "rimel": 14,
    "mascarillas": 27
}

maquillaje_total = 0
for val in inventario.values():
    maquillaje_total += val 

print("por favor ingresa tu nombre")
nombre = input()
print("por favor escribe tu apellido")
apellido = input()

#Concatenacion 
nombre_completo = nombre + "   " + apellido

print("Gracias por visitarnos", nombre_completo)

compras = {}

def mostrar_menu():
    print("")
    print("===========================")
    print("eleccionar la opcion que deseas:")
    print("1: Conocer cuantos maquillajes tiene la tienda")
    print("2: Comprar un maquillaje")
    print("3 Mostrar compras")
    print("4: Salir del programa")

    def mostrar_inventario():
        print("****INVENTARIO****")
        for llave, valor in inventario.items():
            print(f"    {llave}:  {valor}")
        print("En total tenemos", maquillaje_total, "maquillaje")
