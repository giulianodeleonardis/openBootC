
import pickle
class Vehiculo:
    puertas = 0
    motor = 0
    color = ""
    def __init__(self, puertas, motor, color):
        self.puertas = puertas
        self.motor = motor
        self.color = color
a = Vehiculo(5, 4.0, 'Azul')
f = open('vehiculo.bin', 'wb')
pickle.dump(a, f)
f.close()
a1 = Vehiculo(5, 4.0, 'Azul')
f1 = open('vehiculo.bin', 'rb')
obj = pickle.load(f1)
f1.close()
print('Número de puertas:',obj.puertas) 
print('Capacidad del motor:',obj.motor) 
print('Color del vehículo:',obj.color) 


