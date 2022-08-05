# Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.

val1 = int(input("Introduce un número entero: "))
val2 = int(input("Introduce otro número entero: "))

if val1 == 0 or val2 == 0:
    print ("Este programa no admite valores nulos.")
elif val1 < 0 or val2 < 0:
    print ("Este programa no admite valores negativos.")
elif val1 > val2:
    if val1 % val2:
        print (f"{val1} no es múltiplo de {val2}")
    else:
        print (f"{val1} es múltipolo de {val2}")
elif val1 < val2:
    if val2 % val1:
        print (f"{val2} no es múltiplo de {val1}")        
    else:
        print (f"{val2} es múltiplo de {val1}")
elif val1 == val2:
    if val1 % val2:
        print (f"{val1} no es múltiplo de {val2}")
    else:
        print (f"{val1} es múltipolo de {val2}")


# Mejore el programa anterior haciendo que el programa avise cuando se escriben valores negativos o nulos.
# Lineas de la 6 la 9
'''
if val1 == 0 or val2 == 0:
    print ("Este programa no admite valores nulos.")
elif val1 < 0 or val2 < 0:
    print ("Este programa no admite valores negativos.")
'''