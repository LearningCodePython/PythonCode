# Escriba un programa que pida una cantidad de segundos y que escriba cuántos minutos y segundos son.

val1 = float(input("Introduce una la cantidad en segundos a calcular: "))

segundos = int(val1 % 60)
minutos = int(val1 // 60)
horas = int(minutos //60)
minutos2 = (minutos % 60)

print(f"{val1} segundos equivalen a {horas} horas, {minutos2} minutos y {segundos} segundos")

print (horas)

# El ejercicio solo son los minutos i los segundos pero se puede ampliar mas en los resultados. Dias semanas meses etc