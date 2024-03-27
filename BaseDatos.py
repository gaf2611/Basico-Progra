vehiculo = []
repuestos = []
mano_obra = []
def guardarDato(archivo,tabla):
    if not isinstance(archivo,str):
        return "Error: Tipo de parámetro no es texto."
    archivoDato = open(archivo)
    linea = archivo.readlines()
    for linea in tabla:
            
            for elemento in linea:
                file.write( str(elemento)+ ','  )
            file.write('\n')
    archivo.close()
"""""   
def cargarDato(archivo,tabla):

def tablaMostrar(tabla):
    for linea in tabla:
        print(linea)

#FUNCIONES DE ADMINISTRADOR
def tipoVehiculo():
    print("Porfavor elija una opción:")
    print("")
def repuesto():

def manoObra():

def mantenimiento():

def reparaciones():

def facturar():

#FUNCIONES DE CONSULTA
def planesM():

def genReservacion():

def cancelReservacion():

def consulReparacion():

def consulFacturacion():