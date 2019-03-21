from lib.flask import Flask, render_template, request
from idioms import findIdioms

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', iList = ["iList", "lol", "hah","yeet"])
def index(x):
    if x == 0:
        return render_template("index.html",iList = ["iList", "hello", "sup","damnnn"])

@app.route('/',methods = ['GET', 'POST'])
def result():
    index(0)
    if request.method == 'POST':
      phrase = request.form['phrase']
      iList = findIdioms(phrase)
      return render_template("index.html",iList = ["iList", "hello", "sup","damnnn"])


if __name__ == "__main__":
    app.run(debug = True)
