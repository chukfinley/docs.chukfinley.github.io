## Seafile Installation

# Fixing Seafile CSRF Issues

## Quick Fix (One-Liner Commands)
```bash
# Find seahub_settings.py
find /opt/seafile -name "seahub_settings.py"

# Add CSRF settings (replace with your domain)
echo -e "CSRF_TRUSTED_ORIGINS = ['https://file.exmaple.com']\nCSRF_COOKIE_SECURE = True\nCSRF_COOKIE_SAMESITE = 'Strict'" | sudo tee -a /path/to/seahub_settings.py

# Restart services
docker-compose down && docker-compose up -d && sudo systemctl restart apache2
```

## Detailed Solution

### 1. Apache Configuration
```apache
<VirtualHost *:443>
    ServerName file.example.com
    SSLEngine on
    SSLCertificateFile /etc/ssl/chuk/chuk.dev.pem
    SSLCertificateKeyFile /etc/ssl/chuk/chuk.dev.key

    ProxyRequests Off
    ProxyPreserveHost On

    RequestHeader set X-Forwarded-Proto "https"
    RequestHeader set X-Forwarded-Port "443"
    RequestHeader set X-Forwarded-For "%{REMOTE_ADDR}s"
    RequestHeader set X-Real-IP "%{REMOTE_ADDR}s"
    RequestHeader set Host "file.example.com"

    ProxyPass / http://localhost:801/
    ProxyPassReverse / http://localhost:801/

    RewriteEngine On
    RewriteCond %{HTTP:Upgrade} websocket [NC]
    RewriteCond %{HTTP:Connection} upgrade [NC]
    RewriteRule ^/?(.*) "ws://localhost:801/$1" [P,L]

    ErrorLog /var/log/apache2/file.example.com_error.log
    CustomLog /var/log/apache2/file.example.com_access.log combined
</VirtualHost>
```

### 2. Docker Compose Configuration
```yaml
services:
  seafile:
    environment:
      - SEAFILE_SERVER_HOSTNAME=file.example.com
      - SEAFILE_SERVER_SCHEME=https
      - SERVICE_URL=https://file.example.com
      - CSRF_TRUSTED_ORIGINS=https://file.example.com
```

### Common Issues and Solutions

1. **CSRF Verification Failed**
   - Ensure no trailing slash in CSRF_TRUSTED_ORIGINS
   - Domain must match exactly in all configurations
   - Use complete https:// URL in settings

2. **Required Apache Modules**
   ```
   sudo a2enmod ssl proxy proxy_http proxy_wstunnel headers rewrite
   ```

3. **If Changes Don't Take Effect**
   ```
   docker-compose down
   docker-compose up -d
   sudo systemctl restart apache2
   ```

Remember to replace `file.example.com` with your actual domain name in all configurations.
