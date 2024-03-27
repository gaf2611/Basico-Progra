import os
vehiculo = []
repuestos = []
mano_obra = []
mantenimiento = []
def guardarDato(archivo,tabla):
    if not isinstance(archivo,str):
        return "Error: Tipo de parámetro no es texto."
    if (archivo == ""):
        return "Error: El nombre del archivo no debe ser vacio"

    if not os.path.exists(archivo):

        return f"Error: El archivo '{archivo}' no existe"
    abrir = open(archivo, encoding= "utf-8", mode= "w")

    for fila in tabla:
            
            for elemento in fila:
                archivo.write( str(elemento)+ ','  )
            archivo.write('\n')
    archivo.close()
  
def cargarDato(archivo,tabla):
    if not isinstance(archivo,str):
        return "Error: Tipo de parámetro no es texto."
    if (archivo == ""):
        return "Error: El nombre del archivo no debe ser vacio"
    if not os.path.exists(archivo):
        return f"Error: El archivo '{archivo}' no existe"
      
    abrir = open(archivo, encoding = "utf-8", mode = "r")
    for linea in abrir:
        fila  = linea.split(",")
        fila = fila[:-1]
        tabla += fila
        tabla.write(fila)

def tablaMostrar(tabla):
    for linea in tabla:
        print(linea)
###########################
#FUNCIONES DE ADMINISTRADOR
###########################       
#1: Primero guardo el dato de vehiculo
def guardarTipoVehiculo():
    guardarDato("gestion",vehiculo)
#2 Muestro el dato guardado de vehiculo en la tabla
def mostrarTipoVehiculo():
    tablaMostrar(vehiculo)
# 3 Se repite el proceso con todas las funciones
def guardarRepuesto():
    guardarDato("gestion",repuestos)
def mostrarRepuesto():
    tablaMostrar(repuestos)

def guardarManoObra():
    guardarDato("gestion",mano_obra)
    
def guardarMantenimiento():
    guardarDato("gestion",mantenimiento)
def mostrarMantenimiento():
    tablaMostrar(mantenimiento)

#def reparaciones():

#def facturar():

#FUNCIONES DE CONSULTA
#def planesM():

#def genReservacion():

#def cancelReservacion():

#def consulReparacion():

#def consulFacturacion():

#agregar 
def agregarVehiculo():
    tipoVehiculo = input(str("Ingrese el tipo de vehÍculo:"))
    marcaVehiculo = input(str ("Ingrese la marca del vehículo:"))
    cantPasajeros =input (str("Ingrese la cantidad de pasajeros del vehículo:"))
    cantEjes = input(str("Ingrese la cantidad de ejes del vehículo:"))
    infoVehiculo = [tipoVehiculo, marcaVehiculo, cantPasajeros, cantEjes]
    vehiculo.write(infoVehiculo)
    guardarTipoVehiculo()
    print("¡El Vehículo ha sido guardado exitosamente!")

def agregarRepuesto():
    nombre = input(str("Ingrese el nombre del repuesto:"))
    costoCompra = input(str ("Ingrese el costo del repuesto:"))
    precioVenta =input(str("Ingrese el precio de venta para el repuesto:"))
    infoRepuesto = [nombre, costoCompra, precioVenta]
    repuestos.write(infoRepuesto)
    guardarRepuesto()
    print("¡El repuesto ha sido guardado exitosamente!")

def agregarManoObra():
    nombreM = input(str("Ingrese el nombre del mecánico a cargo del vehículo:"))
    tiempo = input(int("Ingrese el tiempo estimado de ejecución:"))
    precio = input(int("Ingrese el precio final de mano de obra:"))
    infoManoObra = [nombreM, tiempo, precio]
    mano_obra.write(infoManoObra)
    guardarManoObra()
def agregarMantenimiento():
    nombreMantenimiento = input(str("Ingrese el tipo de mantenimiento que desea realizar:"))
    tipoVehiculo = input("Elija el tipo de vehiculo", vehiculo)
    precioServicio = input("agregue el precio del servicio a cobrar:")
