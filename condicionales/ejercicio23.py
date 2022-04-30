# Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.

val1 = int(input("Escibe el primer número para comparar: "))
val2 = int(input("Escibe el segundo número para comparar: "))

if val1 < val2:
    print (f"{val1} es menor que {val2}")
elif val1 > val2:
    print (f"{val1} es mayor que {val2}")
else:
    print (f"Ambos numeros son iguales")