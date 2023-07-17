from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')

def hello(name):
    return f'<h1>Hello bey</h1> {name}'

@app.route('/class/<int:number>')

def cls(number):
    return f'my class is {number}'

if __name__ == '__main__':
    app.run(debug = True)