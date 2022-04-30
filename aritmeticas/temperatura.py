# Escriba un programa que pida una temperatura en grados Celsius,
# y que escriba esa temperatura en grados Fahrenheit.
# Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: F = 1,8 * C + 32

temp = float(input("Introduce una temperatura en Celsius: "))

r = (1.8 * temp) + 32

print (f"La temperatura de {temp} gradot Celsius equivale a {r} grados Fahrenheit.")