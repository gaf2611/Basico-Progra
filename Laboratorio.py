class Vehiculo:
    def __init__(self,placa,horaEntrada):

        self.placa = placa
        self.horaEntrada = horaEntrada
        self.listaVehiculos = []
        
      
    
    def mostrar(self):
        
        informacion = "Placa: " + self.placa + ", "
        informacion += "Hora de Entrada: " + self.horaEntrada
        return informacion

class Parqueo:

    def __init__(self,direccion,Nombre,Campos):
        self.direccion = direccion
        self.Nombre = Nombre
        self.Campos = Campos
        self.listaVehiculos = []
       
        
    def datosParqueo(self):
        informacion = "Direccion: " + self.direccion + ", "
        informacion += "Nombre: " + self.Nombre + ","
        informacion += "Campos: " + str(self.Campos)
        
        return informacion

    def agregarVehiculo(self,placa,horaEntrada):
        if not isinstance(placa,str):
            return "Error placa no es String"
        
        if not isinstance(horaEntrada,str):
            return "Error horaEntrada no es String"
        
        if len(self.listaVehiculos )>= self.Campos:
            return "Parqueo lleno"
        
        for plc in self.listaVehiculos:
            if placa == plc.placa:
                return "Error: Placa existente"
            
        vehiculo = Vehiculo(placa,horaEntrada)
        self.listaVehiculos += [vehiculo]
        print("Vehiculo agregado con éxito.")
        
    def quitarVehiculo(self, placa):
        if not isinstance(placa, str):
            return "Error: Debe ser string"
        listaN= []
        for vehiculo in self.listaVehiculos:
            if vehiculo.placa != placa:
                listaN+=[vehiculo]
        self.listaVehiculos = listaN
        return "Vehiculo Borrado"

        
    def totalVehiculos(self):
        resultado=len(self.listaVehiculos)
        return resultado
    
    def mostrarVehiculos(self):
        placas = []
        for vehiculo in self.listaVehiculos:
            placas+=[vehiculo.placa]
        return placas

        
    
    
