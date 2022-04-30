# Escriba un programa que pida primero un número par y a continuación un numero impar (positivos o negativos).
# En cada petición, si el valor no es correcto se mostrará un aviso.

in1 = float(input("Escribe un numero par: "))
r1 = in1 % 2
if r1 != 0:
    print ("Ese no es un número par.")

in2 = float(input("Ahora escribe un número impar: "))
r2 = in2 % 2
if r2 == 0:
    print ("Este no es un número impar.")

if r1 or r1:
    print ("Repite al programa para reintentarlo.")
else:
    print ("Gracias por tu colaboración.")