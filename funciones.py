#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 30/3/2023 12:25am
#Ultima version: 30/3/2023 1:30pm
#Version: 3.10.6

import re

def decodificarReposteria(pCodigo):
    pCodigo=pCodigo.upper()
    if re.match('[1245]',pCodigo[3]):
        articulo="un"
    elif re.match('[367]',pCodigo[3]):
        articulo="una"
    if re.match('^(RED[1345])$',pCodigo):
        tiposDulces=["1","nidito","4","biscuit","5","crocante","3","orejita"]
        tipo=tiposDulces[tiposDulces.index(pCodigo[3])+1]
        return f"Usted solicita una reposteria de sabor dulce, correspondiente a {articulo}: {tipo}."
    if re.match('^(RES[26])$',pCodigo):
        tiposSalados=["2","palito de queso","6","enchilada"]
        tipo=tiposSalados[tiposSalados.index(pCodigo[3])+1]
        return f"Usted solicita una reposteria de sabor salado, correspondiente a {articulo}: {tipo}."
    else:
        if re.match('^(RES[12]\w{2})$',pCodigo):
            sabores=["1","pollo","2","carne"]
            sabor=sabores[sabores.index(pCodigo[4])+1]
            tamannos=["PQ","pequeña","MD","mediana","GR","grande"]
            medida=tamannos[tamannos.index(pCodigo[5:])+1]
            return f"Usted solicita una reposteria de sabor salada, correspondiente a {articulo}: empanada de {sabor}, de tamaño {medida}."
        else:
            return "Digite un codigo valido"
