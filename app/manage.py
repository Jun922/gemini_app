import pathlib
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
    file_name = request.form["upload_file"]
    file_path = "" + file_name
    # need abs path

    for line in main(model, file_path):
        buff.append(line)
    return render_template("index.html", buff=buff)


if __name__ == "__main__":
    app.run(debug=True)