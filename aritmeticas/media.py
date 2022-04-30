# Escriba un programa que pida dos números y que escriba su media aritmética.
# Se recuerda que la media aritmética de dos números es la suma de ambos números dividida por 2.

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

media = (numero1 + numero2) / 2

print (f"La media aritmética de {numero1} y {numero2} es de {media}")



######## Donde he fallado:########
# el el tipo de dato. si no le pongo el timpo de dato a las variables numero1 y numero2 cundo las\
# recibo por el teclado, me las interpreta como str. 
# En la concatenación yo propuse:
## print ("La media aritmética de" + numero1 + " y " + numero2 + "es de " + media).
# para poder hacerlo como yo dije debería convertir los nuermos y el resultado a str.
# n1 = str(numero1)
# n2 = str(numero2)
# r = str(media)
# print ("La media aritmética de " + n1 + " y " + n2 + "es de " + r)