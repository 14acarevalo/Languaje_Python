#Programa para prácticar las funciones con Python

#Crear una funcion para realizar un saludo

def saludar(nombre):
    
    print("Hola " + nombre + " ¿Como estas?")
    
#Llamamos a la función
saludar("Alberto")

##Función para realizar una operación

def operacion(num1, num2):
    suma = num1 + num2
    multiplicacion = num1 * num2
    promedio = (num1 + num2) / 2

    if num1 > num2:
        resta = num1 - num2
        division = num1 / num2
    else:
        resta = None
        division = None
        mensaje = "El primer número debe ser mayor que el segundo para hacer la resta y división."

    # Usamos f-strings para construir el resultado
    resultado = (
        f"Suma: {suma}\n"
        f"Multiplicación: {multiplicacion}\n"
        f"Promedio: {promedio}\n"
    )

    if resta is not None and division is not None:
        resultado += f"Resta: {resta}\n"
        resultado += f"División: {division}\n"
    else:
        resultado += mensaje

    return resultado


# Llamamos a la función
resultado = operacion(10, 5)
print("El resultado de la operación es:\n" + resultado)

#Operaciones con numeros complejos

def analizar_numeros(num1, num2):
    if (num1 > num2):
        num1Mayor = f"El primer numero {num1} es mayor que el segundo numero {num2}"
    elif (num1 < num2):
         num2Mayor = f"El segundo número, {num2} es mayor que el primero, {num1}"
         
    suma = num1 + num2
    multiplicacion= num1 * num2
    promedio = (num1 + num2) / 2
    
    if num1 > num2:
        resta = num1 - num2
        division = num1 / num2
    else:
        resta = None
        division = None
        mensaje = "El primer número debe ser mayor que el segundo para hacer la resta y división."
        
    resultado = (
        f"Suma: {suma}\n"
        f"Multiplicación: {multiplicacion}\n"
        f"Promedio: {promedio}\n"
        f"{num1Mayor if 'num1Mayor' in locals() else num2Mayor}\n"
        f"{mensaje if 'mensaje' in locals() else ''}\n"
        f"Resta: {resta if resta is not None else 'No se realizó la resta'}\n"
        f"División: {division if division is not None else 'No se realizó la división'}\n"
    )
    
    return resultado

#Llamamos a la función
operacion = analizar_numeros(11, 6)
print("El resultado de la operación 2 es:\n" + operacion)


#Trabajar con listas
def procesar_lista(lista):
    if not lista:
        return "La lista está vacia"

    else:
        suma = sum(lista)
        promedio= sum(lista)/len(lista)
        mayor = max(lista)
        menor = min(lista)
    
        resultado = (
            f"Suma de los elementos: {suma}\n"
            f"Promedio de los elementos: {promedio}\n"
            f"Mayor elemento: {mayor}\n"
            f"Menor elemento: {menor}\n"
        )
        
        return resultado
    
#Llamamos a la función
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
resultado_lista = procesar_lista(lista_numeros)
print("El resultado de la lista es:\n" + resultado_lista)

#Funcion para saludar a una persona

def saludar_persona(nombre, edad):
    if edad <18:
        return f"Hola {nombre}, eres menor de edad. "
    elif edad >= 18 and edad < 65:
        return f"Hola {nombre}, eres mayor de edad."
    else:
        return f"Hola {nombre}, eres un jubilado ya."
    
resultado_saludo = saludar_persona("Alberto", 31)
print(resultado_saludo)
    

    