## Gitea via docker-compose

### Requirements

and ubuntu or debian vps with a static ip

### Install

##### update and upgrade os and install docker and docker-compose
```
sudo apt update 
sudo apt upgrade
sudo apt install docker docker.io docker-compose apparmor
```
##### setup docker compose file
edit docker-compose.yml
```
nano docker-compose.yml
```
##### paste

```
version: "3"

networks:
  gitea:
    external: false

services:
  server:
    image: gitea/gitea:1.21.4
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
    restart: always
    networks:
      - gitea
    volumes:
      - ./gitea:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "3001:3000"
      - "22:22"
```
##### start the docker container

```
docker-compose up -d
```
##### setup apache config chnage the domain and subdomain how you like 
```
#git.yourdomain.com
<VirtualHost *:443>
    ServerName git.yourdomain.com

    # SSL/TLS Configuration (assuming you have SSL certificate/key files)
    SSLEngine on
    SSLCertificateFile /etc/ssl/yourdomain.com/yourdomain.com.pem
    SSLCertificateKeyFile /etc/ssl/yourdomain.com/yourdomain.com.key

    # Proxy Configuration
    ProxyPass / http://localhost:3001/
    ProxyPassReverse / http://localhost:3001/

    # Additional Proxy Headers (optional)
    ProxyPreserveHost On
    ProxyRequests Off
    AllowEncodedSlashes NoDecode

    # Logging (optional)
    TransferLog /var/log/apache2/git.yourdomain.com_access.log
    ErrorLog /var/log/apache2/git.yourdomain.com_error.log

    # SSL Protocol and Cipher Suite (optional)
    SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1
    SSLCipherSuite HIGH:!aNULL:!MD5:!3DES
</VirtualHost>
```
##### point you domain to the ip of the server
##### go to the url and follow the wizard leave everything how it is and just add you options

##### to use it with git cli go to your profile pic and settings in the drop down, click on applications set a name, Select permissions from the drop down you probably only need repository Read and Write for git cli and click on Generate Token. Copy the token from the top and setup your git cli.
