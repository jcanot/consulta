# funcion para calcular años bosiestos
year = int(input("ingresar año"))


if year == ValueError:
     print("debe ingresar el valor en numeros")
else:
    pass


def calcular_si_es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False    



es_bisiesto = calcular_si_es_bisiesto(year)
if es_bisiesto == True:
    print(f"El año {year} es bisiesto")
else:
    print(f"El año {year} no es bisiesto")
