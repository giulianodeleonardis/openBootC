import pickle
class Juguete:
    nombre = ''
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre

j1 = Juguete('Potato', 10.5)
print(type(j1))
print(j1.getNombre())

f = open('datos.bin', 'wb')
pickle.dump(j1, f)
f.close()