# O que é isso?
Este é um programa simples em python que se conecta ao servidor ssh e executa comandos no mesmo.

## Primeiro passo

Caso você ainda não tenha a biblioteca ***paramiko***, istale-a rodando o seguinte comando no terminal do PyCharm: 

` pip install paramiko `

> _O Paramiko é uma implementação do protocolo SSHv2, escrita inteiramente em Python. Ele oferece uma maneira prática e eficaz de realizar operações SSH, como execução de comandos remotos ou transferência de arquivos, programaticamente._
 (Fonte: https://didatica.tech)

Então, execute o ***ssh_cliente***:

 ![image](https://github.com/LeRodrigues2005/Cliente-SSH/assets/97632543/612f3451-1eda-4eb4-a3cf-67fa603ec8ca)

 ## Segundo passo
 Abra um terminal e execute o comando ` ssh root@127.0.0.1 `, onde _root_ é o nome de sua máquina.
 
 Depois, rode o programa ***ssh_client*** no PyCharm. No terminal você verá um input escrito _Comando_.

 ![image](https://github.com/LeRodrigues2005/Cliente-SSH/assets/97632543/defdab5e-0f60-4a77-b789-625a83514ff7)

 ## Terceiro Passo
Utilize o terminal do PyCharm para executar comandos.

![image](https://github.com/LeRodrigues2005/Cliente-SSH/assets/97632543/9afadcee-6ceb-4dfa-b782-873856edb8bd)

## Utilizando o terminal do Linux

Você também pode utilizar o Netcat e fazer os comandos no terminal do próprio linux.

Para isso, execute o seguinte código no terminal do linux: ` nc -lvp 7899 `.
Depois, rode o ***ssh_cliente*** e escreva o seguinte no terminal do PyCharm: ` nc 127.0.0.1 7899 -e bin/bash `, pressione Enter.

Pronto, comexão feita!

![image](https://github.com/LeRodrigues2005/Cliente-SSH/assets/97632543/f9f46e54-42c2-429d-8797-b28bee941e6d)

