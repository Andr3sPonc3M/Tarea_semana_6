# Tarea Semana 6.
# Clases, objetos, herencia, encapsulamiento y polimorfismo.

# definición de la clase Animal.
class Animal:
    # Clase base para representar un animal.
    def __init__(self, nombre, edad):
        # Inicializa un nuevo objeto Animal.
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        # Método para representar el sonido de un animal.
        return "Sonido de animal"

# definición de la clase gato que es herencia de animal.
class Gato(Animal):
    # Clase que representa un gato heredado de animal.
    def hablar(self):
        # Método de hablar para gatos.
        return "Miau"

# Polimorfismo.
def hacer_hablar(animal):
    # Función de polimirfismo para hacer que gato hable.
    print(animal.hablar())

# Creación de instancias de las clases.
gato = Gato("Yube", 3)

# Llamada de los métodos y demostrar la funcionalidad.
print(f"Nombre del gato: {gato.nombre}")
print(f"Edad del gato: {gato.edad}")
print(f"Como habla el gato: {gato.hablar()}")

print("\nEjemplo de Polimorfismo:")
hacer_hablar(gato)
# Llama al método hablar del objeto gato

# Fin del programa.

# Andrés Ponce M.