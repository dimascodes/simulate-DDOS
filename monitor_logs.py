import paramiko

ubuntu_ip = "xx.xxx.xx.xx"
user = "xxxx"
password = "your_password"
log_file = "/var/log/apache2/access.log"

def monitor_logs():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ubuntu_ip, username=user, password=password)
    sftp = ssh.open_sftp()
    with sftp.open(log_file, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line.strip())
    sftp.close()
    ssh.close()

if __name__ == "__main__":
    monitor_logs()
