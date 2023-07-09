from flask import Flask

from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello1")
def hello_world1():
    return "<h2>Hello, World1!</h2>"

@app.route("/hello2")
def hello_world2():
    
    return "<h3 style = 'color : red'>Hello, World2!</h3>"

@app.route("/test")
def test():

    a = 8+9
    return "this is my function to run app {}".format(a)

@app.route("/test2")
def test2():
    data = request.args.get('x')
    return "this is a data input form my url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
