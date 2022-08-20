from config import sshList
import os
from SSHConnect import ssh_connect


# sshList = [
#     ("ip", "username", "password")
# ]

def setup_env(ssh_client):
    ssh_client.exec_command('cd /tmp/ && git clone https://github.com/l3unger/RemoteScan.git')
    ssh_client.exec_command('cd /tmp/RemoteScan/ && chmod +x setup.sh &&./setup.sh')
    print("已完成服务器的初始化部署")


def upload_file_to_server(ssh_client, index, projectname):
    local_file = os.path.abspath('.') + '/targets/{}/{}.txt'.format(projectname, index)
    remote_dir = '/tmp/RemoteScan/Server/pppXray/target.txt'
    sftp = ssh_client.open_sftp()
    sftp.put(local_file, remote_dir)
    sftp.close()
    print("{}文件已上传至远程服务器{}".format(local_file, remote_dir))


def main():
    projectname = "cmcc"
    for index in range(0, len(sshList)):
        hostname = sshList[index][0]
        username = sshList[index][1]
        password = sshList[index][2]
        ssh_client = ssh_connect(hostname=hostname, username=username, password=password)
        # setup_env(ssh_client)
        # upload_file_to_server(ssh_client, index, projectname)
        ssh_client.close()


if __name__ == '__main__':
    main()
