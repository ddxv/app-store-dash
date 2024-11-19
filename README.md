# AppGoblin Analytics Dashboard for Mobile App Ecosystem

You can see a production version of the site at [appgoblin.info](https://appgoblin.info)

[<img src="/frontend/static/appgoblin_screenshot.png" width="500"/>](/frontend/static/appgoblin_screenshot.png)

This is the code I use to create [AppGoblin](https://appgoblin.info) for tracking app store ranks and SDKs of mobile companies like ad networks and mobile attribution companies. The goal was simply to have a good source of data for Apps on the Google Play and iOS stores. The code is provided here incase it helps anyone. As this is a project for general fun and learning, please don't hesitate to reach out if you have any questions or suggestions, Discord below.

## Features

- **[Companies Directory](https://appgoblin.info/companies)**: Rankings based on SDK integration frequency
  - Filter by category 
    - Example: [Most popular Ad Networks for Casino Games](https://appgoblin.info/companies/types/ad-networks/game_casino)
    - Example: [Most popular Product analytics for Business Apps](https://appgoblin.info/companies/types/product-analytics/business)
- **Company Intelligence**: See the top client apps for mobile app companies
  - Example: [Salesforce Clients](https://appgoblin.info/companies/salesforce.com)
  - Example: [AppsFlyer Top Apps](https://appgoblin.info/companies/appsflyer.com)
- **[App Rankings](https://appgoblin.info/rankings/store/1/collection/1/category/1)**: Daily tracking of top apps from Google Play and Apple App Store.
- **[SDK Analysis](https://appgoblin.info/sdks)**: Detailed list of decompiled Android and iOS Apps and their internally used SDKs. See what tracking SDKs are used in which apps.


### Project Structure

   1. Python Litestar backend API found in `backend/`
   2. Javascript SvelteKit+Tailwind UI found in `frontend/`

### Data & Database

The database referred to in this repository is created by [adscrawler](https://github.com/ddxv/adscrawler), a crawler for scraping the Google & Apple play stores and storing that to a PostgreSQL database. That repo also contains a number of materialized views prepping data for the dashboard. It generally would be difficult to recreate it as it's only ever been managed by me the original creator, but I'm open to sharing data if you have something you need.

### API Service

`litestar run --debug` to start API. Once run, api documentation can be found at `api/docs`

### Setup

- Current setup is based on Python3.12
- pip install dependencies, found in pyproject.toml: `pip install`

### Running

- To run locally for testing use
  - Backend: in `backend/` run `gunicorn -k uvicorn.workers.UvicornWorker app:app` or `litestar run dev`
  - Frontend: in `frontend` run `npm run dev`
- This repo includes the scripts used to run in production as well. These are located in the steps in `.github/actions` as well as `scripts` for systemd services for frontend and backend.
- Additionally, you will need a proxy. I used Nginx. This is wherever you have your nginx configuration set, possibly sites-available `/etc/nginx/sites-available/app-store-api` or `/etc/nginx/conf.d/app-store-api.conf`

### AppGoblin Community

**Have questions or suggestions? Let's connect!**

🧙‍♂️ [Join Discord Server](https://discord.gg/7jpWEhkXRW)





