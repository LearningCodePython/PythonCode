numero = input("Introduce un numero entre 1 y 1000 ")
r = int(numero) % 2

if r == 0:    
    print("El número " + numero + " es un múmero par")
else:
    print("El número " + numero + " es un número impar")
