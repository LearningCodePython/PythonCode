# Escriba un programa que pida primero un número par y a continuación un numero impar (positivos o negativos).
# En caso de que uno o los dos valores no sean correctos, se mostrarán uno o dos avisos.

valor1 = float(input("Introduce un numero par: "))
valor2 = float(input("Introduce un numero impar: "))
 
r1 = valor1 % 2
r2 = valor2 % 2

# Condicion.

if r1 != 0:
    print ("No ha escrito un número par.")

if r2 == 0:
    print ("No ha escrito un número impar.")

if r1 == 0 and r2 != 0:
    print ("Gracias pos su colaboración")