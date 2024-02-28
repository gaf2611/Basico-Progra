"""
Nombre: division_v1
Entrada: No tiene, por input
Salida: Retorna la division entre dos numeros
        retornar si es exacta la division o si tiene residuo
Restricción: Numero debe ser positivo
"""
def division_v1():
            
            dividendo = input("Ingrese el valor del dividendo:")
            if dividendo == "":
                return "Error: Digite valores numéricos"
            try:
                dvidendo = int(dividendo)
            except:
                return "Error: No se puede convertir dividendo a numero"
            
            divisor = input("Ingrese el valor del divisor:")
            if divisor == "":
               return "Error: Digite valores numéricos"
            try:
                divisor = int(divisor)
            except:
                return "Error: No se puede convertir divisor a numero"
            cociente = dividendo // divisor
            residuo = dividendo % divisor
            if residuo == 0:
                print ("La división es exacta, el cociente es" + str(cociente))
            else:
                print("La division no es exacta, el cociente es: \n" + str(cociente)+ "\n" "y residuo:\n"+ str(residuo)) 
            
def division_v2():
    dividendo = int(input("Ingrese el valor del dividendo:"))
    if dividendo == "":
        return "Error: Digite valores numéricos"
    if dividendo == 0:
        return "Error: No se puede dividir por cero"

    divisor = int(input("Ingrese el valor del divisor:"))
    if divisor == "":
        return "Error: Digite valores numéricos"
    if divisor == 0:
        return "Error: No se puede dividir por cero"
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    if residuo == 0:
        print ("La división es exacta, el cociente es" + str(cociente))
    else:
        print("La division no es exacta, el cociente es: \n" + str(cociente)+ "\n" "y residuo:\n"+ str(residuo))
