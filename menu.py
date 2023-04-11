#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 30/3/2023 12:25am
#Ultima version: 30/3/2023 1:30pm
#Version: 3.10.6

from funciones import *

def validarBin(pEntrada: str):
    while True:
        if pEntrada.upper().replace("Í", "I") == "SI":
            return True
        elif pEntrada.lower() == "no":
            return False
        else:
            pEntrada = input("Entrada incorrecta, vuelva a intentar ( ingrese sí o no) ")

def menu():
    salir = False
    while not salir:
        print(
            "Productos disponibles:\n"
            "[RE]Repostería [D]Dulce o [S]Salada\n"
            "1. Nidito\n"
            "2. Palito de queso\n"
            "3. Orejita\n"
            "4. Biscuit\n"
            "5. Crocante\n"
            "6. Enchilada\n"
            "7. Empanada (1.Pollo/2.Carne)\n"
            "   [PQ]Pequeña, [MD]Mediana o [GR]Grande\n"
            "______________________________________\n"
            "[QE]Queque [GR]Grande o [PQ]Pequeño\n"
            "[FR]Fresa-chocolate\n"
            "[VN]Vainilla\n"
            "[CM]Caramelo\n"
            "[CE]Chocolate\n"
            "______________________________________\n"
            "[TCAGR]Torta chilena grande\n"
        )
        codigo = input("Ingrese un código: ")
        print(decodificarProducto(codigo))

        salir = not validarBin(input("Desea decodificar un nuevo producto? "))

menu()
