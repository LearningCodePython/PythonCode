import telnetlib
from fileinput import close
import ipaddress

#Creamos la lista de IP
net4 =ipaddress.ip_network('172.16.54.0/24')
f = open ("ip.lst", "w")
for x in net4.hosts():
    f.write(str(x) + '\n')
f.close()

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
    
fichero = open('ip.lst', 'r')
for linea in fichero:
	if linea[-1] == '\n':
		linea = linea[:-1]
	port(linea)

fichero.close()
