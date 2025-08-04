class Coche:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
        self.encendido = False
        self.velocidad = 0
        self.combustible = 100
        self.marcha_actual = 'P'
        self.limites_marcha = {
            'P': 0,
            'N': 0,
            'R': 20,
            '1': 30,
            '2': 50,
            '3': 70,
            '4': 90,
            '5': 120    
        }

    def caracteristicas(self):
        return f"Este coche es un {self.marca} del año {self.año}."

    def arrancar(self):
        if self.combustible > 0:
            self.encendido = True
            return f"El coche {self.marca} ha arrancado."
        else:
            return "No hay combustible suficiente para arrancar el coche."

    def acelerar(self, cantidad):
        if not self.encendido:
            return "No puedes acelerar, el coche está apagado."
        if self.combustible <= 0:
            return "No puedes acelerar, no hay combustible."
        if self.marcha_actual in ['P', 'N']:
            return f"No puedes acelerar en marcha {self.marcha_actual}."

        limite = self.limites_marcha[self.marcha_actual]
        nueva_velocidad = self.velocidad + cantidad
        if nueva_velocidad > limite:
            self.velocidad = limite
            mensaje = f"Has alcanzado el límite de velocidad para la marcha {self.marcha_actual}."
        else:
            self.velocidad = nueva_velocidad
            mensaje = f"Acelerando a {self.velocidad} km/h."

        self.combustible -= cantidad * 0.1
        if self.combustible < 0:
            self.combustible = 0
            self.encendido = False
            mensaje += " El coche se ha apagado por falta de combustible."

        return mensaje + f" Combustible restante: {self.combustible:.1f} l"

    def frenar(self):
        if not self.encendido:
            return "No puedes frenar, el coche está apagado."
        if self.velocidad <= 0:
            return f"El coche {self.marca} ya está detenido."
        self.velocidad = 0
        return f"El coche {self.marca} ha frenado y se ha detenido."

    def marcha_atras(self):
        if not self.encendido:
            return "No puedes ir marcha atrás, el coche está apagado."
        if self.marcha_actual != 'R':
            return f"No puedes ir marcha atrás, estás en marcha {self.marcha_actual}."
        if self.velocidad > 0:
            return f"No puedes ir marcha atrás, el coche se está moviendo a {self.velocidad} km/h."
        if self.combustible <= 0:
            return "No puedes ir marcha atrás, el coche no tiene combustible."
        self.velocidad = 0
        return f"El coche {self.marca} se ha detenido y va en marcha atrás."

    def cambiar_marcha(self, nueva_marcha):
        if self.velocidad > 0:
            return "No puedes cambiar de marcha mientras el coche está en movimiento."
        if nueva_marcha in self.limites_marcha:
            self.marcha_actual = nueva_marcha
            return f"Marcha cambiada a {nueva_marcha}."
        else:
            return "Marcha no válida."

    def deposito_combustible(self, cantidad):
        if self.combustible + cantidad > 100:
            return f"No puedes añadir {cantidad} l. El depósito solo admite hasta 100 l."
        else:
            self.combustible += cantidad
            return f"Has añadido {cantidad} l. Combustible actual: {self.combustible:.1f} l"

    def mostrar_info(self):
        return (f"Marca: {self.marca}, Año: {self.año}, Velocidad: {self.velocidad} km/h, "
                f"Marcha: {self.marcha_actual}, Combustible: {self.combustible:.1f} l, "
                f"Encendido: {'Sí' if self.encendido else 'No'}")
