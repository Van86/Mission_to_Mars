from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    mars_data = mongo.db.mars.find_one()
    print(mars_data)
    return render_template("index.html", marsInfo= mars_data)

@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data =  mars_scrape.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)