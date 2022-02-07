import paramiko
 
ssh = paramiko.SSHClient()
know_hosts = paramiko.AutoAddPolicy()
ssh.set_missing_host_key_policy(know_hosts)

ip = input("¿Direccion IP del AP? ")
 
ssh.connect(
    hostname= ip,
    port=22,
    username="",
    password=""
)
 
shell = ssh.invoke_shell()
shell.settimeout(1)
 
# command = input(">>>") + "\n"
command = ("\n") # Le envio un enter para acceder directamente al ash
shell.send(command)

while True:
    try:
        recv = shell.recv(512).decode()
        if recv:
            print(recv)
        else:
            continue
    except:
        command = input(">>>") + "\n"
        shell.send(command)

ssh.close()

# set-inform http://192.168.252.111:8080/inform
