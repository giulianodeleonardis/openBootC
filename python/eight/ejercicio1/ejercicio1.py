import pickle

def main():
    f = open('miFichero.txt', 'a')
    f.write('Mi nombre es Giuliano\n')
    f.write('Mi edad: 36 años\n')
    f.close()
    f1 = open('miFichero.txt', 'r')
    datos1 = 'a'
    while datos1 != "":
        datos1 = f1.readline()
        if datos1.startswith('Mi nombre'):
            print("NOMBRE |", datos1) 
        if datos1.startswith('Mi edad'):
            print("EDAD |", datos1)  
    f1.close()                   
if __name__ == '__main__':
    main()
