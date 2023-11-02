# API & Dashboard for App Store Dash

You can visit the site at [appgoblin.info](https://appgoblin.info)

[<img src="/frontend/static/appgoblin_screenshot.png" width="500"/>](/frontend/static/appgoblin_screenshot.png)

This is the code I used to create AppGoblin. The goal was simply to have a good source of data for Apps on the Google Play and iOS stores. The code is provided here incase it helps anyone. As this is a project for general fun and learning, please don't hesitate to reach out if you have any questions or suggestions.

This repo has two parts:

   1. Python Litestar backend API found in `backend/`
   2. Javascript SvelteKit+Tailwind UI found in `frontend/`

## Data & Database

The database referred to in this repository is created by [adscrawler](https://github.com/ddxv/adscrawler), a crawler for scraping the Google & Apple play stores and storing that to a PostgreSQL database.

## API Service

Once run api documentation can be found at `api/docs`

## Setup

- Current setup is based on Python3.12
- pip install dependencies, found in pyproject.toml: `pip install`

## Running

- To run locally for testing use
  - Backend: in `backend/` run `gunicorn -k uvicorn.workers.UvicornWorker app:app` or `litestar run dev`
  - Frontend: in `frontend` run `npm run dev`
- This repo includes the scripts used to run in production as well. These are located in the steps in `.github/actions` as well as `scripts` for systemd services for frontend and backend.
- Additionally, you will need a proxy. I used Nginx. This is wherever you have your nginx configuration set, possibly sites-available `/etc/nginx/sites-available/app-store-api` or `/etc/nginx/conf.d/app-store-api.conf`


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

