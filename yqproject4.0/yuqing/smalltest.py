import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('42.96.134.205', 22, 'root', 'ViveMax2016')

str_command = "touch aaa"
stdin, stdout, stderr = ssh.exec_command(str_command)
ssh.close()