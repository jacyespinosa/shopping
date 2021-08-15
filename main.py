from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template('register.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1000, debug=True)