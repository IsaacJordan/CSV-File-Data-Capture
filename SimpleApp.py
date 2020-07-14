import csv
import sys
encendido = bool(True)

def leer():
    #Preguntar el nombre del archivo
    nombre = input("Ingrese el nombre del archivo: ")
    print("\n")
    #Leer archivo para verificacion
    with open(nombre+'.csv', 'r', newline='') as f:
         print(f.read())

    

def crear():
    #Preguntar el nombre del archivo
    nombre = input("Ingrese el nombre del archivo: ")

    #Crear o abrir archivo
    with open(nombre+'.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)

        #Preguntar si es un archivo nuevo
        resp = input("Es un archivo nuevo? (y/n): ")

        if resp == "y":
            #Tags default
            default = [["Nombre", "Monto"]]
            writer.writerows(default)
    
        ventas = int(input("Ventas del dia: "))
    
        i=1
        while i <= ventas:
            cliente = input("Nombre del cliente: ")
            monto = float(input("Monto de venta (MXN): "))
            entrada = [[cliente, monto]]
            writer.writerows(entrada)
            i+=1    

    file.close()


def apagar():
    quit()

def menu():
    print("**********Python Software Test**********")
    print("****************************************")
    print("\n")
    print("1. Crear o abrir documento.")
    print("2. Leer Documento")
    print("3. Apagar")
    
    var = int(input(": "))

    if var == 1:
        crear()
    if var == 2:
        leer()
    if var == 3:
        apagar()



while encendido :
    menu()



