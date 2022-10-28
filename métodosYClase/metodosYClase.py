class Dino:
    encendido = False
    def enciende():
        pass
d = Dino()
#La variable d contiene todos los métodos de la clase Dino
print(d.encendido)
d.encendido = True
print(d.encendido)
#------#
print()
print("Uso de la palabra reservada self")
class Dino:
    apagado = False
    def enciende(self):
        self.apagado = True
d = Dino()
print(d.apagado)
d.enciende()
print(d.apagado)
#------#
class Juguete:
    _encendido = True
    def enciende(self):
        self._encendido = True
    def apaga(self):
        self._encendido = False
    def isEncendido(self):
        return self._encendido
class Potato:
    _encendido = True
    def enciende(self):
        self._encendido = True
    def apaga(self):
        self._encendido = False
    def isEncendido(self):
        return self._encendido   
    def quitarOreja(self):
        pass   
    def ponerOreja(self):
        pass      
class Dino:
    _encendido = True
    def enciende(self):
        self._encendido = True
    def apaga(self):
        self._encendido = False
    def isEncendido(self):
        return self._encendido    
    def verEscamas(self):
        return self._encendido   
p = Dino()
p.enciende()
print(p.isEncendido())               
#---#
class Juguete1:
    _encendido = True
    def enciende(self):
        self._encendido = True
    def apaga(self):
        self._encendido = False
    def isEncendido(self):
        return self._encendido
class Potato1(Juguete1): 
    def quitarOreja(self):
        pass   
    def ponerOreja(self):
        pass      
class Dino1(Juguete1):  
    def verEscamas(self):
        return self._encendido             
p = Dino1()
p.enciende()
print(p.isEncendido())    
#------#
print()
print("Ver las propiedades y métodos de una clase") 
print(dir(p))    
#------#
print()
print("Constructor")
class Agua:
    def __init__(self, nombre):
        print("Estoy en el constructor", nombre)
a = Agua("Fría") 
#---#
class Persona():
    color = None
    nombre = None
    def __init__(self, nombre):
        self.color = "Verde"
        self.nombre = nombre
        print("Estoy en el constructor de la clase Persona()")
a = Persona("Giuliano")   
print(a.nombre)
print(a.color)  
#------#
print()
print("Ejecutar el constructor de una clase padre")
class Persona2:
    color = None
    nombre = None
    def __init__(self):
        print("Estoy en el constructor de la clase Persona2()")
class Carro(Persona2):
    color = None
    nombre = None
    def __init__(self, nombre):
        super().__init__()
        print("Estoy en el constructor de la clase Carro()")
d = Carro('Ferrari')
#------#
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
    def diHola(self):
        print("Hola")
class Perro(Animal):
    def sonido(self):
        print("Guau")   
class Gato(Animal):
    def sonido(self):
        print("Miau")    
p = Perro()
p.sonido()
p.diHola()
m = Gato()
m.sonido() 
m.diHola()
#------#
class Motor:
    tipo = "Diesel"
class Ventanas:
    cantidad = 5
    def cambiarCantidad(self, valor):
        self.cantidad = valor
class Ruedas:
    cantidad = 4
class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()
class Coche:
    motor = Motor()
    carroceria = Carroceria()
c = Coche()
print("Motor es ", c.motor.tipo)    
print("Ventanas: ",c.carroceria.ventanas.cantidad)    
c.carroceria.ventanas.cambiarCantidad(2)
print("Ventanas: ",c.carroceria.ventanas.cantidad)     
#------#
class Categorias:
    idCategoria = 0
    nombre = ""
class Proveedores:
    idProveedor = 0
    nombre = 0
class Productos:
    idProducto = 0
    categoriaDeProducto = Categorias()
    precio = 0
    tamaño = 0
    tipoDeProducto = 0
    cifProveedor = Proveedores()      
p = Productos()
p.cifProveedor.nombre                    