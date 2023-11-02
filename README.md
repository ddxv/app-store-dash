# Mobile App Store Dash

# API & Dashboard for App Store Dash

[<img src="/frontend/static/appgoblin_screenshot.png" width="500"/>](/frontend/static/appgoblin_screenshot.png)

This repo has two parts:

1. Python Litestar API found in `backend/`
3. Javascript SvelteKit+Tailwind UI found in `frontend/`

## Database

The database referred to in this repository is created by [adscrawler](https://github.com/ddxv/adscrawler)

## API Service

Once run api documentation can be found at `api/docs`

## Setup

- Current setup is based on Python3.12
- pip install dependencies, found in pyproject.toml: `pip install`

## Running Locally

- To run locally for testing use
  - Backend: in `backend/` run `gunicorn -k uvicorn.workers.UvicornWorker app:app`
  - Frontend: in `frontend` run `npm run dev`

## Running in production

myscript TODO: bash script should do:
 - system link
 - stop service python
 - stop service js
 - system link
 - start service python
 - wait(2)
 - start service js

### Socket Unit File

system link to location: `/etc/systemd/system/app-store-api.socket`

```ini
[Unit]
Description=Gunicorn socket

[Socket]
ListenStream=/run/app-store-api.sock
User=www-data

[Install]
WantedBy=sockets.target
```

### Service Unit file

location: `/etc/systemd/system/app-store-api.service`

```ini
[Unit]
Description=Gunicorn instance to serve App Store API
After=network.target

[Service]
Type=Notify
User=ubuntu
Group=ubuntu
RuntimeDirectory=gunicorn
WorkingDirectory=/home/ubuntu/app-store-dash/backend
Environment=/home/ubuntu/venvs/app-store-dash-env/bin
ExecStart=/home/ubuntu/venv/app-store-dash-env/bin/gunicorn -k uvicorn.workers.UvicornWorker --workers 1 --bind unix:app-store-api.sock -m 007 app:app
ExecReload=/bin/kill -s HUP $MAINPID
Restart=on-failure
KillMode=mixed
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

### Nginx config file

This is wherever you have your nginx configuration set, possibly sites-available `/etc/nginx/sites-available/app-store-api` or `/etc/nginx/conf.d/app-store-api.conf`


```Nginx
server {
    listen 80;
    client_max_body_size 2M;

    location /api {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-NginX-Proxy true;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_pass http://unix:/run/app-store-api.sock;
    }
}
```

If you put your nginx configuration in a new file in sites-available, be sure to link to sites-enabled to start:

```Shell
sudo ln -s /etc/nginx/sites-available/app-store-api /etc/nginx/sites-enabled/app-store-api
sudo systemctl restart nginx.service 
```

## Start the service and socket

NOTE: If you have a socket and a service, you do not need to start the service, the socket will start the related service
- `systemctl enable app-store-api.socket` to automatically start socket on server reboot
- `sudo systemctl start app-store-api.socket` start
- `sudo systemctl status app-store-api` to check status

## Check your API endpoints

try visiting example.com/api/docs/

## Troubleshooting

Checking your local API docs:

`http://127.0.0.1:8000/api/docs`

Restarting Unit service manually, ensure you do not start the service, let the socket start the related service.
- `sudo systemctl stop app-store-api.socket`
- `sudo systemctl stop app-store-api.service`
- `sudo systemctl start app-store-api.socket`
