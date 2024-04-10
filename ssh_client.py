import paramiko

host = "127.0.0.1"
user = "root"  # DEPOIS - mudar para user e senha padrao
passwd = "1939"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # tornar o host conhecido para permitir conexão
client.connect(host, username=user, password=passwd)

while True:
    # entrada, saída, erro:
    stdin, stdout, stderr = client.exec_command(input("Comando: "))
    for line in stdout.readlines():
        print(line.strip())

    erros = stderr.readlines()
    if erros:
        print(erros)
