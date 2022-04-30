# Escriba un programa que pida primero un número par (positivo o negativo) y si el valor no es correcto,
# muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o negativo) y si el valor no es correcto,
# mostrará un aviso.

# Declaración:

npar = float(input("Introduce un número par: "))
valor1 = npar % 2

# Condicion

if valor1 != 0:
    print("El numero introducido no es par")    
elif valor1 == 0:
    nimpar = float(input("Ahora introduce un número impar: "))
    valor2 = nimpar % 2
    if valor2 != 0:
        print ("Gracias por su colaboración.")
    else:
        print ("Uno de los valores no es correcto vuelva a ejecutar el programa")