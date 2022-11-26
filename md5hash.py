# @ By Cristo Emiliano Hernandez Daria
# Codigo que pregunta una contraseña y la encripta usando MD5
# 
import hashlib

contraseña = input("¿Contraseña?")
h = hashlib.new("md5",b"Y4iVq98p")

# h = hashlib.new("md5",b"Emilio54")

print(h.hexdigest())
