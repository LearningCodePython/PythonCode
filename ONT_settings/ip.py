from fileinput import close
import ipaddress

net4 =ipaddress.ip_network('10.104.40.0/23')
f = open ("ip.lst", "w")
for x in net4.hosts():
    f.write(str(x) + '\n')
f.close()