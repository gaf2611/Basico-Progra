"""
Nombre: contarCaracteres
Entrada: Archivo.
Salida: Debe retornar la cantidad de caracteres en el archivo.
Restricción: El parámetro de entrada debe ser STRING y debe ser diferente de VACÍO.
"""

def contarCaracteres(nombreArchivo):
    if not isinstance(nombreArchivo, str):
        return "Error: Tipo de parámetro no es texto."
    if (nombreArchivo == ""):
        return "Error: El nombre del archivo debe ser diferente a vacío."
    archivo = open(nombreArchivo)
    linea = archivo.read()
    contador = 0
    for caracter in linea:
        contador+=1
    archivo.close
    print("Total Caracteres",(contador))
"""
Nombre: contarCaracteresAvanzado
Entrada: Archivo,Caracter.
Salida: Debe retornar la cantidad de caracteres que hay dentro del archivo
        MENOS el caracter que se indica en el parámetro de entrada.
Restricción: Ambos parámetros deben ser STRING y diferentes de VACÍO.

"""

def contarCaracteresAvanzado(nombreArchivo,caracter):
     if not isinstance(nombreArchivo, str) and isinstance (caracter,str):
        return "Error: Los parámetros DEBEN ser STRING."
     if (nombreArchivo == ""):
        return "Error: El nombre de archivo y caracter deben ser diferentes a vacío."
     archivo = open(nombreArchivo)
     linea = archivo.readline()
     contador = 0
     for letra in linea:
         if caracter != letra:
            contador+=1
     archivo.close
     print ("Total De Caracteres",(contador))    
"""
Nombre: existePalabras
Entrada: Archivo, Caracter o Palabra
Salida: Debe retornar la cantidad de palabras o caracteres que hay
        dentro del archivo.
Restricción: Ambos parámetros deben ser STRING y diferentes de VACÍO.
"""
def existePalabras(nombreArchivo,C_P):
    if not isinstance(nombreArchivo, str) and isinstance (caracter,str):
        return "Error: Los parámetros DEBEN ser STRING."
    if (nombreArchivo == ""):
        return "Error: El nombre de archivo y caracter o palabra deben ser diferentes a vacío."
    archivo = open(nombreArchivo)
    linea = archivo.readline()
    contador = 0
    for letra in linea:
        if C_P == letra:
            contador+=1
    archivo.close
    print("Total Palabras:",(contador)
