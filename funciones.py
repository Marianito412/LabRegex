#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 30/3/2023 12:25am
#Ultima version: 30/3/2023 1:30pm
#Version: 3.10.6

#Importación de bibliotecas
import re

#Definición de funciones
def decodificarReposteria(pCodigo):
    """
    Funcionalidad: Decodifica el código de repostería
    Entradas:
    -pCodigo(str): El código a decodificar
    Salida:
    -return(str): El texto describiendo el producto
    """
    pCodigo=pCodigo.upper()
    if re.match('[1245]',pCodigo[3]):
        articulo="un"
    elif re.match('[367]',pCodigo[3]):
        articulo="una"
    if re.match('^(RED[1345])$',pCodigo):
        try:
            tiposDulces=["1","nidito","4","biscuit","5","crocante","3","orejita"]
            tipo=tiposDulces[tiposDulces.index(pCodigo[3])+1]
            return f"Usted solicita una reposteria de sabor dulce, correspondiente a {articulo}: {tipo}."
        except:
            return "Digite un código válido"
    if re.match('^(RES[26])$',pCodigo):
        try:
            tiposSalados=["2","palito de queso","6","enchilada"]
            tipo=tiposSalados[tiposSalados.index(pCodigo[3])+1]
            return f"Usted solicita una reposteria de sabor salado, correspondiente a {articulo}: {tipo}."
        except:
            return "Digite un código válido"
    else:
        if re.match('^(RES7[12]\w{2})$',pCodigo):
            try:
                sabores=["1","pollo","2","carne"]
                sabor=sabores[sabores.index(pCodigo[4])+1]
                tamannos=["PQ","pequeña","MD","mediana","GR","grande"]
                medida=tamannos[tamannos.index(pCodigo[5:])+1]
                return f"Usted solicita una reposteria de sabor salada, correspondiente a {articulo}: empanada de {sabor}, de tamaño {medida}."
            except:
                return "Digite un código válido"
        else:
            return "Digite un codigo valido"

def decodificarQueque(pCodigo):
    """
    Funcionalidad: Decodifica el código de en queque
    Entradas:
    -pCodigo(str): El código a decodificar
    Salida:
    -return(str): El texto describiendo el producto
    """
    if re.match("\w{5}", pCodigo):
        try:
            codigoTamannos = ["PQ", "Pequeño", "GR", "Grande"]
            tamanno = codigoTamannos[codigoTamannos.index(pCodigo[2:4])+1]

            codigoSabor = ["FR", "Fresa", "VN", "Vainilla", "CM","Caramelo", "CE", "Chocolate"]
            sabor = codigoSabor[codigoSabor.index(pCodigo[4:6])+1]
            return f"Usted solicita un queque de sabor de {sabor}, de tamaño: {tamanno}"
        except:
            return "Digite un código válido"
    return "Digite un código válido"

def decodificarTorta(pCodigo):
    """
    Funcionalidad: Decodifica el código de una torta chilena
    Entradas:
    -pCodigo(str): El código a decodificar
    Salida:
    -return(str): El texto describiendo el producto
    """
    if re.match("\w{5}", pCodigo):
        if pCodigo == "TCAGR":
            return "Usted solicita una torta chilena, de tamaño: grande"
    return "Digite un código válido"

def decodificarProducto(pCodigo):
    """
    Funcionalidad: detecta el tipo de código y delega su decodificación a la respectiva función
    Entradas:
    -pCodigo(str): El código a decodificar
    Salida:
    -return(str): El texto describiendo el producto
    """
    #return "Mjm, definitivamente es comida"
    if "RE" == pCodigo[:2]:
        return decodificarReposteria(pCodigo)
    elif "QE" == pCodigo[:2]:
        return decodificarQueque(pCodigo)
    elif "TCA" == pCodigo[:3]:
        return decodificarTorta(pCodigo)
    else:
        return "Digite un código válido"
    

