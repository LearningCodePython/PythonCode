from random import random
from turtle import up
import random

mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
caracteres_especiales = "!@#$%^&*\/_+"

user_for = mayusculas + minusculas + numeros + caracteres_especiales
length_for_password = 40

password ="".join(random.sample(user_for, length_for_password))

print (password)
