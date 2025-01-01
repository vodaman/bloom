from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return render_template('not_found.html')

@app.route("/signup")
def signup():
    return render_template("signup.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/forgot")
def forgot():
    return render_template("forgot.html")
@app.route("/community")
def community():
    return render_template("community.html")
@app.route("/activities")
def activities():
    return render_template("activities.html")
@app.route("/search")
def search():
    return render_template("search.html")
@app.route("/profile")
def profile():
    return render_template("john.html")
@app.route("/john")
def jon():
    return render_template("john.html")
@app.route("/vova")
def vova():
    return render_template("vova.html")
@app.route("/oleg")
def oleg():
    return render_template("oleg.html")
@app.route("/misha")
def misha():
    return render_template("miha.html")

app.run(debug=True)
