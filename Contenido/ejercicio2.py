

class Coche:
    def __init__(self, marca, gasolina):
        self.marca = marca
        self.gasolina = float(gasolina)
        self.kilometros_recorridos = 0

    def conducir(self, km):
        litros_necesarios = km / 10
        if litros_necesarios <= self.gasolina:
            self.kilometros_recorridos += km
            self.gasolina -= litros_necesarios
            print(f"Conduciste {km} km. Gasolina restante: {self.gasolina} L")

        else:
            km_posibles = self.gasolina * 10
            self.kilometros_recorridos += km_posibles
            self.gasolina = 0
            print(f"Solo pudiste conducir {km_posibles} km. Te quedaste sin gasolina.")

    def cargar_gasolina(self, litros):
        self.gasolina += float(litros)
        print(f"Cargaste {litros} L. Gasolina actual: {self.gasolina} L")



# FALTA CREAR OBJETO
coche1 = Coche()
coche2 = Coche()
