from flask import Flask

app = Flask(__name__)

@app.route("/api")
def show_sorted_data():
    return "<p>Hello, World!</p>"