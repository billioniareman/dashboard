from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
