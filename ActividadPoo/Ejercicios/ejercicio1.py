# Ejemplo de clase con atributos y métodos

# Definición de la clase Coche
class Gato:
    # Método especial __init__ para inicializar los atributos al crear una instancia
    def __init__(self, nombre, edad):
        # Inicialización de atributos con los valores proporcionados
        self.nombre = nombre
        self.edad = edad
 
    # Método para encender el coche
    def Ronronear(self):
        print(f'{self.nombre} esta ronroneando .')

    # Método para apagar el coche
        print(f'{self.nombre} ha saltado.')

# Crear una instancia de la clase Coche llamada mi_coche
mi_Gato =Gato('Tommy', '4')

# Usar métodos y acceder a atributos
print(f'Mi gato se llama {mi_Gato.nombre}.')
print(f'Mi gato tiene {mi_Gato.edad} años. ')