import paramiko
from config import sshList


def startupEnv():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for index in range(0, len(sshList)):
        hostname = sshList[index][0]
        username = sshList[index][1]
        password = sshList[index][2]
        ssh_client.connect(hostname=hostname, port=22, username=username, password=password)
        stdin, downloadScript, stderr = ssh_client.exec_command('cd /tmp/ && git clone ')
        stdin, startupEnv, stderr = ssh_client.exec_command('cd /tmp/RemoteScan/ && chmod +x setup.sh &&./setup.sh')
        ssh_client.close()

def uploadTarget():
    with open('./Server/pppXray/target.txt','r') as targetFile:


if __name__ == '__main__':
    startupEnv()
    uploadTarget()

