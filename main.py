import flask
import json

from flask import Flask
app = Flask(__name__)

@app.route('/categories')
def hello_world():
   f = open('data.json')
   data = json.load(f)
   return data
   # Opening JSON file


if __name__ == '__main__':
   app.run()