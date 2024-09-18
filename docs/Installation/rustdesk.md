## Rustdesk

### Requirements

and ubuntu or debian vps with a static ip

### Install

##### allow ssh ufw
```
ufw allow 22
```

##### allow rustdesk in ufw
```
ufw allow 21115:21119/tcp
ufw allow 8000/tcp
ufw allow 21116/udp
sudo ufw enable
```

##### download rustdesk and run install script
```
wget https://raw.githubusercontent.com/techahold/rustdeskinstall/master/install.sh
chmod +x install.sh
./install.sh
```

follow the installer steps set to ip not domain

got to your cloudflare and point dns record without proxying to the ip address

you can find the api key at /opt/rustdesk/id_ed25519.pub
```
cat /opt/rustdesk/id_ed25519.pub
```