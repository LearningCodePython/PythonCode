import telnetlib
from fileinput import close
import ipaddress

# La intencios es crear un codigo que primero cree una lista de ip
# Segundo pregunte cual el el puerto sip que deseamos configurar, lo almacene, y modifique todas las ONT
# 
#
# Creamos la lista de IP y la almacenamos en el fichero ip.lst
# En futuras revisiones debe ser preguntado al usuario y almacenado en una variable.

net4 =ipaddress.ip_network('172.16.54.0/24')
f = open ("ip.lst", "w")
for x in net4.hosts():
    f.write(str(x) + '\n')
f.close()

# Creamos la función 
def port(ip):
    try:
        user = "support"
        password = "!Onuitp2022"
        tn = telnetlib.Telnet(ip)
        tn.read_until(b"Login: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
        tn.write(b"voice set proxyPort 0# 60029 \n")
        tn.write(b"voice set regPort 0# 60029 \n")
        tn.write(b"voice set obProxPort 0# 60029 \n")
        tn.write(b"voice save \n")
        tn.write(b"exit\n")
        print(tn.read_all().decode('ascii'))
        print (f"La dirección {ip} ha quedado configurada")
        tn.close()
    except OSError:
        print(f"La direccion {ip} no es una ONT o no comunica")

# Abrimos el listado de IP y lo recorremos ejecutando la función en cada interaccion.
fichero = open('ip.lst', 'r')
for linea in fichero:
	if linea[-1] == '\n':
		linea = linea[:-1]
	port(linea)

fichero.close()
