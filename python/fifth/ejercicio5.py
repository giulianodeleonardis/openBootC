leapYear = 2000
def leapY(year):
    operation = year % 4
    if operation == 0:
        print("El año",year,"es bisiesto")
    else:
        print("El año",year,"NO es bisiesto")
leapY(2022)        