from flask import Flask,render_template,url_for,request,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sucess/<int:score>')
def sucess(score):
    return f'<h1>You are passed with {score} marks</h1>'

@app.route('/fail/<int:score>')
def fail(score):
    return f'<h1>You are failed with {score} marks</h1>'


@app.route('/calculation',methods = ['POST','GET'])
def calculation():
    total = 0
    if request.method == "POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        total = (science+maths)/2
    res = ''
    if total > 50:
        res = 'sucess'
    else:
        res = 'fail'

    return redirect(url_for(res,score = total))

if __name__ == "__main__":
    app.run(debug=True)
    