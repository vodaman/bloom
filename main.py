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

@app.route("/profile")
def profile():
    return render_template("profile.html")

app.run(debug=True)