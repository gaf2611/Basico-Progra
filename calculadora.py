def suma():
    a= int(input("DIGITE UN VALOR PARA a:\t"))
    
    b= int(input("DIGITE EL VALOR DE b:\t"))
    print (a+b)
    
def resta():
    a= int(input("DIGITE UN VALOR PARA a:\t"))
    
    b= int(input("DIGITE EL VALOR DE b:\t"))
    print (a-b)
def multiplicacion():
    a= int(input("DIGITE UN VALOR PARA a:\t"))
    
    b= int(input("DIGITE EL VALOR DE b:\t"))
    resultado = 0 
    for numero in range(b):
        resultado += b
    print(resultado)
        
def division():
    a= int(input("DIGITE UN VALOR PARA EL DIVIDENDO:\t"))
    
    b= int(input("DIGITE EL VALOR EL DIVISOR:\t"))
    if b != 0:
        print (a/b)
    else:
         print("Numero no se puede dividir por CERO")
        
def potencia():
    a= int(input("DIGITE UN VALOR PARA a:\t"))
    
    b= int(input("DIGITE EL VALOR DE b:\t"))
    print (a**b)
def factorial():
    a = int(input("INSERTE UN NUMERO:\t")) 
    r=1
    for n in range(1,a+1):
        r*= n
        print(r)

def calculadora():
    print("===================")
    print ("CALCULADORA MASTER")
    print("===================")
    print ("\n")
    print ("OPCIONES:")
    print ("1. SUMA")
    print ("2. RESTA")
    print ("3. MULTIPLICACIÓN")
    print ("4. DIVISIÓN")
    print ("5. POTENCIA")
    print ("6. FACTORIAL")
    
    opcion = int(input ("DIGITE EL NÚMERO DE UNA DE LAS OPCIONES:"))
    if opcion == 1:
        suma()
        return calculadora()
    elif opcion == 2:
        resta()
        return calculadora()
    elif opcion == 3:
        multiplicacion()
        return calculadora()
    elif opcion == 4:
        division()
        return calculadora()
    elif opcion == 5:
        potencia()
        return calculadora()
    elif opcion == 6:
        factorial()
        return calculadora()
    
        
