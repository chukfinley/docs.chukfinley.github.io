# Apache Installation and Configuration

## Install/Update Apache PHP Modules

```bash
# Install/reinstall PHP Apache module
sudo apt-get install --reinstall libapache2-mod-php8.1

# Enable required Apache modules
sudo a2enmod php8.1
sudo a2enmod ssl
sudo a2enmod rewrite
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo a2enmod proxy_wstunnel

# Restart Apache service
sudo systemctl restart apache2

# Verify Apache status
systemctl status apache2.service
```

## Common Apache Modules

- `php8.1`: PHP 8.1 module
- `ssl`: HTTPS/SSL support
- `proxy`: Basic proxy functionality
- `proxy_http`: HTTP proxy support
- `proxy_wstunnel`: WebSocket support
- `rewrite`: URL rewriting
- `headers`: Custom HTTP headers

## Additional Commands

```bash
# List enabled modules
apache2ctl -M

# Disable a module
sudo a2dismod module_name

# Test configuration
apache2ctl configtest

# View error logs
tail -f /var/log/apache2/error.log
```
