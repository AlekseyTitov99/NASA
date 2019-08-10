from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data", methods=['POST'])
def data():
    api_key = request.form['api']
    url = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + api_key)

    fixed_json = json.loads(url.text)

    for key in fixed_json.keys():
        if key == 'error':
            return invalid()

    title = fixed_json['title']
    date = fixed_json['date']
    exp = fixed_json['explanation']
    image = fixed_json['url']

    return render_template("result.html", title=title, date=date, exp=exp, image=image)

@app.route("/invalid")
def invalid():
    return render_template("invalid.html")

if __name__ == "__main__":
    app.run()
