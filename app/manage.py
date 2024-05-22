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
    buff.append(prompt)
    buff.append("\n")
    for line in main(model, prompt):
        buff.append(line)
    return render_template("index.html", buff=buff)


if __name__ == "__main__":
    app.run(debug=True)