def nombre():
    pass

def miFuncion():
    print('Nombre')
print('Antes')
miFuncion()
print('Después')
#------#
print()
print('Parámetro de una función')
def miFuncion(nombre):
    print("Hola ", nombre)
miFuncion("Giuliano")
def suma(a, b):
    print('La suma de a + b es: ', a + b)
suma(4, 2)
#------#
print()
print('Variable SHADOWING')
hoyHace = 12.0
def shadow(nombre):
    hoyHace = 6.0
    print("Hola ", nombre+".", "La temperatura de hoy es: ", hoyHace)
shadow("Giuliano")
print("¿Sigue siendo el mismo valor?: ",hoyHace)
#---#
hoyHace = 12.0
def shadow(nombre):
    global hoyHace
    hoyHace = 6.0
    print("Hola ", nombre+".", "La temperatura de hoy es: ", hoyHace)
shadow("Giuliano")
print("¿Sigue siendo el mismo valor?: ",hoyHace)
#------#
print()
print('Valor por defecto de un parámetro de una función')
def funcionName(nombre = "Giuliano"):
    hoyHace = 6.0
    print("Hola ", nombre)
funcionName()
funcionName("Antonio")
#------#
print()
print('Valor por defecto de un parámetro de una función')
def funcionSuma(a=1, b=3, c=5):
    suma = a + b + c
    print("Total: ", suma)
funcionSuma()
funcionSuma(5)
funcionSuma(5,2)
funcionSuma(1,1,1)
#------#
print()
print('Named parameters')
def funcionSuma(a=1, b=3, c=5):
    suma = a + b + c
    print("Total: ", suma)
funcionSuma(c=18)
funcionSuma(c=9, a=4 , b=1)
#------#
print()
print('Parámetros variables')
def funcionSuma1(*misParametros):
    print("Parámetros: ", misParametros)
funcionSuma1()
funcionSuma1(1,2,3,4,5)
#---#
def funcionSuma2(*misParametros):
    resultado = 0
    for arg in misParametros:
        resultado += arg
    print("Suma total es: ", resultado)
funcionSuma2(2,3)
funcionSuma2(1,2,3,4,5)
#------#
print()
print('Parámetros variables con nombre')
def funcionSuma1(**misParametros):
    print("Parámetros: ", misParametros)
funcionSuma1()
funcionSuma1(size="big", color="blue")
#---#
def valoresNombre(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)
valoresNombre(vivienda="piso", coche="rojo")
#---#
def valoresNombre(**kwargs):
    if kwargs['coche'] == 'bonito':
        print("To coche es bonito")
    else:
        print("Tu coche como que es algo feo")
valoresNombre(coche="feo")
valoresNombre(coche="bonito")
#---#
print()
def valoresNombre1(**kwargs):
    if 'coche' not in kwargs:
        return
    if kwargs['coche'] == 'bonito':
        print("To coche es bonito")
    else:
        print("Tu coche como que es algo feo")
valoresNombre1()  
valoresNombre1(coche="feo")
valoresNombre1(coche="bonito")
#------#
print()
print('Palabra return')
def funcionSuma3(a, b):
    return a + b
result = funcionSuma3(1, 5)
print(result)
#---#
print()
def funcionSuma3(a, b):
    return a + b, a - b, a * b, a / b
result = funcionSuma3(1, 5)
print(result)
print(result[0])
print(result[1])
#---#
print()
def funcionSuma3(a, b):
    return a + b, a - b, a * b, a / b
suma, resta, multi, divi = funcionSuma3(1, 5)
print(suma)
print(resta)
print(multi)
print(divi)
#---#
print()
print("Guión bajo para ignorar un valor")
def funcionSuma3(a, b):
    return a + b, a - b, a * b, a / b
suma, resta, multi, _ = funcionSuma3(1, 5)
print(suma)
print(resta)
print(multi)
#------#
print()
print('Operador ternario del IF')
def sumador(**kwargs):
    inicial = kwargs['inicial'] if 'inicial' in kwargs else 0
    final = kwargs['final'] if 'final' in kwargs else 0

    resultado = 0 
    for x in range(inicial, final + 1):
        resultado += x    
    return resultado
print(sumador())
print(sumador(inicial=15))
print(sumador(final=15))
print(sumador(inicial=15, final=30))

#------#
print()
print('Función anónima')
anonima = lambda: print("Hola, función anónima")
anonima()
#---#
print()
anonima = lambda nombre: print("Hola, función anónima: ", nombre)
anonima("Giuliano")
#---#
print()
anonima = lambda nombre1, nombre2: print("Hola ", nombre1+".", "Adios ", nombre2)
anonima("Giuliano", "Antonio")
#---#
print()
sumatoria = lambda x: x + x
print(sumatoria(2))