from flask import Flask
from forms import InputForm

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    pass


if __name__ == "__main__":
    app.run(debug=True)