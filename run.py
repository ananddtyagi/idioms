from lib.flask import Flask, render_template, request
from idioms import findIdioms

app = Flask(__name__)

@app.route('/')
def index():
    return index(0)
    if x == 0:
        return render_template('index.html', iList = ["iList", "lol", "hah","yeet"])
    if x == 1:
        return render_template("index.html",iList = ["iList", "hello", "sup","damnnn"])

@app.route('/',methods = ['GET', 'POST'])
def result():
    index(1)
    if request.method == 'POST':
      phrase = request.form['phrase']
      iList = findIdioms(phrase)
      return render_template("index.html",iList = ["iList", "hello", "sup","damnnn"])


if __name__ == "__main__":
    app.run(debug = True)
