# Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona
# y que calcule su índice de masa corporal (imc).
# Se recuerda que el imc se calcula con la fórmula imc = peso / altura ** 2

peso = float(input("Introduce to peso en Kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

altura_= altura ** 2
imc = peso / altura_

print (f"Tu indice de masa corporal es de {imc}")