"""
Los cuatro pilares de la Programación Orientada a Objetos
Aplicando los principios de:
1. Abstracción
2. Encapsulamiento
3. Herencia
4. Polimorfismo
"""

# Abstracción.
# Consiste en mostrar los detalles esenciales de un objeto, 
# ocultando su complejidad interna.

print ("Ejemplo de Abstracción");
class Cafetera:
    def encender(self):
        print("Cafetera encendida")
    def preparar_cafe(self):
        print("Preparando cafe")
cafetera = Cafetera()
cafetera.preparar_cafe()
print()

# Encapsulamiento
"""
Es el principio de ocultar datos internos y proteger el 
estado del objeto. Se logra restringiendo el acceso a 
ciertos atributos/métodos.
"""

# Convenciones en Python
"""
_atributo: Atributo "protegido" uso interno (por convención).
__atributo: Nombre manipulado (name mangling), más protegido.
"""

print("Ejemplo. Encapsulamiento")
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo # ENCAPSULAMIENTO
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
    def obtener_saldo(self):
        return self.__saldo
cuenta = CuentaBancaria("Ana Mariia", 1000)
cuenta.depositar(500)
print(cuenta.obtener_saldo())
##print(cuenta._saldo)
print(cuenta.titular)
print()

# Herencia 
"""
La herencia es un mecanismo que permite a una 
clase hija (subclase) heredar los atributos y métodos de una
clase padre (superclase).
"""
print("Ejemplo Herencia")
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print("El animal hace un sonido")
class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice ¡Guau!")
class Gato(Animal):
    def hablar(self):
       print(f'{self.nombre} dice ¡Miau!')
class Cangrejo(Animal):
    pass
p = Perro("Lassie")
p.hablar()
print()

g = Gato("Cata")
g.hablar()
print()
c = Cangrejo("Nemo")
c.hablar()
print()

# Polimorfismo
"""
Capacidad de usar el mismo método en diferentes objetos 
y obtener comportamiento distintos.
"""
print("Ejemplo Polimorfismo")
class Gato:
    def hablar(self):
        print("Miau")
class Perro:
    def hablar(self):
        print('Guau')

# Polimorfismo
animales = [Gato(), Perro()]
for animal in animales:
    animal.hablar()
print()