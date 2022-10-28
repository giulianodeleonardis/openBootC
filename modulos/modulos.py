import operaciones
import paquete.suma
import paquete.sumador.sum
import paquete.restador.rest

def main():
    #Código principal de mi programa 
    print("Hola en main()")
    print("Valor de PI: ", operaciones.PI)
    sum = operaciones.suma(2, 2)
    print("Suma: ", sum)
    mult = operaciones.Operador()
    print("La multiplicación es: ", mult.multiplicacion(2, 5))
    print(paquete.suma.suma(2, 3))
    print(paquete.sumador.sum.suma(8, 8))
    print(paquete.restador.rest.resta(8, 8))


if __name__ == '__main__':
    main()