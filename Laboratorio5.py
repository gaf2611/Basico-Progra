"""
Nombre: sumaImparesPares
Entrada: lista1,lista2
Salida:una lista que contenga la suma de las posiciones pares de las dos listas
 de la misma manera con las posiciones impares
Restricciones:

"""


def sumaImparesPares(lista1, lista2):
    pares = 0
    impares = 0
    posicion=0
    if not isinstance (lista2,str):
        for valor in lista1:
            if posicion % 2 == 0:
                pares += lista1[0]
            else:
                impares += lista1[0]
            lista1=lista1[1:]
            posicion +=1

            
        
        for valor in lista2:
           if posicion % 2 == 0:
               pares += lista2[0]
           else:
               impares += lista2[0]
           lista2=lista2[1:]
           posicion +=1

       
        return [pares,impares]
    else:
        return"Error: segundo argumento debe ser entero"

"""
Nombre: eliminarElemento
Entrada:lista,elemento
Salida: devuelve una lista eliminando los valores iguales a elmento
Restricciones:

"""
def eliminarElemento(lista, elemento):
    nueva_lista = []
    for elem in lista:
        if elem != elemento:
            nueva_lista += [elem]
    return nueva_lista




"""
Nombre: eliminarRepetidos
Entrada: lista1,lista2
Salida:evuelve una lista eliminando los valores iguales a lista2
Restricciones

"""

def eliminarRepetidos(lista1, lista2):

    for valor in lista2:
        lista1= eliminarElemento(lista1,valor)

    return lista1












