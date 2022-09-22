# save this as app.py version 1 in FutureStack22-Jakarta -updated 1 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!! for the branch"

@app.route("/ping")
def ping():
    return "pong"

@app.route("/error")
def error():
    return 1/0
if __name__ == '__main__':
    app.run(debug=True)