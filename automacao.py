import paramiko


ip = '192.168.0.200'
usuario = 'root'
senha = 'teste'


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Abre a conexão com o servidor
ssh.connect(hostname=ip , username=usuario , password=senha)
#roda o comando via ssh
stdin, stdout, stderr = ssh.exec_command('cat /etc/passwd')
#fecha a conexão estabelecida
stdin.close()



with open('readme.txt', 'w') as f:
    for line in stdout.readlines():
        f.write(line)





ssh.close()