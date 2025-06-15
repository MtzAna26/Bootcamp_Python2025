class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, {self.nombre}, tiene {self.edad} años")

p1 = Persona('Ana', 22)
p1.saludar()

p2 = Persona('Juan', 30)
p2.saludar()


#Ejemplo 2.
class Cafetera:
    def __init__(self, marca, capacidad):
        self.marca =  marca
        self.capacidad = capacidad
    def servir_cafe(self):
        print("Sirviendo café caliente☕")
mi_cafetera = Cafetera("Oster", 1.5)
print(mi_cafetera.marca)
mi_cafetera.servir_cafe()
print()
mi_cafetera2 = Cafetera("BD", 2.0)
print(mi_cafetera2.capacidad)
print()

#Ejemplo 3
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

r = Rectangulo(4, 5)
print("Área del rectángulo:", r.area())
