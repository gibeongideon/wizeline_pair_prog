from os import path, curdir

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify('hello world')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')