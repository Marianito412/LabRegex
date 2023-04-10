#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 30/3/2023 12:25am
#Ultima version: 30/3/2023 1:30pm
#Version: 3.10.6

import re

def decodificarProducto(pCodigo):
    resultado=""
    if re.match('red\d',pCodigo):
        resultado="Usted solicita una reposteria de sabor dulce, correspondiente a articulo: tipo."
        if re.match('1',pCodigo[3]):
            resultado=resultado.replace("tipo","nidito")
        elif re.match('4',pCodigo[3]):
            resultado=resultado.replace("tipo","biscuit")
        elif re.match('5',pCodigo[3]):
            resultado=resultado.replace("tipo","crocante")
        elif re.match('3',pCodigo[3]):
            resultado=resultado.replace("tipo","orejita")
        else:
            return "Debe digitar un codigo valido"
    elif re.match('res\d',pCodigo):
        resultado="Usted solicita una reposteria de sabor salada, correspondiente a articulo: tipo."
        if re.match('2',pCodigo[3]):
            resultado=resultado.replace("tipo","palito de queso")
        elif re.match('6',pCodigo[3]):
            resultado=resultado.replace("tipo","enchilada")
        else:
            return "Debe digitar un codigo valido"
    elif re.match('res\w{4}',pCodigo) :
        resultado="Usted solicita una reposteria de sabor salada, correspondiente a articulo: tipo de sabor, de tamaño medida."
        if re.match('7',pCodigo[3]):
            resultado=resultado.replace("tipo","empanada")
            if re.match('1',pCodigo[4]):
                resultado=resultado.replace("sabor","pollo")
            elif re.match('2',pCodigo[4]):
                resultado=resultado.replace("sabor","carne")
            else:
                return "Solo hay dos sabores"
            if re.match('pq',pCodigo[5:]):
                resultado=resultado.replace("medida","pequeña")
            elif re.match('md',pCodigo[5:]):
                resultado=resultado.replace("medida","mediana")
            elif re.match('gd',pCodigo[5:]):
                resultado=resultado.replace("medida","grande")
            else:
                return "Solo hay tres tamaños"
    else:
        return "Digite un codigo valido"
    return resultado
                
            
    """if re.match('[1245]',pCodigo[3]):
        resultado=resultado.replace("articulo","un")
        if re.match('[367]',pCodigo[3]):
            resultado=resultado.replace("articulo","una")
        return resultado"""
