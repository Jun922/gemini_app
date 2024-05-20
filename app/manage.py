from flask import Flask, render_template, request
from config import model
from src import main


app = Flask(__name__)
buff = []


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route("/index", methods=["post"])
def post():
    prompt = request.form["prompt"]
    buff.append(main(model, prompt))
    return render_template("index.html", buff=buff)


if __name__ == "__main__":
    app.run(debug=True)