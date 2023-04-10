#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 30/3/2023 12:25am
#Ultima version: 30/3/2023 1:30pm
#Version: 3.10.6

import re

def decodificarQueque(pCodigo):
    if re.match("\w{5}", pCodigo):
        codigoTamannos = ["PQ", "Pequeño", "GR", "Grande"]
        tamanno = codigoTamannos[codigoTamannos.index(pCodigo[2:4])+1]

        codigoSabor = ["FR", "Fresa", "VN", "Vainilla", "CM","Caramelo", "CE", "Chocolate"]
        sabor = codigoSabor[codigoSabor.index(pCodigo[4:6])+1]
        return f"Usted solicita un queque de sabor de {sabor}, de tamaño: {tamanno}"
    return "Código inválido"

def decodificarTorta(pCodigo):
    if re.match("\w{5}", pCodigo):
        if pCodigo == "TCAGR":
            return "Usted solicita una torta chilena, de tamaño: grande"
    return "Código inválido"

def decodificarProducto(pCodigo):
    #return "Mjm, definitivamente es comida"
    if "QE" == pCodigo[:2]:
        return decodificarQueque(pCodigo)
    elif "TCA" == pCodigo[:3]:
        return decodificarTorta(pCodigo)