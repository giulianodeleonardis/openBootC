# Borra y escribe el fichero
f = open('mifichero.txt', 'w')
f.write('datos')
f.write('datos2')
f.write('\n')
f.write('datos\n')
f.write('datos2\n')
# Writing lists
lista = [
    'una linea\n',
    'dos lineas\n',
    'tres lineas\n'
]
f.writelines(lista)
f.close()
