from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/destytojas/')
def destytojas():
    return render_template("destytojas.html")

@app.route('/egle/')
def egle():
    return render_template("egle.html")


if __name__ == "__main__":
    app.run(debug=True)
