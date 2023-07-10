# Csie-Camp-NA-EasyWeb

## download
``` bash
git clone https://github.com/Jimmy01240397/Csie-Camp-NA-EasyWeb
cd Csie-Camp-NA-EasyWeb
```

## install frontend
```bash
mv frontend /var/www/frontend
```

## start backend
```bash
pip3 install flask
python3 backend/main.py
```

## setup nginx
```bash
nano /etc/nginx/site-enable/csiecampeasyweb
```

write this
```
server {
    listen 80;
    listen [::]:80;
    root /var/www/frontend;
    index index.html;
    server_name <your domain name>;
    location / {
        try_files $uri $uri/ =404;
    }
    location /backend {
        proxy_pass http://localhost:5000/backend;
    }
}
```
