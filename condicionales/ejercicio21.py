# Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no.

val1 = float(input("Introduce un número entero: "))
val2 = float(input("Introduce otro número entero: "))
cociente = val1 // val2 #cociente.
resto = val1 % val2 # Resto

if resto == 0:
    print (f"La division es exacta, el cociente es {cociente}")
else:
    print (f"La division no es exacta tiene cociente: {cociente} y el resto es {resto}")