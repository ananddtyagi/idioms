from lib.flask import Flask, render_template, request
from idioms import findIdioms

app = Flask(__name__)

@app.route('/')
def index():
    if i == 0:
        i = i + 1
        return render_template('index.html', iList = ["iList", "lol", "hah","yeet"])
    return render_template("index.html",iList = ["iList", "hello", "sup","damnnn"])


@app.route('/',methods = ['POST'])
def result():
    flash("WRSDFASDFSDF")
    phrase = request.form['phrase']
    iList = findIdioms(phrase)
    return render_template("index.html",iList = ["iList", "hello", "sup","damnnn"])


if __name__ == "__main__":
    app.run(debug = True)
