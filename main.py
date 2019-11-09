from flask import Flask, render_template
import datetime
app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Hello Message!"
    current_year = datetime.datetime.now()
    return render_template("index.html", some_text=some_text, current_year=current_year)


@app.route("/about-me")
def about_me():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


if __name__ == '__main__':
    app.run()