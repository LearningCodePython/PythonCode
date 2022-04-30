# Escriba un programa que pida primero un número par y luego un número impar (positivos o negativos).
# En caso de que uno o los dos valores no sea correcto, se mostrará un único aviso.

numeropar = float(input("Introduce un numero par positivo o negativo: "))
numeroimpar = float(input("Introduce un numero impar positivo o negativo: "))

# Evaluar.

val1 = numeropar % 2
val2 = numeroimpar % 2

if val1 != 0 or val2 == 0:
    print (f"Unos de los números no es correcto par / impar.")
