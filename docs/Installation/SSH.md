# Setup ssh secure

#### Use SSH Key Authentication
Generate key on local machine:
```bash
ssh-keygen -t ed25519
```

#### Copy key to server:
```bash
ssh-copy-id user@server_ip
```

#### Disable password authentication:
```bash
sudo nano /etc/ssh/sshd_config
# Set PasswordAuthentication no
sudo systemctl restart ssh
```
## Change the Default SSH Port
#### Edit SSH config:
```bash
sudo nano /etc/ssh/sshd_config
# Change Port 22 to Port 2222 (or any other number)
sudo systemctl restart ssh
```

## Limit User Access
#### Create a new user:
```
sudo adduser sshuser
sudo usermod -aG sudo sshuser
```
#### Disable root login:
```
sudo nano /etc/ssh/sshd_config
# Set PermitRootLogin no
sudo systemctl restart ssh
```

## Use a Firewall
#### Install and configure UFW:
make sure to open news ssh port before updating
```
sudo apt install ufw
sudo ufw allow 2222/tcp
sudo ufw enable
```

## Keep Software Updated
```
sudo apt update
sudo apt upgrade
```
## Implement Fail2Ban
```
sudo apt install fail2ban
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nano /etc/fail2ban/jail.local
# Configure as needed
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```
## Disable Unused Features
#### Edit SSH config:
```
sudo nano /etc/ssh/sshd_config
# Set:
# AllowTcpForwarding no
# X11Forwarding no
# AllowAgentForwarding no
sudo systemctl restart ssh
```

## Setup Gotify for ssh login
