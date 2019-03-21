from lib.flask import Flask, render_template, request
from idioms import findIdioms

app = Flask(__name__)

@app.route('/')
def index():
    return index(0)
def index(x):
    if x == 0:
        return render_template('index.html', iList = ["iList", "lol", "hah","yeet"])
    if x == 1:
        return render_template("index.html",iList = ["iList", "hello", "sup","damnnn"])

@app.route('/',methods = ['GET', 'POST'])
def result():
    return index(1)

if __name__ == "__main__":
    app.run(debug = True)
