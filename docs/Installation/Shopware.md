# Shopware installation
#### Install Updates and stuff
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install zsh zsh-syntax-highlighting zsh-autosuggestions tree ufw htop ncdu yt-dlp btop thefuck python3 python3-pip neofetch python3-pip jq git aria2 cmake make gcc build-essential docker docker.io docker-compose tmux net-tools curl wget -y
sudo sh -c '> /etc/motd'
chmod -x /etc/update-motd.d/*

sed -i 's/^PrintMotd.*/PrintMotd no/' /etc/ssh/sshd_config
sed -i 's/^PrintLastLog.*/PrintLastLog no/' /etc/ssh/sshd_config
if ! grep -q "^PrintMotd no" /etc/ssh/sshd_config; then
    echo -e "PrintMotd no" >> /etc/ssh/sshd_config
fi
if ! grep -q "^PrintLastLog no" /etc/ssh/sshd_config; then
    echo -e "PrintLastLog no" >> /etc/ssh/sshd_config
fi

ufw allow openssh
ufw allow 22
ufw enable
systemctl restart sshd
sudo dpkg-reconfigure -plow unattended-upgrades
systemctl enable unattended-upgrades.service
```
#### Installing php 8.1
```bash
sudo apt update && sudo apt install php8.1 php8.1-common php8.1-mysql php8.1-xml php8.1-xmlrpc php8.1-curl php8.1-gd php8.1-imagick php8.1-cli php8.1-intl php8.1-zip php8.1-mbstring -y
```
#### install mariadbserver
```bash
sudo apt install mariadb-server mariadb-client -y
```
#### Run mysql setup
```bash
mysql_secure_installation
```
![grafik](https://gist.github.com/assets/77645077/df3e878f-d797-48f2-91d9-6393e8b3a370)

#### Setup database replace YOURPASSWORD with a secure password and write it down!

```bash
mariadb -u root -p
CREATE DATABASE shopware;
GRANT ALL PRIVILEGES ON shopware.* TO 'shopware_user'@'localhost' IDENTIFIED BY 'YOURPASSWORD';
FLUSH PRIVILEGES;
EXIT;
```
#### edit `/etc/php/8.1/apache2/php.ini`
#### set values to
`memory_limit = 512M` <br>
`post_max_size = 32M` <br>
`upload_max_filesize = 32M` <br>
`opcache.memory_consumption = 256` <br>

### Install Composer
```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === 'edb40769019ccf227279e3bdd1f5b2e9950eb000c3233ee85148944e555d97be3ea4f40c3c2fe73b22f875385f6a5155') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"
sudo mv composer.phar /usr/bin/composer
```
#### enable ssl
`sudo a2enmod ssl`

#### set ip to domain cloudflare
![grafik](https://gist.github.com/assets/77645077/f50a562e-ce38-4550-b0b0-a317d837c5bd)

#### get your ssl crt and key from cloudflare
![grafik](https://gist.github.com/assets/77645077/f3d87c86-0385-4ff5-b7d1-284defb9298a)
![grafik](https://gist.github.com/assets/77645077/b2a64d1f-52f4-4254-a3a2-e67b1fc7a3cb)
![grafik](https://gist.github.com/assets/77645077/38a2a13a-4328-4082-a1d4-6d75c2dc714f)
and put it in the right place <br>
`mkdir -p /etc/ssl/yourdomain.com` <br>
`/etc/ssl/yourdomain.com/cert.crt` <br>
`/etc/ssl/yourdomain.com/cert.key` <br>
### Apache config, edit
`/etc/apache2/sites-available/000-default.conf`

```bash
<VirtualHost *:443>
    ServerName yourdomain.com
    DocumentRoot /var/www/html

    SSLEngine on
    SSLCertificateFile /etc/ssl/yourdomain.com/cert.crt
    SSLCertificateKeyFile /etc/ssl/yourdomain.com/cert.key
    SSLCertificateChainFile /etc/ssl/yourdomain.com/cert.crt

    <Directory /var/www/html>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/shopware_error.log
    CustomLog ${APACHE_LOG_DIR}/shopware_access.log combined
</VirtualHost>
```

#### open port 443
```bash
ufw allow 443
```
#### restart apache2
```bash
sudo systemctl restart apache2.service
```
#### get installer
```bash
cd /var/www/html
rm index.html
wget https://github.com/shopware/web-recovery/releases/latest/download/shopware-installer.phar.php
```
#### set installer write premission
`sudo chown -R www-data:www-data /var/www/html`

#### go to url
`https://yourdomain.com/shopware-installer.phar.php`

#### follow the installer when done you get a 404 dont worry
![grafik](https://gist.github.com/assets/77645077/dd947c53-cf27-41ec-bec9-eb40ac690e50)

#### goto
`/var/www/html`
#### and run
`composer install`
#### now edit
`/etc/apache2/sites-available/000-default.conf`
####  and change
`/var/www/html`
#### to
`/var/www/html/public`
#### restart apache2
`sudo systemctl restart apache2`
`sudo a2enmod rewrite`
#### got to yourdomain.com
and follow the configuration

#### block port 80
`ufw deny 80`


#### edit
`/var/ww/html/.env` <br>
`/var/ww/html/.env.local` <br>
and set APP_URL to shop url yourdomain.com
