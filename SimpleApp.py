import csv
import sys
encendido = bool(True)

def leer():
    #Ask for name of the document
    nombre = input("Name of the file: ")
    print("\n")
    #Read document
    with open(nombre+'.csv', 'r', newline='') as f:
         print(f.read())

    

def crear():
     #Ask for name of the document
    nombre = input("Name of the file: ")

    #Open or create the document by name
    with open(nombre+'.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)

        #Ask if the document is new
        resp = input("Creating a new document? (y/n): ")

        if resp == "y":
            #Tags default
            default = [["Name", "Price"]]
            writer.writerows(default)
    
        ventas = int(input("Number of sales: "))
    
        i=1
        while i <= ventas:
            cliente = input("Name of client: ")
            monto = float(input("Selling price (dlls): "))
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
    print("1. Creat or open a document.")
    print("2. Read Document")
    print("3. Exit")
    
    var = int(input(": "))

    if var == 1:
        crear()
    if var == 2:
        leer()
    if var == 3:
        apagar()



while encendido :
    menu()



