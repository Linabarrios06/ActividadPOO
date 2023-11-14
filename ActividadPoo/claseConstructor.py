# Definición de la clase Materia

class materia1: #CLASS es una clase  
    
    # Método especial __init__ que se llama al crear una nueva instancia
    
    def __init__(self, codigo, nombre, nivel): #DEF ss una palabra reservada que indica a Python que una nueva función está siendo definida
        
        # Inicialización de los atributos de la instancia con los valores proporcionados
        
        self.codigo = codigo #SELF. es una convención que se utiliza como nombre para el primer parámetro de un método en una clase
        self.nombre = nombre #SELF. es hacer referencia al objeto que se está manipulando cuando se llama al método
        self.nivel  = nivel 
 
    # Método para imprimir la información de la materia 
    def imprimir_Informacion(self):
        print(self.codigo, self.nombre, self.nivel)

# Creación de una instancia de la clase Estudiante1 llamada adso1
transversal1 = materia1(6, 'Matematicas', 'Avanzado')

# Llamada al método imprimir_Informacion para mostrar la información de la materia
transversal1.imprimir_Informacion()  