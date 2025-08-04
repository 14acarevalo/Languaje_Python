class Persona:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad    
    
    
    def __saludar__(self):
        return f"Hola, me llamo {self.nombre} {self.apellidos} y tengo {self.edad} años"
    


class Evento:
    def __init__ (self, nombre, fecha, lugar, tipo):
        self.nombre = nombre
        self.fecha = fecha
        self.lugar = lugar
        self.tipo = tipo
        
    def __caracteristica__(self):
        return f"El evento {self.nombre} se llevará a cabo en la fecha {self.fecha}, en {self.lugar}, y es de tipo {self.tipo}."

persona1 = Persona("Alberto", "Campanero", 30)
#Ejemplo de como no funciona sin el print
persona1.__saludar__()

actividad = Evento("Concierto de Rock", "2023-10-15", "Estadio Nacional", "Musical")    
#Ejemplo de como no funciona sin el print
actividad.__caracteristica__()


print(persona1.__saludar__()) 
print(actividad.__caracteristica__())

class Informe:
    def __init__ (self, titulo, nombre_encargado, fecha, descripcion, contenido):
        self.titulo = titulo
        self.nombre_encargado = nombre_encargado
        self.fecha = fecha
        self.descripcion = descripcion
        self.contenido = contenido
        
    def __contenido_informe__(self):
        return f"Informe: {self.titulo}\nEncargado: {self.nombre_encargado}\nFecha: {self.fecha}\nDescripción: {self.descripcion}\nContenido: {self.contenido}"
