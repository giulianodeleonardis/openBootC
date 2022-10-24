from ctypes.wintypes import HLOCAL


a = 5
b = 6
c = 7

# > Mayor
# >= Mayor o igual
# == Exáctamente igual
# < Menor
# <= Menor o igual

resultado = a > 5 and c < 7
# resultado = (False and c < 7)
# resultado = (False and False)
# resultado = (False)
print(resultado)
print()
# AND -> True, False
print('AND')
print('T y T', True and True)
print('T y F', True and False)
print('F y T', False and True)
print('F y F', False and False)
print()
# OR -> True, False
print('OR')
print('T o T', True or True)
print('T o F', True or False)
print('F o T', False or True)
print('F o F', False or False)
print()
# XOR -> True, False
print('XOR')
print('T xo T', True ^ True)
print('T xo F', True ^ False)
print('F xo T', False ^ True)
print('F xo F', False ^ False)
print()
#if
print('if')
d = 5
e = 6
if d >= 5 and e <= 6:
    print('D es mayor o igual a 5 y E es menor o igual a 6') 
print()
#elif
print('elif')
d = 6
e = 6
if d > 6 and e <= 6:
    print('D es mayor o igual a 5 y E es menor o igual a 6') 
elif d >= 6:
    print('D es mayor o igual 6')
print()
#else
print('else')
d = 6
e = 6
if d > 6 and e <= 6:
    print('D es mayor o igual a 5 y E es menor o igual a 6') 
elif d == 5:
    print('D es mayor o igual 6')
else:
    print('Dentro del else')
print()
#while
# while 'la condición sea True':
#   ejecuta las acciones
print('while')
contador = 0

while contador <= 10:
    print('contador vale: ', contador)
    contador += 1

contador1 = 0
while contador1 <= 10:
    if contador1 % 2 == 0:
        print('Este numero: ',contador1,', es par')
    contador1 += 1
print()
#break
print('break')
contador = 0

while contador <= 10:
    print('contador vale: ', contador)
    contador += 1
    if contador == 5:
        break
print()
#continue
print('continue')
contador = 0

while contador <= 10:
    print('contador vale: ', contador)
    contador += 1
    if contador % 2 == 0:
        print(contador, ' es un número par')
        continue
    print('Estoy aquí porque contador vale: ', contador, ' y no se ha disparado el continue')
print()
#for
#for valor in cosa:
#   acciones
print('for')
lista = ['a', 'b', 'c', 'd', 'e']
tupla = (1, 2, 3, 'd', 5)

for valorActual in lista:
    print(valorActual)
print()
print('tupla')
for valorTupla in tupla:
    print(valorTupla)

print()
#range
#for numero in range(10):
#   acciones
print('range')

for numero in range(10):
    print(numero)
print()
for numero in range(5, 10):
    print(numero)
print()
#range para recorrer un array
print('range para recorrer un array')

longitud = len(lista)
for numero in range(longitud):
    print(lista[numero])
print()
print("Recorriendo todo un array en busca de...")
lista2 = ["hola", "mensaje", "adios"]
for palabra in lista2:
    print("palabra actual: ", palabra)
    if palabra == "mensaje":
        print("He encontrado la palabra 'mensaje'")
print()
print("Recorriendo un array hasta que encuentre un valor")
lista2 = ["hola", "mensaje", "adios"]
for palabra in lista2:
    print("palabra actual: ", palabra)
    if palabra == "mensaje":
        print("He encontrado la palabra 'mensaje'")
        break
print()
print("Recorriendo un array directamente con un IF")
lista2 = ["hola", "mensaje", "adios"]
if "mensaje" in lista2:
    print("He encontrado la palabra 'mensaje'")
print()
print("Recorriendo un array directamente con un IF con negación")
lista2 = ["hola", "mensaje", "adios"]
if "hello" not in lista2:
    print("No se encuentra la palabra 'hello'")
print()

print("Ordenar progresivamente una lista")
lista3 = [3, 4, 1, 2, 5]
print(lista3)
listaOrdenada = sorted(lista3)
print(listaOrdenada)
print()

print("Ordenar regresivamente una lista")
lista3 = [3, 4, 1, 2, 5]
print(lista3)
listaOrdenada = sorted(lista3, reverse = True)
print(listaOrdenada)
print()

print("Ordenar progresivamente una lista de letras")
lista4 = ['A', 'Z', 'p', 'z', 'P', 'a']
print(lista4)
listaOrdenada = sorted(lista4, reverse = False)
print(listaOrdenada)
print()

print("Switch")
valor = 3
match valor:
    case 1:
        print("Valor es 1")
    case 2:
        print("Valor es 2")
    case 3:
        print("Valor es 3")
    case 4:
        print("Valor es 4")
    case 5:
        print("Valor es 5")                                

print()
print("Caso extraño del FOR y ELSE")
list5 = ["hola", "", "adios"]
for palabra in list5:
    if palabra == 'mensaje':
        print("He encontrado la palabra 'mensaje'")
        break
else:
    print("No he encontrado nada")

print()
var = ['hola', 'hello', 'adios']
for palabra in var:
    temp = 'temporal'
    if palabra == 'hello':
        print('Encontrada la palabra HELLO')
print(var)
print(temp)

print()
print('Ejercicio 4 | Regresión de números')
array = []
for i in range(1, 101):
    array.append(i)
print(sorted(array, reverse = True))
print()
