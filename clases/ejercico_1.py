# 🧪 EJERCICIO 1 (para ti)
#Crea una clase llamada Coche.
#Que tenga los atributos: marca y año.
#Que tenga un método mostrar_info que imprima:
#"Este coche es un [marca] del año [año]".
#Luego, crea un coche con los datos que tú quieras y llama al método mostrar_info().



class Coche:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
        
    def mostrar_info(self):
        return f"Este coche es un {self.marca} del año {self.año}."
    
mi_coche = Coche ("Kia", 2025)
print(mi_coche.mostrar_info())

#🧠 PASO 2: Añadir comportamiento dinámico
#Vamos a añadir: Un atributo nuevo llamado encendido, que será False al principio.
#Un método arrancar() que cambie encendido a True.
#Un método detener() que cambie encendido a False.
#Un método estado() que diga si el coche está encendido o apagado.

class Coche1:
    def __init__(self, marca, año, encendido=False):
        self.marca = marca
        self.año = año
        self.encendido = encendido
        
    def mostrar_info(self):
        return f"Este coche es un {self.marca} del año {self.año}."
    
    
    
    def arrancar(self):
        self.encendido = True
        return f"El coche {self.marca} ha arrancado."
    
    def detener(self):
        self.encendido = False
        return f"El coche {self.marca} se ha detenido."
    
    def estado(self):
        if self.encendido:
            return f"El coche {self.marca} está encendido."
        else:
            return f"El coche {self.marca} está apagado."
    
mi_coche = Coche ("Kia", 2025)
print(mi_coche.mostrar_info())

mi_coche1 = Coche1("Opel", 1997)
print(mi_coche1.mostrar_info())
print(mi_coche1.arrancar())
print(mi_coche1.estado())
print(mi_coche1.detener())
print(mi_coche1.estado())


#🧠 PASO 3: Añadir velocidad, acelerar y frenar
#Nuevos elementos:
#Atributo velocidad, que empieza en 0.
#Método acelerar(cantidad) → suma a la velocidad si el coche está encendido.
#Método frenar(cantidad) → resta a la velocidad sin bajar de 0.
#Método mostrar_velocidad() → muestra la velocidad actual.

class Coche2:
    
    def __init__(self, marca, año, encendido = False, velocidad=0):
        self.marca = marca
        self.año = año
        self.encendido = encendido
        self.velocidad = velocidad
    
    def mostrar_info(self):
        return f"Este coche es un {self.marca} del año {self.año}."
    
       
    def arrancar(self):
        self.encendido = True
        return f"El coche {self.marca} ha arrancado."
    
    def detener(self):
        self.encendido = False
        return f"El coche {self.marca} se ha detenido."
    
    def estado(self):
        if self.encendido:
            return f"El coche {self.marca} está encendido."
        else:
            return f"El coche {self.marca} está apagado."
        
    def acelerar(self, cantidad):
        if self.encendido:
            self.velocidad += cantidad
            return f"El coche {self.marca} ha acelerado a {self.velocidad} km/h."
        else:
            self.velocidad = 0
            return f"El coche {self.marca} está apagado, no puede acelerar."
        
    def frenar(self,cantidad):
        if self.velocidad - cantidad < 0:
            self.velocidad = 0
        else:
            self.velocidad -= cantidad
        return f"El coche {self.marca} ha frenado a {self.velocidad} km/h."
        

    def mostrar_velocidad(self):
        return f"La velocidad actual del coche {self.marca} es {self.velocidad} km/h."
    
mi_coche3 = Coche2("Ford", 2020)
print(mi_coche3.mostrar_info())
print(mi_coche3.arrancar())
print(mi_coche3.acelerar(50))
print(mi_coche3.mostrar_velocidad())
print(mi_coche3.frenar(20))
print(mi_coche3.mostrar_velocidad())
