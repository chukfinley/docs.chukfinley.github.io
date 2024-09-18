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
```bash
sudo adduser sshuser
sudo usermod -aG sudo sshuser
```
#### Disable root login:
```bash
sudo nano /etc/ssh/sshd_config
# Set PermitRootLogin no
sudo systemctl restart ssh
```

## Use a Firewall
#### Install and configure UFW:
make sure to open news ssh port before updating
```bash
sudo apt install ufw
sudo ufw allow 2222/tcp
sudo ufw enable
```

## Keep Software Updated
```bash
sudo apt update
sudo apt upgrade
```
## Implement Fail2Ban
```bash
sudo apt install fail2ban
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo nano /etc/fail2ban/jail.local
# Configure as needed
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```
## Disable Unused Features
#### Edit SSH config:
```bash
sudo nano /etc/ssh/sshd_config
# Set:
# AllowTcpForwarding no
# X11Forwarding no
# AllowAgentForwarding no
sudo systemctl restart ssh
```

## Setup Gotify for ssh login

##### copy the following script to /usr/local/bin/ssh-gotify-notif
##### set url gotify url and token
```bash
exec &> /dev/null #Hide output

Gotify_URL='https://example.tld/gotify'
Gotify_Token='gotify-app-token'

notify() {

        now=$(date -d "-60 seconds" +%s) #Get current time minus 60 seconds
        end=$((SECONDS+30)) #Set 30s Timeout for loop

        while [ $SECONDS -lt $end ]; do

                SSHdate=$(date -d "$(who |grep pts|tail -1 | awk '{print $3, $4}')" +%s) #Check for the latest SSH session

                if [ $SSHdate -ge $now ]; then #Once who is updated continue with sending Notification

                        title="SSH Login for $(/bin/hostname -f)"
                        message="$(/usr/bin/who | grep pts)"

                        /usr/bin/curl -X POST -s \
                                -F "title=${title}" \
                                -F "message=${message}" \
                                -F "priority=5" \
                                "${Gotify_URL}/message?token=${Gotify_Token}"

                        break
                fi
        done

}

notify & #Run in background to prevent holding up the login process

```

##### make it exacutable
```bash
chmod +x /usr/local/bin/ssh-gotify-notif
```

##### In the file /etc/pam.d/sshd add the following line
```bash
session optional pam_exec.so /usr/local/bin/ssh-gotify-notif
```
