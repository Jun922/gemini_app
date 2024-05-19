from flask import Flask
from config import model
from src import main


if __name__ == "__main__":
    main(model)


app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World!'

app.run(debug=True)