from flask import Flask, render_template

from dbcon.queries import get_top_apps_by_installs, get_app_categories, get_single_app

app = Flask(__name__)


@app.route("/")
def index():
    # Fetch top X most installed apps from the database

    cats = get_app_categories()
    category_dicts = cats.to_dict(orient="records")
    return render_template("index.html", cats=category_dicts)


@app.route("/<store>/<app_id>")
def app_detail(store, app_id):
    # Fetch app details from the database using store and app_id
    app = get_single_app(app_id)
    app_dict = app.to_dict(orient="records")[0]
    print(app_dict)
    return render_template("app_detail.html", app=app_dict)


@app.route("/category/<category>")
def category(category):
    # Your logic here for handling the category page
    apps = get_top_apps_by_installs(category_in=[category], limit=15)
    apps_dict = apps.to_dict(orient="records")
    return render_template("category_detail.html", category=category, apps=apps_dict)


if __name__ == "__main__":
    app.run(debug=True)
