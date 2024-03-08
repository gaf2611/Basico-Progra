def cantidadDigitos (num):
 
    contador = 0
    while num > 0:
        num = num // 10
        contador = contador + 1
    return contador


def totalDigitosDivisibles(num,dig):
    if isinstance(num,int) and isinstance(dig,int):
        if num > 0 and dig > 0:
            contador = 0
            while (num > 0):
                
                if (num%10) % dig == 0:
                    contador += 1
                num //= 10
            return contador
        else:
            return "Número y digito deben ser mayores a cero."
    else:
        return "Número y Digito deben ser Números enteros."

def contarDivisores(num):
    if isinstance(num,int):
        if num > 0 :
            contarDiv = 0
            Divisor = 1
            while(num >= Divisor):
                if (num%Divisor)== 0:
                    contarDiv +=1
                    return Divisor
                Divisor += 1
            return contarDiv
        else:
            return "Número debe ser mayor a cero."       
    else:
         return "Número debe ser Número entero."          
##############################SACAR EL DIGITO MAYOR DEL NUMERO###############################
def digitoMayor(num):
    if isinstance (num,int):
        if num > 0:
            nMayor= 0
            while(num>0):
                digito = num%10
                if digito > nMayor:
                    nMayor = digito
                num//=10
            return nMayor
        else: "Error: Numero debe ser mayor a CERO"
    else: "Error: Número debe ser ENTERO"
######################RETORNAR DIGITOS PARES EN LA LISTA#####################################
def listaDigitosPares(num):
    if isinstance(num,int):
        if num > 0:
            lPares = []
            while (num>0):
                digito = num%10
                if(digito%2) == 0:
                    lPares +=[digito]
                num//=10
            return lPares
        else:
            return "Número Debe Ser Mayor A CERO"
    else:
        return "Número Debe Ser ENTERO"
####################MITAD DE NUMERO PAR Y RETORNARLO EN LISTA#########################           
def dividirMitadNumero(num):
    v1 = cantidadDigitos(num)
    if not isinstance(num,int):
        return "Error: Número debe ser ENTERO"
    elif num < 0:
        return "Error: Número debe ser mayor a CERO"
    elif (v1 == 2):
        return "Error: la cantidad de digitos debe ser mayor"
    elif (v1%2) != 0:
        return "Error: Digitos deben ser pares"
    Valor= v1 /2
    der = 0
    izq = 0
    exponente = 0
    lPar = []
    for n in range (int(Valor)):
        digito = num%10
        der+=digito*10**exponente
        exponente +=1
        num//=10
    izq*num
    lPar+=[izq,der]
    return lPar
##################################CADENAS DE TEXTO#######################################

def buscarEnTexto(cadenaTexto, textoBuscar):
    if not (isinstance (cadenaTexto,str) and isinstance(textoBuscar,str)):
        return "Error: Los parámetros deben ser String."
        if not (cadenaTexto!= '' and textoBuscar != ''):
            return "Error: ambos parametros deben ser diferentes a vacío"
        
        return buscarEnTexto_Aux(cadenaTexto, textoBuscar)
        
def buscarEnTexto_Aux(cadenaTexto, textoBuscar):
    resultado = False

    for caracter in cadenaTexto:
        if textoBuscar == caracter:
            resultado = True
    return resultado
"""
    Nombre: largoTexto
    Entrada: texto
    salida: La cantidad de caracteres que contiene largoTexto
    Restricción: Que no sea vacío
"""
def largoTexto(texto):
    if  isinstance(largoTexto, str):
        if texto!= '':
            return largoTexto_Aux(texto)
        else:
            return "Error: Parámetro debe ser diferente a vacío"
        
    else:
        return "Error: Parámetro debe ser String"
def largoTexto_Aux(texto):
    resultado = 0 
    for caracter in texto:
        resultado += 1
        
    return resultado
        
