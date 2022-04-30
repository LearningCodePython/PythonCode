# Mejore el programa ejercicio21.py anterior haciendo que tenga en cuenta que no se puede dividir por cero:

from ast import Break


val1 = int(input("Introduce un número entero: "))
val2 = int(input("Introduce otro número entero: "))
cociente = 1
resto = 1
if val2 == 0:
    print ("No es posible dividir por 0")
elif val2 != 0:
    cociente = val1 // val2 #cociente.
    resto = val1 % val2 # Resto
    if resto == 0:
        print (f"La division es exacta, el cociente es {cociente}")
    else:
        print (f"La division no es exacta tiene cociente: {cociente} y el resto es {resto}")