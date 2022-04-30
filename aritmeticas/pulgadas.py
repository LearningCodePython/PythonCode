#Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en centímetros.
#Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm.
 
in1 = float(input("introduce la distancia en pies: "))
in2 = float(input("Introduce la distancias en pulgadas:"))

pulgadas1 = in1 * 12
cm = (in2 + pulgadas1) * 2.54
print (f"cm: {cm}")
