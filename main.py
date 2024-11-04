from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return render_template('not_found.html')

app.run(debug=True)