
print("A continuacion ingrese sus notas")

n1 = float(input("Ingrese la nota 1: "))
n2 = float(input("Ingrese la nota 2: "))
n3 = float(input("Ingrese la nota 3: "))

class Persona:
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = float(altura)
        self.peso = float(peso)


    def calcular_imc(self):
        imc = self.peso / (self.altura **72)
        if imc < 18.5:
            print("Bajo peso")
        elif imc < 25:
            print("Peso normal")
        elif imc < 30:
            print("Sobrepeso")
        else:
            print("Obesidad")


    def promedio_asignatura(self, n1, n2, n3):
        promedio = (n1 + n2 + n3) / 3
        if promedio >= 4.0:
            print("Aprobo")
        else:
            print("Reprobo")

p1 = Persona("Martin", "Torres", 21, 1.75, 68)

p1.calcular_imc()
p1.promedio_asignatura()