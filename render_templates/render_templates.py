from flask import Flask,render_template
app = Flask(__name__)

posts = [
    {
        'author' : "Tony stark",
        'invention' : "Arc Reacter",
        'profession' : 'Super hero'
    },
    {
        'author' : "Howard stark",
        'invention' : "Vibranium shield",
        'profession' : 'scientist'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title = 'About')

if __name__ == "__main__":
    app.run(debug=True)