import os
from flask import Flask, render_template, request
from config import model
from src import main


app = Flask(__name__)
buff = []


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/index', methods=["post"])
def upload():
    file = request.files.get('file')
    file_path = f"{os.getcwd()}/app/upload/{file.filename}"
    file.save(file_path)
    return render_template("index.html", buff=buff)


if __name__ == "__main__":
    app.run(debug=True)