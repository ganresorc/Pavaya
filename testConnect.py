import paramiko
import getpass

password = getpass.getpass()
ssh = paramiko.SSHClient()


currentIP = 10.1.1.10
currentPort = 22

ctrly = ssh.send("\x25")

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(currentIP, port=currentPort, ctrly, username=USER, password=password)
stdin, stdout,stderr = ssh.exec_command('show run')

output = stdout.readlines()
type(output)
<type 'list'>
print '\n.join(output)
close()