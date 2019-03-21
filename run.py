from lib.flask import Flask, render_template, request
from idioms import findIdioms

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods = ['POST'])
def result():
   if request.method == 'POST':
      phrase = request.form['phrase']
      iList = findIdioms(phrase)
      return render_template("index.html",iList = iList)


if __name__ == "__main__":
    app.run(debug = True)
