import paramiko

# As seguintes informações podem ser mudadas conforme o que você queira acessar.
# Esses são os valores para acessar o localhost com o ssh padrão.
host = "127.0.0.1"
user = "kali"
passwd = "kali"

client = paramiko.SSHClient()  # Cria uma instância do cliente SSH.
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Torna o host conhecido para permitir conexão
# Estabelece uma conexão SSH com o host especificado usando o nome de usuário e senha fornecidos:
client.connect(host, username=user, password=passwd)

while True:
    # entrada, saída, erro:
    stdin, stdout, stderr = client.exec_command(input("Comando: "))
    for line in stdout.readlines():
        print(line.strip())

    erros = stderr.readlines()
    if erros:
        print(erros)
