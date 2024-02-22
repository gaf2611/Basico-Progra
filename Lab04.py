def totalizar(archivo: str, valorCol1: str, valorCol2: str) -> str:
        # Abrir el archivo en modo lectura
    with open(archivo, "r") as f:
        # Inicializar las variables
        total = 0
        encontrado = False

        # Leer el archivo línea por línea
        for linea in f:
            # Separar la línea por comas
            datos = linea.strip().split(",")
            # Si los datos coinciden con los parámetros de entrada
            if datos[0] == valorCol1 and datos[1] == valorCol2:
                # Sumar el valor de la tercera columna
                total += float(datos[2])
                encontrado = True

        # Si se encontraron datos para totalizar, devolver el resultado
        if encontrado:
            return f"Total para {valorCol1.capitalize()} por concepto de {valorCol2.capitalize()} es: {total} colones"
        else:
            return f"No se encontraron datos para {valorCol1.capitalize()} y {valorCol2.capitalize()}"


import Lab04

Lab04.totalizar("archivo1.txt", "lunes", "comida")
