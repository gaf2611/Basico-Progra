

#Formula de area de trapecio
"""
Calcular el area del trapecio aplicando la formula
Entrada : Base mayor, Base menor, Altura
Salida: Area del trapecio
Restricciones el numero debe ser entero y mayor a cero
"""



def areaTrapecio ():
    B = float (input ( "ingrese B"));
    b = float (input( "ingrese b"));
    h = float (input("ingrese h"));
    if B >0 and b >0 and h >0:
     area = (B+b)*h/2
     return area
    else:
     return "error"

    #Grupo de poblacion
"""
comprobar el grupo de poblacion
entrada: edad
salida : grupo de poblacion
restricciones: la edad debe ser mayor a 0 o menor a 125

"""

def grupoPoblacion (edad):
    if edad >=0 and edad <= 125 :
         if edad >=0 and edad <=10:
             return "niños"
         if edad > 10 and edad <= 18:
            return "adolescentes"
         if edad > 18 and edad <= 50:
            return "adultos"
         if edad > 50 and edad <= 125 :
            return "Ancianos"
    else:
        return "Es una edad poco probable"




def sonImpares (num):
        while (num > 0):
            numero = num % 10
            numero = numero % 2
            if numero == 0:
                return False
            else:
                num= num // 10
                if num == 0:
                    return True
        



    
 
