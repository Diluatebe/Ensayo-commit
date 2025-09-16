def suma (a,b):
    return a+b
def resta (a,b):
    return a-b
def multiplicacion (a,b):
    return a*b
def division (a,b):
    if b!=0:
        return a/b
    else:
        print("Error, división por 0")  
print("CALCULADORA SIMPLE CON HISTORIAL")
operacion=int()
historial=[]  
while operacion<6:
    print("Seleccione una opción para la operación deseada ")
    print("Operaciones disponibles: para suma:1; para resta:2, para multiplicación:3," \
    " para división:4, para ver el historial:5, salir:6")
    operacion = int(input ("Su selección es:"))
    if operacion>=6:
        print("Gracias por usar la calculadora")
        break
    elif operacion==5:
        for item in historial:
            print(item)
    else:
        a=float(input("ingrese primer número:"))
        b=float(input("ingrese segundo número:"))
        
        if operacion==1:
            resultado=suma(a,b)
            print("El resultado de tu operación es:", suma(a,b))
            historial.append(f"{a}+{b}={resultado}")
        elif operacion==2:
            resultado=resta(a,b)
            print ("se restará primer número menos segundo número")
            print("El resultado de tu operación es=", resta(a,b))
            historial.append(f"{a}-{b}={resultado}")
        elif operacion==3:
            resultado=multiplicacion(a,b)
            print("El resultado de tu operación es=", multiplicacion(a,b))
            historial.append(f"{a}*{b}={resultado}")
        else:
            resultado=division(a,b)
            print("Se dividirá el primer número entre el segundo número, el cual debe ser diferente de cero")
            print("El resultado de tu operación es=", division(a,b))
            historial.append(f"{a}/{b}={resultado}")
   
           
         