"""
Nombre: Sumatoria
Entrada: Recibe dos parametros a y b
Salida: Suma dos parametros a y b
Restricción: Los dos parámetros deben ser ENTEROS
             Los dos parámetros debenser mayores a CERO
"""
def sumatoria(a,b):
    if isinstance (a,int) and isinstance (b,int):
        if a > 0 and b > 0:
            print (a+b)
        else:
            return "ERROR: los parámetros deben ser mayor a CERO"
    else:
        return "ERROR: Los parámetros deben ser de tipo ENTERO"
###############################################################################
"""
Nombre: Mayor De Edad
Entrada: El parámetro recibe una Edad
Salida: Se valida si con la edad ingresada es mayor o menor de edad
Restricción: El parámetro debe ser ENTERO
             El parámetro debe ser mayor a CERO
"""
def MayorEdad(edad):
    if isinstance (edad,int):
        if edad > 0:
            if edad >= 18:
                return "Es Mayor de edad"
            else:
                return "Es Menor de edad"
        else:
            return "EDAD DEBE SER MAYOR A CERO"
    else:
        return " ERROR: DIGITE LA EDAD" 
       
###############################################################################
"""
Nombre: Promedio
Entrada: son 4 parámetros que contienen diversos valores
Salida:  Se deben sumar los parámetros y luego se dividen entre cuatro
Restricción: Los parámetros deben ser ENTEROS
             Los parámetros deben ser mayor a CERO
"""
def promedio(n1,n2,n3,n4):
    if isinstance (n1,int) and isinstance(n2,int) and isinstance(n3,int)and isinstance(n4,int):
        if n1>0 and n2>0 and n3>0 and n4>0:
            
            resultado = (n1+n2+n3+n4)/4
            return resultado
            
        else:
            return "Los parámetros deben ser mayor a CERO"
    else:
        return "Los parámetros deben ser ENTEROS"
###############################################################################

"""
Nombre: Promedio
Entrada: son 4 parámetros que contienen diversos valores
Salida:  Se deben sumar los parámetros y luego se dividen entre cuatro
Restricción: Los parámetros deben ser ENTEROS
             Los parámetros deben ser mayor a CERO
"""
def volumen_caja(largo,alto,ancho):
    Resultado = largo*alto*ancho
    return Resultado
###############################################################################
def calcular_IVA(precio):
    IVA = 13/100
    Resultado = (precio*IVA)+precio
    return Resultado
###############################################################################
def mayor(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2


"""
Nombre: Presupuesto Evento
Entrada: Recibe un parámetro de numero de personas
Salida:  Cada que aumenta el numero de personas el costo del platillo reduce
Restricción: El parámetro debe ser ENTERO
             El parámetro debe ser mayor a CERO
"""
"""
def presupuestoEvento(numPersonas):
    if isinstance (numPersonas,int):
        if numPersonas > 0:
            numPersonas = 9500
            if numPersonas > 5 or <= 10:
                numPersonas=numPersonas -1000
   """             
################################################################################
"""
Nombre: contar_digitos
Entrada: recibe un numero entero
Salida:  divide por partes tantas veces el numero para contar sus digitos
Restricción: El parámetro debe ser ENTERO
             El parámetro debe ser mayor a CERO
"""
def contar_digitos(num):
    if isinstance(num,int):
        digitos = 0
        while(num>0):
            num = num//10
            digitos += 1
        return digitos
    else:
        return "Número debe ser entero"
