# Borra y escribe el fichero
f = open('mifichero2.txt', 'a')
f.write('datos')
f.write('datos2')
f.write('\n')
f.write('datos\n')
f.write('datos2\n')
f.close()
