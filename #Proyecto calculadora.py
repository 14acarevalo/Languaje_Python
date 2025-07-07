#Proyecto calculadora


def calculadora(num1, num2, operador):
    if operador == "+":
        return num1+num2
    elif operador == "-":
        if num1 >= num2:
            return num1-num2
        else: 
            return "Error: El primer numero tiene que ser igual o mayor que el segundo"
    elif operador == "*":
        return num1*num2
    elif operador == "/":
        if num1 >= num2:
            return num1/num2
        else:
            return "Error: No se puede dividir al ser el segundo número mayor que el primero"
    
operacion_suma = calculadora(10, 5, "+")
operacion_resta_1 = calculadora(10, 5, "-")
operacion_resta_2 = calculadora(10, 20, "-")
operacion_division_1 = calculadora(10, 5, "/")
operacion_division_2 = calculadora(7, 20, "/")
operacion_multiplicacion = calculadora(10, 5, "*")

print("Operación Suma de los dos digitos: ", operacion_suma)
print("Operación Resta 1 de los dos digitos: ", operacion_resta_1)
print("Operación Resta 2 de los dos digitos: ", operacion_resta_2)
print("Operación División 1 de los dos digitos: ", operacion_division_1)
print("Operación División 2 de los dos digitos: ", operacion_division_2)
print("Operación Multiplicación de los dos digitos: ", operacion_multiplicacion)