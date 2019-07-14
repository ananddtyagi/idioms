from lib.flask import Flask, render_template, request
from flask.ext.cors import CORS, cross_origin

from idioms import findIdioms

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', iList="")

@app.route('/test', methods = ['GET'])
def test():
    return 'Test String From Flash Server'

@app.route('/',methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
      phrase = request.form['phrase']
      iList = findIdioms(phrase)
      #THE PROBLEM TAKES PLACE WITHIN THE GOOGLE TRANSLATE ITSELF BECAUSE I NEED A KEY, IT"S BLOCKING ME FROM MAKING A CALL FROM A WEBSITE BUT WORKS IF I JUST MAKE IT FROM A LOCAL HOST
      return render_template("index.html",iList = iList)

if __name__ == "__main__":
    app.run(debug = True)
