#import BaseDatos
import datetime
def inicio():
    while True:
        print("TALLER MECANICO GAF")
        print(" Elija una opción: ")
        print("1. Opciones Administrativas.")
        print("2. Consultas Técnicas. ")
        print("3. Salir. ")
        
        opcion = input("Selecciona una opción: ")
        if (opcion == "1"):
            menuAdmin()
        elif (opcion == "2"):
            menuConsulta()
        elif (opcion == "3"):
            break    
        else:
            print("Error: ¡Opción ingresada no existe! Ingrese una opción válida.")

    
def menuAdmin():
    while True:
        usuarioI = "TMG26"
        passwordI = "1234"
        print("Bienvenido! Primero ingresa tus datos.")
        print ("Digite el usuario: ")
        usuario = input()
        print("Digite la contraseña: ")
        password = input()
        if (usuario == usuarioI) and (password == passwordI):
            print("Has ingresado exitosamente al menú TMG ¡BIENVENIDO!") 

            print("Seleccione una de las opciones:")
            opcion = input ("Digite una opción: ")

            print("1. Tipo De Vehículo ")
            print("2. Repuestos ")
            print("3. Mano De Obra ")
            print("4. Mantenimiento ")
            print("5. Reparaciones ")
            print("6. Facturar ")
            print("7. Salir ")
    

            if  (opcion == "1"):
                BaseDatos.tipoVehiculo()
            elif(opcion == "2"):
                BaseDatos.repuesto()
            elif(opcion == "3"):
                BaseDatos.manoObra()
            elif(opcion == "4"):
                BaseDatos.mantenimiento()
            elif(opcion == "5"):
                BaseDatos.reparaciones()
            elif(opcion == "6"):
                BaseDatos.facturar()
            elif(opcion == "7"):
                break
            else: 
                print ("¡Opción ingresada no valida! Ingrese un dato válido")        
        else:   
            print ("¡Usuario o contraseña no válido! Vuelva a ingresar los datos.")
def menuConsulta():
    while True:
        print("Bienvenido(a) al menú de consultas técnicas")
        print("Elija una de las opciones: ")
        print("1. Planes De Mantenimiento. ")
        print("2. Generar Reservación. ")
        print("3. Cancelar Reservación. ")
        print("4. consulta Reparación. ")
        print("5. consulta Facturación. ")
        print("6. Salir. ")
        opcion = input("Seleccione una opción:")
        if  (opcion == "1"):
            BaseDatos.planesM()
        elif(opcion == "2"):
            BaseDatos.genReservacion()
        elif(opcion == "3"):
            BaseDatos.cancelReservacion()
        elif(opcion == "4"):
            BaseDatos.consulReparacion()
        elif(opcion == "5"):
            BaseDatos.consulFacturacion()
        elif(opcion == "6"):
            break
        else:
            print("¡Opción NO es válida! ingrese de nuevo una opción.")
    
inicio()   


    