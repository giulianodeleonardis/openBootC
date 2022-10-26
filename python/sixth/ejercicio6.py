class Vehiculo:
    color = "Azul"
    ruedas = 4
    puertas = 5
class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 4.0
coche = Coche()
print("El coche es de color:", coche.color)
print("El coche tiene ", coche.ruedas, "ruedas")
print("El coche tiene ", coche.puertas, "puertas")
print("El coche tiene una velocidad máxima de:", coche.velocidad)
print("El coche tiene una cilindrada de:", coche.cilindrada, "litros")