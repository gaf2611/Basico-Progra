"""
Nombre: multiplicacion
Entrada : num,factor
Salida: resultado de la multiplicaion
Restricciones:
  numero debe ser entero y mayor a 0
"""
def multiplicacion (num,factor):
    resultado= 0
    if isinstance (num,int):
        if num >0:
            for  i in range (factor):
                resultado=num+resultado
            return resultado
        else:
            "El numero es menor o igual que 0"
    else:
        "EL numero no es entero"

"""
Nombre: invertirNumero
Entrada : num
Salida: Numero invertido
Restricciones:
  numero debe ser diferente a 0
"""
def invertirNumero (num):
    resultado=0
    while num !=0:
        resultado = 10 * resultado + num % 10
        num //=10
    return resultado
"""
Nombre: invertirNumero
Entrada : num
Salida: Numero invertido
Restricciones:
  numero debe ser diferente a 0
"""
def divisores(num):
    divisor = num
    resultado=[]
    residuo=0
    if num >0:
        while num >0:
            num % divisor
            if residuo==0:
                resultado+=1
                divisor-=1
            else:
                divisor-=1
                
        

"""
Nombre: invertirNumero
Entrada : num
Salida: Numero invertido
Restricciones:
  numero debe ser diferente a 0
"""
def contarDigitosFlotante(num):
    contador=1
    numeroentero=0
    num = str(num)
    for i in num:
        if i == ".":
            contador -=1
        else:
            contador+=1
        if i == "-":
            contador -=1
    
    return contador 
    

"""
Nombre: invertirNumero
Entrada : num
Salida: Numero invertido
Restricciones:
  numero debe ser diferente a 0
"""

def indiceNumero(numero, indice):
    num_str = str(numero)
    if indice >= len(num_str):
        return "Error: Indice fuera del rango del número"
    else:
        return int(num_str[indice])


                    
"""
Nombre: invertirNumero
Entrada : num
Salida: Numero invertido
Restricciones:
  numero debe ser diferente a 0
"""
def multiplicarElmentosLista (lista):
    producto=1
    for numero in lista:
        producto*=lista
        return producto

"""
Nombre: invertirNumero
Entrada : num
Salida: Numero invertido
Restricciones:
  numero debe ser diferente a 0
"""
def corrimientoAEntero(num):
    resultado=0
    original=num
    if isinstance(num, float):
        if num <0:
            num*=-1
        if int(num*10)== num *10 :
           resultado= num*10
        else:
            resultado= num*100
        if original <0:
                resultado*=-1
        return int(resultado)
   
    else:
        return " Ingrese un numero con decimales para convertirlo en entero"



def cortarNumero(num,ini,fin):
    if isinstance(num, int) and (num > 0):
       if isinstance(ini, int) and(ini >= 0):
           if isinstance(fin, int) and(fin > 0):

               num= str(num)
               if ini>= len (num) or fin >= len(num):
                   return  "Indices fuera del rango del número"
                                           
               else:
                   resultado=(num[ini:fin+1])
                   return int(resultado)
           else:
                return "el final deber ser entero mayor a cero"
       else:
            return " El inicio debe ser un numero entero mayor o igual a cero"
    else:
        return " El numero debe ser un numero entero mayor a cero"

def textoPalindromo(texto):
    if isinstance(texto,str):
        if texto != "":

            texto = texto.lower().replace("","")
            if texto== texto[::-1]:
                return True
            else:
                return False
        else:
            return "Error el texto no debe ser vacio"
    else:
        return " Error: ingrese un texto"

def multiplicarElementosLista(lista):
    resultado=1

    if lista != []:
        for pares in (lista):
            if isinstance (pares,int):
                if pares % 2 == 0:
                    resultado*= pares
        return resultado    
                   
    else:
        return "Error: lista no debe ser vacia"

    
    
                
           
    

    
    
    
        
        
        




