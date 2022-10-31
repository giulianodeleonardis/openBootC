def escribe(fichero, datos):
    f = open(fichero, 'w')
    for linea in datos:
        if not linea.endswith('\n'):
            linea = linea + '\n'
        f.write(linea)
    f.close()

lista = [
    'una linea',
    'dos lineas',
    'tres lineas'
]

escribe('mifichero3.txt', lista)
