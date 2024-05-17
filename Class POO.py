class Rectangulo:
    def __init__(self, alto, ancho):
        
        self.alto = alto
        self.ancho = ancho
        
    def calcularArea(self):
        return (alto*ancho)
    def calcularPerimetro(self):
        return (2*alto) + (2*ancho)
    def verAlto(self):
        return self.alto
    def verAncho(self):
        return self.ancho
    
class Calculadora:
    def __init__(self,operador1,operador2):
        if not isinstance(operador1,int) and (operador2,int):
            return "Error los operadores deben ser enteros."
        self.operador1 = operador1
        self.operador2 = operador2
    def suma(self):
        return self.operador1 + self.operador2
    def resta(self):
        return self.operador1 - self.operador2
    def multiplicacion(self):
        return(self.operador1 * self.operador2)
    def division(self):
        return self.operador1 // self.operador2
    def poterncia(self):
        return self.operador1 ** self.operador2
class Facturador:
    def __init__(self):

        self.fecha = ""
        self.nombreCliente = ""
        self.numFactura = 0
        self.totalFactura = 0
        self.totalImpuesto = 0

        self.listaItem = []
    def crearFactura(self,numFactura,fecha,nomCliente):

        self.numFactura = numFactura
        self.fecha = fecha
        self.nombreCliente = nomCliente
        
    def agregarItem(self, producto, precio,cantidad):
        self.listaItem += [[producto,precio,cantidad]]
    def verTotal(self):
         impuesto = 0
         subtotal = 0
         total = 0

         for item in self.listaItem:
             subtotal = item[1] * item[2]
             impuesto = subtotal * 0.13
             total += subtotal + impuesto
             
         self.totalImpuesto = total* 0.13
         self.totalFactura = total
         return self.totalFactura
    
    def cerrarFactura(self):
        return "Total a pagar es de:" + str(self.totalFactura)+ "colones"
