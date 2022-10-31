#Forma antigua, usando tuplas (hasta la versión 3.6 de Python)
from cgitb import text


numero = 5
texto = "hola"
otroNum = 1.2
# %d, %s y %f son placeholders (un placeholder es una referencia)
# %d significa que va un número, %s un string y %f un float
print("El número es %d y el texto es %s, y tiene %f" %(numero, texto, otroNum))
print()
# Un solo placeholder (no hace falta los paréntesis)
print("El número es %d" %numero)
print()
# Modificar el tamaño de un flotante. En este caso se va a mostrar solo un decimal
print("Elflotante es %.1f" %otroNum)
print()
print("Función FORMAT")
# Format es una propiedad de las strings. Format es un método. 
print("El número es {} y el texto es {}, y tiene {}".format(numero, texto, otroNum))
# Se puede cambiar el orden de los placeholders
print("El número es {} y el texto es {}, y tiene {}".format(otroNum, numero, texto))
print()
print("Colocando número dentro de las llaves")
print("El número es {1} y el texto es {0}, y tiene {2}".format(numero, texto, otroNum))
print()
print("Colocando nombres dentro de las llaves")
# Esta es la manera más habitual
print("El número es {n1} y el texto es {n2}, y tiene {n3}".format(n1 = numero, n2 = texto, n3  = otroNum))
print()
print("La mejor manera de hacerlo hoy en día")
# La mejor manera de hacerlo hoy en día
print(f"El número es {numero} y el texto es {texto}, y tiene {otroNum}")
# La mejor manera de hacerlo hoy en día con manipulación
print(f"El número es {numero} y el texto es {texto.upper()}, y tiene {otroNum}")
# La mejor manera de hacerlo hoy en día con función
def suma(a, b):
    return a + b
print(f"El número es {suma(numero, numero)} y el texto es {texto.upper()}, y tiene {otroNum}")
print()
print("Sobrecarga de método")
# Sin sobrecarga
qty = 156

print(type(str(qty)))

class Juguete:
    nombre = ""
    num = 0
    def __init__(self, nombre, num):
        self.nombre = nombre
        self.num = num
    def __str__(self):
        return f"Mi nombre es {self.nombre} y mi precio es {self.num}"
    def __repr__(self):
        return f"Potato({self.nombre}, {self.num})"
j1 = Juguete("Potato", 10.5)
# Para demostrar que se modifica el método STR
print(j1)
# Sobrecargar el método REPR. Este método muestra la representación interna de un objeto
print(repr(j1))
print()
print("Conocer los métodos para cadenas de texto")
import pprint
pprint.pprint(dir(""))
cadena = "algún lugar en la manchA"
print(cadena.capitalize())
print(cadena.title())
print("La cantidad de a minúscula en el texto es:",cadena.count("a"))
print("La cantidad de a mayúscula en el texto es:",cadena.count("A"))
print(cadena.lower())
print(cadena.upper())
print(cadena.lower().count("a"))

# Para saber si un dato string es un número
print()
print("Para saber si un dato string es un número")
dato = "5"
print(dato.isdigit())

# Para saber si un dato es alfanumérico
print()
print("Para saber si un dato es alfanumérico")
dato = "~"
print(dato.isalnum())

# Para saber si un dato es alfanumérico
print()
print("Para saber si un dato es alfabético")
dato = "1"
print(dato.isalpha())

# Para eliminar espacios al principio y al final de una cadena
print()
print("Para eliminar espacios al principio de una cadena")
data = "                  Para saber si un dato es alfabético             "
print(data)
print(data.strip())

# Para eliminar espacios a la izquierda de una cadena
print()
print("Para eliminar espacios al principio de una cadena")
data = "                  Para saber si un dato es alfabético             "
print(data)
print(data.lstrip())

# Para eliminar espacios a la derecha de una cadena
print()
print("Para eliminar espacios al principio de una cadena")
data = "                  Para saber si un dato es alfabético             "
print(data)
print(data.rstrip())

# Función split
print()
print("Función SPLIT")
data = "                  Para saber si un dato es alfabético             "
print(data)
print(data.split())
# Para separarlo por algún lugar en específico
print(data.split("si"))

# Para saber si un string comienza con algún caracter(s)
print()
print("Para saber si un string comienza con algún caracter(s)")
data = "Para saber si un dato es alfabético             "
print(data)
print(data.startswith("Para"))

# Para saber si un string termina con algún caracter(s)
print()
print("Para saber si un string termina con algún caracter(s)")
data = "Para saber si un dato es alfabético"
print(data)
print(data.endswith("o"))
print(data.endswith("alfabético"))

# Guardar o leer datos en un fichero
print()
print("Guardar o leer datos en un fichero")
# Leer todo el fichero
f = open("readme.md", "r")
datos1 = f.read()
print("DATOS1:",datos1)
# Leer algunos bytes del fichero
f = open("readme.md", "r")
datos2 = f.read(2)
print("DATOS2 (solo dos bytes):",datos2)
# Leer la primera linea del fichero
f = open("readme.md", "r")
datos3 = f.readline()
print("Solo la primera linea (solo un readline):",datos3)
f = open("readme.md", "r")
datos3 = f.readline()
datos3 = f.readline()
print("Solo la primera linea (con dos readline juntos):",datos3)
# readline con el bucle while
f = open("readme.md", "r")
datos4 = "a"
while datos4 != "":
    datos4 = f.readline()
    print("readline con el bucle while:",datos4)
# readline con el bucle while
f = open("readme.md", "r")
datos4 = "a"
while len(datos4) > 0:
    datos4 = f.readline()
    print("readline con el bucle while:",datos4)   
# Leer todo el fichero en una lista
f = open("readme.md", "r")
datos5 = f.readlines()
print("Leer todo el fichero en una lista:",datos5)       

f.close()

