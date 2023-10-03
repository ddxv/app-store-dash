from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch top 10 most installed apps from the database
    # For now, let's use dummy data
    apps = [
        {"id": "com.example.app1", "name": "App 1", "installs": 10000},
        {"id": "com.example.app2", "name": "App 2", "installs": 9000},
        # ... add more dummy apps ...
    ]
    return render_template('index.html', apps=apps)

@app.route('/<store>/<app_id>')
def app_detail(store, app_id):
    # Fetch app details from the database using store and app_id
    # For now, let's use dummy data
    app = {
        "title": "App 1",
        "app_id": "com.example.app1",
        "installs": 10000,
        "reviews": 500,
        "rating": 4.5,
        "last_updated": "2023-10-01"
    }
    return render_template('app_detail.html', app=app)

if __name__ == '__main__':
    app.run(debug=True)

